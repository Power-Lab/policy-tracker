#!/usr/bin/env python3
"""Scan official legal portals for new documents that may affect energy.

    python3 scripts/scan_portals.py            fetch every source, update data/watch/seen.json,
                                               write scan_report.md with new energy-related documents
    python3 scripts/scan_portals.py --file vn-chinhphu page.html    parse a saved page (for testing)

Run weekly by .github/workflows/portal-scan.yml, which turns the report into an
issue for a person to triage. Nothing is added to rules.csv automatically.
Configuration comes from the search framework (docs/SEARCH-PROTOCOL.md):
sources with an adapter in data/search/sources.csv, per-source options in
data/search/adapters.json, and keywords from data/search/vocabulary.csv (the
_general set flags a document; topic sets suggest its topics). A source that
fails to load is reported and skipped; the others still run.
"""
import csv
import html
import io
import json
import os
import re
import sys
import urllib.request
from datetime import date
from pathlib import Path
from urllib.parse import urljoin

sys.path.insert(0, str(Path(__file__).resolve().parent))
import search  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
WATCH = ROOT / "data" / "watch"
UA = ("Mozilla/5.0 (compatible; PowerLab-Policy-Tracker/1.0; +https://github.com/"
      + (os.environ.get("GITHUB_REPOSITORY") or "Power-Lab/policy-tracker") + ")")


def clean(t):
    return html.unescape(" ".join(re.sub(r"<[^>]+>", " ", t).split()))


def parse_chinhphu(page, base):
    """vanban.chinhphu.vn list rows: document code, issue date, summary, docid link."""
    out = []
    for row in re.findall(r"<tr>(.*?)</tr>", page, re.S):
        m_id = re.search(r"href='([^']*docid=(\d+))'", row)
        m_code = re.search(r'<span class="code">(.*?)</span>', row, re.S)
        m_sum = re.search(r'<span class="substract">(.*?)</span>', row, re.S)
        if not (m_id and m_code and m_sum):
            continue
        m_date = re.search(r'<span class="issued-date">\s*(\d{2})/(\d{2})/(\d{4})', row)
        out.append({"key": m_id.group(2), "code": clean(m_code.group(1)), "title": clean(m_sum.group(1)),
                    "date": f"{m_date.group(3)}-{m_date.group(2)}-{m_date.group(1)}" if m_date else "",
                    "url": urljoin(base, m_id.group(1))})
    return out


def parse_esdm(page, base):
    """jdih.esdm.go.id home page cards: full title, document id and PDF link."""
    out, seen = [], set()
    for m in re.finditer(r'newsbar-card-title"\s+title="([^"]+)">\s*<a[^>]+href="(/dokumen/view\?id=(\d+))"(.*?)</div>',
                         page, re.S):
        title, href, key, rest = clean(m.group(1)), m.group(2), m.group(3), m.group(4)
        if key in seen:
            continue
        seen.add(key)
        num = re.search(r"Nomor\s+([\w./-]+)(?:\s+Tahun\s+(\d{4}))?", title)
        pdf = re.search(r'href="(/dokumen/download\?id=[^"]+)"', rest)
        out.append({"key": key, "code": (num.group(1) + ("/" + num.group(2) if num.group(2) else "")) if num else "",
                    "title": title, "date": "", "url": urljoin(base, href),
                    "file": urljoin(base, pdf.group(1)) if pdf else ""})
    return out


def parse_links(page, base, pattern):
    """Generic: every link whose href matches `pattern` and has a descriptive text."""
    out, seen = [], set()
    for href, text in re.findall(r'<a[^>]+href=["\']([^"\']+)["\'][^>]*>(.*?)</a>', page, re.S):
        title = clean(text)
        if len(title) < 25 or not re.search(pattern, href, re.I):
            continue
        url = urljoin(base, href)
        if url in seen:
            continue
        seen.add(url)
        out.append({"key": url, "code": "", "title": title, "date": "", "url": url})
    return out


def parse(source, page):
    if source["adapter"] == "chinhphu":
        items = parse_chinhphu(page, source["url"])
    elif source["adapter"] == "esdm":
        items = parse_esdm(page, source["url"])
    else:
        items = parse_links(page, source["url"], source.get("link_pattern", "."))
    # Per-source filters: keep only titles matching "require", drop titles matching any "skip".
    if source.get("require"):
        items = [i for i in items if re.search(source["require"], i["title"], re.I)]
    for pat in source.get("skip", []):
        items = [i for i in items if not re.search(pat, i["title"], re.I)]
    return items


def hits_for(source, item, cfg):
    """Why an item is flagged: keyword matches, or the source itself if every document is in scope."""
    if source.get("match_all"):
        return [source.get("match_label", "source in scope")]
    lang = source["language"]
    return relevant(item, cfg["keywords"].get(lang, []), cfg.get("exclude", {}).get(lang, []))


def relevant(item, words, exclude=()):
    """Keywords found as whole words, after removing excluded phrases (e.g. "điện tử", electronic)."""
    text = f" {item['code']} {item['title']} ".lower()
    for x in exclude:
        text = text.replace(x.lower(), " ")
    return [w for w in words if re.search(rf"(?<!\w){re.escape(w.lower())}(?!\w)", text)]


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "en,vi,id"})
    with urllib.request.urlopen(req, timeout=40) as r:
        return r.read().decode("utf-8", errors="replace")


