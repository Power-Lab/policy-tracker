# Scouting report: India

Prepared 2026-11-19 for the Power Transformation Lab policy tracker. It comes with [`in-rules.csv`](in-rules.csv) (40 candidate rules, 32-column schema), [`in-country.csv`](in-country.csv) and [`in-sources.csv`](in-sources.csv). Everything here is a lead for reviewers, not checked data. Where a fact rests only on news, a law-firm note or a tax portal, the row's `notes` say so.

How this was checked: official portals were requested with `curl` (desktop user agent, through the session proxy); the status codes below come from those requests. PIB press releases were read directly. One gazette copy (Rights of Consumers Rules 2020, hosted by MERC) was downloaded and read through its text layer. Web searches filled the remaining gaps. The Gazette of India and CBIC could not be reached from this environment, so no S.O./G.S.R. or customs notification was read in its official copy.

---

## 1. Summary

- **Structure.** Electricity is on the Constitution's concurrent list. The **Electricity Act, 2003** (Act 36 of 2003) is the framework law: generation is delicensed (captive generation included), transmission and distribution are licensed, and open access is provided for. The **Ministry of Power** (MoP) makes Rules under section 176 and policy orders; the **Central Electricity Authority** (CEA) prepares the National Electricity Plan; **CERC** and the state commissions (SERCs) regulate tariffs, grid access and markets. Renewable policy (bidding schemes, rooftop solar, ALMM, solar PLI) sits with the **Ministry of New and Renewable Energy** (MNRE).
- **Renewable demand-side rules.** Renewable purchase obligations moved onto a statutory footing under the **Energy Conservation (Amendment) Act, 2022**: a renewable consumption obligation (S.O. 4617(E), 2023-10-20) replaced by a revised notification of 2025-09-27. The **Green Energy Open Access Rules, 2022** (G.S.R. 418(E), 2022-06-06) cut the open-access threshold for green power from 1 MW to 100 kW. ISTS charges for solar and wind are waived fully for projects commissioned by 30 June 2025, then reduced 25% a year.
- **Carbon pricing.** The 2022 amendment also enabled the **Carbon Credit Trading Scheme, 2023** (S.O. 2825(E), 2023-06-28; offset mechanism added December 2023). The first binding intensity targets came with the **GHG Emission Intensity Target Rules, 2025** (MoEFCC, notified 2025-10-08; extended to more sectors in January 2026).
- **Supply chain: a dense, layered toolkit.** India combines (a) **production-linked incentives** (solar PV modules tranche I Rs 4,500 crore and tranche II Rs 19,500 crore; ACC batteries Rs 18,100 crore; automobiles and components Rs 25,938 crore; rare earth magnets Rs 7,280 crore approved 2025-11-26) with (b) **local-content conditions** inside those schemes (value-addition milestones) and in EV schemes (SPMEPCI: 50% domestic value addition in five years in exchange for 15% duty on CBU imports), and (c) **critical-mineral policy**: the MMDR Amendment Act 2023 (central auctions of critical minerals, in force 2023-08-17), the National Critical Mineral Mission (2025-01-29) and a recycling incentive (2025-09-03).
- **Trade: India is the most active user of trade tools in our sample.**
  - **Approved lists:** the ALMM Order (2019) with List-I (modules, first list 2021-03-10; in abeyance FY 2023-24), List-II for cells (from 2026-06-01) and List-III for ingots and wafers (from 2028-06-01).
  - **Standards:** a compulsory BIS registration order for solar goods (S.O. 2920(E), 2017) replaced by S.O. 492(E) of 2025-01-27.
  - **Tariffs:** basic customs duty on cells 25% and modules 40% from 2022-04-01, rebalanced in Budget 2025 to 20% BCD plus AIDC (7.5% cells, 20% modules); duty exemptions for 25 critical minerals from July 2024.
  - **Trade remedies:** safeguard duty on cells (2018-2021); anti-dumping duty on aluminium solar frames from China (16/2024-Customs (ADD)) and on solar glass from China and Vietnam (11/2025-Customs (ADD)); DGTR recommended anti-dumping duty of up to 30% on Chinese cells and modules (final findings 2025-09-29), but no Finance Ministry notification was found.
  - **Investment screening:** Press Note 3 (2020) requires government approval for investment from land-border countries; Press Note 2 (2026) eases it for non-controlling stakes up to 10%.
