# Where the schema strains

The proof of concept's job was to test whether one schema fits two different legal systems (Indonesia and Vietnam). It mostly does. These are the cases that didn't fit cleanly in the first 55 rows, with a proposed fix for each. **Status (2026-11-04):** the team agreed the proposals. Items marked ✅ are implemented; the rest are still open.

| # | Problem | Example in the data | Proposed fix | Priority |
| --- | --- | --- | --- | --- |
| 1 | ✅ **Implicit supersession.** A higher-ranking rule overrides parts of a lower one without amending or revoking it. | Perpres 112/2022 set new renewable ceiling prices that replace the pricing articles of Permen ESDM 50/2017 in practice; 50/2017 was never revoked. Today the link lives only in `notes`. | Add an `overrides` link (third link type next to `amends` and `revokes`), drawn as a dotted line. Status of the older rule stays as it is. | High |
| 2 | ✅ **Implementing rules.** Circulars and ministerial rules that implement a decision or law, without amending it. | Circular 16/2017 implements Decision 11/2017 (Vietnam solar FIT); PP 25/2021 implements the Job Creation Law. | Add an `implements` link. Lets a rule page show "implementing rules", and makes the history chart less cluttered. | High |
| 3 | ✅ **Emergency regulations.** Indonesia's Perppu sits between a law and the law that later enacts it. | Law 11/2020 was revoked by Perppu 2/2022, which became Law 6/2023. Perppu 2/2022 has no row; the link currently goes straight from 6/2023 to 11/2020. | Add doc type `emergency regulation`, give Perppu 2/2022 its own row, and model "enacted as" as `revokes` from the law to the Perppu, with a note. | Medium |
| 4 | ✅ **Plans replacing plans.** National power plans are approved by decision and usually replaced without an express revocation clause. | PDP8 (Decision 500/2023) supersedes revised PDP7 (Decision 428/2016); RUPTL 2025–2034 replaces RUPTL 2021–2030. | Keep `revokes` for the link but record the basis in a new `link_basis` field: `express clause`, `implied by successor` or `expired`. | Medium |
| 5 | ✅ **Party and policy documents.** Not legal instruments, but later laws cite them. | Vietnam's Politburo Resolution 55-NQ/TW; Thailand's NEPC and Cabinet resolutions (expected next). | Keep doc type `party resolution`, and add a `binding` flag (yes/no). Non-binding documents get status `guidance` instead of "in force". | Medium |
| 6 | ✅ **Expired, but still in effect for existing projects.** A tariff window closes, but contracts signed under it keep running for 20 years. | Vietnam's FIT decisions 11/2017, 13/2020 and 39/2018. | Add a `grandfathered` field (yes/no plus a short note), shown on the rule page. | Medium |
| 7 | **Partial dates.** Many seed rows only know the year or month. | Permen ESDM 13/2019 (year only); many ministerial rules have month only. | Already handled: `YYYY` / `YYYY-MM` allowed and plotted mid-period. Reviewers should fill in full dates. | Done |
| 8 | **Issuing bodies that were renamed or merged.** | Vietnam merged several ministries in 2025 (for example, environment and agriculture), so the same issuer has different names over time. | Add `data/issuers.csv` with stable ids, names and dates of each name; rows point to the issuer id. | Low |
| 9 | **Framework laws tagged with many topics.** | Vietnam's Electricity Law 2024 has four topics, so it shows up in four places in Compare. | Accept it, but add a "primary topic" (first in the list) and show it in the comparison table only for the primary topic, linking from the others. | Low |
| 10 | **Utility and regional rules.** PLN's own regulations and provincial rules change practice but sit outside the national hierarchy. | PLN rules on rooftop solar quotas and wheeling fees (not yet in the data). | If added, use doc type `utility rule` and origin `utility`, and keep them out of status counts by default. | Decide |

### How they were implemented

- **1, 2, 16:** new link columns `overrides` and `implements` (back-links `overridden_by` and `implemented_by` are derived). Overrides appear in the history chart as a dotted line; implementing rules are listed in their own section on each rule page.
- **3:** doc type `emergency regulation`; Perppu 2/2022 now has its own row between Law 11/2020 and Law 6/2023.
- **4:** `link_basis` column (express clause, implied by successor, expired). PDP8 and RUPTL 2025–2034 are marked "implied by successor".
- **5:** `binding` column (`no` for non-binding documents). Implemented as a flag rather than a separate `guidance` status, so status stays about time (in force, ended, not yet).
- **6:** `grandfathered` column, shown on rule pages as "Still applies to".
- **11:** statuses `draft` and `pending`. They don't count as "still applies", and draft or pending rules don't trigger "revoked but still in force" warnings for the rules they would replace. Shown as "Coming up" on country, topic and compare pages.
- **13:** convention: each guideline revision is its own row with an `-REV1`, `-REV2` id that amends the original.
- **14:** `jurisdiction` column (for example `MY-SBH`), validated against the country code.
- **15, 19:** doc types `advisory`, `code`, `regulator determination`, `directive`.
- **17:** the validator rejects years above 2400 as unconverted Buddhist Era dates.
- **20:** topics `cross-border-trade`, `energy-storage`, `energy-efficiency`.
- Still open: 8 (issuer register), 9 (primary topic), 10 (utility and regional rules), 18 (ASEAN pseudo-country and its doc types `regional plan` and `MoU` are allowed but there is no ASEAN page yet).

