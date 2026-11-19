#!/usr/bin/env python3
"""Apply a review submitted as a GitHub issue to data/rules.csv.

Run by .github/workflows/review-to-pr.yml. The issue body is untrusted input:
this script only reads the fenced ```json review block, only changes fields on
the EDITABLE list, refuses to overwrite a field that changed since the reviewer
loaded it, and validates the result. Nothing in the issue is ever executed.
A maintainer still has to merge the pull request this produces.

Inputs (environment): ISSUE_BODY, ISSUE_NUMBER, ISSUE_AUTHOR, ISSUE_CREATED (ISO date).
Outputs: data/rules.csv (edited in place), review_result.json, review_summary.md.

Local test:  ISSUE_BODY="$(cat body.md)" ISSUE_AUTHOR=me python3 scripts/apply_review.py
"""
import csv
import io
import json
import os
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build  # noqa: E402
import rules_diff  # noqa: E402

ROOT = build.ROOT
RULES = ROOT / "data" / "rules.csv"
CONFIG = json.loads((ROOT / "config.json").read_text(encoding="utf-8"))
CHECKS = ["status", "links", "dates", "summary", "source"]
# Fields a review may change. Identity fields (id, country) and the fields this
# script sets itself (verification, reviewed_by, reviewed_on, status_checked) are excluded.
EDITABLE = {"status", "date_signed", "date_in_force", "amends", "revokes", "title_english", "summary_english",
            "title_original", "number", "short_name", "issuing_body", "doc_type", "origin_sector",
            "energy_channel", "topics", "technologies", "source_url", "source_type", "notes", "language",
            "implements", "overrides", "link_basis", "binding", "grandfathered", "jurisdiction"}
MAX_VALUE = 3000
BLOCK_RE = re.compile(r"```json review\s*\n(.*?)\n```", re.S)


class ReviewError(Exception):
    pass


def parse_payload(body):
    m = BLOCK_RE.search(body or "")
    if not m:
        raise ReviewError("No machine-readable review block found. Submit reviews from the site's reviewer view, "
                          "or include a fenced ```json review block.")
    try:
        p = json.loads(m.group(1))
    except json.JSONDecodeError as e:
        raise ReviewError(f"The review block is not valid JSON ({e.msg}). Was it edited by hand?")
    if not isinstance(p, dict) or p.get("v") != 1 or not isinstance(p.get("rules"), list) or not p["rules"]:
        raise ReviewError("The review block has an unexpected format (expected v=1 and a list of rules).")
    cfg = CONFIG.get("reviews", {})
    n_max = cfg.get("max_rules_per_review", 10) if cfg.get("multi_rule") else 1
    if len(p["rules"]) > n_max:
        raise ReviewError(f"This review covers {len(p['rules'])} rules; the limit is {n_max}"
                          + ("" if cfg.get("multi_rule") else " because multi-rule reviews are turned off") + ".")
    return p