- **Export restrictions.** No Indian export control on clean-tech goods or critical minerals was found in this pass; reviewers should search DGFT notifications (rare earths, IREL) before concluding there are none.
- **Tracking difficulty: moderate to high.** Everything binding is in English (with Hindi), and numbering is regular (S.O./G.S.R. numbers with "(E)", "Notification No. NN/YYYY-Customs (ADD)"). But the two tier-1 sources (eGazette, CBIC) failed TLS verification from our proxy, MNRE's new site serves a script shell, and MoP's site migration broke old PDF links. Many key "instruments" are Cabinet approvals announced by press release, with the binding guidelines published separately and often weeks later.
- **Recommendation: worth adding for the supply-chain and trade modules.** India has more instruments per trade topic than any Southeast Asian country, and ALMM, PLI and the solar duties are the reference cases the lab's comparisons will need. Plan for manual or browser-based access to eGazette and CBIC, and for one row per notification rather than per scheme where amendments matter (ALMM, PM E-DRIVE, CCTS).

## 2. Legal hierarchy and document types

From highest to lowest rank. Numbering formats come from the documents and summaries we saw.

| Rank | Type | Issuer | How it is numbered and cited | Our `doc_type` |
| --- | --- | --- | --- | --- |
| 1 | Constitution | People | Article; Seventh Schedule lists (electricity is List III, entry 38) | (not tracked) |
| 2 | **Act of Parliament** | Parliament, assented by the President | "Act 36 of 2003", "Act No. 19 of 2022"; amending Acts named "... (Amendment) Act, YYYY" | `law` |
| 3 | **Rules** and **statutory orders/notifications** of the Central Government | Ministries in the name of the Central Government, under an Act | Gazette of India, Extraordinary, Part II Section 3 (sub-sections from general knowledge: 3(i) G.S.R., 3(ii) S.O.): **G.S.R. NNN(E)** (rules, e.g. G.S.R. 818(E) of 2020) or **S.O. NNNN(E)** (orders, schemes, e.g. S.O. 2825(E) CCTS) | `government regulation` |
| 3a | **Customs notifications** | Ministry of Finance (Department of Revenue) under the Customs Tariff Act | Separate series per year: "NN/YYYY-Customs" (tariff), "-Customs (ADD)", "-Customs (CVD)", "-Customs (SG)" | `government regulation` |
| 4 | **Regulations** of statutory regulators | CERC, SERCs, CEA (technical standards) | CERC file numbers (e.g. L-1/261/2021/CERC) and short titles with year | `regulator determination` |
| 5 | **Ministry orders, office memoranda, guidelines and resolutions** | MNRE, MoP, MHI | File numbers, e.g. O.M. No. 283/54/2018-GRID SOLAR (ALMM); bidding guidelines issued as MoP Resolutions in the Gazette | `ministerial regulation` (ALMM) or `decision` (guidelines, orders) |
| 6 | **Cabinet-approved schemes and missions** | Union Cabinet, then implementing ministry | No number; dated by Cabinet meeting and PIB release, followed by gazette notification and/or guidelines | `decision` |
| 7 | **Press Notes** (FDI policy) | DPIIT | "Press Note No. 3 (2020 Series)"; legal effect through FEMA (Non-debt Instruments) Rules amendments | `circular` |
| 8 | **Plans** | CEA (National Electricity Plan, under section 3(4) of the Electricity Act) | Volume and period | `plan` |
| (other) | **DGTR findings** | Directorate General of Trade Remedies | Case numbers e.g. AD(OI) 27/2023; recommendations only, binding once the Finance Ministry notifies | `decision` with `binding = no` |

