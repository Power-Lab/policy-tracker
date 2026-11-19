#!/usr/bin/env python3
"""Generate a search plan for a module of the search protocol (docs/SEARCH-PROTOCOL.md).

    python3 scripts/search_plan.py power-core
    python3 scripts/search_plan.py power-core --country TH --topic rooftop-solar
    python3 scripts/search_plan.py asean-expansion --out plan.md

For each country in the module the plan lists the registered sources in tier
order with their access status, the keyword queries for each topic in each
language (for portal search and for domain-restricted web search), the
recorded instruments to use for citation chasing, and the monitoring status.
"""
import argparse
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path
from urllib.parse import urlparse

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build  # noqa: E402
import search  # noqa: E402

LANG_NAMES = {"en": "English", "id": "Indonesian", "vi": "Vietnamese", "th": "Thai", "ms": "Malay", "km": "Khmer",
              "lo": "Lao", "my": "Burmese", "pt": "Portuguese"}
SEARCHABLE = {"open", "partial", "unknown"}


def quote(term):
    return f'"{term}"' if " " in term or "," in term else term


def portal_query(terms):
    return " OR ".join(quote(t) for t in terms)


def web_query(terms, domains):
    sites = " OR ".join(f"site:{d}" for d in domains)
    return f"({portal_query(terms)}) ({sites})" if domains else portal_query(terms)


def plan(module, fw, data, only_country=None, only_topic=None):
    topics = [t for t in module["topics"] if not only_topic or t == only_topic]
    countries = [c for c in module["countries"] if not only_country or c == only_country]
    names = {c: (data.countries[c]["name"] if c in data.countries else c) for c in countries}
    out = [f"# Search plan: {module['name']} (`{module['id']}`)", "",
           f"Generated {date.today().isoformat()} from `data/search/` by `scripts/search_plan.py`. "
           f"Protocol: docs/SEARCH-PROTOCOL.md. Instruments signed from {module['period_from']} onward, "
           "plus earlier instruments that included ones amend, revoke, implement or cite.", "",
           f"Topics: {', '.join(data.topics[t]['label'] for t in topics)}.", ""]
    rules_by_country = defaultdict(list)
    for r in data.rules.values():
        rules_by_country[r["country"]].append(r)

    for c in countries:
        srcs = sorted((s for s in fw["sources"] if s["country"] == c), key=lambda s: (s["tier"], s["id"]))
        langs = search.languages_for(c, fw["sources"])
        out += [f"## {names[c]} ({c})", "", "### 1. Sources", "",
                "| Tier | Source | Languages | Access (checked) | How to search |", "| --- | --- | --- | --- | --- |"]
        for s in srcs:
            how = ("enumerate listings by year and type" if s["tier"] in {"1", "2"} else
                   "dates, numbers and texts; keyword search" if s["tier"] == "3" else "discovery only")
            if s["access"] in {"restricted", "unreachable"}:
                how += "; **manual search by a reviewer or from within the country**"
            out.append(f"| {s['tier']} | [{s['name']}]({s['url']}) | {', '.join(s['languages'])} | "
                       f"{s['access']} ({s['checked'] or 'not checked'}) | {how} |")
        open_domains = [urlparse(s["url"]).netloc for s in srcs if s["access"] in SEARCHABLE and s["tier"] != "4"]

        out += ["", "### 2. Enumeration", ""]
        enum = [s for s in srcs if s["tier"] in {"1", "2"}]
        out += [f"- [ ] {s['name']}: browse every listing page from {module['period_from']}; record each relevant "
                f"instrument in `screening.csv` (strategy `enumeration`)." for s in enum] or ["- No tier 1–2 source registered."]

        out += ["", "### 3. Keyword queries", "",
                "Run each query on the portals' own search where available, and as a web search restricted to the "
                "open official domains. Log each run in `search-log.csv` (strategy `keyword`).", ""]
        for t in topics:
            out.append(f"**{data.topics[t]['label']}**")
            out.append("")
            for lang in langs:
                v = fw["vocab"].get((t, lang))
                if not v:
                    out.append(f"- {LANG_NAMES.get(lang, lang)}: _no vocabulary yet; add it to `vocabulary.csv`_")
                    continue
                note = "" if v["status"] == "validated" else " _(draft vocabulary)_"
                out.append(f"- {LANG_NAMES.get(lang, lang)}{note}")
                out.append(f"  - portal: `{portal_query(v['terms'])}`")
                if open_domains:
                    out.append(f"  - web: `{web_query(v['terms'], open_domains)}`")
                if v["exclude"]:
                    out.append(f"  - discard results containing: {', '.join(v['exclude'])}")
            out.append("")

        recorded = [r for r in rules_by_country.get(c, []) if set(r["topics"]) & set(topics)]
        out += ["### 4. Citation chasing", ""]
        if recorded:
            open_chains = [r for r in recorded if "not a row" in r["notes"] or "not rows" in r["notes"]
                           or (r["status"] == "amended" and not r["amended_by"])]
            out += [f"{len(recorded)} recorded instruments in these topics. For each, check its preamble and final "
                    "provisions for earlier instruments (backward), and search its number for later amending, "
                    "implementing or revoking instruments (forward)."]
            if open_chains:
                out += ["", "Instruments whose notes or status point to related instruments not yet recorded:", ""]
                out += [f"- [ ] {r['short_name']} (`{r['id']}`): {r['notes'][:160]}" for r in open_chains]
        else:
            out.append("No instruments recorded yet: start from the main instruments listed in the country's "
                       "scouting report.")
        out += ["", "### 5. Monitoring", ""]
        monitored = [s for s in srcs if s["adapter"]]
        candidates = [s for s in srcs if not s["adapter"] and s["access"] == "open" and s["tier"] in {"1", "2"}]
        out += [f"- Monitored weekly: {', '.join(s['name'] for s in monitored) or 'none'}.",
                f"- Open tier 1–2 sources without an adapter (candidates for monitoring): "
                f"{', '.join(s['name'] for s in candidates) or 'none'}.", ""]
    return "\n".join(out) + "\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("module")
    ap.add_argument("--country")
    ap.add_argument("--topic")
    ap.add_argument("--out")
    a = ap.parse_args()
    fw = search.load()
    data = build.load()
    module = next((m for m in fw["modules"] if m["id"] == a.module), None)
    if not module:
        sys.exit(f"unknown module '{a.module}'; modules: {', '.join(m['id'] for m in fw['modules'])}")
    text = plan(module, fw, data, a.country, a.topic)
    if a.out:
        Path(a.out).write_text(text, encoding="utf-8")
        print("wrote", a.out)
    else:
        print(text)


if __name__ == "__main__":
    main()
