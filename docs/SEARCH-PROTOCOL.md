# Search and inclusion protocol

This protocol sets out how instruments are identified, screened and recorded, so that the dataset can be extended to new topics and countries in a consistent and reproducible way. It follows the structure of a systematic review protocol: the scope of each search is declared in advance, sources and queries are recorded, and every inclusion or exclusion decision has a stated reason.

The machine-readable parts of the protocol are in [`data/search/`](../data/search/). `scripts/search_plan.py` generates a search plan from them, and `scripts/check_search.py` checks that they are consistent (it runs in CI).

## 1. Unit of analysis

The unit of analysis is a **legal or policy instrument**: a single document issued by a public authority, identified by its number or, where it has none, by issuer and date. Each instrument becomes one row in `data/rules.csv`. A revision of a document that keeps its number (for example, a Malaysian Energy Commission guideline) is recorded as a separate row that amends the original.

## 2. Search modules

Searches are organised in **modules**, each defined by a set of countries, a set of topics and a start date (`data/search/modules.csv`). Extending the dataset means adding or widening a module rather than searching ad hoc.

| Module | Countries | Topics | From | Status |
| --- | --- | --- | --- | --- |
| `power-core` | Indonesia, Viet Nam, Thailand, Philippines, Malaysia | electricity category | 2017 | active |
| `cross-sector` | same | energy and climate category | 2017 | active |
| `supply-chain` | same, extended to India, Australia, Pakistan and Bangladesh as their sources are registered | supply chain and trade categories, and electric vehicle adoption | 2015 | active |
| `asean-expansion` | Singapore, Cambodia, Lao PDR, Brunei, Timor-Leste, Myanmar | electricity category | 2017 | planned |

Topics are grouped in four categories (`data/categories.csv`): electricity; energy and climate; supply chain and industrial policy; trade. A module lists its topics explicitly, so a category can be searched in some economies before others.

## 3. Eligibility criteria

An instrument is **included** if all of the following hold:

1. **Issuer.** It is issued by a national legislature, head of state or government, cabinet, ministry, national regulator, or a state-level authority with its own power sector jurisdiction (for example, Sabah). Utility-internal rules are excluded until the open question in [SCHEMA-NOTES.md](SCHEMA-NOTES.md) item 10 is decided.
2. **Form.** It is one of the document types in the schema (law, emergency regulation, government or presidential regulation, ministerial regulation, decree, decision or resolution, circular, advisory, code, regulator determination, directive, plan, MoU, party resolution).
3. **Relevance.** It falls under at least one topic of the module and affects the energy sector through at least one recorded channel (demand, supply, prices, investment, grid access, emissions). For the supply chain and trade categories, an instrument is relevant if it applies to clean energy technologies (solar PV, wind, batteries, electric vehicles, grid equipment, hydrogen), their components, or the minerals used to make them; general trade or investment instruments are included only where they contain provisions specific to these goods or sectors.
4. **Date.** It was signed on or after the module's start date, **or** it is earlier but is amended, revoked, implemented or cited by an included instrument (backward citation rule).
5. **Status.** It is in force, amended, replaced, revoked or expired, or it is a draft or pending instrument under formal consideration (adopted for public consultation, approved in principle by cabinet, or enacted but not commenced).

An instrument is **excluded**, with the reason recorded, if it is:

| Code | Reason |
| --- | --- |
| E1 | Outside the module's topics or without an energy channel |
| E2 | Administrative or personnel matter (appointments, internal organisation, delegation of signing authority) |
| E3 | Routine periodic notice that sets a value under an existing rule without changing the rule (for example, monthly reference prices) |
| E4 | Individual decision applying a rule to a single party (a licence, a tariff approval for one utility) |
| E5 | Announcement, speech or statement of intent without a document that has legal or formal policy effect |
| E6 | Duplicate of an instrument already recorded |
| E7 | Draft that has not reached a formal stage (see criterion 5) |

## 4. Sources

Sources are listed in `data/search/sources.csv` with their tier, the languages they publish in, and the access status last observed. Tiers rank sources by authority:

| Tier | Kind | Use |
| --- | --- | --- |
| 1 | Official gazette or official legal database | Authoritative text and dates; preferred for `source_url` |
| 2 | Issuing body's own listing (ministry, regulator) | Enumeration of new instruments; often the fastest source |
| 3 | Legal register or established reference collection | Dates, numbering and texts when tier 1–2 are inaccessible |
| 4 | Secondary: law firm notes, research reports, news | **Discovery only.** A tier 4 source can identify a candidate but cannot be the sole basis of a verified entry |

Access status is one of `open`, `partial`, `restricted` (bot challenge or HTTP 403), `unreachable` or `unknown`. Restricted sources are searched manually by a reviewer or from within the country. A source's status and date of check are updated whenever it is used.

