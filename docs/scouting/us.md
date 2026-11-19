# Scouting report: United States

Prepared 2026-11-19 for the Power Transformation Lab policy tracker. It comes with [`us-rules.csv`](us-rules.csv) (39 candidate rules, 32-column schema), [`us-country.csv`](us-country.csv) and [`us-sources.csv`](us-sources.csv). The United States is recorded as a comparison economy. The emphasis is on federal supply-chain and trade measures for solar, wind, batteries, EVs and critical minerals since 2015. Everything here is a lead for reviewers, not checked data.

How this was checked: Federal Register citations, publication, signing and effective dates and abstracts were taken from the **Federal Register JSON API** (`/api/v1/documents.json`), which returned 200. The FederalRegister.gov HTML pages redirected (302) to a bot check. Full texts of Public Laws, proclamations, executive orders and the section 301 notice were downloaded from **govinfo.gov** (200) and the operative clauses read. IRS Notices 2023-38, 2025-42 and 2026-15 were read from irs.gov PDFs. Web searches filled the remaining gaps: the Supreme Court IEEPA ruling, the California items and some release dates. Where a fact rests on general knowledge or secondary sources, the row's `notes` say so.

---

## 1. Summary

- **Structure.** Electricity regulation is split. **FERC** regulates interstate transmission and wholesale markets under the Federal Power Act (interconnection, transmission planning, storage participation). **States** regulate retail service, resource planning, renewable portfolio standards and net metering through their legislatures and public utility commissions. There is no federal RPS or national power plan. **EPA** sets power plant and vehicle greenhouse gas standards under the Clean Air Act.
- **Industrial policy runs through the tax code.**
  - The **Inflation Reduction Act** (P.L. 117-169, 2022-08-16) created 45X (manufacturing), 45Y/48E (clean electricity) and a revised 30D (clean vehicles), with sourcing and foreign-entity rules. Treasury implemented them by final rules (30D 2024-05-06; 45X 2024-10-28; 45Y/48E 2025-01-15) and IRS notices (domestic content, Notice 2023-38).
  - The **One Big Beautiful Bill Act** (P.L. 119-21, 2025-07-04) made these changes:
    - ended 30D for vehicles acquired after 2025-09-30;
    - ended 45Y/48E for wind and solar placed in service after 2027 unless construction begins within 12 months of enactment;
    - ended 45X for wind components after 2027 and phases it out for critical minerals in 2031-2033;
    - added "prohibited foreign entity" and "material assistance" restrictions.
  - **EO 14315** (2025-07-07) and IRS **Notice 2025-42** tightened beginning-of-construction rules. **Notice 2026-15** gave interim material-assistance guidance.
- **Minerals.** The **IIJA** (P.L. 117-58) funds battery materials processing and battery manufacturing grants ($3 billion each, section 40207) and mineral programmes. DOE interpreted "foreign entity of concern" in a 2024 rule. Defense Production Act determinations cover large-capacity battery minerals (PD 2022-11) and recoverable critical minerals such as black mass and magnet scrap (PD 2026-19). **EO 14241** (2025) speeds up mineral permitting and DPA use. The section 232 critical minerals action (**Proclamation 11001**, 2026-01-14) chose negotiations over tariffs.
- **Trade: dense and fast-changing.**
  - **Solar safeguard:**
    - Proclamation 9693 (2018) set the safeguard.
    - Proclamation 10339 (2022) extended it.
    - Proclamation 10790 raised the cell quota to 12.5 GW in 2024.
    - The measure reached its eight-year limit in February 2026.
  - **Solar AD/CVD:**
    - Orders on China (2012, 2015) and Taiwan (2015).
    - A 2023 circumvention finding covering Cambodia, Malaysia, Thailand and Vietnam. A 24-month emergency duty pause applied first (Proclamation 10414, 2022-06-06 to 2024-06-06).
    - New orders on those four countries (2025-06-24) and on India, Indonesia and Laos (2026-11-09).
  - **Section 301 China tariffs:** the 2024 four-year review set EVs at 100% and solar cells at 50% from 2024. EV lithium-ion batteries and other critical minerals went to 25% from 2024. Non-EV lithium-ion batteries, natural graphite and permanent magnets go to 25% from 2026. Polysilicon and wafers rose from 2025.
  - **Polysilicon (section 232):** **Proclamation 11052** (2026-08-06) sets minimum import prices for polysilicon, wafers, cells and modules plus a 15% duty, from **2026-12-04**. It is recorded as `pending`.
  - **IEEPA and successor tariffs:**
    - **EO 14257** (2025) reciprocal tariffs excluded certain critical minerals and energy products.
    - The Supreme Court struck down the IEEPA tariffs on 2026-02-20, and EO 14389 terminated them.
    - A 150-day section 122 surcharge (Proclamation 11012) followed.
    - USTR section 301 tariffs on 60 economies took effect on 2026-07-24 (not recorded; see risks).
  - **UFLPA:** the Uyghur Forced Labor Prevention Act (P.L. 117-78) bars Xinjiang-linked goods, which matters for polysilicon.