def load_config():
    """Scan configuration from the search framework, in the shape the scanner uses."""
    fw = search.load()
    adapters = json.loads((search.SEARCH / "adapters.json").read_text(encoding="utf-8"))
    sources = []
    for s in fw["sources"]:
        if s["adapter"]:
            sources.append({"id": s["id"], "country": s["country"], "name": s["name"], "url": s["url"],
                            "adapter": s["adapter"], "language": s["languages"][0], **adapters.get(s["id"], {})})
    keywords, exclude, topics = {}, {}, {}
    for (topic, lang), v in fw["vocab"].items():
        exclude.setdefault(lang, [])
        exclude[lang] += [x for x in v["exclude"] if x not in exclude[lang]]
        if topic == search.GENERAL:
            keywords[lang] = v["terms"]
        else:
            topics.setdefault(lang, {})[topic] = v["terms"]
    return {"sources": sources, "keywords": keywords, "exclude": exclude, "topics": topics}


def topics_for(item, cfg, lang):
    """Topic ids whose vocabulary matches the item (a suggestion for the person triaging)."""
    excl = cfg.get("exclude", {}).get(lang, [])
    return [t for t, terms in cfg.get("topics", {}).get(lang, {}).items() if relevant(item, terms, excl)]


def main():
    cfg = load_config()
    if len(sys.argv) == 4 and sys.argv[1] == "--file":
        src = next(s for s in cfg["sources"] if s["id"] == sys.argv[2])
        for item in parse(src, Path(sys.argv[3]).read_text(encoding="utf-8", errors="replace")):
            hits = hits_for(src, item, cfg)
            tps = topics_for(item, cfg, src["language"]) if hits else []
            print(("★ " if hits else "  ") + f"{item['date']} {item['code']} {item['title'][:100]}"
                  + (f"  [{', '.join(hits)}]" if hits else "") + (f"  topics: {', '.join(tps)}" if tps else ""))
        return

    seen_path = WATCH / "seen.json"
    try:
        seen = json.loads(seen_path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        seen = {}  # first run, or an empty/corrupt file: start a new baseline
    report, failures, total_new, all_hits, log = [], [], 0, [], []
    for src in cfg["sources"]:
        try:
            items = parse(src, fetch(src["url"]))
        except Exception as e:  # noqa: BLE001 — one broken portal must not stop the scan
            failures.append(f"- **{src['name']}**: could not load ({type(e).__name__}: {str(e)[:120]})")
            continue
        if not items:
            failures.append(f"- **{src['name']}**: loaded, but no documents were recognised (layout may have changed).")
            continue
        known = set(seen.get(src["id"], {}).get("keys", []))
        first_run = not known
        new = [i for i in items if i["key"] not in known]
        hits = [(i, hits_for(src, i, cfg)) for i in new]
        hits = [(i, h) for i, h in hits if h]
        log.append([f"{date.today().isoformat()}-scan", date.today().isoformat(), "", src["country"], src["id"],
                    "monitoring", src["language"], "", len(items), len(hits), "portal-scan",
                    "baseline" if first_run else ""])
        seen[src["id"]] = {"keys": sorted(known | {i["key"] for i in items})[-2000:], "checked": date.today().isoformat()}
        if first_run:
            report.append(f"### {src['name']}\n\nFirst scan: recorded {len(items)} existing documents as a baseline.\n")
            continue
        total_new += len(hits)
        all_hits += [{**i, "source": src["id"], "country": src["country"], "language": src["language"],
                      "topics": topics_for(i, cfg, src["language"])} for i, _ in hits]
        if hits:
            report.append(f"\n### {src['name']}\n\n{len(new)} new document(s), {len(hits)} mention energy keywords:\n")
            for i, h in hits:
                tps = topics_for(i, cfg, src["language"])
                report.append(f"- [ ] [{i['code'] or 'document'}]({i['url']}) {i['date']}: {i['title'][:220]}"
                              + (f" ([PDF]({i['file']}))" if i.get("file") else "")
                              + f" _(matched: {', '.join(h[:4])}"
                              + (f"; suggested topics: {', '.join(tps)}" if tps else "") + ")_")
    seen_path.write_text(json.dumps(seen, ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    md = [f"Weekly scan of official portals, {date.today().isoformat()}.", ""]
    md += report or ["No new energy-related documents found."]
    if failures:
        md += ["", "#### Sources that need attention", ""] + failures
    md += ["", "Screen each item under the eligibility criteria in docs/SEARCH-PROTOCOL.md: record the decision in "
               "`data/search/screening.csv` (strategy `monitoring`) and add included instruments to `data/rules.csv`. "
               "Sources and keywords are in `data/search/`."]
    Path("scan_report.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    Path("scan_hits.json").write_text(json.dumps(all_hits, ensure_ascii=False, indent=1), encoding="utf-8")
    buf = io.StringIO()
    csv.writer(buf, lineterminator="\n").writerows(log)
    Path("scan_log.csv").write_text(buf.getvalue(), encoding="utf-8")
    Path("scan_result.json").write_text(json.dumps({"new": total_new, "failures": len(failures)}), encoding="utf-8")
    print("\n".join(md))


if __name__ == "__main__":
    main()
