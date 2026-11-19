# Power Transformation Lab Policy Tracker

A public, English-language dataset of laws, regulations, decrees and plans on **electricity, energy, clean technology supply chains and trade** in Asia-Pacific, maintained by the [Power Transformation Lab](https://pwrlab.org/) at the University of California San Diego. For each instrument it records what it does, which earlier instruments it amends, revokes or implements, and whether it is in force, with a link to the official source.

**Site:** https://power-lab.github.io/policy-tracker/

**Status:** under development (see [docs/ROADMAP.md](docs/ROADMAP.md)). Every entry is currently `unverified`: entries were compiled from desk research and secondary sources and have not yet been checked against the official text. Not legal advice.

## Categories

Instruments are classified in four categories, each with a fixed set of topics applied identically in every economy (`data/categories.csv`, `data/topics.csv`):

| Category | Topics |
| --- | --- |
| Electricity | framework law, power plans, grid codes and market rules, tariffs and PPA terms, renewable pricing and procurement, rooftop solar, wheeling and direct PPAs, captive power, coal phase-out, energy storage, cross-border electricity trade |
| Energy and climate | energy strategy, energy efficiency, carbon pricing, coal supply, electric vehicle adoption |
| Supply chain and industrial policy | critical minerals and downstreaming, local content requirements, manufacturing incentives, foreign investment rules |
| Trade | import tariffs, trade remedies, import approvals and standards, export restrictions |

Technology-specific instruments are also tagged by technology (solar PV, wind, batteries, electric vehicles, grid equipment, hydrogen).

## Site

| Page | Path | Contents |
| --- | --- | --- |
| Home | `/` | Search, summary counts, categories and countries |
| Explore | `/rules/` | Search and filters (category, country, topic, status, technology, document type, verification); filters are kept in the URL |
| Instrument | `/rules/<id>/` | Summary, key facts, amendment history, implementing instruments, related instruments, citation, corrections |
| Countries | `/countries/<code>/` | Legal hierarchy, sources searched, timeline by topic, instruments in force by topic |
| Topics | `/topics/` and `/topics/<id>/` | Topics by category; for each economy, the instruments in force and their history |
| Compare | `/compare/` | Topic × economy table of instruments in force |
| Timeline | `/timeline/` | All instruments by date of signature |
| Data | `/data/` | CSV and JSON downloads, field definitions, source registry |
| About | `/about/` | Scope, definitions, method, search protocol, limitations |
| Updates | `/updates/` | Log of every change to the data, with an Atom feed |
| Reviewer view | `/review/` | Queue and editor for reviewers |

## How it works

```
data/*.csv ──► scripts/build.py ──► scripts/render.py ──► _site/ ──► GitHub Pages
               validate, derive      Jinja2 templates,
               back-links            SVG charts, downloads
```

- **`data/rules.csv`** is the single source of truth: one row per instrument. Field definitions are in `data/fields.csv` and on the Data page.
- `scripts/build.py` validates the data and warns when a status contradicts the recorded links.
- `scripts/render.py` generates every page into `_site/` (not committed); `scripts/check_site.py` fails the build on broken links.
- `.github/workflows/pages.yml` validates, tests, builds and deploys `main` to GitHub Pages.
- `.github/workflows/review-to-pr.yml` turns review issues from the reviewer view into pull requests ([docs/REVIEWING.md](docs/REVIEWING.md)).
- `.github/workflows/portal-scan.yml` checks registered official portals every Monday and opens a triage issue for new documents. With an `ANTHROPIC_API_KEY` repository secret, it also drafts an unverified entry for each new document; `.github/workflows/accept-draft.yml` adds a draft on a maintainer's `/accept <id>` comment.
- The change log on each instrument page and the Updates page are generated from the git history of `data/rules.csv`.

### Search framework

How instruments are identified, screened and recorded is set out in [docs/SEARCH-PROTOCOL.md](docs/SEARCH-PROTOCOL.md). The machine-readable parts are in `data/search/`: search modules (`modules.csv`), the source registry (`sources.csv`), the multilingual vocabulary (`vocabulary.csv`), scan adapter options (`adapters.json`), and the screening and search logs.

```bash
python3 scripts/search_plan.py supply-chain --country ID --topic local-content
```

```bash
python3 scripts/check_search.py
```

The first command prints a search plan (sources in tier order, queries in each language, instruments to use for citation chasing); the second checks the framework files and runs in CI.

### Run locally

```bash
pip install -r requirements.txt
```

```bash
python3 scripts/render.py && python3 scripts/check_site.py
```

```bash
python3 -m http.server -d _site 8000
```

```bash
python3 -m unittest discover -s tests
```

### Add or change an instrument

1. Edit `data/rules.csv` (list fields are separated by `;`).
2. Link to earlier instruments by id in `amends`, `revokes`, `implements` or `overrides`; the reverse links are derived by the build.
3. Run `python3 scripts/build.py` and resolve any errors or warnings.
4. Open a pull request; the site rebuilds when it is merged into `main`.

### Repository settings

- **Pages:** Settings → Pages → Source: GitHub Actions.
- **Actions:** Settings → Actions → General → Workflow permissions: read and write, and allow GitHub Actions to create and approve pull requests (needed by the review and draft workflows).
- **Optional secret:** `ANTHROPIC_API_KEY`, for model-drafted entries in the weekly scan.

## Documentation

- [docs/ROADMAP.md](docs/ROADMAP.md): objective, status and next steps
- [docs/SEARCH-PROTOCOL.md](docs/SEARCH-PROTOCOL.md): search and inclusion protocol
- [docs/ADDING-A-COUNTRY.md](docs/ADDING-A-COUNTRY.md): step-by-step guide to adding an economy, with a reusable [research brief](docs/templates/research-brief.md)
- [docs/SCHEMA-NOTES.md](docs/SCHEMA-NOTES.md): schema decisions and open questions
- [docs/REVIEWING.md](docs/REVIEWING.md): review workflow
- [docs/scouting/](docs/scouting/): source and coverage reports by economy

## Licence

Data, summaries and documentation: [CC BY 4.0](LICENSE-DATA.md). Code: [MIT](LICENSE). The official legal texts the tracker links to are not covered by either.