- **Climate and EV rules reversed in 2025-2026.**
  - EPA repealed most of the 2024 power plant Carbon Pollution Standards (final 2026-09-17, effective 2026-11-16).
  - EPA rescinded the 2009 endangerment finding and all vehicle GHG standards (effective 2026-04-20).
  - Congress disapproved California's Advanced Clean Cars II waiver (P.L. 119-16).
  - EO 14154 paused IRA/IIJA disbursements, including EV charging funds.
- **Tracking difficulty: moderate.** Everything is in English, citations are regular (P.L., FR, Proclamation and EO numbers), and the Federal Register API is open and structured. The difficulty is volume and churn: many instruments are amended within months, and trade measures are layered (safeguard plus AD/CVD plus 301 plus 232 plus IEEPA/122). Several agency sites (FERC, USITC, CBP, trade.gov, Treasury policy pages, congress.gov home) returned 403 to scripted requests.
- **Recommendation:** useful as a comparison economy for the supply-chain and trade modules. Keep scope federal, add states selectively (California recorded twice), and consider an adapter on the Federal Register API, which can be queried by agency, type and term.

## 2. Legal hierarchy and document types

| Rank | Type | Issuer | How it is numbered and cited | Our `doc_type` |
| --- | --- | --- | --- | --- |
| 1 | Constitution | | Article, section | (not tracked) |
| 2 | **Act of Congress** (Public Law) | Congress, signed by the President | "Public Law 117-169" (Congress-number); Statutes at Large "136 Stat. 1818"; section numbers; codified in the U.S. Code (tax credits in Title 26 as "section 45X") | `law` |
| 2a | Joint resolution under the Congressional Review Act | Congress | Public Law number and H.J. Res. number | `law` |
| 3 | **Proclamations, executive orders, presidential determinations** | President, under statutory delegations (Trade Act ss.201, 122; Trade Expansion Act s.232; Tariff Act s.318; IEEPA; DPA) | "Proclamation 9693", "Executive Order 14257", "Presidential Determination No. 2022-11"; published in the Federal Register (Title 3) | `presidential regulation` |
| 4 | **Agency final rules** | Treasury/IRS, DOE, EPA, Commerce/BIS | Federal Register citation "89 FR 37706" and FR Doc. number; codified in the CFR; "effective" date usually 30-60 days after publication | `ministerial regulation` |
| 4a | **FERC orders (rules)** | FERC (independent commission) | "Order No. 2023", with rehearing orders "2023-A"; FR citation | `regulator determination` |
| 4b | **AD/CVD orders** | Commerce (ITA), after ITC injury findings | FR notice; case numbers A-/C-xxx-xxx; "applicable" date | `regulator determination` |
| 5 | **USTR determinations** | USTR | FR notice ("Notice of Action", "Notice of Modification") | `decision` |
| 6 | **IRS notices and revenue procedures** | IRS/Treasury | "Notice 2025-42" in the Internal Revenue Bulletin | `circular` |
| (state) | State statutes; PUC decisions; agency regulations | State legislature; PUC; state agencies | "SB 100 (Chapter 312, Statutes of 2018)"; "D.22-12-056" | `law`; `regulator determination`; `ministerial regulation` |

Dating notes: Public Laws take effect on approval unless stated, but individual sections often apply to later periods (e.g. OBBBA credit changes). Federal Register rules carry a publication date and a separate effective date. Proclamations usually apply to goods "entered for consumption" from a stated time. AD/CVD orders are "applicable" from publication. We used the signing or publication date for `date_signed` and the stated effective or applicable date for `date_in_force`.

## 3. Official sources

Requested 2026-11-19 with `curl` (desktop user agent, through the session proxy).

