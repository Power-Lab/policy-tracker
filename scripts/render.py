#!/usr/bin/env python3
"""Build the static site into _site/.

    python3 scripts/render.py
    python3 -m http.server -d _site 8000

Every page is pre-rendered from data/*.csv with the Jinja2 templates in
templates/. Charts (amendment chains, timelines) are drawn here as inline SVG
so they work without JavaScript. All links are relative, so the site works
under /policy-tracker/, on a custom domain or from a local folder.
"""
import csv
from datetime import date
import io
import json
import os
import shutil
import sys
from collections import defaultdict
from html import escape
from pathlib import Path
from urllib.parse import urlparse

from jinja2 import Environment, FileSystemLoader, StrictUndefined, select_autoescape
from markupsafe import Markup

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build  # noqa: E402
import search  # noqa: E402
import history  # noqa: E402

ROOT = build.ROOT
OUT = ROOT / "_site"
# The repository the site is built from (set by GitHub Actions); the site URL follows from it
# unless SITE_URL is set, e.g. for a custom domain.
REPO = os.environ.get("GITHUB_REPOSITORY") or "Power-Lab/policy-tracker"
_owner, _name = REPO.split("/", 1)
SITE_URL = os.environ.get("SITE_URL") or f"https://{_owner.lower()}.github.io/{_name}/"
SITE_NAME = "Power Transformation Lab Policy Tracker"
CONFIG = json.loads((ROOT / "config.json").read_text(encoding="utf-8"))
# listed: allow search engines to index the site; downloads: publish the CSV files and link them.
SITE_OPTS = {"listed": True, "downloads": True, **CONFIG.get("site", {})}


# ---------------------------------------------------------------- helpers

def to_year(d):
    """'2024', '2024-01' or '2024-01-29' → fractional year; partial dates sit mid-period."""
    if not d:
        return None
    parts = [int(p) for p in d.split("-")]
    y, m, day = (parts + [7, 15])[:3] if len(parts) == 1 else (parts + [15])[:3]
    return y + (m - 1) / 12 + (day - 1) / 365


def fmt_date(d):
    if not d:
        return "—"
    months = "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split()
    p = d.split("-")
    if len(p) == 1:
        return p[0]
    if len(p) == 2:
        return f"{months[int(p[1]) - 1]} {p[0]}"
    return f"{int(p[2])} {months[int(p[1]) - 1]} {p[0]}"


def plot_date(r):
    """Date used to place and sort an instrument: date signed, or date in force when that is all that is known."""
    return r.get("date_signed") or r.get("date_in_force") or ""


def sort_key_date(r):
    return to_year(plot_date(r)) or 9999


def component(data, rule):
    """Every rule reachable from `rule` through amend, revoke or override links, oldest first.

    Implementing rules are left out on purpose: following them would pull every decree
    under a framework law into one chain. They are listed separately on rule pages.
    """
    seen, queue = {rule["id"]}, [rule["id"]]
    while queue:
        cur = data.rules[queue.pop(0)]
        for rid in (cur["amends"] + cur["revokes"] + cur["overrides"]
                    + cur["amended_by"] + cur["revoked_by"] + cur["overridden_by"]):
            if rid not in seen:
                seen.add(rid)
                queue.append(rid)
    return sorted((data.rules[i] for i in seen), key=lambda r: (sort_key_date(r), r["id"]))


def group_current(data, rs):
    """Rules that still apply, with pure amendments folded under the rule they amend.

    Returns [(rule, [amending rules])]. An amendment is folded only when every
    rule it amends is also in the list, so nothing disappears.
    """
    cur = sorted((r for r in rs if r["status"] in build.CURRENT), key=lambda r: -sort_key_date(r))
    ids = {r["id"] for r in cur}
    folded = {r["id"] for r in cur if r["amends"] and not r["revokes"] and all(a in ids for a in r["amends"])}
    return [(r, [data.rules[x] for x in r["amended_by"] if x in folded])
            for r in cur if r["id"] not in folded]


def status_slug(s):
    return s.replace(" ", "-")


# ---------------------------------------------------------------- SVG charts