## 5. Search strategies

Each module combines five strategies. Each search run is logged (section 7) with the strategy it used.

1. **Enumeration (`enumeration`).** Browse the issuance listings of tier 1–2 sources by year and document type, from the module's start date. This is the primary strategy, because keyword searches miss instruments with uninformative titles.
2. **Keyword search (`keyword`).** Search tier 1–3 sources, and web search restricted to their domains, using the controlled vocabulary in `data/search/vocabulary.csv` (terms per topic per language, with exclusion terms). Searches are run in the language of the binding text, not only in English.
3. **Citation chasing (`citation`).** For each included instrument, record (a) the instruments it cites, amends or revokes (backward), from its preamble ("considering", "mengingat", "căn cứ") and final provisions, and (b) later instruments that amend, implement or revoke it (forward), by searching for its number. This is how amendment chains are completed.
4. **Monitoring (`monitoring`).** The weekly portal scan (`scripts/scan_portals.py`) checks the sources in the registry that have an adapter and opens a triage issue listing new documents that match the vocabulary. Each match records the topic(s) it matched.
5. **Expert consultation (`expert`).** Country reviewers and partner institutes identify instruments and check completeness for their country. Desk research by the project team is recorded as `scouting`.

## 6. Screening

Candidates are screened in two stages:

1. **Title and metadata screening.** Exclude candidates that clearly fail a criterion (usually E1–E3) on the basis of title, issuer and type.
2. **Full-text screening.** Read the instrument (or its official summary) and apply all criteria. Included candidates are then extracted into the schema as `unverified` entries.

Each decision is recorded in `data/search/screening.csv` with the candidate, source, strategy, stage, decision (`include`, `exclude`, `defer`), reason code, screener and date, and, for included candidates, the resulting `rule_id`. Deferred candidates are revisited when more information is available (for example, a draft reaching a formal stage).

**Quality control.** For each new country, a sample of at least 20% of title-stage exclusions is screened again by a second person; disagreements are resolved by discussion and the agreement rate is reported in the country's scouting report.

## 7. Documentation and reproducibility

- **Search log** (`data/search/search-log.csv`): one row per search run and source, with date, module, country, source, strategy, language, query, number of results and number of new candidates. The weekly scan writes its own log on the `watch-state` branch.
- **Screening log** (`data/search/screening.csv`): one row per screening decision, as above.
- **Flow summary.** For each module and country, report the number of records identified (by strategy), screened, excluded (by reason) and included, in the manner of a PRISMA flow diagram. These numbers can be produced from the two logs.
- **Version control.** All data, logs and the vocabulary are under version control, so any past state of the dataset and the searches behind it can be reconstructed.

Entries created before this protocol was adopted (the Indonesia and Vietnam seed entries and the Thailand, Philippines and Malaysia scouting rounds) are recorded in the search log as `expert` and `scouting` runs. Their individual queries were not logged; their sources are documented in the scouting reports.

## 8. Extending the dataset

**Adding a topic**

1. Add the topic to `data/topics.csv` with a description that defines its boundary.
2. Add vocabulary rows for the topic in every language used by the countries of the module (`data/search/vocabulary.csv`), marked as drafts until reviewed by a native speaker.
3. Add the topic to the relevant module in `data/search/modules.csv`.
4. Run the search plan for the module (`python3 scripts/search_plan.py <module> --topic <topic>`) and carry out enumeration, keyword search and citation chasing for each country.

**Adding a country**

1. Prepare a scouting report following the structure of the existing reports in [scouting/](scouting/): sector structure, legal hierarchy, official sources with observed access status, main instruments since the start date, fit with the schema, partner institutes, risks.
2. Register the sources in `data/search/sources.csv`, with tiers and access status.
3. Add vocabulary in the language(s) of the binding texts for every topic of the module.
4. Add the country to a module and to `data/countries.csv` (legal hierarchy, sources, introduction).
5. Run the search plan, screen candidates, and add included instruments as `unverified` rows.
6. Where a source is open and stable, write an adapter so that the weekly scan monitors it.

**Adding a geography beyond ASEAN** follows the same steps, with a new module. Country codes are ISO 3166-1 alpha-2; sub-national jurisdictions use the `jurisdiction` field.

## 9. Limitations

- Restricted portals (several gazettes and regulators) cannot be searched automatically; coverage of those sources depends on manual searches by reviewers.
- Keyword vocabularies in languages other than English are drafts until reviewed by native speakers, and keyword searches miss instruments with uninformative titles; enumeration is used to compensate.
- The weekly scan reads only the first listing page of each source, so it detects new documents but does not back-fill.
- The eligibility criteria require judgement, particularly on relevance (criterion 3) and on exclusion code E3. Reason codes and the second-screener sample are intended to make that judgement visible and checkable.