| Name | URL | Tier | Languages | What it holds | Access result |
| --- | --- | --- | --- | --- | --- |
| GovInfo (GPO) | https://www.govinfo.gov/ | 1 | en | Public Laws, Federal Register issues, presidential documents (HTML/PDF) | **200** (HTML files under /content/pkg/ fetched without problems) |
| Federal Register | https://www.federalregister.gov/ | 1 | en | All rules, notices, presidential documents since 1994 | Home **302** (bot check); full-text links 302; **API 200** |
| Congress.gov | https://www.congress.gov/ | 1 | en | Bills, Public Laws | Home **403**; direct /119/plaws/ file **200** |
| White House presidential actions | https://www.whitehouse.gov/presidential-actions/ | 2 | en | EOs, proclamations, fact sheets | **200** |
| USTR section 301 tariff actions | https://ustr.gov/issue-areas/enforcement/section-301-investigations/tariff-actions | 2 | en | 301 notices, exclusions | **200** |
| ITA ACCESS | https://access.trade.gov/ | 2 | en | AD/CVD case records | **200** (trade.gov AD/CVD page **403**; enforcement.trade.gov **301**) |
| USITC | https://www.usitc.gov/ | 2 | en | Safeguard and injury determinations | **403** (hts.usitc.gov **200**) |
| IRS | https://www.irs.gov/ | 2 | en | Notices, IRB, credit pages | **200** |
| Treasury | https://home.treasury.gov/ | 2 | en | Press releases, IRA pages | Home **200**; IRA page **403** |
| FERC | https://www.ferc.gov/ | 2 | en | Orders, dockets | **403** |
| EPA | https://www.epa.gov/ | 2 | en | Rule pages | **200** |
| DOE | https://www.energy.gov/ | 2 | en | Funding programmes, FEOC guidance | Home **200**; programme URL tried **404** |
| CBP | https://www.cbp.gov/ | 2 | en | UFLPA, tariff guidance | **403** |
| CPUC | https://www.cpuc.ca.gov/ | 2 | en | Decisions, NBT page | **200** |
| California Legislative Information | https://leginfo.legislature.ca.gov/ | 1 | en | State statutes | **403** |
| CARB | https://ww2.arb.ca.gov/ | 2 | en | ACC II regulation | **419** |

## 4. Key instruments by category

### Electricity
- **FERC Order No. 2023** (88 FR 61014; effective 2023-11-06): cluster-based generator interconnection reform; Order 2023-A followed.
- **FERC Order No. 1920** (89 FR 49280; effective 2024-08-12): long-term regional transmission planning and cost allocation; 1920-A and 1920-B followed.
- **EPA Carbon Pollution Standards 2024** (89 FR 39798) and their **partial repeal** (91 FR 58954, effective 2026-11-16); a further proposal to rescind all power plant GHG requirements is open (91 FR 59002).
- **California:** SB 100 (2018) RPS 60% by 2030 and 100% clean by 2045; CPUC **D.22-12-056** net billing tariff replacing NEM 2.0 for applications from 2023-04-15.
- Not recorded: FERC Order 841 (storage in RTO markets, 83 FR 9580, 2018) and Order 2222 (DER aggregation); IRA 45Y/48E storage provisions are covered via the Treasury rule.

### Energy
- **EO 14154** (2025-01-20): energy policy and pause of IRA/IIJA disbursements.
- **EPA rescission of the endangerment finding and vehicle GHG standards** (91 FR 7686; effective 2026-04-20), which removes the 2024 light/medium-duty and heavy-duty Phase 3 GHG standards.
- **P.L. 119-16** (2025-06-12): CRA disapproval of California's ACC II waiver.
- IRA **30D** final rule (2024) and its termination by OBBBA (vehicles acquired after 2025-09-30).
- No federal carbon price exists; EPA GHG standards were mapped to `carbon-pricing` for lack of a better topic (see section 5).

### Supply chain
- **IRA** (P.L. 117-169) and **OBBBA** (P.L. 119-21) credits: 45X, 45Y/48E, 30D, domestic content bonus (Notice 2023-38), prohibited foreign entity rules (Notice 2026-15), beginning of construction (Notice 2025-42), EO 14315.
- **IIJA** (P.L. 117-58) battery and minerals programmes; **DOE FEOC interpretation** (89 FR 37079).
- **DPA:** PD 2022-11 (battery minerals, section 303); PD 2026-19 (recoverable critical minerals, section 101); **EO 14241** mineral production.
- **Section 232 critical minerals:** Proclamation 11001 (negotiations).