def chain_svg(nodes, current_id, root, compact=False):
    """Amendment chain: one row per rule, x = date signed, curved links newer → older."""
    years = [to_year(plot_date(n)) for n in nodes if plot_date(n)] or [float(date.today().year)]
    lo = int(min(years))
    hi = max(int(max(years)) + 1, lo + 2)
    W, label_w, pad_r = 720, 190, 24
    row_h = 30 if compact else 36
    top = 28
    H = top + len(nodes) * row_h + 6
    x = lambda y: label_w + (y - lo) / (hi - lo) * (W - label_w - pad_r)  # noqa: E731
    pos = {}
    for i, n in enumerate(nodes):
        pos[n["id"]] = (x(to_year(plot_date(n)) or hi), top + i * row_h + row_h / 2)

    out = [f'<svg class="chart chain" viewBox="0 0 {W} {H}" role="img" '
           f'aria-label="Amendment chain of {len(nodes)} rules from {lo} to {hi}">']
    step = 1 if hi - lo <= 8 else 2 if hi - lo <= 16 else 5
    for y in range(lo, hi + 1, step):
        out.append(f'<line class="grid" x1="{x(y):.1f}" x2="{x(y):.1f}" y1="{top - 8}" y2="{H}"/>'
                   f'<text class="axis" x="{x(y):.1f}" y="14" text-anchor="middle">{y}</text>')
    for n in nodes:
        for kind in ("amends", "revokes", "overrides"):
            for t in n[kind]:
                if t in pos:
                    (x1, y1), (x2, y2) = pos[n["id"]], pos[t]
                    mx = min(x1, x2) - 22
                    out.append(f'<path class="edge {kind}" d="M{x1:.1f},{y1:.1f} C{mx:.1f},{y1:.1f} '
                               f'{mx:.1f},{y2:.1f} {x2:.1f},{y2:.1f}"/>')
    for n in nodes:
        cx, cy = pos[n["id"]]
        cur = n["id"] == current_id
        label = escape(n["short_name"])
        out.append(
            f'<a href="{root}rules/{n["slug"]}/"><title>{label}: {escape(n["status"])}, signed '
            f'{escape(fmt_date(n["date_signed"]))}</title>'
            f'<rect class="hit" x="0" y="{cy - row_h / 2:.1f}" width="{W}" height="{row_h}"/>'
            f'<text class="label{" current" if cur else ""}" x="0" y="{cy + 4:.1f}">{label}</text>'
            f'<circle class="dot s-{status_slug(n["status"])}{" current" if cur else ""}" cx="{cx:.1f}" '
            f'cy="{cy:.1f}" r="{7 if cur else 5.5}"/></a>')
    out.append("</svg>")
    return Markup("".join(out))


def swimlane_svg(rules, topics, root, lo=None, hi=None):
    """Timeline with one lane per topic; each rule is a dot in each of its topic lanes."""
    lanes = [t for t in topics.values() if any(t["id"] in r["topics"] for r in rules)]
    years = [to_year(plot_date(r)) for r in rules if plot_date(r)] or [float(date.today().year)]
    lo = lo or int(min(years))
    hi = hi or int(max(years)) + 1
    W, label_w, pad_r, lane_h, top = 900, 230, 20, 34, 26
    H = top + len(lanes) * lane_h + 4
    x = lambda y: label_w + (y - lo) / (hi - lo) * (W - label_w - pad_r)  # noqa: E731
    out = [f'<svg class="chart swimlane" viewBox="0 0 {W} {H}" role="img" '
           f'aria-label="Timeline of {len(rules)} rules by topic, {lo} to {hi}">']
    step = 1 if hi - lo <= 10 else 2 if hi - lo <= 20 else 5
    for y in range(lo, hi + 1, step):
        out.append(f'<line class="grid" x1="{x(y):.1f}" x2="{x(y):.1f}" y1="{top - 8}" y2="{H}"/>'
                   f'<text class="axis" x="{x(y):.1f}" y="14" text-anchor="middle">{y}</text>')
    for i, t in enumerate(lanes):
        cy = top + i * lane_h + lane_h / 2
        out.append(f'<line class="lane" x1="{label_w}" x2="{W - pad_r}" y1="{cy}" y2="{cy}"/>'
                   f'<a href="{root}topics/{t["id"]}/"><text class="label" x="0" y="{cy + 4}">'
                   f'{escape(t["label"])}</text></a>')
        placed = []
        for r in sorted((r for r in rules if t["id"] in r["topics"] and plot_date(r)), key=sort_key_date):
            cx = x(to_year(plot_date(r)))
            # Nudge dots that would overlap within this lane.
            k = sum(1 for p in placed if abs(p - cx) < 9)
            placed.append(cx)
            dy = (0, -8, 8, -15, 15)[k % 5]
            out.append(f'<a href="{root}rules/{r["slug"]}/"><title>{escape(r["short_name"])}: '
                       f'{escape(r["title_english"])} ({escape(r["status"])}, {escape(fmt_date(r["date_signed"]))})'
                       f'</title><circle class="dot s-{status_slug(r["status"])}" cx="{cx:.1f}" '
                       f'cy="{cy + dy:.1f}" r="5.5"/></a>')
    out.append("</svg>")
    return Markup("".join(out))


