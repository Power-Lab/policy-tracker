#!/usr/bin/env python3
"""Check scouting candidate files (docs/scouting/*-candidates.csv) against the tracker's vocabularies.

    python3 scripts/check_candidates.py                  check every candidates file
    python3 scripts/check_candidates.py docs/scouting/ph-candidates.csv

Candidates are leads from desk research, not tracker rows: this only reports
problems that would block promoting them into data/rules.csv later.
"""
import csv
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build  # noqa: E402

HEADER = ["id", "doc_type", "number", "short_name", "issuing_body", "date_signed", "title_english", "topics",
          "amends", "revokes", "status", "source_url", "confidence", "notes"]


def check(path, topics):
    problems = []
    with open(path, encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames != HEADER:
            problems.append(f"header differs from the expected {len(HEADER)} columns")
        rows = list(reader)
    ids = {r.get("id") for r in rows}
    for n, r in enumerate(rows, start=2):
        where = f"line {n} ({r.get('id')})"
        if r.get("doc_type") not in build.DOC_TYPES:
            problems.append(f"{where}: doc_type '{r.get('doc_type')}'")
        if r.get("status") not in build.STATUSES:
            problems.append(f"{where}: status '{r.get('status')}'")
        for t in build.split(r.get("topics")):
            if t not in topics:
                problems.append(f"{where}: topic '{t}'")
        d = (r.get("date_signed") or "").strip()
        if d and not build.DATE_RE.match(d):
            problems.append(f"{where}: date '{d}'")
        for f in ("amends", "revokes"):
            for t in build.split(r.get(f)):
                if t not in ids:
                    problems.append(f"{where}: {f} points to '{t}', not in this file")
        if r.get("confidence") not in {"high", "medium", "low"}:
            problems.append(f"{where}: confidence '{r.get('confidence')}'")
    return rows, problems


def main():
    topics = {r["id"] for r in build.read_csv(build.DATA / "topics.csv")[0]}
    paths = sys.argv[1:] or sorted(str(p) for p in (build.ROOT / "docs" / "scouting").glob("*-candidates.csv"))
    bad = 0
    for p in paths:
        rows, problems = check(p, topics)
        conf = Counter(r.get("confidence") for r in rows)
        print(f"{Path(p).name}: {len(rows)} candidates ({', '.join(f'{k} {v}' for k, v in sorted(conf.items()))}), "
              f"{len(problems)} problems")
        for x in problems:
            print("  -", x)
        bad += bool(problems)
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