### Trade
- **Safeguard:** Proclamations 9693, 10339 (rows); 10101, 10779 and 10790 (in notes).
- **AD/CVD:** China 2012, China/Taiwan 2015, the 2023 circumvention finding, Southeast Asia 2025, India/Indonesia/Laos 2026. The **active anode material (graphite)** case ended without orders: Commerce found dumping and subsidies (final 2026-02-17), but the ITC made a negative determination (91 FR 16968, 2026-04-03). It is not recorded as a row.
- **Section 301 China:** 2018 action and the 2024 four-year review (EVs, batteries, solar cells, critical minerals, graphite, magnets); polysilicon and wafers increase (89 FR 101682) in notes.
- **Section 232 polysilicon:** Proclamation 11052 (pending, from 2026-12-04); BIS anti-stockpiling rule (91 FR 60505) in notes.
- **Emergency and general tariffs:** Proclamation 10414 (solar duty pause), EO 14257 (revoked), EO 14389, Proclamation 11012 (section 122).
- **Import prohibition:** UFLPA (P.L. 117-78).
- **Export restrictions:** no US export control specific to clean-tech goods or minerals was found. PD 2026-19 could lead to Commerce measures on scrap and black mass; check.

## 5. Fit with the schema

- **Many layers on the same goods.** A solar module from Southeast Asia may face the safeguard, AD/CVD, section 301 (if Chinese origin), section 232 (polysilicon content), UFLPA and a general tariff all at once. We recorded each instrument once and named related notices in `notes` rather than adding a row for each modifying proclamation or administrative review.
- **AD/CVD orders.** AD/CVD orders on the same product and countries published on the same day were combined into one row, with both FR citations in `number`. Reviewers may prefer one row per order.
- **IRS notices** were mapped to `circular`; Treasury final rules to `ministerial regulation`; FERC orders and AD/CVD orders to `regulator determination`; USTR notices to `decision`.
- **Topic gaps.** There is no topic for vehicle or power-plant emission standards (mapped to `ev-adoption`, `coal-phase-out`, `carbon-pricing`) or for forced-labour import bans (UFLPA mapped to `import-standards`). Foreign-entity restrictions inside tax credits were mapped to `investment-rules` and `local-content`.
- **Status choices.**
  - The **30D rule** is `expired` because the statute ended the credit; the CFR text remains.
  - **Proclamation 11012** is `expired` on the assumption that its 150-day limit ran out.
  - The **safeguard** rows are `expired` on the eight-year statutory limit.
  - **Proclamation 11052** is `pending`.
  - Rows marked `amended` without an amending row in the file: IRA guidance Notice 2023-38, EO 14241, FERC Orders 2023 and 1920, SB 100, Section 301 2018 (amended by the 2024 row). The build will warn for those without a recorded amender.
- **State rows** use jurisdiction `US-CA`; ids start with `US-` (`US-CA-2018-SB100`, `US-CPUC-2022-D2212056`).

## 6. Partner institutes and possible reviewers

Not identified in this pass. Candidates to approach: university energy-law centres with tax-credit and trade expertise, and trade-remedy practitioners (for AD/CVD scope and rates).

## 7. Risks and open questions

1. **Churn.** Several rows changed in 2026: the Supreme Court IEEPA ruling, section 122 and 301 replacement tariffs, Proclamation 11052, the EPA repeals. Re-check status before merging.
2. **Section 122 expiry and the 60-economy section 301 tariffs.** We did not confirm whether the 150-day surcharge ended or was extended. The USTR forced-labour section 301 tariffs on 60 economies (91 FR 47318, applicable 2026-07-24) apply to all products with annex exemptions; they are not recorded because their clean-tech-specific content was not checked.
3. **Safeguard end date** (2026-02-06) is inferred from the statute, not from a termination notice.
4. **Rates not recorded.** Company-specific AD/CVD rates, safeguard rates by year and the polysilicon/wafer section 301 rate (50%, secondary knowledge) need checking.
5. **Agency pages blocked** (FERC, USITC, CBP, trade.gov, congress.gov home); FERC issuance dates and some IRS release dates rest on general knowledge.
6. **Litigation** on EPA repeals, the CRA waiver resolutions, FERC Order 1920 and IEEPA refunds is not tracked.
7. **Coverage gaps:**
   - 48C advanced energy project credit allocations;
   - DOE Loan Programs Office;
   - NEVI charging programme guidance and its 2025 suspension;
   - BIS export controls;
   - USMCA automotive rules of origin (P.L. 116-113), which were not checked for EV battery provisions;
   - Section 232 actions on copper (Proclamation 10962) and other inputs;
   - state rules beyond California.

