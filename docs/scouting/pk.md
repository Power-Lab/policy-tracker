# Scouting report: Pakistan

Prepared 2026-11-19 for the Power Transformation Lab policy tracker. It comes with `pk-rules.csv` (15 candidate rows), `pk-country.csv` and `pk-sources.csv`. Everything here is a lead for reviewers, not checked data; several rows rest on Pakistani business press (Dawn, Business Recorder, Express Tribune, Profit) and say so in their notes.

How this was checked: NEPRA PDFs were downloaded with `curl` and read through their text layer (the December 2025 Prosumer Regulations text and the August 2026 amending S.R.O.). An FBR circular was downloaded but its text layer covers only the first page. Other facts come from web searches. Pakistan Code, the Ministry of Climate Change and powerdivision.gov.pk did not respond; PPIB returned 403.

## 1. Summary

- **Structure.** The NEPRA Act 1997 (Act XL of 1997) sets up NEPRA as licensing and tariff regulator. The 2018 amendment (Act XII of 2018, 2018-05-02) restructured the sector toward competition: supplier licences, market and system operator functions, a National Electricity Policy and Plan (s. 14A), an appellate tribunal, and an end to distribution companies' exclusive supply rights. The National Electricity Policy 2021 (CCI, 2021-06-21) followed. The **Competitive Trading Bilateral Contract Market (CTBCM)**, run by the Independent System and Market Operator (ISMO), began commercial operations on 2026-01-22 per press reports, and a first **wheeling auction** framework (800 MW) was approved in March 2026.
- **Distributed solar** moved from **net metering** (S.R.O. 892(I)/2015) to **net billing** under the **NEPRA (Prosumer) Regulations, 2026**, notified around 2026-02-09: exports are bought at the national average energy purchase price under five-year agreements. An August 2026 amendment (S.R.O. 1330(I)/2026) lets distribution companies approve systems of 25 kW or below without NEPRA concurrence.
- **Renewable procurement**: the ARE Policy 2019 (20% by 2025, 30% by 2030, competitive bidding) succeeded the 2006 RE policy. IGCEP 2025-35 / Integrated System Plan 2025-35 was filed by ISMO and reportedly approved by NEPRA in 2026.
- **Trade and manufacturing**: the **Finance Act 2024** set 0% customs duty on machinery and certain inputs for local manufacture of solar panels, inverters and batteries; the **Finance Act 2025** removed the Sixth Schedule sales tax exemption on solar panels and applied a reduced 10% rate to imports (cut from a proposed 18%).
- **EVs**: National EV Policy 2019 (cabinet 2019-11-05) and the **NEV Policy 2025-30** (launched 2025-06-19), with a 30% EV share of new sales by 2030 and subsidies for two- and three-wheelers.
- **Tracking difficulty: moderate to high.** Everything is in English, and NEPRA numbers its regulations by S.R.O. But policies are approved by the CCI or Cabinet without a gazette number, fiscal measures are buried in annual Finance Acts and schedule serial numbers, and several ministry sites are unreachable. NEPRA's site is the most useful source.

## 2. Legal hierarchy and document types

| Rank | Type | Issuer | Numbering | Our `doc_type` |
| --- | --- | --- | --- | --- |
| 1 | Constitution (1973) | - | Articles; Federal Legislative List Part II (electricity) gives the CCI a role | (not tracked) |
| 2 | Act of Parliament | Majlis-e-Shoora, President's assent | "Act XII of 2018" (Roman numerals per year) | law |
| 2 | Finance Act | Parliament (annual budget) | unnumbered by convention; amends Customs Act, Sales Tax Act schedules | law |
| 2 | Ordinance | President (Art. 89) | "Ordinance No. N of YYYY" | emergency regulation |
| 3 | Rules | Federal Government | S.R.O. N(I)/YYYY | government regulation |
| 3 | NEPRA regulations, determinations | NEPRA | S.R.O. N(I)/YYYY; decisions by case number | regulator determination |
| 3 | Customs / sales tax notifications | FBR | S.R.O. N(I)/YYYY | ministerial regulation |
| 4 | Policies (ARE, NEP, EV, NEV) | CCI or Federal Cabinet | unnumbered | plan |
| 4 | Plans (IGCEP, ISP, NE Plan) | ISMO / Power Division, approved by NEPRA or Cabinet | unnumbered | plan |