Validity notes: Rules and S.O. notifications usually take effect on publication in the Gazette unless they state otherwise. Acts often commence on a date notified separately (the Energy Conservation (Amendment) Act 2022 is an example). Customs ADD notifications can apply retroactively from the date of provisional duty (solar glass).

## 3. Official sources

Requested 2026-11-19 with `curl` through the session proxy (desktop user agent).

| Name | URL | Tier | Languages | What it holds | Access result |
| --- | --- | --- | --- | --- | --- |
| Gazette of India (eGazette) | https://egazette.gov.in/ | 1 | hi, en | All S.O./G.S.R. notifications, Acts | **Failed**: TLS verification error ("unable to get local issuer certificate"); WebFetch of a gazette PDF gave **503** |
| India Code | https://www.indiacode.nic.in/ | 1 | en, hi | Central Acts with amendment history | **200** first request; connection failed on retry |
| CBIC (customs notifications) | https://www.cbic.gov.in/ ; https://taxinformation.cbic.gov.in/ | 1 | en, hi | Customs tariff, ADD, CVD, SG notifications | **Failed**: TLS verification error; one proxy tunnel drop |
| PIB | https://www.pib.gov.in/ | 2 | en, hi | Press releases by ministry | **200**, server-rendered, scrapeable |
| MNRE | https://mnre.gov.in/ | 2 | en, hi | ALMM lists and orders, PLI, schemes, "centre rules" | **200** but identical 4.7 KB script shell on every page; old document URLs **404** |
| Ministry of Power | https://powermin.gov.in/ | 2 | en, hi | Rules, orders, circulars | **200** (redirect to www); older PDF and circular URLs **404** |
| CERC | https://cercind.gov.in/ | 2 | en | Regulations (Current_reg.html), orders | **200** |
| CEA | https://cea.nic.in/ | 2 | en | NEP, technical standards | **200**; NEP PDF link **404** |
| BEE | https://beeindia.gov.in/ | 2 | en | CCTS procedures | **200**; one CCTS PDF **404** |
| DGTR | https://www.dgtr.gov.in/ | 2 | en | Trade remedy initiations and findings | **200** (redirect to /en) |
| DPIIT | https://dpiit.gov.in/ | 2 | en | Press Notes, FDI policy | **200** (redirect to www) |
| Ministry of Heavy Industries | https://heavyindustries.gov.in/ | 2 | en, hi | PLI ACC, PLI Auto, SPMEPCI, FAME | **200** |
| PM E-DRIVE portal | https://pmedrive.heavyindustries.gov.in/ | 2 | en | PM E-DRIVE gazette notifications | **200**; extension PDF downloaded |
| Ministry of Mines | https://mines.gov.in/ | 2 | en, hi | MMDR, NCMM, auctions | **200** (3.8 KB page, probably script shell) |
| BIS | https://www.bis.gov.in/ | 2 | en, hi | Quality control orders | **200** |
| MoEFCC | https://moef.gov.in/ | 2 | en, hi | GHG intensity target rules | **200** |
| PM India | https://www.pmindia.gov.in/ | 2 | en | Cabinet decision releases | **200** |
| PM Surya Ghar portal | https://pmsuryaghar.gov.in/ | 2 | en | Scheme guidelines | **403** |
| MERC (copies of central rules) | https://merc.gov.in/ | 3 | en | Gazette copies of MoP rules | **200** |
| PRS Legislative Research | https://prsindia.org/ | 4 | en | Act texts, bill summaries | **200** |
| IEA Policies database | https://www.iea.org/policies | 4 | en | Policy summaries | not tried (search results only) |

Not tried: dgft.gov.in (export policy), seci.co.in, ireda.in, grid-india.in, the Lok Sabha/Rajya Sabha question archives (eparlib.sansad.in, which reproduces several notifications).

## 4. Key instruments by category

Row ids refer to `in-rules.csv`.

### Electricity