## What worked well

- One row per rule, with links by id, handled every amendment chain in the seed data, including the five-rule rooftop solar chain and the 2004 → 2012 → 2024 Electricity Law chain in Vietnam.
- The fixed topic list worked for both countries without change.
- The `origin_sector` and `energy_channel` fields allowed the cross-sector rows (nickel export ban, coal DMO, carbon pricing) to be filtered without a separate table.
- Deriving `amended_by` and `revoked_by` instead of typing them removed a whole class of inconsistencies.

## What the scouting of the next countries adds

The scouting reports in [scouting/](scouting/) (Philippines, Thailand, Malaysia, and the rest of ASEAN) found these further gaps. Numbers continue the table above.

| # | Problem | Where | Proposed fix | Priority |
| --- | --- | --- | --- | --- |
| 11 | ✅ **Drafts and laws not yet in force.** Several important instruments are drafts, or have been enacted but not yet commenced. Previously they could not be recorded without a misleading status. | Thailand: PDP2026, the Climate Change Bill, final direct PPA rules. Malaysia: the 2025 Electricity Supply amendments. | Add statuses `draft` (proposed, not adopted) and `pending` (adopted, not yet in force). Keep both out of the "still applies" counts. | High (before Thailand or Malaysia) |
| 12 | ✅ **Decisions by committee resolution.** In Thailand the binding moves are NEPC and EPAC resolutions, which the ERC then implements. | Thailand (about 2,300 resolutions since 2012 in the EPPO database). | Use doc type `decision` with issuer NEPC/EPAC, plus the `binding` flag from item 5 and an `implements` link (item 2) from the ERC regulation to the resolution. | High (Thailand) |
| 13 | ✅ **Guidelines revised in place.** A guideline keeps its number and URL while its text is revised, sometimes several times a year, and the old PDF is overwritten. | Malaysia: Energy Commission guidelines (`GP/ST/No.x/yyyy`) for rooftop solar, third-party access and tariffs. | Record each revision as its own row that `amends` the original (id suffix `-REV1`, `-REV2`), and archive each PDF version, because the URL won't keep it. | High (Malaysia) |
| 14 | ✅ **State-level law.** Some states have their own electricity law and regulator. | Malaysia: Sabah (own regulator since 2024) and Sarawak (federal Act suspended since 1990). | Add a `jurisdiction` field (default national; for example `MY-SBH`), shown as a filter on country pages. | Medium |
| 15 | ✅ **Rules issued as advisories, notices and press releases.** Some important decisions have no numbered instrument. | Philippines: the 2020 coal moratorium and its 2025 widening are DOE advisories. Malaysia: charges and quotas first appear in ministry press releases. | Add doc type `advisory` (covers advisories, notices and binding press releases), and require a link to the official page. | Medium |
| 16 | ✅ **Paired rules from two issuers.** Policy from one body becomes binding through another. | Philippines: DOE department circulars and ERC resolutions on the same topic. | Covered by the `implements` link (item 2); show the pair together on rule pages. | Medium |
| 17 | ✅ **Buddhist Era dates.** Thai texts are dated B.E. (Gregorian year = B.E. − 543). | Thailand. | Store Gregorian dates; keep the B.E. number in `number` as printed. The validator can flag years above 2400 as unconverted. | Low |
| 18 | **Regional instruments.** ASEAN plans and MoUs have no member country. | APAEC 2026–2030, the ASEAN Power Grid MoU, LTMS-PIP. | Allow a pseudo-country `ASEAN` with its own page, and doc types `regional plan` and `MoU`. | Low (later phase) |
| 19 | ✅ **Regulator codes and determinations.** In some systems most rules are codes and determinations, not numbered acts. | Singapore (EMA codes and determinations), Brunei (directives). | Add doc types `code`, `regulator determination` and `directive`. | Low (later phase) |
| 20 | ✅ **Topics the fixed list lacks.** | Cross-border trade (Singapore imports, Lao exports, Cambodia), energy storage, energy efficiency. | Add topics `cross-border-trade`, `energy-storage` and `energy-efficiency`. Topic changes apply to every country, so decide them once. | Medium |

### Process findings (not schema)

- **Broken links that look fine.** After the Philippine DOE moved its site, old links return a "Page not found" page with HTTP 200, so a plain status-code check passes them. A source-link checker must look at the page content too.
- **Scanned PDFs.** 16 of the 23 DOE PDFs the scout downloaded are scans. The portal scan and AI drafting need OCR (or PDF input to the model, which handles scans) for the Philippines.
- **Blocked portals.** The ERC (Philippines and Thailand), the Royal Thai Gazette, the Official Gazette and Singapore Statutes Online all block automated requests. Plan for manual downloads by country reviewers, or fetching from inside the country.
- **Reviewers who read the language** are needed for Thailand (Thai), Malaysia (Malay press releases), Lao PDR, Myanmar and Timor-Leste (Portuguese).
