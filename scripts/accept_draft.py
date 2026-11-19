#!/usr/bin/env python3
"""Add AI-drafted rows from a portal-scan issue to data/rules.csv.

Run by .github/workflows/accept-draft.yml when a maintainer comments
"/accept ID-..." (one or more ids) on a scan issue. Reads the ```csv blocks the
scan wrote into the issue body, appends the requested rows, and validates.

Inputs (environment): ISSUE_BODY, COMMENT_BODY. Outputs: data/rules.csv, accept_result.json, accept_summary.md.
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

RULES = build.ROOT / "data" / "rules.csv"
CSV_BLOCK = re.compile(r"```csv\n(.*?)\n```", re.S)


def requested_ids(comment):
    m = re.search(r"^/accept\s+(.+)$", comment or "", re.M)
    return [i for i in re.split(r"[\s,]+", m.group(1).strip()) if i] if m else []


def drafted_rows(body, columns):
    rows = {}
    for block in CSV_BLOCK.findall(body or ""):
        for values in csv.reader(io.StringIO(block)):
            if len(values) == len(columns) and values[0] != "id":
                rows[values[0]] = dict(zip(columns, values))
    return rows


def main():
    raw = RULES.read_bytes().decode("utf-8")
    newline = "\r\n" if "\r\n" in raw else "\n"
    columns, current = rules_diff.read_rows(raw)
    ids = requested_ids(os.environ.get("COMMENT_BODY", ""))
    drafts = drafted_rows(os.environ.get("ISSUE_BODY", ""), columns)
    errors, added = [], []
    if not ids:
        errors.append("No ids given. Use `/accept ID-PERMEN-ESDM-2026-12` (several ids can be separated by spaces).")
    for i in ids:
        if i in current:
            errors.append(f"`{i}` is already in the tracker.")
        elif i not in drafts:
            errors.append(f"No draft with id `{i}` in this issue.")
        else:
            current[i] = drafts[i]
            added.append(i)
    if not errors:
        buf = io.StringIO()
        w = csv.DictWriter(buf, fieldnames=columns, lineterminator=newline)
        w.writeheader()
        w.writerows(current.values())
        RULES.write_bytes(buf.getvalue().encode("utf-8"))
        data = build.load()
        if data.errors:
            errors += data.errors
            RULES.write_bytes(raw.encode("utf-8"))
    ok = not errors
    md = ([f"Added {len(added)} draft row(s) as **unverified**: " + ", ".join(f"`{a}`" for a in added),
           "", "Each still needs a review against the official text before it counts as verified."]
          if ok else ["Could not add the drafts:"] + [f"- {e}" for e in errors])
    Path("accept_summary.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    Path("accept_result.json").write_text(json.dumps({"ok": ok, "added": added, "errors": errors}), encoding="utf-8")
    print("\n".join(md))


if __name__ == "__main__":
    main()