- **framework-law**: Electricity Act 2003 (`IN-ACT-2003-36`). A Draft Electricity (Amendment) Bill, 2025 was circulated on 2025-10-09; introduction in Parliament not confirmed (not recorded).
- **rooftop-solar**: Electricity (Rights of Consumers) Rules 2020, G.S.R. 818(E), net metering up to 10 kW (`IN-GSR-2020-818`; amended 2024-02-22); PM Surya Ghar (`IN-CAB-2024-PM-SURYA-GHAR`).
- **wheeling-dppa / captive-power**: Green Energy Open Access Rules 2022 (`IN-GSR-2022-418`; amended 2023); RCO 2025 covers open access and captive users (`IN-NOTIF-MOP-2025-RCO`).
- **grid-market-rules**: ISTS charge waiver (`IN-ORDER-MOP-2021-ISTS`). CERC GNA Regulations 2022 (notified 2022-06-07, effective 2022-10-15 per trade press) and the CERC sharing regulations' fourth amendment of 2025-06-26 are not recorded but should be added if the grid module is extended to India.
- **re-pricing**: RCO 2023 and 2025 (`IN-SO-2023-4617`, `IN-NOTIF-MOP-2025-RCO`); solar TBCB guidelines 2023 (`IN-RES-MOP-2023-SOLAR-TBCB`). The MoP RPO/ESO trajectory order of 2022-07-22 is described in notes only.
- **power-plans**: NEP 2022-32 Vol. I (`IN-PLAN-CEA-2023-NEP`); Vol. II Transmission notified October 2024 (not recorded).
- **energy-storage**: BESS VGF 2023 (`IN-CAB-2023-BESS-VGF`); the 2025 30 GWh tranche and a reported Rs 14,500 crore VGF for 2026-31 are in notes.

### Energy

- **energy-efficiency / carbon-pricing**: Energy Conservation Act 2001 and 2022 amendment (`IN-ACT-2001-52`, `IN-ACT-2022-19`); CCTS 2023 (`IN-SO-2023-2825`); GHG Emission Intensity Target Rules 2025 (`IN-RULES-MOEFCC-2025-GEI`).
- **energy-strategy**: National Green Hydrogen Mission (`IN-CAB-2023-NGHM`).
- **ev-adoption**: FAME II (`IN-SO-2019-1300`, expired); PM E-DRIVE (`IN-SO-2024-4259`, extended to 2028-03-31).

### Supply chain

- **manufacturing-incentives**: PLI solar tranches I and II (`IN-GUIDE-MNRE-2021-PLI-SOLAR-T1`, `-T2`); PLI ACC (`IN-NOTIF-MHI-2021-PLI-ACC`); PLI Auto (`IN-SO-2021-3946`); SIGHT under NGHM; rare earth magnets (`IN-CAB-2025-REPM`); recycling (`IN-CAB-2025-CM-RECYCLING`); SPMEPCI (`IN-NOTIF-MHI-2024-SPMEPCI`).
- **local-content**: value-addition conditions in PLI ACC, PLI Auto and SPMEPCI; ALMM orders (also tagged import-standards). Domestic content requirements (DCR) in PM Surya Ghar, PM-KUSUM and the CPSU scheme were not confirmed and are not recorded.
- **mineral-downstreaming**: MMDR Amendment Act 2023 (`IN-ACT-2023-16`); NCMM (`IN-CAB-2025-NCMM`); recycling scheme; REPM scheme; critical-mineral customs exemption (`IN-CUS-2024-CRITMIN`).
- **investment-rules**: Press Note 3 (2020) and Press Note 2 (2026) (`IN-PN-DPIIT-2020-3`, `IN-PN-DPIIT-2026-2`); SPMEPCI investment commitment.

### Trade

