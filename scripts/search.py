"""Load and validate the search framework in data/search/ (see docs/SEARCH-PROTOCOL.md).

Used by search_plan.py, check_search.py and scan_portals.py.
"""
import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SEARCH = ROOT / "data" / "search"

TIERS = {"1", "2", "3", "4"}
ACCESS = {"open", "partial", "restricted", "unreachable", "unknown"}
STRATEGIES = {"enumeration", "keyword", "citation", "monitoring", "expert", "scouting"}
MODULE_STATUS = {"active", "planned", "closed"}
DECISIONS = {"include", "exclude", "defer"}
STAGES = {"title", "full-text"}
EXCLUSION_REASONS = {
    "E1": "Outside the module's topics or without an energy channel",
    "E2": "Administrative or personnel matter",
    "E3": "Routine periodic notice that sets a value under an existing rule",
    "E4": "Individual decision applying a rule to a single party",
    "E5": "Announcement or statement without a document of legal or formal policy effect",
    "E6": "Duplicate of an instrument already recorded",
    "E7": "Draft that has not reached a formal stage",
}
GENERAL = "_general"  # vocabulary pseudo-topic: generic energy terms used by the weekly scan
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def split(v):
    return [x.strip() for x in (v or "").split(";") if x.strip()]


def read(name):
    with (SEARCH / name).open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def load():
    modules = read("modules.csv")
    for m in modules:
        m["countries"], m["topics"] = split(m["countries"]), split(m["topics"])
    sources = read("sources.csv")
    for s in sources:
        s["languages"] = split(s["languages"])
    vocab = {}
    for v in read("vocabulary.csv"):
        vocab[(v["topic"], v["language"])] = {"terms": split(v["terms"]), "exclude": split(v["exclude"]),
                                              "status": v["status"]}
    return {"modules": modules, "sources": sources, "vocab": vocab,
            "screening": read("screening.csv"), "log": read("search-log.csv")}


def languages_for(country, sources):
    """Languages of a country's sources, most common first (English last unless it is the only one)."""
    langs = []
    for s in sources:
        if s["country"] == country:
            for lang in s["languages"]:
                if lang not in langs:
                    langs.append(lang)
    return sorted(langs, key=lambda x: x == "en")


def validate(fw, topic_ids, known_countries):
    """Return (errors, warnings). known_countries: codes in countries.csv or pipeline.csv."""
    errors, warnings = [], []
    ids = set()
    for s in fw["sources"]:
        where = f"sources.csv {s['id']}"
        if s["id"] in ids:
            errors.append(f"{where}: duplicate id")
        ids.add(s["id"])
        if not s["id"].startswith(s["country"].lower() + "-"):
            errors.append(f"{where}: id should start with the lower-case country code")
        if s["country"] not in known_countries:
            errors.append(f"{where}: country {s['country']} not in countries.csv or pipeline.csv")
        if s["tier"] not in TIERS:
            errors.append(f"{where}: tier must be 1-4")
        if s["access"] not in ACCESS:
            errors.append(f"{where}: access '{s['access']}' not in {sorted(ACCESS)}")
        if s["checked"] and not DATE_RE.match(s["checked"]):
            errors.append(f"{where}: checked must be YYYY-MM-DD")
        if s["access"] != "unknown" and not s["checked"]:
            warnings.append(f"{where}: access is '{s['access']}' but no check date")
        if not s["url"].startswith("https://"):
            errors.append(f"{where}: url must start with https://")
    for m in fw["modules"]:
        where = f"modules.csv {m['id']}"
        if m["status"] not in MODULE_STATUS:
            errors.append(f"{where}: status '{m['status']}'")
        for t in m["topics"]:
            if t not in topic_ids:
                errors.append(f"{where}: topic '{t}' not in topics.csv")
        for c in m["countries"]:
            if c not in known_countries:
                errors.append(f"{where}: country '{c}' unknown")
            elif not any(s["country"] == c for s in fw["sources"]):
                errors.append(f"{where}: no sources registered for {c}")
            elif m["status"] == "active":
                for lang in languages_for(c, fw["sources"]):
                    missing = [t for t in m["topics"] if (t, lang) not in fw["vocab"]]
                    if missing:
                        warnings.append(f"{where}: no '{lang}' vocabulary for {c} topics {', '.join(missing)}")
    for (t, lang) in fw["vocab"]:
        if t != GENERAL and t not in topic_ids:
            errors.append(f"vocabulary.csv: topic '{t}' not in topics.csv")
    for n, r in enumerate(fw["screening"], start=2):
        where = f"screening.csv line {n}"
        if r["decision"] not in DECISIONS:
            errors.append(f"{where}: decision '{r['decision']}'")
        if r["stage"] not in STAGES:
            errors.append(f"{where}: stage '{r['stage']}'")
        if r["decision"] == "exclude" and r["reason"] not in EXCLUSION_REASONS:
            errors.append(f"{where}: exclusions need a reason code E1-E7")
        if r["strategy"] not in STRATEGIES:
            errors.append(f"{where}: strategy '{r['strategy']}'")
        if r["source_id"] and r["source_id"] not in ids:
            errors.append(f"{where}: unknown source '{r['source_id']}'")
    for n, r in enumerate(fw["log"], start=2):
        where = f"search-log.csv line {n}"
        if r["strategy"] not in STRATEGIES:
            errors.append(f"{where}: strategy '{r['strategy']}'")
        if r["source_id"] and r["source_id"] not in ids:
            errors.append(f"{where}: unknown source '{r['source_id']}'")
        if not DATE_RE.match(r["date"]):
            errors.append(f"{where}: date must be YYYY-MM-DD")
    return errors, warnings