def apply(payload, rows, author, on_date):
    """Apply the payload to `rows` (dict id → row, edited in place). Returns (errors, conflicts)."""
    errors, conflicts = [], []
    reviewer = re.sub(r"[\r\n]+", " ", str(payload.get("reviewer") or "")).strip()[:120]
    who = f"{reviewer} (@{author})" if reviewer else f"@{author}"
    seen = set()
    for entry in payload["rules"]:
        rid = entry.get("id") if isinstance(entry, dict) else None
        if not rid or rid not in rows:
            errors.append(f"Unknown rule id `{rid}`. New rules can't be added through a review yet; open a pull request instead.")
            continue
        if rid in seen:
            errors.append(f"`{rid}` appears twice in this review.")
            continue
        seen.add(rid)
        row = rows[rid]
        changes = entry.get("set") or {}
        base = entry.get("base") or {}
        if not isinstance(changes, dict) or not isinstance(base, dict):
            errors.append(f"`{rid}`: malformed changes.")
            continue
        for field, value in changes.items():
            if field not in EDITABLE:
                errors.append(f"`{rid}`: field `{field}` can't be changed through a review.")
                continue
            value = str(value)
            if len(value) > MAX_VALUE or "\x00" in value:
                errors.append(f"`{rid}`: value for `{field}` is too long or contains invalid characters.")
                continue
            current = row.get(field, "")
            if current == value:
                continue  # already applied (e.g. the issue was edited and re-run)
            if field in base and str(base[field]) != current:
                conflicts.append(f"`{rid}` `{field}`: the reviewer started from “{rules_diff.short(str(base[field]), 60)}”, "
                                 f"but the data now says “{rules_diff.short(current, 60)}”. Not overwritten.")
                continue
            row[field] = value
        checks = entry.get("checks") or {}
        n = sum(bool(checks.get(k)) for k in CHECKS)
        if n:
            row["verification"] = "verified" if n == len(CHECKS) else "partly verified"
            row["reviewed_by"] = who
            row["reviewed_on"] = on_date
            if checks.get("status"):
                row["status_checked"] = on_date
    return errors, conflicts


def write_rows(columns, rows, newline):
    buf = io.StringIO()
    w = csv.DictWriter(buf, fieldnames=columns, lineterminator=newline)
    w.writeheader()
    for r in rows.values():
        w.writerow({c: r.get(c, "") for c in columns})
    return buf.getvalue()


def main():
    body = os.environ.get("ISSUE_BODY", "")
    author = re.sub(r"[^A-Za-z0-9-]", "", os.environ.get("ISSUE_AUTHOR", "unknown"))[:39] or "unknown"
    on_date = (os.environ.get("ISSUE_CREATED") or "")[:10] or __import__("datetime").date.today().isoformat()
    number = os.environ.get("ISSUE_NUMBER", "")
    result = {"ok": False, "errors": [], "conflicts": [], "warnings": [], "changed": []}

    raw = RULES.read_bytes().decode("utf-8")
    newline = "\r\n" if "\r\n" in raw else "\n"
    columns, rows = rules_diff.read_rows(raw)
    try:
        payload = parse_payload(body)
        errors, conflicts = apply(payload, rows, author, on_date)
        result["errors"] += errors
        result["conflicts"] += conflicts
    except ReviewError as e:
        result["errors"].append(str(e))

    new_text = write_rows(columns, rows, newline)
    d = rules_diff.diff(raw, new_text)
    result["changed"] = list(d["changed"])
    if not result["errors"] and not d["changed"]:
        result["errors"].append("Nothing to change: the review has no edits and no checklist items ticked, "
                                "or every change is already in the data.")

    if not result["errors"]:
        RULES.write_bytes(new_text.encode("utf-8"))
        data = build.load()
        result["errors"] += data.errors
        touched = set(d["changed"])
        for r in d["changed"]:
            touched |= set(data.rules[r]["amends"] + data.rules[r]["revokes"])
        result["warnings"] = [w for w in data.warnings if w.split(":")[0] in touched]
        if data.errors:  # leave the file as it was
            RULES.write_bytes(raw.encode("utf-8"))
    result["ok"] = not result["errors"]

    md = [f"Review from issue #{number} by @{author}." if number else f"Review by @{author}.", ""]
    if result["ok"]:
        md.append(rules_diff.markdown(d, rows))
    if result["conflicts"]:
        md += ["", "**Not applied (conflicts):**"] + [f"- {c}" for c in result["conflicts"]]
    if result["warnings"]:
        md += ["", "**Warnings to check before merging:**"] + [f"- {w}" for w in result["warnings"]]
    if result["errors"]:
        md += ["", "**Could not apply this review:**"] + [f"- {e}" for e in result["errors"]]
    Path("review_summary.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    Path("review_result.json").write_text(json.dumps(result, indent=1), encoding="utf-8")
    print("\n".join(md))
    # Exit 0 either way: the workflow reads review_result.json and comments on the issue.


if __name__ == "__main__":
    main()
