#!/usr/bin/env python3
"""Load and validate the tracker data.

Reads data/rules.csv, data/topics.csv, data/countries.csv and data/fields.csv,
checks them, and derives amended_by / revoked_by from the amends / revokes
links so the amendment chain can be walked in both directions.

    python3 scripts/build.py          validate and print a report
    python3 scripts/render.py         validate, then build the site into _site/

Other scripts import load() from here.
"""
import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"

DOC_TYPES = {"law", "emergency regulation", "government regulation", "presidential regulation",
             "ministerial regulation", "decree", "decision", "circular", "advisory", "code",
             "regulator determination", "directive", "plan", "regional plan", "MoU", "party resolution"}
ORIGIN_SECTORS = {"energy", "mining", "industry-trade", "finance-fiscal", "environment"}
CHANNELS = {"demand", "supply", "prices", "investment", "grid-access", "emissions"}
TECHNOLOGIES = ["solar-pv", "wind", "batteries", "electric-vehicles", "grid-equipment", "hydrogen"]
STATUSES = ["in force", "amended", "pending", "draft", "replaced", "revoked", "expired"]  # display order
VERIFICATION = ["verified", "partly verified", "unverified"]
SOURCE_TYPES = {"document", "portal-search"}
CURRENT = {"in force", "amended"}  # statuses that mean "still applies"
ENDED = {"revoked", "replaced", "expired"}
NOT_YET = {"pending", "draft"}  # adopted but not in force yet / proposed, not adopted

REQUIRED = ["id", "country", "doc_type", "number", "short_name", "issuing_body", "origin_sector",
            "energy_channel", "title_original", "title_english", "summary_english", "topics", "status",
            "status_checked", "source_url", "source_type", "language", "verification"]
LIST_FIELDS = ["energy_channel", "topics", "technologies", "amends", "revokes", "implements", "overrides"]
# Link fields and the back-links derived from them (never typed in the CSV).
LINKS = [("amends", "amended_by"), ("revokes", "revoked_by"), ("implements", "implemented_by"),
         ("overrides", "overridden_by")]
LINK_BASIS = {"", "express clause", "implied by successor", "expired"}
JURISDICTION_RE = re.compile(r"^[A-Z]{2}-[A-Z0-9]{2,4}$")
DATE_RE = re.compile(r"^\d{4}(-\d{2}(-\d{2})?)?$")


class Data:
    """Validated tracker data."""

    def __init__(self, rules, columns, topics, countries, fields, errors, warnings, categories=None):
        self.rules = rules            # dict id -> rule (dict), in CSV order
        self.columns = columns        # CSV column order
        self.topics = topics          # dict id -> topic (with its category)
        self.categories = categories or {}  # dict id -> category, in display order
        self.countries = countries    # dict code -> country
        self.fields = fields          # list of field docs
        self.errors = errors
        self.warnings = warnings

    @property
    def generated(self):
        """Latest check/review date in the data (not today), so builds are reproducible."""
        return max(d for r in self.rules.values() for d in (r.get("status_checked"), r.get("reviewed_on")) if d)

    def vocab(self):
        return {"doc_type": sorted(DOC_TYPES), "origin_sector": sorted(ORIGIN_SECTORS),
                "energy_channel": sorted(CHANNELS), "status": STATUSES,
                "verification": VERIFICATION, "source_type": sorted(SOURCE_TYPES),
                "link_basis": sorted(LINK_BASIS), "binding": ["", "no"], "technologies": TECHNOLOGIES}


def split(v):
    return [x.strip() for x in (v or "").split(";") if x.strip()]


def read_csv(path):
    with path.open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        return list(reader), reader.fieldnames