# ---------------------------------------------------------------- site

def citation(r, country_name):
    url = f"{SITE_URL}rules/{r['slug']}/"
    return (f"{r['short_name']}, “{r['title_english']}”. {r['issuing_body']}, {country_name}, "
            f"signed {fmt_date(r['date_signed'])}. In: {SITE_NAME}, status checked "
            f"{fmt_date(r['status_checked'])}. {url}")


def correction_url(r):
    from urllib.parse import urlencode
    body = (f"Rule: **{r['short_name']}** (`{r['id']}`)\n\n"
            "**What is wrong?**\n\n\n**What should it say?**\n\n\n"
            "**Source (link to the official text if possible)**\n\n")
    return f"https://github.com/{REPO}/issues/new?" + urlencode(
        {"title": f"Correction: {r['short_name']} ({r['id']})", "body": body, "labels": "correction"})


def _update_summary(u):
    parts = []
    if u["added"]:
        parts.append(f"{len(u['added'])} rule(s) added")
    if u["n_changed"]:
        parts.append(f"{u['n_changed']} rule(s) updated")
    parts += [f"{n['r']['short_name']}: {n['field']} {n['old'] or '—'} → {n['new'] or '—'}" for n in u["notable"][:10]]
    return "; ".join(parts)


def main():
    data = build.load()
    if not build.report(data):
        sys.exit(1)
    rules = list(data.rules.values())
    fw = search.load()
    events = history.load()
    rule_history = history.per_rule(events)
    by_date = sorted(rules, key=lambda r: (sort_key_date(r), r["id"]))

    env = Environment(loader=FileSystemLoader(ROOT / "templates"), autoescape=select_autoescape(),
                      undefined=StrictUndefined, trim_blocks=True, lstrip_blocks=True)
    env.filters["date"] = fmt_date
    env.filters["sslug"] = status_slug
    in_prose = {"Philippines": "the Philippines", "United States": "the United States"}  # names that take an article in running text
    names = [in_prose.get(c["name"], c["name"]) for c in data.countries.values()]
    country_names = names[0] if len(names) == 1 else ", ".join(names[:-1]) + " and " + names[-1]
    tech_labels = {"solar-pv": "Solar PV", "wind": "Wind", "batteries": "Batteries", "electric-vehicles": "Electric vehicles",
                   "grid-equipment": "Grid equipment", "hydrogen": "Hydrogen"}
    env.globals.update(categories=data.categories, technologies=build.TECHNOLOGIES, tech_labels=tech_labels,
                       country_names=country_names, site_name=SITE_NAME, site_url=SITE_URL, repo=REPO, topics=data.topics,
                       countries=data.countries, statuses=build.STATUSES, verification=build.VERIFICATION,
                       generated=data.generated, n_rules=len(rules), rules_by_id=data.rules,
                       listed=SITE_OPTS["listed"], downloads=SITE_OPTS["downloads"])

    if OUT.exists():
        shutil.rmtree(OUT)
    shutil.copytree(ROOT / "static", OUT / "assets")
    pages = []

    def page(path, template, title, nav=None, root=None, **ctx):
        """Render `template` to OUT/path (a directory → index.html, or an .html file)."""
        target = OUT / path / "index.html" if not path.endswith(".html") else OUT / path
        depth = len(Path(path).parts) - (1 if path.endswith(".html") else 0)
        root = "../" * depth if root is None else root
        target.parent.mkdir(parents=True, exist_ok=True)
        html = env.get_template(template).render(root=root, title=title, nav=nav, path=path, **ctx)
        target.write_text(html, encoding="utf-8")
        pages.append(path)

    def counts(rs):
        c = {"total": len(rs), "current": sum(r["status"] in build.CURRENT for r in rs),
             "verified": sum(r["verification"] == "verified" for r in rs)}
        c["by_status"] = {s: sum(r["status"] == s for r in rs) for s in build.STATUSES}
        return c

    # Home
    featured = data.rules.get("ID-PERMEN-ESDM-2024-02") or by_date[-1]
    page("", "home.html", None, nav="home",
         stats=counts(rules), recent=sorted(rules, key=lambda r: (-sort_key_date(r), r["id"]))[:6],
         featured=featured, featured_chain=chain_svg(component(data, featured), featured["id"], "", compact=True),
         country_stats={c: counts([r for r in rules if r["country"] == c]) for c in data.countries},
         topic_counts={t: sum(t in r["topics"] for r in rules) for t in data.topics})

    # Explore
    page("rules", "explore.html", "Explore rules", nav="rules",
         rules=sorted(rules, key=lambda r: (-sort_key_date(r), r["id"])),
         doc_types=sorted({r["doc_type"] for r in rules}))

    # Rule pages
    for r in rules:
        comp = component(data, r)
        chain_ids = {n["id"] for n in comp}
        related = sorted((o for o in rules if o["country"] == r["country"] and o["id"] not in chain_ids
                          and set(o["topics"]) & set(r["topics"])), key=lambda o: -sort_key_date(o))[:6]
        page(f"rules/{r['slug']}", "rule.html", r["short_name"], nav="rules", r=r,
             country=data.countries[r["country"]],
             chain=chain_svg(comp, r["id"], "../../") if len(comp) > 1 else None, chain_nodes=comp,
             related=related, cite=citation(r, data.countries[r["country"]]["name"]),
             correction_url=correction_url(r), changes=rule_history.get(r["id"], []))

    # Countries
    pipeline = []
    if (ROOT / "data" / "pipeline.csv").exists():
        pipeline = sorted((p for p in build.read_csv(ROOT / "data" / "pipeline.csv")[0] if p["code"] not in data.countries),
                          key=lambda p: int(p["order"]))
        for p in pipeline:
            p["sources"] = [dict(zip(("name", "url"), x.split("|", 1))) for x in build.split(p["sources"])]
    page("countries", "countries.html", "Countries", nav="countries", pipeline=pipeline,
         country_stats={c: counts([r for r in rules if r["country"] == c]) for c in data.countries})
    for code, c in data.countries.items():
        rs = [r for r in by_date if r["country"] == code]
        by_topic = defaultdict(list)
        for r in sorted(rs, key=lambda r: -sort_key_date(r)):
            for t in r["topics"]:
                by_topic[t].append(r)
        page(f"countries/{code.lower()}", "country.html", c["name"], nav="countries", c=c, rules=rs,
             registry=sorted((s for s in fw["sources"] if s["country"] == code), key=lambda s: (s["tier"], s["name"])),
             stats=counts(rs), timeline=swimlane_svg(rs, data.topics, "../../"),
             by_topic=[(data.topics[t], group_current(data, by_topic[t]),
                        [r for r in by_topic[t] if r["status"] in build.ENDED],
                        [r for r in by_topic[t] if r["status"] in build.NOT_YET]) for t in data.topics if by_topic[t]])

    # Topics
    page("topics", "topics.html", "Topics", nav="topics",
         topic_counts={t: {c: sum(t in r["topics"] and r["country"] == c for r in rules) for c in data.countries}
                       for t in data.topics})
    for tid, t in data.topics.items():
        per_country = []
        for code, c in data.countries.items():
            rs = sorted((r for r in rules if r["country"] == code and tid in r["topics"]),
                        key=lambda r: -sort_key_date(r))
            current = [r for r in rs if r["status"] in build.CURRENT]
            # Chain diagrams: one per connected group that contains a current rule, de-duplicated.
            chains, shown = [], set()
            for r in current:
                if r["id"] in shown:
                    continue
                comp = component(data, r)
                shown |= {n["id"] for n in comp}
                if len(comp) > 1:
                    chains.append(chain_svg(comp, r["id"], "../../", compact=True))
            per_country.append({"c": c, "rules": rs, "current": group_current(data, rs), "chains": chains,
                                "ended": [r for r in rs if r["status"] in build.ENDED],
                                "upcoming": [r for r in rs if r["status"] in build.NOT_YET]})
        page(f"topics/{tid}", "topic.html", t["label"], nav="topics", t=t, per_country=per_country)

    # Compare
    matrix = []
    for tid, t in data.topics.items():
        row = {"t": t, "cells": []}
        for code in data.countries:
            rs = [r for r in rules if r["country"] == code and tid in r["topics"]]
            row["cells"].append({"current": group_current(data, rs),
                                 "ended": sum(r["status"] in build.ENDED for r in rs),
                                 "upcoming": [r for r in rs if r["status"] in build.NOT_YET], "code": code})
        matrix.append(row)
    page("compare", "compare.html", "Compare countries", nav="compare", matrix=matrix)

    # Timeline
    all_years = [to_year(plot_date(r)) for r in rules if plot_date(r)]
    lo, hi = int(min(all_years)), int(max(all_years)) + 1
    page("timeline", "timeline.html", "Timeline", nav="timeline",
         lanes=[(c, swimlane_svg([r for r in rules if r["country"] == code], data.topics, "../", lo, hi))
                for code, c in data.countries.items()])

    # Data, about, review, 404
    page("data", "data.html", "Data", nav="data", fields=data.fields, vocab=data.vocab())
    page("about", "about.html", "About", nav="about")

    # Updates: one entry per commit that changed the data, newest first.
    updates = []
    for e in reversed(events):
        notable = []
        for rid, ch in e["changed"].items():
            for f, a, b in ch:
                if f in history.NOTABLE and rid in data.rules:
                    notable.append({"r": data.rules[rid], "field": f, "old": a, "new": b})
        updates.append({**e, "notable": notable,
                        "added_rules": [data.rules[i] for i in e["added"] if i in data.rules],
                        "n_changed": len(e["changed"])})
    page("updates", "updates.html", "Updates", nav="updates", updates=updates)
    feed_entries = "".join(
        f"<entry><title>{escape(u['subject'])}</title><id>{SITE_URL}updates/#{u['sha'][:12]}</id>"
        f"<link href=\"{SITE_URL}updates/#{u['sha'][:12]}\"/><updated>{u['date']}T00:00:00Z</updated>"
        f"<summary>{escape(_update_summary(u))}</summary></entry>" for u in updates[:50])
    (OUT / "updates").mkdir(exist_ok=True)
    (OUT / "updates" / "feed.xml").write_text(
        '<?xml version="1.0" encoding="utf-8"?><feed xmlns="http://www.w3.org/2005/Atom">'
        f"<title>{SITE_NAME}: updates</title><id>{SITE_URL}updates/</id><author><name>{SITE_NAME}</name></author>"
        f'<link href="{SITE_URL}updates/"/><link rel="self" href="{SITE_URL}updates/feed.xml"/>'
        f"<updated>{(updates[0]['date'] if updates else data.generated)}T00:00:00Z</updated>{feed_entries}</feed>",
        encoding="utf-8")
    page("review", "review.html", "Reviewer view", nav=None)
    # GitHub Pages serves 404.html at any depth, so its links must be absolute.
    page("404.html", "404.html", "Page not found", nav=None, root=urlparse(SITE_URL).path)
    # Redirects from the proof-of-concept URLs.
    page("review.html", "redirect.html", "Moved", nav=None, to="review/")

    # Data downloads
    export = [{k: v for k, v in r.items()} for r in rules]
    (OUT / "data").mkdir(exist_ok=True)
    (OUT / "data" / "rules.json").write_text(json.dumps({
        "generated": data.generated, "columns": data.columns, "vocab": data.vocab(), "config": CONFIG,
        "countries": {k: v["name"] for k, v in data.countries.items()},
        "topics": list(data.topics.values()), "rules": export}, ensure_ascii=False, indent=1), encoding="utf-8")
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    cols = data.columns + [back for _, back in build.LINKS]
    w.writerow(cols)
    for r in rules:
        w.writerow([";".join(r[c]) if isinstance(r.get(c), list) else r.get(c, "") for c in cols])
    if SITE_OPTS["downloads"]:
        (OUT / "data" / "rules.csv").write_text(buf.getvalue(), encoding="utf-8")
        shutil.copy(search.SEARCH / "sources.csv", OUT / "data" / "sources.csv")
    (OUT / ".nojekyll").write_text("")

    # Sitemap and robots.txt. An unlisted site asks crawlers not to index it (robots meta tag on every
    # page, robots.txt) and publishes no sitemap. This is a request to crawlers, not access control.
    if SITE_OPTS["listed"]:
        urls = "".join(f"<url><loc>{SITE_URL}{p + '/' if p and not p.endswith('.html') else p}</loc></url>"
                       for p in pages if p not in ("404.html", "review.html", "review"))
        (OUT / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>'
                                         f'<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>')
        (OUT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}sitemap.xml\n")
    else:
        (OUT / "robots.txt").write_text("User-agent: *\nDisallow: /\n")
    print(f"built {len(pages)} pages into {OUT.relative_to(ROOT)}/")


if __name__ == "__main__":
    main()