## 3. Official sources

| Name | URL | Tier | Languages | What it holds | Access observed |
| --- | --- | --- | --- | --- | --- |
| NEPRA | https://www.nepra.org.pk/ | 2 | en | Regulations (S.R.O. PDFs), determinations, IGCEP filings, admission notices | HTTP 200; folder listings 403 |
| FBR | https://www.fbr.gov.pk/ | 2 | en | Finance Acts, SROs, circulars | HTTP 200 |
| AEDB | https://www.aedb.org/ | 2 | en | RE policies, net metering info | HTTP 200 |
| Power Division | https://www.power.gov.pk/ | 2 | en | Policies, plans | HTTP 200 (powerdivision.gov.pk: 000) |
| ISMO | https://ismo.gov.pk/ | 2 | en | Market operation, wheeling auctions | HTTP 200 |
| CPPA-G | https://cppa.gov.pk/ | 2 | en | Market data | HTTP 200 |
| Ministry of Industries and Production | https://moip.gov.pk/ | 2 | en | Auto and NEV policies | HTTP 200 |
| Ministry of Climate Change | https://www.climatechange.gov.pk/ | 2 | en | EV Policy 2019 | unreachable (000) |
| PPIB | https://www.ppib.gov.pk/ | 2 | en | IPP policies, net metering guide | 403 |
| Pakistan Code | https://pakistancode.gov.pk/ | 1 | en, ur | Federal Acts | unreachable (000) |

## 4. Key instruments by category

**Electricity**
- NEPRA Act 1997 and Amendment Act 2018 (framework-law, grid-market-rules).
- National Electricity Policy 2021; IGCEP / ISP 2025-35 (power-plans).
- CTBCM commercial operations (2026-01-22) and the wheeling auction mechanism (2026) (grid-market-rules, wheeling-dppa).
- Net Metering Regulations 2015 (S.R.O. 892(I)/2015), replaced by the Prosumer Regulations 2026, amended by S.R.O. 1330(I)/2026 (rooftop-solar).
- RE Policy 2006 and ARE Policy 2019 (re-pricing).

**Energy**
- National EV Policy 2019 and NEV Policy 2025-30 (ev-adoption).

**Supply chain**
- ARE Policy 2019 manufacturing incentives; Finance Act 2024 Fifth Schedule 0% duty on inputs for solar panel, inverter and battery makers (manufacturing-incentives).

**Trade**
- Finance Act 2024 (import-tariffs on inputs) and Finance Act 2025 (10% sales tax on imported panels) (import-tariffs). No anti-dumping, import-standard or export-restriction instrument specific to clean tech was found.

## 5. Fit with the schema

- NEPRA regulations fit `regulator determination` with S.R.O. numbers; the S.R.O. series is shared across all federal bodies, so the number alone does not identify the issuer.
- CCI/Cabinet policies have no number and often no gazette; dates are approval-meeting dates reported in the press.
- Finance Acts change many unrelated things; rows should be scoped to the relevant schedule entries (we did this in `title_english`). Sales tax on imports is not a customs duty but fits `import-tariffs` best.
- The CTBCM and wheeling auctions are regulator approvals of operator documents (Market Commercial Code, auction guidelines); `regulator determination` works but each needs its NEPRA decision reference.

## 6. Risks and open questions

- Prosumer Regulations: gazetted S.R.O. number and exact date not found; the linked text is NEPRA's December 2025 version with a blank S.R.O. Reported buyback rates (Rs11/kWh, Rs25.9/kWh) were not confirmed.
- Net Metering Regulations 2015: issue day reported as 1 or 15 September 2015.
- ARE Policy 2019: CCI approval date not found; sometimes called ARE Policy 2020.
- IGCEP/ISP 2025-35: NEPRA approval date and decision not found.
- NEV Policy 2025-30: approval body and date inconsistent across reports; official text not located.
- Finance Act 2025: reports conflict on whether fully assembled panels or only components bear 10%.
- Not yet scouted: NEPRA wheeling regulations (2016), Auto Industry Development and Export Policy 2021-26, National Electricity Plan 2023-27, Electric Vehicle two/three-wheeler phase (2020), IGCEP 2022-31.