- **import-standards**: ALMM Order 2019 (`IN-NOTIF-MNRE-2019-ALMM`), List-II cells (`IN-OM-MNRE-2024-ALMM-II`), List-III wafers (`IN-OM-MNRE-2026-ALMM-III`, pending to 2028-06-01); solar QCOs 2017 and 2025 (`IN-SO-2017-2920`, `IN-SO-2025-492`). A BIS registration requirement for lithium-ion cells and batteries (MeitY Compulsory Registration Scheme) exists but was not dated in this pass.
- **import-tariffs**: BCD on cells and modules 2022 (`IN-CUS-2022-BCD-SOLAR`) and Budget 2025 changes (`IN-CUS-2025-AIDC-SOLAR`); critical minerals 2024 (`IN-CUS-2024-CRITMIN`); SPMEPCI concessional duty.
- **trade-remedies**: safeguard duty on cells (`IN-CUS-SG-2018-1`); ADD on aluminium frames (`IN-CUS-ADD-2024-16`) and solar glass (`IN-CUS-ADD-2025-11`); DGTR findings on cells (`IN-DGTR-2025-SOLAR-CELLS`, pending).
- **export-restrictions**: none found.

## 5. Fit with the schema

- **Rules vs Acts.** Central Rules (G.S.R.) and statutory S.O. notifications map to `government regulation`. The ALMM orders are ministry office memoranda with regulatory effect; we used `ministerial regulation`. Cabinet-approved schemes map to `decision`; where a scheme has a gazette notification (PLI ACC, PLI Auto, FAME II, PM E-DRIVE) we used the notification as the row and `government regulation`.
- **Scheme vs guidelines.** Many schemes have three dated events: Cabinet approval, gazette notification and operational guidelines. We dated rows by the notification or guidelines where known and put the other dates in notes. Reviewers should agree a single convention before more Indian rows are added.
- **Numbers.** Several key instruments are missing a confirmed number (customs notifications for the 2022 and 2025 solar duties, PLI ACC S.O., RCO 2025 S.O.). We used `unnumbered (...)` with an explanation rather than guessing.
- **Pending and not yet effective.** ALMM List-III is issued but applies from 2028-06-01; we set `status = pending` with date_in_force 2028-06-01, following the search protocol's "enacted but not commenced". The DGTR cell findings are `pending` with `binding = no` and an empty date_in_force, because no duty is confirmed; this departs from the spec's "date_in_force may not be empty" and is flagged in the row.
- **Trade remedies.** ADD notifications can take effect from the provisional-duty date (solar glass: 2024-12-04), so date_in_force can precede date_signed.
- **technologies field** fits well; hydrogen appears in NGHM and PLI Auto; grid-equipment was not needed.
- **language.** Binding texts are bilingual (Hindi and English) in the Gazette; we recorded `en`.

## 6. Risks and open questions

1. **Tier-1 access.** eGazette and CBIC failed TLS verification from this environment. Until a browser-based or partner route is in place, numbers and dates for customs and gazette notifications rest on tax portals and law-firm notes.
2. **Solar cell anti-dumping duty.** DGTR final findings of 2025-09-29 recommend 0-30% duty on Chinese cells and modules; we found no Finance Ministry notification. Check whether it was imposed or lapsed.
3. **ISTS waiver status.** The waiver now sits in CERC regulations (fourth amendment of 2025-06-26); decide whether the 2021 MoP order or the CERC amendment is the row of record.
4. **RCO instrument.** Trade press links the 2025 RCO revision to "Electricity (Amendment) Rules, 2025"; check whether the obligation is in an EC Act notification, an Electricity Act rule, or both.
5. **Energy Conservation (Amendment) Act 2022 commencement.** The Act leaves commencement to notification; date_in_force rests on one database.
6. **Press Note 2 (2026).** All details come from law-firm notes and news, which conflict on whether Chinese direct investors benefit.
7. **Basic customs duty instruments.** The legal vehicle for the April 2022 BCD rates (customs notification or Finance Act tariff amendment) was not identified.
8. **Earlier-instrument rows from general knowledge.** Energy Conservation Act 2001 and Electricity Act 2003 dates are from general knowledge (low/medium confidence).
9. **Not yet recorded but likely relevant:** CERC GNA Regulations 2022; NEP Vol. II (2024); BESS VGF 2025 tranche and the 2026-31 VGF; EMPS 2024; SIGHT guidelines; Mineral (Auction) Rules amendments; provisional ADD 26/2024-Customs (ADD); safeguard extension 02/2020-Customs (SG); PM-KUSUM and CPSU scheme DCR; MeitY CRS for lithium-ion batteries; DGFT export policy on rare earths.

