# Scouting report: Bangladesh

Prepared 2026-11-19 for the Power Transformation Lab policy tracker. It comes with `bd-rules.csv` (20 candidate rows), `bd-country.csv` and `bd-sources.csv`. Everything here is a lead for reviewers, not checked data. Rows from bdlaws are well anchored; policy, guideline and SRO rows rest largely on Bangladeshi press and think-tank notes and say so.

How this was checked: the Laws of Bangladesh site (bdlaws.minlaw.gov.bd) was fetched with `curl`. Its chronological index (UTF-16 HTML) was parsed for energy-related Acts and Ordinances, and each Act page was read for number, date, repeal notes and section headings. Web searches filled the gaps. SREDA failed TLS verification; BERC, BPDB, BRTA and the environment ministry did not respond. The Power Division and NBR home pages loaded but the specific documents were not located there.

## 1. Summary

- **Structure.** The Power Division of the Ministry of Power, Energy and Mineral Resources leads policy. BPDB is the single buyer; state companies run transmission and distribution. BERC (BERC Act 2003, Act 13 of 2003) licenses and sets tariffs. The Electricity Act 2018 (Act 7 of 2018) replaced the 1910 Act and provides for an Independent System Operator. SREDA (Act 48 of 2012) promotes renewables and efficiency.
- **2023-2026 legal churn.** The BERC (Amendment) Act 2023 (Act 6 of 2023, 2023-01-31) inserted s. 34A letting the government set tariffs without BERC. After August 2024 the interim government governed by presidential ordinance: Ordinance 7 of 2024 (2024-08-27) deleted s. 34A, and Ordinance 15 of 2024 (2024-11-28) repealed the Quick Enhancement of Electricity and Energy Supply (Special Provisions) Act 2010. The new Parliament replaced both ordinances by Acts dated 2026-04-10 (Act 40 of 2026 and Act 18 of 2026). bdlaws records all of these, including the repeal chain.
- **Renewables.** The Renewable Energy Policy 2025 (Advisory Council approval 2025-05-06, published June 2025) replaced the 2008 policy, targeting 20% by 2030 and 30% by 2040 (some sources say 2041). Rooftop solar runs through the Net Metering Guidelines 2018 (revised 2019), replaced by a 2025 guideline (100% of sanctioned load, single-phase eligible), the July 2025 National Rooftop Solar Programme for public buildings, and the **Special Solar Power Installation Ordinance 2026** (Ordinance 39 of 2026, 2026-10-19).
- **Trade.** Solar equipment import taxes were cut by NBR SRO No. 159-Law/2026/14-Customs (2026-06-08), exempting customs, regulatory duty and advance tax, and a September 2026 notification reportedly brought total incidence to 1% for 180 days. Earlier duty levels (FY2024-25, FY2025-26) were not confirmed.
- **EVs.** The Electric Motor Vehicle Registration and Operation Guidelines 2023 (gazette 2023-04-18) allow EV registration. No purchase incentive instrument was found beyond budget reports.
- **Plans.** IEPMP 2023 (to 2050) is formally current; a draft 25-year Energy and Power Sector Master Plan 2026-2050 was prepared by the interim government and contested. The Mujib Climate Prosperity Plan 2022-2041's status after 2024 is unclear.
- **Tracking difficulty: moderate.** bdlaws is an excellent tier-1 source for Acts and Ordinances (numbers, dates, repeal notes), but it does not hold policies, guidelines, circulars or SROs. Those sit on ministry and NBR sites that are slow, partly unreachable, often bilingual and frequently scanned. Bengali is the binding language for most legislation.

## 2. Legal hierarchy and document types

