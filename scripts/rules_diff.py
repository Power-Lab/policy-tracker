"""Compare two versions of data/rules.csv, row by row and field by field.

Used by the review workflow (PR summaries), the PR data check and the change
history on the site.

    python3 scripts/rules_diff.py OLD.csv NEW.csv     print a Markdown summary
"""
import csv
import io
import sys

DERIVED = {"slug", "categories", "amended_by", "revoked_by", "implemented_by", "overridden_by"}
LABEL_FIELDS = ("short_name", "id")


def read_rows(text):
    """CSV text → (columns, {id: row}) keeping row order."""
    reader = csv.DictReader(io.StringIO(text))
    rows = {}
    for r in reader:
        if r.get("id"):
            rows[r["id"]] = r
    return reader.fieldnames or [], rows


def diff(old_text, new_text):
    """Return {"added": [row], "removed": [row], "changed": {id: [(field, old, new)]}}."""
    old_cols, old = read_rows(old_text)
    new_cols, new = read_rows(new_text)
    shared = [c for c in new_cols if c in old_cols and c not in DERIVED]
    out = {"added": [new[i] for i in new if i not in old],
           "removed": [old[i] for i in old if i not in new],
           "changed": {}}
    for i in new:
        if i in old:
            changes = [(c, old[i].get(c, ""), new[i].get(c, "")) for c in shared
                       if (old[i].get(c) or "") != (new[i].get(c) or "")]
            if changes:
                out["changed"][i] = changes
    return out


def label(row):
    return row.get("short_name") or row.get("id")


def short(v, n=90):
    v = (v or "").replace("\n", " ").replace("|", "\\|")
    return (v[: n - 1] + "…") if len(v) > n else (v or "—")


def markdown(d, new_rows=None):
    """Human-readable summary of a diff for PR bodies and job summaries."""
    lines = []
    if not (d["added"] or d["removed"] or d["changed"]):
        return "No changes to `data/rules.csv`."
    if d["added"]:
        lines.append(f"**Added {len(d['added'])} rule(s):** " + ", ".join(f"{label(r)} (`{r['id']}`)" for r in d["added"]))
    if d["removed"]:
        lines.append(f"**Removed {len(d['removed'])} rule(s):** " + ", ".join(f"{label(r)} (`{r['id']}`)" for r in d["removed"]))
    for rid, changes in d["changed"].items():
        name = label(new_rows[rid]) if new_rows and rid in new_rows else rid
        lines += ["", f"#### {name} (`{rid}`)", "", "| field | was | now |", "| --- | --- | --- |"]
        lines += [f"| `{f}` | {short(a)} | {short(b)} |" for f, a, b in changes]
    return "\n".join(lines)


if __name__ == "__main__":
    old_text = open(sys.argv[1], encoding="utf-8").read()
    new_text = open(sys.argv[2], encoding="utf-8").read()
    print(markdown(diff(old_text, new_text), read_rows(new_text)[1]))