## 7. Sources

- https://www.nepra.org.pk/
- https://nepra.org.pk/Admission%20Notices/2025/12%20Dec/NEPRA%20Prosumer%20Regulations.pdf
- https://www.nepra.org.pk/Legislation/3-Reg/3.35%20NEPRA%20%20Prosumer%20Regulations%202026/SRO%201330(I)-2026%20Dated%2006-08-2026.pdf
- https://www.nepra.org.pk/Legislation/3-Reg/3.13%20NEPRA%20(Alternative%20&%20Renewable%20Energy)%20Distributed%20Generation%20and%20Net%20Metering%20Regulations,%202015/S.R.O%201135(I)-2018%2013-09-2018.pdf
- https://www.nepra.org.pk/Legislation/3-Reg/3.13%20NEPRA%20(Alternative%20&%20Renewable%20Energy)%20Distributed%20Generation%20and%20Net%20Metering%20Regulations,%202015/SRO%201025(I)2017%2010-10-2017.pdf
- https://ke.com.pk/assets/uploads/2024/11/SRO-892-Sep-2015.pdf
- https://nepra.org.pk/Admission%20Notices/2025/08%20Aug/IGCEP_2025-35_R2.pdf
- https://www.nepra.org.pk/publications/Annual%20Reports/Annual%20Report%202017-18.pdf
- https://policy.asiapacificenergy.org/sites/default/files/Regulation%20of%20Generation%2C%20Transmission%20and%20Distribution%20of%20Electric%20Power%20%28Amendment%29%20Act%2C%202018.pdf
- https://practiceguides.chambers.com/practice-guides/power-generation-transmission-distribution-2025/pakistan
- https://www.brecorder.com/news/40406474/nepra-notifies-prosumer-regulations
- https://www.pv-magazine.com/2025/12/18/pakistan-unveils-new-net-metering-rules-for-rooftop-pv/
- https://www.dawn.com/news/1574133
- https://www.climate-laws.org/geographies/pakistan/policies/alternative-and-renewable-energy-policy-2019
- https://rise.esmap.org/data/files/library/pakistan/Renewable%20Energy/Pakistan_Alternative%20and%20Renewable%20energy%20Policy_2019.pdf
- https://www.dawn.com/news/1630689/cci-approves-national-electricity-policy-2021-to-reform-power-sector-hammad-azhar
- https://www.icimod.org/wp-content/uploads/2022/07/National-Electricity-Policy-2021.pdf
- https://www.brecorder.com/news/40371311/ctbcm-commercial-operations-may-begin-by-sept-end
- https://tribune.com.pk/story/2541896/competitive-power-market-faces-delays
- https://profit.pakistantoday.com.pk/2026/03/25/pakistans-power-regulator-approves-first-electricity-wheeling-auction-mechanism
- https://profit.pakistantoday.com.pk/2019/11/05/cabinet-approves-electric-motor-vehicle-policy
- https://arabnews.pk/node/1580471
- https://www.dawn.com/news/1565948/pakistan-launches-electric-vehicle-plan-with-cars-in-slow-lane
- https://www.dawn.com/news/1918321
- https://www.arabnews.pk/node/2605436
- https://fbr.gov.pk/Budget2024-25/FinanceBill/Notes-on-Clauses.pdf
- https://assets.kpmg.com/content/dam/kpmg/pk/pdf/2024/7/a_brief_on_finance_act_2024.pdf
- https://download1.fbr.gov.pk/Docs/202584118361586CircularNO02of2025-26SalesTax%26FederalExcise.pdf
- https://assets.kpmg.com/content/dam/kpmg/pk/pdf/2025/07/A-Brief-on-Finance-Act-2025.pdf
- https://www.arabnews.pk/node/2604926
- https://www.aedb.org/ae-technologies/solar-power/net-metering
- https://www.power.gov.pk/
- https://moip.gov.pk/
