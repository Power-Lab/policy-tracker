# Adding a country

This guide sets out, step by step, how to add a new economy to the tracker. It applies the general procedure in [SEARCH-PROTOCOL.md](SEARCH-PROTOCOL.md) (section 8) and uses the existing countries as worked examples. A checklist at the end summarises the steps.

Work on a branch and open a pull request; every step below can be checked locally before the pull request is opened.

```bash
git checkout -b add-<country>
```

## Overview

| Step | What | Files |
| --- | --- | --- |
| 1 | Scouting report | `docs/scouting/<cc>.md` |
| 2 | Country profile | `data/countries.csv` |
| 3 | Source registry | `data/search/sources.csv` |
| 4 | Search vocabulary | `data/search/vocabulary.csv` |
| 5 | Search modules | `data/search/modules.csv` |
| 6 | Searches and screening | `data/search/search-log.csv`, `data/search/screening.csv` |
| 7 | Instruments | `data/rules.csv` |
| 8 | Validation and preview | (commands only) |
| 9 | Monitoring (optional) | `scripts/scan_portals.py`, `data/search/adapters.json` |
| 10 | Pull request and review | (GitHub) |

`<cc>` is the ISO 3166-1 alpha-2 code in lower case (for example `in`, `au`); in data files the code is upper case (`IN`, `AU`).

## 1. Scouting report

Before any data are entered, write a short report on how the economy's rules are made and where they are published. Use the existing reports as models: [ph.md](scouting/ph.md) (an English-language system), [th.md](scouting/th.md) (resolutions and Buddhist Era dates), [my.md](scouting/my.md) (guidelines revised in place, state law), [in.md](scouting/in.md) (all four categories).

Sections:

1. **Summary**: how the power sector and industrial policy are organised; the main issuers; how difficult the record will be to compile, and why.
2. **Legal hierarchy and document types**: from highest to lowest rank, with how each type is numbered and dated, and how it maps to the tracker's `doc_type` values.
3. **Official sources**: a table with name, URL, tier (1–4, see [SEARCH-PROTOCOL.md](SEARCH-PROTOCOL.md) section 4), languages, what it holds, and the access result you observed (HTTP status, bot challenge, or "not tried").
4. **Key instruments by category**: electricity; energy and climate; supply chain and industrial policy; trade.
5. **Fit with the schema**: instruments that do not fit cleanly, and how you propose to record them.
6. **Partner institutes and possible reviewers**.
7. **Risks and open questions**.
8. **Sources**: every URL used.

## 2. Country profile

Add one row to `data/countries.csv`:

| Column | Content | Example (India) |
| --- | --- | --- |
| `code` | ISO code, upper case | `IN` |
| `name` | English short name | `India` |
| `language` | Language(s) of the binding texts, written out | `English and Hindi` |
| `status` | `Compiled from desk research; unverified` until a reviewer has checked the entries | |
| `hierarchy` | Document types from highest to lowest rank, `;`-separated, each with its tracker `doc_type` in brackets | `Act of Parliament (law);Rules and statutory orders (government regulation);…` |
| `sources` | Two to four official sources as `Name|https://url`, `;`-separated | `India Code|https://www.indiacode.nic.in/;…` |
| `intro` | Two or three neutral sentences on how the sector and industrial policy are organised | |

If the economy is listed in `data/pipeline.csv` (the coverage roadmap), remove its row there: the site shows a country either on the roadmap or as covered, not both.

## 3. Source registry

Add every source from the scouting report to `data/search/sources.csv`:

| Column | Content |
| --- | --- |
| `id` | `<cc>-<short-name>`, lower case, e.g. `in-egazette` |
| `country` | ISO code |
| `name`, `url` | Name and `https://` address |
| `tier` | 1 gazette or official legal database; 2 issuing body's listing; 3 legal register or reference collection; 4 secondary (discovery only) |
| `kind` | `gazette`, `legal database`, `agency listing`, `legal register` or `secondary` |
| `languages` | Language codes, `;`-separated (e.g. `en;hi`) |
| `access` | `open`, `partial`, `restricted` (bot challenge or 403), `unreachable` or `unknown` |
| `checked` | Date of the access check (YYYY-MM-DD); empty only if `access` is `unknown` |
| `adapter` | Empty unless the weekly scan parses the source (step 9) |
| `notes` | What the source holds and anything that affects searching it |

To record an access result:

```bash
curl -s -o /dev/null -m 20 -w '%{http_code}\n' https://example.gov/
```

## 4. Search vocabulary

Add search terms for every topic of each module the country joins (step 5), in the language(s) of the binding texts, to `data/search/vocabulary.csv`. One row per topic and language: `topic`, `language`, `terms` (`;`-separated), `exclude` (terms that signal a false match), `status`.

- Mark new rows `draft: needs review by a native speaker` until a native speaker has checked them, then `validated`.
- English rows already exist for every topic. For economies whose binding texts are published in English (or bilingually, as in India), English terms are sufficient to start; `scripts/check_search.py` reports any missing language as a warning, not an error.
- Do not machine-translate terms without review: legal terminology is specific (for example, Indonesian *Peraturan Menteri*, Vietnamese *Thông tư*).

## 5. Search modules

Add the country code to the `countries` column of each relevant module in `data/search/modules.csv` (normally `power-core`, `cross-sector` and `supply-chain`). Then check the framework:

```bash
python3 scripts/check_search.py
```

## 6. Searches and screening

Generate a search plan for the country:

```bash
python3 scripts/search_plan.py supply-chain --country <CC> --out plan-<cc>.md
```