| Rank | Type | Issuer | Numbering | Our `doc_type` |
| --- | --- | --- | --- | --- |
| 1 | Constitution | - | Articles (Art. 93 ordinance power) | (not tracked) |
| 2 | Act of Parliament (আইন) | Jatiya Sangsad | "Act No. N of YYYY" (২০২৬ সনের ৪০ নং আইন) | law |
| 2 | Ordinance (অধ্যাদেশ) | President, when Parliament is dissolved or not in session | "Ordinance No. N of YYYY" | emergency regulation |
| 3 | Rules (বিধিমালা) | Government by SRO | SRO No. N-Law/YYYY | government regulation |
| 3 | SROs / notifications | NBR, ministries | "SRO No. 159-Law/2026/14-Customs" | ministerial regulation |
| 3 | BERC regulations, orders | BERC | regulation title/year | regulator determination |
| 4 | Policies, master plans | Cabinet / Advisory Council, ministry | unnumbered | plan |
| 4 | Guidelines, circulars | Ministry divisions | memo numbers (not found) | circular |

## 3. Official sources

| Name | URL | Tier | Languages | What it holds | Access observed |
| --- | --- | --- | --- | --- | --- |
| Laws of Bangladesh | http://bdlaws.minlaw.gov.bd/ | 1 | bn, en | Acts, Ordinances, President's Orders, with repeal notes | HTTP 200 |
| Bangladesh Gazette (BG Press) | https://www.dpp.gov.bd/bgpress/ | 1 | bn, en | Gazette PDFs | HTTP 200 (not searched) |
| Power Division | https://powerdivision.gov.bd/ | 2 | bn, en | Policies, guidelines, circulars | HTTP 200 (documents not located) |
| NBR | https://nbr.gov.bd/ | 2 | bn, en | Customs and VAT SROs | HTTP 200 (SRO not located) |
| SREDA | https://sreda.gov.bd/ | 2 | bn, en | Net metering, RE data | TLS verification failure |
| BERC | https://berc.org.bd/ | 2 | bn, en | Tariff orders, regulations | unreachable (000) |
| BPDB | https://www.bpdb.gov.bd/ | 2 | bn, en | Tenders, PPAs | unreachable (000) |
| BRTA | https://brta.gov.bd/ | 2 | bn | EV registration | unreachable (000) |
| MoEFCC | https://moef.portal.gov.bd/ | 2 | bn, en | Climate plans (MCPP) | unreachable (000) |

## 4. Key instruments by category

**Electricity**
- Electricity Act 2018 (framework-law); BERC Act 2003 and the 2023 / 2024 / 2026 amendments (framework-law, tariffs-ppa).
- Quick Enhancement Act 2010 and its 2024 and 2026 repeals (tariffs-ppa, re-pricing).
- RE Policy 2008 and 2025 (re-pricing, energy-strategy).
- Net Metering Guidelines 2018 and 2025; National Rooftop Solar Programme 2025; Special Solar Power Installation Ordinance 2026 (rooftop-solar).
- IEPMP 2023 (power-plans, energy-strategy).

**Energy**
- SREDA Act 2012 (energy-efficiency); EV Registration and Operation Guidelines 2023 (ev-adoption); Mujib Climate Prosperity Plan 2022-2041 (energy-strategy).

**Supply chain**
- Nothing specific found: no local-content, manufacturing-incentive or mineral instrument for clean tech was located. Budget reports for FY2026-27 mention tax breaks for local EV and electronics assembly; not confirmed.

**Trade**
- SRO 159-Law/2026/14-Customs (2026-06-08) and the September 2026 NBR notification (import-tariffs).

## 5. Fit with the schema

- bdlaws Acts and Ordinances map cleanly, and their repeal notes give `revokes` links with express clauses. Ordinances fit `emergency regulation`, as with Indonesia's Perppu, and the 2024 -> 2026 ordinance-to-Act chain is a direct analogue of Perppu 2/2022 -> Law 6/2023.
- Guidelines and circulars lack visible numbers; we used "unnumbered (...)".
- Budget-linked SROs change every June and some are time-limited (180 days), so `expired` will be common.
- `language`: Acts are bn; SROs from NBR and some policies are in English. Check each.

## 6. Risks and open questions