def load():
    errors, warnings = [], []
    categories = {c["id"]: c for c in sorted(read_csv(DATA / "categories.csv")[0], key=lambda c: int(c["order"]))}
    topics = {r["id"]: r for r in read_csv(DATA / "topics.csv")[0]}
    for t in topics.values():
        if t.get("category") not in categories:
            errors.append(f"topics.csv {t['id']}: category '{t.get('category')}' not in data/categories.csv")
    countries = {}
    for c in read_csv(DATA / "countries.csv")[0]:
        c["hierarchy"] = split(c["hierarchy"])
        c["sources"] = [dict(zip(("name", "url"), s.split("|", 1))) for s in split(c["sources"])]
        countries[c["code"]] = c
    fields = read_csv(DATA / "fields.csv")[0]
    rows, columns = read_csv(DATA / "rules.csv")

    by_id = {}
    for i, r in enumerate(rows, start=2):  # line 1 is the header
        rid = (r.get("id") or "").strip()
        where = f"line {i} ({rid or 'no id'})"
        for f in REQUIRED:
            if not (r.get(f) or "").strip():
                errors.append(f"{where}: missing {f}")
        if rid in by_id:
            errors.append(f"{where}: duplicate id")
        if r.get("country") not in countries:
            errors.append(f"{where}: country '{r.get('country')}' not in data/countries.csv")
        elif not rid.startswith(r["country"] + "-"):
            errors.append(f"{where}: id should start with the country code")
        for f, allowed in [("doc_type", DOC_TYPES), ("origin_sector", ORIGIN_SECTORS), ("status", STATUSES),
                           ("verification", VERIFICATION), ("source_type", SOURCE_TYPES)]:
            if r.get(f) and r[f] not in allowed:
                errors.append(f"{where}: {f} '{r[f]}' not in {sorted(allowed)}")
        for f in LIST_FIELDS:
            r[f] = split(r.get(f))
        for c in r["energy_channel"]:
            if c not in CHANNELS:
                errors.append(f"{where}: energy_channel '{c}' not in {sorted(CHANNELS)}")
        for t in r["topics"]:
            if t not in topics:
                errors.append(f"{where}: topic '{t}' not in data/topics.csv")
        for t in r["technologies"]:
            if t not in TECHNOLOGIES:
                errors.append(f"{where}: technology '{t}' not in {TECHNOLOGIES}")
        r["categories"] = [c for c in categories if any(topics.get(t, {}).get("category") == c for t in r["topics"])]
        for f in ["date_signed", "date_in_force", "status_checked", "reviewed_on"]:
            v = (r.get(f) or "").strip()
            if v and not DATE_RE.match(v):
                errors.append(f"{where}: {f} '{v}' must be YYYY, YYYY-MM or YYYY-MM-DD")
            elif v and int(v[:4]) > 2400:
                errors.append(f"{where}: {f} '{v}' looks like a Buddhist Era year; convert to Gregorian (B.E. − 543)")
        if (r.get("binding") or "") not in {"", "yes", "no"}:
            errors.append(f"{where}: binding must be empty, 'yes' or 'no'")
        if (r.get("link_basis") or "") not in LINK_BASIS:
            errors.append(f"{where}: link_basis '{r.get('link_basis')}' not in {sorted(LINK_BASIS - {''})}")
        j = (r.get("jurisdiction") or "").strip()
        if j and not (JURISDICTION_RE.match(j) and j.startswith(r.get("country", "") + "-")):
            errors.append(f"{where}: jurisdiction '{j}' should look like '{r.get('country')}-XXX' (empty = national)")
        if r.get("verification") == "verified" and not (r.get("reviewed_by") and r.get("reviewed_on")):
            errors.append(f"{where}: verified rows need reviewed_by and reviewed_on")
        if rid:
            r["slug"] = rid.lower()
            by_id[rid] = r

    for r in by_id.values():
        for _, back in LINKS:
            r[back] = []
    for rid, r in by_id.items():
        for f, back in LINKS:
            for target in r[f]:
                if target == rid:
                    errors.append(f"{rid}: {f} points to itself")
                elif target not in by_id:
                    errors.append(f"{rid}: {f} unknown id '{target}'")
                else:
                    by_id[target][back].append(rid)

    # Status consistency: statuses that contradict the links. Draft and pending rules
    # don't change anything yet, so they don't count as amending or revoking.
    def effective(ids):
        return [x for x in ids if by_id[x]["status"] not in NOT_YET]

    for rid, r in by_id.items():
        s = r["status"]
        revokers, amenders = effective(r["revoked_by"]), effective(r["amended_by"])
        if revokers and s not in ENDED:
            warnings.append(f"{rid}: revoked by {revokers} but status is '{s}'")
        if s in {"revoked", "replaced"} and not revokers:
            warnings.append(f"{rid}: status '{s}' but no rule in force revokes it (missing link or row?)")
        if amenders and s == "in force":
            warnings.append(f"{rid}: amended by {amenders} but status is 'in force'")
        if s == "amended" and not amenders:
            warnings.append(f"{rid}: status 'amended' but no rule in force amends it")
        if (r["amends"] or r["revokes"]) and not r.get("link_basis") and "link_basis" in columns:
            warnings.append(f"{rid}: has amends/revokes links but no link_basis")

    return Data(by_id, columns, topics, countries, fields, errors, warnings, categories)


def report(data):
    for w in data.warnings:
        print("warning:", w)
    for e in data.errors:
        print("ERROR:", e)
    print(f"{len(data.rules)} rules, {len(data.errors)} errors, {len(data.warnings)} warnings")
    return not data.errors


if __name__ == "__main__":
    sys.exit(0 if report(load()) else 1)