The plan lists the sources in tier order, the queries for each topic in each language, and (once instruments exist) the instruments to use for citation chasing. Carry out the five strategies in [SEARCH-PROTOCOL.md](SEARCH-PROTOCOL.md) section 5: enumeration of tier 1–2 listings, keyword searches, citation chasing, monitoring and expert consultation.

- Log each search run in `data/search/search-log.csv` (date, module, country, source, strategy, language, query, number of results, number of new candidates).
- Record screening decisions in `data/search/screening.csv`, with an exclusion code (E1–E7) for every exclusion.
- Apply the eligibility criteria in [SEARCH-PROTOCOL.md](SEARCH-PROTOCOL.md) section 3. For the supply chain and trade categories, include general trade or investment instruments only where they contain provisions specific to clean energy technologies or their mineral inputs.

## 7. Instruments

Add one row per instrument to `data/rules.csv`. Field definitions are in `data/fields.csv` and on the site's Data page. Points that need particular care:

- **`id`**: `<CC>-<TYPE>-<YEAR>-<NUMBER>`, upper case (e.g. `IN-ACT-2003-36`, `AU-ACT-2024-FMIA`). It must start with the country code and never change once published, because it is part of the instrument's address.
- **`doc_type`**: one of the values in `data/fields.csv`. Map each national form to the closest type and keep the national name in `number` or `short_name` (see the hierarchy in step 2).
- **`number`**: as printed. Use `unnumbered (…)` when the instrument has no number (for example `unnumbered (Cabinet resolution)`).
- **Dates**: Gregorian, `YYYY-MM-DD`, or `YYYY-MM` / `YYYY` when only that is known. Convert other calendars (Thai Buddhist Era: subtract 543). Fill `date_in_force` when it differs from the signing date.
- **`topics`** and **`technologies`**: topic ids from `data/topics.csv`; technologies only when the instrument specifically concerns them.
- **Links**: `amends`, `revokes`, `implements`, `overrides` refer to other ids in `data/rules.csv`. Add `link_basis` for every row with `amends` or `revokes`. The reverse links are derived by the build; never type them.
- **`status`**: an instrument amended by a recorded instrument is `amended`; one revoked or replaced is `revoked` or `replaced`. Use `pending` for adopted instruments not yet in force and `draft` for those under formal consideration.
- **`summary_english`**: two or three neutral sentences on what the instrument does and what it changed. No evaluative or causal claims that the instrument itself does not support.
- **`source_url`** and **`source_type`**: link to the official text where possible (`document`); otherwise to the portal or search page (`portal-search`) and say so in `notes`.
- **`verification`**: `unverified` until a reviewer has checked the entry against the official text (step 10). Start `notes` with how the entry was compiled and what a reviewer must check.

List fields use `;` with no spaces. Write the file with a CSV-aware tool (Python's `csv` module, or a spreadsheet saved as UTF-8 CSV) to keep quoting intact.

## 8. Validation and preview

```bash
python3 scripts/build.py
python3 scripts/check_search.py
python3 -m unittest discover -s tests
python3 scripts/render.py && python3 scripts/check_site.py
python3 -m http.server -d _site 8000
```

- `build.py` must report 0 errors. Warnings of the form "status 'amended' but no rule in force amends it" are acceptable when the amending instrument is not yet recorded; name it in `notes`.
- Open http://localhost:8000/countries/<cc>/ and check the timeline, the "what applies now" lists and the sources searched.

## 9. Monitoring (optional)

If an open tier 1–2 source publishes a listing of new instruments, it can be added to the weekly scan:

1. Write a parser in `scripts/scan_portals.py` (see `parse_chinhphu` and `parse_esdm` for examples) and register it in the `parse` function.
2. Set the `adapter` column of the source in `data/search/sources.csv`, and add any per-source options (`require`, `skip`, `match_all`) to `data/search/adapters.json`. Then test the parser on a saved copy of the page:

   ```bash
   python3 scripts/scan_portals.py --file <source-id> page.html
   ```
3. Add a test with a small HTML fixture in `tests/test_build.py`.

The first scan after a source is added records a baseline and reports nothing; later scans report new documents.

## 10. Pull request and review

- Open a pull request. The build workflow adds a summary of the data changes to the run, and all checks must pass before merging.
- Log the research in `data/search/search-log.csv` (one row per run; strategy `scouting` for desk research).
- Ask a country reviewer to work through the new entries in the reviewer view (`/review/`), following [REVIEWING.md](REVIEWING.md). When their checks are complete, the country's `status` in `data/countries.csv` can be updated.

## Using an AI assistant for steps 1–3 and 7

The scouting reports and first entries for India, Australia, Pakistan and Bangladesh were compiled with an AI research assistant working to the specification in [templates/research-brief.md](templates/research-brief.md). The specification can be reused for a new economy: it defines the output files, the 32-column row format, the allowed values and a validation command. Output prepared this way is always `unverified`, must be checked with step 8, and should be read before it is merged; the assistant's notes on access failures and missing numbers belong in the scouting report.

## Checklist

- [ ] Scouting report `docs/scouting/<cc>.md`
- [ ] Country row in `data/countries.csv` (and removed from `data/pipeline.csv`, if listed)
- [ ] Sources in `data/search/sources.csv`, with tiers and access checks
- [ ] Vocabulary in the binding language(s), marked as drafts
- [ ] Country added to the modules in `data/search/modules.csv`
- [ ] Search runs logged; screening decisions recorded
- [ ] Instruments in `data/rules.csv`, all `unverified`, with notes
- [ ] `build.py` (0 errors), `check_search.py`, tests, `render.py` and `check_site.py` pass
- [ ] Country page checked locally
- [ ] Pull request opened; reviewer identified