## 8. Sources

Federal Register API and documents:
- https://www.federalregister.gov/api/v1/documents.json
- https://www.federalregister.gov/documents/2018/01/25/2018-01592/to-facilitate-positive-adjustment-to-competition-from-imports-of-certain-crystalline-silicon
- https://www.federalregister.gov/documents/2020/10/16/2020-23108/to-further-facilitate-positive-adjustment-to-competition-from-imports-of-certain-crystalline-silicon
- https://www.federalregister.gov/documents/2022/02/09/2022-02906/to-continue-facilitating-positive-adjustment-to-competition-from-imports-of-certain-crystalline
- https://www.federalregister.gov/documents/2024/06/26/2024-14143/to-further-facilitate-positive-adjustment-to-competition-from-imports-of-certain-crystalline-silicon
- https://www.federalregister.gov/documents/2024/08/15/2024-18444/to-further-facilitate-positive-adjustment-to-competition-from-imports-of-certain-crystalline-silicon
- https://www.federalregister.gov/documents/2022/06/09/2022-12578/declaration-of-emergency-and-authorization-for-temporary-extensions-of-time-and-duty-free
- https://www.federalregister.gov/documents/2018/06/20/2018-13248/notice-of-action-and-request-for-public-comment-concerning-proposed-determination-of-action-pursuant
- https://www.federalregister.gov/documents/2024/09/18/2024-21217/notice-of-modification-chinas-acts-policies-and-practices-related-to-technology-transfer
- https://www.federalregister.gov/documents/2024/12/16/2024-29462/notice-of-modification-chinas-acts-policies-and-practices-related-to-technology-transfer
- https://www.federalregister.gov/documents/2012/12/07/2012-29668/crystalline-silicon-photovoltaic-cells-whether-or-not-assembled-into-modules-from-the-peoples
- https://www.federalregister.gov/documents/2012/12/07/2012-29669/crystalline-silicon-photovoltaic-cells-whether-or-not-assembled-into-modules-from-the-peoples
- https://www.federalregister.gov/documents/2015/02/18/2015-03183/certain-crystalline-silicon-photovoltaic-products-from-the-peoples-republic-of-china-antidumping
- https://www.federalregister.gov/documents/2015/02/18/2015-03179/certain-crystalline-silicon-photovoltaic-products-from-taiwan-antidumping-duty-order
- https://www.federalregister.gov/documents/2023/08/23/2023-18161/antidumping-and-countervailing-duty-orders-on-crystalline-silicon-photovoltaic-cells-whether-or-not
- https://www.federalregister.gov/documents/2025/06/24/2025-11588/crystalline-silicon-photovoltaic-cells-whether-or-not-assembled-into-modules-from-the-socialist
- https://www.federalregister.gov/documents/2025/06/24/2025-11589/crystalline-silicon-photovoltaic-cells-whether-or-not-assembled-into-modules-from-malaysia-and
- https://www.federalregister.gov/documents/2026/11/09/2026-22824/crystalline-silicon-photovoltaic-cells-whether-or-not-assembled-into-modules-from-india-indonesia
- https://www.federalregister.gov/documents/2026/11/09/2026-22825/crystalline-silicon-photovoltaic-cells-whether-or-not-assembled-into-modules-from-the-lao-peoples
- https://www.federalregister.gov/documents/2026/02/17/2026-02998/active-anode-material-from-the-peoples-republic-of-china-final-affirmative-determination-of-sales-at
- https://www.federalregister.gov/documents/2026/04/03/2026-06488/active-anode-material-from-china-determinations
- https://www.federalregister.gov/documents/2026/01/20/2026-01045/adjusting-imports-of-processed-critical-minerals-and-their-derivative-products-into-the-united
- https://www.federalregister.gov/documents/2026/08/11/2026-16400/adjusting-imports-of-polysilicon-and-its-derivatives-into-the-united-states
- https://www.federalregister.gov/documents/2026/09/24/2026-19537/measures-to-restrict-stockpiling-of-polysilicon-and-polysilicon-derivatives-under-proclamation-11052
- https://www.federalregister.gov/documents/2025/04/07/2025-06063/regulating-imports-with-a-reciprocal-tariff-to-rectify-trade-practices-that-contribute-to-large-and
- https://www.federalregister.gov/documents/2026/02/25/2026-03832/ending-certain-tariff-actions
- https://www.federalregister.gov/documents/2026/02/25/2026-03824/imposing-a-temporary-import-surcharge-to-address-fundamental-international-payments-problems
- https://www.federalregister.gov/documents/2026/07/28/2026-15181/notice-of-actions-in-section-301-investigations-of-acts-policies-and-practices-of-various-economies
- https://www.federalregister.gov/documents/2025/01/29/2025-01956/unleashing-american-energy
- https://www.federalregister.gov/documents/2025/03/25/2025-05212/immediate-measures-to-increase-american-mineral-production
- https://www.federalregister.gov/documents/2025/07/10/2025-12961/ending-market-distorting-subsidies-for-unreliable-foreign-controlled-energy-sources
- https://www.federalregister.gov/documents/2022/04/06/2022-07421/presidential-determination-pursuant-to-section-303-of-the-defense-production-act-of-1950-as-amended
- https://www.federalregister.gov/documents/2026/08/04/2026-15859/presidential-determination-pursuant-to-section-101-of-the-defense-production-act-of-1950-as-amended
- https://www.federalregister.gov/documents/2024/05/06/2024-09094/clean-vehicle-credits-under-sections-25e-and-30d-transfer-of-credits-critical-minerals-and-battery
- https://www.federalregister.gov/documents/2024/05/06/2024-08913/interpretation-of-foreign-entity-of-concern
- https://www.federalregister.gov/documents/2024/10/28/2024-24840/advanced-manufacturing-production-credit
- https://www.federalregister.gov/documents/2025/01/15/2025-00196/section-45y-clean-electricity-production-credit-and-section-48e-clean-electricity-investment-credit
- https://www.federalregister.gov/documents/2023/09/06/2023-16628/improvements-to-generator-interconnection-procedures-and-agreements
- https://www.federalregister.gov/documents/2024/06/11/2024-10872/building-for-the-future-through-electric-regional-transmission-planning-and-cost-allocation
- https://www.federalregister.gov/documents/2024/05/09/2024-09233/new-source-performance-standards-for-greenhouse-gas-emissions-from-new-modified-and-reconstructed
- https://www.federalregister.gov/documents/2026/09/17/2026-19071/partial-repeal-of-the-carbon-pollution-standards-for-fossil-fuel-fired-electric-generating-units
- https://www.federalregister.gov/documents/2025/06/17/2025-10991/repeal-of-greenhouse-gas-emissions-standards-for-fossil-fuel-fired-electric-generating-units
- https://www.federalregister.gov/documents/2026/02/18/2026-03157/rescission-of-the-greenhouse-gas-endangerment-finding-and-motor-vehicle-greenhouse-gas-emission
- https://www.federalregister.gov/documents/2024/04/18/2024-06214/multi-pollutant-emissions-standards-for-model-years-2027-and-later-light-duty-and-medium-duty

