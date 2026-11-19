#!/usr/bin/env python3
"""Check the built site in _site/: every internal link and asset must resolve.

    python3 scripts/render.py && python3 scripts/check_site.py

Also checks that every rule has a page and that no template leaked a
Python/Jinja placeholder such as "None" into visible text.
"""
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse, unquote

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build  # noqa: E402
from render import OUT, SITE_URL  # noqa: E402

BASE_PATH = urlparse(SITE_URL).path  # e.g. /policy-tracker/


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links, self.ids, self.text = [], set(), []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        for k in ("href", "src"):
            if a.get(k):
                self.links.append(a[k])
        if a.get("id"):
            self.ids.add(a["id"])

    def handle_data(self, data):
        self.text.append(data)


def resolve(page, link):
    """Map a link on `page` to a file in OUT, or None if it is external/not a file link."""
    u = urlparse(link)
    if u.scheme in ("http", "https", "mailto", "data", "javascript") or link.startswith("#"):
        return None
    path = unquote(u.path)
    if not path:
        return None
    if path.startswith("/"):
        if not path.startswith(BASE_PATH):
            return OUT / "__outside_site__"
        target = OUT / path[len(BASE_PATH):]
    else:
        target = (page.parent / path).resolve()
    if path.endswith("/") or target.is_dir():
        target = target / "index.html"
    return target


def main():
    problems = []
    pages = sorted(OUT.rglob("*.html"))
    for page in pages:
        p = Links()
        p.feed(page.read_text(encoding="utf-8"))
        for link in p.links:
            target = resolve(page, link)
            if target is not None and not target.exists():
                problems.append(f"{page.relative_to(OUT)}: broken link {link}")
        visible = " ".join(p.text)
        for bad in (r"\bNone\b", r"\bundefined\b", r"\{\{", r"\{%"):
            if re.search(bad, visible):
                problems.append(f"{page.relative_to(OUT)}: placeholder text matching {bad!r}")
    data = build.load()
    for r in data.rules.values():
        if not (OUT / "rules" / r["slug"] / "index.html").exists():
            problems.append(f"missing rule page for {r['id']}")
    for p in problems:
        print("ERROR:", p)
    print(f"checked {len(pages)} pages, {len(problems)} problems")
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