## 7. Sources

Official (tier 1-2):
- https://www.pib.gov.in/PressReleasePage.aspx?PRID=1842737 (GEOA Rules notified 06.06.2022)
- https://www.pib.gov.in/PressReleasePage.aspx?PRID=2008289 (Rights of Consumers amendment, 2024-02-23 release)
- https://www.pib.gov.in/PressReleasePage.aspx?PRID=1928750 (NEP 2022-32)
- https://www.pib.gov.in/PressReleasePage.aspx?PRID=1717938 (Cabinet approval of PLI ACC, 2021-05-12)
- https://www.pib.gov.in/PressReleasePage.aspx?PRID=1757651 (PLI Auto notification)
- https://www.pib.gov.in/PressReleasePage.aspx?PRID=1615711 (Press Note 3)
- https://www.pib.gov.in/PressReleasePage.aspx?PRID=1985837 (MMDR Amendment 2023)
- https://www.pib.gov.in/PressReleasePage.aspx?PRID=1896066 (PLI solar tranche II guidelines)
- https://www.pib.gov.in/PressReleasePage.aspx?PRID=2241170 (ISTS waiver, Rajya Sabha answer 2026-03-17)
- https://www.pib.gov.in/PressReleasePage.aspx?PRID=2039091 (National Green Hydrogen Mission)
- https://merc.gov.in/wp-content/uploads/2022/07/1.-Gazette_Electricity-Rights-of-Consumers-Rules-2020-1.pdf
- https://merc.gov.in/wp-content/uploads/2022/07/Electricity-Promoting-RE-through-Green-Energy-OA-_Rules_2022-1.pdf
- https://mnre.gov.in/en/approved-list-of-models-and-manufacturers-almm/
- https://mnre.gov.in/en/production-linked-incentive-pli/
- https://mnre.gov.in/en/centre-rules/
- https://heavyindustries.gov.in/pli-scheme-national-programme-advanced-chemistry-cell-acc-battery-storage
- https://www.heavyindustries.gov.in/sites/default/files/2025-06/press_release_spmepci.pdf
- https://pmedrive.heavyindustries.gov.in/docs/policy_document/Extension%20of%20Scheme%20till%2031%2003%202028%20dated%2007%2008%202025.pdf
- https://www.pmindia.gov.in/en/news_updates/cabinet-approves-national-critical-mineral-mission/
- https://www.pmindia.gov.in/en/news_updates/cabinet-approves-pm-surya-ghar-muft-bijli-yojana/
- https://www.pmindia.gov.in/en/news_updates/cabinet-approves-rs-1500-crore-incentive-scheme-to-promote-critical-mineral-recycling-in-the-country/
- https://www.newsonair.gov.in/cabinet-approves-rare-earth-magnet-manufacturing-scheme
- https://www.newsonair.gov.in/ministry-of-new-and-renewable-energy-extends-almm-framework-to-cover-solar-ingots-and-wafers-from-june-1-2028
- https://www.cercind.gov.in/Current_reg.html
- Portals checked: https://egazette.gov.in/, https://www.indiacode.nic.in/, https://www.cbic.gov.in/, https://taxinformation.cbic.gov.in/, https://powermin.gov.in/, https://cea.nic.in/, https://beeindia.gov.in/, https://www.dgtr.gov.in/en, https://dpiit.gov.in/, https://mines.gov.in/, https://www.bis.gov.in/, https://moef.gov.in/, https://pmsuryaghar.gov.in/, https://heavyindustries.gov.in/, https://pmedrive.heavyindustries.gov.in/
- Dead links found: https://cea.nic.in/wp-content/uploads/document_upload/2023/06/NEP_2022_32_FINAL_GAZETTE.pdf (404), https://powermin.gov.in/sites/default/files/Waiver_of_Inter_State_Transmission_Charges_on_transmission_of_the_electricity_generated_from_solar_and_Orders.pdf (404), https://powermin.gov.in/sites/default/files/webform/notices/Seeking_comments_on_Draft_Electricity_Amendment_Bill_2025.pdf (404), https://mnre.gov.in/en/document/guidelines-for-tariff-based-competitive-bidding-process-for-procurement-of-power-from-grid-connected-solar-pv-power-projects (404), https://egazette.gov.in/WriteReadData/2024/257610.pdf (503)