GovInfo (full texts):
- https://www.govinfo.gov/content/pkg/PLAW-117publ58/html/PLAW-117publ58.htm
- https://www.govinfo.gov/content/pkg/PLAW-117publ78/html/PLAW-117publ78.htm
- https://www.govinfo.gov/content/pkg/PLAW-117publ169/html/PLAW-117publ169.htm
- https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm
- https://www.govinfo.gov/content/pkg/PLAW-119publ16/html/PLAW-119publ16.htm
- https://www.govinfo.gov/content/pkg/FR-2026-08-11/html/2026-16400.htm (and the corresponding FR-*/html files for the proclamations, orders and notices listed above)

IRS:
- https://www.irs.gov/pub/irs-drop/n-23-38.pdf
- https://www.irs.gov/pub/irs-drop/n-25-42.pdf
- https://www.irs.gov/pub/irs-drop/n-26-15.pdf

California:
- https://www.cpuc.ca.gov/nbt
- https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=201720180SB100

Secondary (dating and context only):
- https://www.law.cornell.edu/wex/Learning_Resources_v_Trump_2026
- https://www.paulweiss.com/insights/client-memos/supreme-court-holds-that-ieepa-does-not-authorize-tariffs
- https://taxnews.ey.com/news/2025-1709-irs-generally-eliminates-5-percent-safe-harbor-for-determining-beginning-of-construction-for-wind-and-solar-projects
- https://kpmg.com/us/en/taxnewsflash/news/2026/02/notice-2026-15-guidance-energy-tax-credits-material-assistance-prohibited-foreign-entities.html
- https://www.whitehouse.gov/briefings-statements/2025/06/statement-by-the-president