- Policy and guideline texts (RE Policy 2025, Net Metering Guideline 2025, rooftop programme circular, EV guidelines) were not read; dates come from press reports.
- Section 34 changes by the 2023 BERC amendment may survive the deletion of s. 34A; check the consolidated Act.
- The 2026 solar ordinance lapses unless Parliament approves it; its substantive scope (what counts as "special solar") was not read.
- MCPP and IEPMP status under the post-2026 government are unclear.
- FY2024-25 and FY2025-26 customs treatment of solar panels and the SRO number of the September 2026 notification were not found.
- Not scouted: BERC regulations (licensing, tariff), Solar Park guidelines, Energy Efficiency and Conservation Master Plan, EV charging guidelines, Private Sector Power Generation Policy.

## 7. Sources

- http://bdlaws.minlaw.gov.bd/laws-of-bangladesh-chronological-index.html
- http://bdlaws.minlaw.gov.bd/act-902.html
- http://bdlaws.minlaw.gov.bd/act-1423.html
- http://bdlaws.minlaw.gov.bd/act-1503.html
- http://bdlaws.minlaw.gov.bd/act-1669.html
- http://bdlaws.minlaw.gov.bd/act-1059.html
- http://bdlaws.minlaw.gov.bd/act-1511.html
- http://bdlaws.minlaw.gov.bd/act-1647.html
- http://bdlaws.minlaw.gov.bd/act-1228.html
- http://bdlaws.minlaw.gov.bd/act-1107.html
- http://bdlaws.minlaw.gov.bd/act-1743.html
- https://www.dpp.gov.bd/bgpress/
- https://powerdivision.gov.bd/
- https://nbr.gov.bd/
- https://www.dhakatribune.com/bangladesh/government-affairs/380534/renewable-energy-policy-approved
- https://www.thedailystar.net/business/news/govt-unveils-new-renewable-energy-policy-3921096
- https://www.tbsnews.net/bangladesh/energy/target-generate-30-electricity-renewables-2040-1456566
- https://thefinancialexpress.com.bd/stock/bangladesh/draft-renewable-energy-policy-2025-falls-short-of-means-to-attain-targets
- https://gpg-pdf.chambers.com/Power-Generation-Transmission-and-Distribution-2025/33/
- https://rise.esmap.org/data/files/library/bangladesh/Renewable%20Energy/Bangladesh_NET%20METERING%20GUIDELINES_2018.pdf
- https://ieefa.org/sites/default/files/2025-08/Rooftop%20Solar%E2%80%99s%20Time%20to%20Shine%20in%20Bangladesh%20.pdf
- https://www.pv-magazine.com/2025/09/10/bangladesh-revises-net-metering-rules-to-expand-solar/
- https://cpd.org.bd/wp-content/uploads/2025/07/CPD_Briefing_on_National_Rooftop_Project.pdf
- https://www.tbsnews.net/bangladesh/energy/solar-panels-be-installed-government-buildings-educational-institutions-hospitals
- https://thefinancialexpress.com.bd/trade/electric-vehicle-reg-policy-takes-effect
- https://thefinancialexpress.com.bd/trade/nbr-cuts-solar-equipment-import-tax-to-1pc
- https://thefinancialexpress.com.bd/trade/high-customs-duties-dwarf-rooftop-solar-ambitions
- https://www.pv-magazine.com/2026/09/18/bangladesh-cuts-solar-equipment-import-taxes-to-1/
- https://www.thedailystar.net/opinion/views/news/why-the-energy-and-power-master-plan-must-be-reviewed-3785171
- https://tds-images.thedailystar.net/news/bangladesh/news/power-energy-govt-unveils-new-25-year-master-plan-4075896
- https://cpd.org.bd/resources/2024/08/Paper_Power-and-Energy-Sector-Reform-Agenda-for-the-Interim-Government_first-draft.pdf
- https://moef.portal.gov.bd/sites/default/files/files/moef.portal.gov.bd/publications/f6c2ae73_30eb_4174_9adb_022323da1f39/Mujib%20Climate%20Prosperity%20Plan%202022-2041.pdf
- https://www.tbsnews.net/node/576230
- https://thefinancialexpress.com.bd/trade/govts-executive-authority-to-raise-power-and-gas-prices-cancelled-through-ordinance
- https://www.jagonews24.com/en/national/news/78733
