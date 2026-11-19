"""Change history of data/rules.csv, worked out from git.

Every commit that touched the file is compared with the one before it, so the
site can show a change log per rule and an updates page without anyone keeping
a separate log. Needs the full git history (CI checks out with fetch-depth: 0);
without git it returns an empty history.
"""
import subprocess
from pathlib import Path

import rules_diff

ROOT = Path(__file__).resolve().parent.parent
PATH = "data/rules.csv"
# Field changes worth calling out by name on the updates page.
NOTABLE = ("status", "verification", "amends", "revokes", "date_in_force", "source_url")


def _git(*args):
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True, check=True).stdout


def commits():
    try:
        out = _git("log", "--reverse", "--format=%H%x1f%ad%x1f%an%x1f%s", "--date=short", "--", PATH)
    except (OSError, subprocess.CalledProcessError):
        return []
    return [dict(zip(("sha", "date", "author", "subject"), line.split("\x1f"))) for line in out.splitlines() if line]


def load():
    """Return a list of change events, oldest first.

    Each event: {sha, date, author, subject, added: [ids], removed: [ids], changed: {id: [(field, old, new)]}}.
    """
    events, prev = [], ""
    for c in commits():
        try:
            text = _git("show", f"{c['sha']}:{PATH}")
        except subprocess.CalledProcessError:
            continue
        d = rules_diff.diff(prev, text) if prev else {"added": list(rules_diff.read_rows(text)[1].values()),
                                                      "removed": [], "changed": {}}
        prev = text
        if d["added"] or d["removed"] or d["changed"]:
            events.append({**c, "added": [r["id"] for r in d["added"]], "removed": [r["id"] for r in d["removed"]],
                           "changed": d["changed"]})
    return events


def per_rule(events):
    """id → list of {date, sha, subject, kind, changes}, newest first."""
    out = {}
    for e in events:
        for rid in e["added"]:
            out.setdefault(rid, []).append({**_meta(e), "kind": "added", "changes": []})
        for rid, ch in e["changed"].items():
            out.setdefault(rid, []).append({**_meta(e), "kind": "changed", "changes": ch})
    for v in out.values():
        v.reverse()
    return out


def _meta(e):
    return {"date": e["date"], "sha": e["sha"], "subject": e["subject"], "author": e["author"]}
