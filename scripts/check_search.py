#!/usr/bin/env python3
"""Check the search framework in data/search/ for consistency (runs in CI).

    python3 scripts/check_search.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build  # noqa: E402
import search  # noqa: E402


def main():
    topics = {r["id"] for r in build.read_csv(build.DATA / "topics.csv")[0]}
    known = {r["code"] for r in build.read_csv(build.DATA / "countries.csv")[0]}
    if (build.DATA / "pipeline.csv").exists():
        known |= {r["code"] for r in build.read_csv(build.DATA / "pipeline.csv")[0]}
    fw = search.load()
    errors, warnings = search.validate(fw, topics, known)
    for w in warnings:
        print("warning:", w)
    for e in errors:
        print("ERROR:", e)
    print(f"{len(fw['modules'])} modules, {len(fw['sources'])} sources, {len(fw['vocab'])} vocabulary sets, "
          f"{len(fw['screening'])} screening decisions, {len(fw['log'])} logged runs: "
          f"{len(errors)} errors, {len(warnings)} warnings")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