Secondary (tier 3-4; used to identify or date instruments):
- https://prsindia.org/files/bills_acts/acts_parliament/2022/The%20Energy%20Conservation%20(Amendment)%20Act,%202022.pdf
- https://prsindia.org/billtrack/the-draft-electricity-amendment-bill-2025
- https://www.iea.org/policies/25639-carbon-credit-trading-scheme-2023
- https://www.iea.org/policies/18753-2022-increase-in-basic-customs-duty-on-solar-pv-cell-and-module-imports
- https://icapcarbonaction.com/en/news/india-notifies-emission-intensity-targets-nine-sectors-under-carbon-credit-trading-scheme
- https://ksandk.com/newsletter/revised-renewable-consumption-obligation-rules-explained/
- https://powerline.net.in/2025/10/03/mop-issues-revised-rco-framework-under-electricity-amendment-rules-2025/
- https://powerline.net.in/2022/10/11/cerc-notifies-effective-date-of-general-network-access-regulations-2022/
- https://indiaenvironmentportal.org.in/reports-and-documents/guidelines-for-tariff-based-competitive-bidding-process-for-procurement-of-power-from-grid-connected-solar-pv-power-projects-2
- https://jmkresearch.com/vgf-scheme-expands-to-support-30-gwh-of-new-standalone-bess-development-in-india/
- https://www.pv-magazine-india.com/2025/06/10/power-ministry-announces-inr-5400-crore-viability-gap-funding-to-support-30-gwh-bess-development
- https://www.lkslaw.com/insights/articles/pn-3-2-0-key-takeaways-from-india-s-updated-fdi-policy-for-land-border-investors
- https://www.lkslaw.com/insights/articles/government-nod-must-for-fdi-from-bordering-countries
- https://www.lkslaw.com/insights/articles/india-s-critical-minerals-strategy-wider-exemption-from-customs-duty-needed-to-fulfil-the-government-s-mission
- https://trilegal.com/knowledge_repository/trilegal-update-budget-2025-key-highlights-for-the-energy-and-the-infrastructure-sectors/
- https://www.seair.co.in/custom-notifications/012018-cus-sg-dt-30-07-2018-339161.aspx
- https://globaltradealert.org/intervention/60135-india-termination-of-definitive-safeguard-duty-on-imports-of-solar-cells
- https://www.constructionworld.in/steel-news/india-imposes-anti-dumping-duty-on-solar-panel-aluminium-frames/66040
- https://worldtradescanner.com/11-Cus(ADD)-08.05.2025.htm
- https://mercomindia.com/india-slaps-anti-dumping-duties-on-solar-glass-imports-from-china-and-vietnam
- https://www.constructionworld.in/amp/policy-updates-and-economic-news/india-imposes-up-to-30--antidumping-duty-on-chinese-solar-cells/79516
- https://www.outlookbusiness.com/news/comm-min-recommends-anti-dumping-duty-on-solar-cells-from-china-for-3-yrs
- https://taiyangnews.info/markets/almm-list-ii-solar-cells-from-june-2026
- https://www.pv-magazine.com/2026/03/19/india-extends-solar-manufacturing-mandate-to-wafers-and-ingots
- https://www.energetica-india.net/news/mnre-has-notified-quality-control-order-2017-compulsory
- https://www.autocarpro.in/news/india-releases-guidelines-for-electric-car-manufacturing-scheme-126756
- https://inc42.com/buzz/govt-extends-pm-e-drive-scheme-till-2028
- https://www.business-standard.com/article/economy-policy/govt-notifies-rs-18-100-cr-pli-scheme-to-promote-acc-battery-making-121062101148_1.html
