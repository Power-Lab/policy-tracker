# Scouting report: Thailand

Prepared 2026-11-04 for the phase 5 expansion. This is desk research from web sources. No row has been checked against the Thai text in the Royal Gazette. The candidate rows are in [th-candidates.csv](th-candidates.csv) (29 rows).

## Summary

- **Structure: an "enhanced single buyer".** The state utility EGAT owns about a third of generating capacity and runs the transmission grid and system operator. It is the single buyer from independent power producers (IPPs, over 90 MW), small power producers (SPPs, 10-90 MW) and imports. EGAT resells to two state distribution utilities: MEA for Bangkok and its metropolitan area, and PEA for the rest of the country. PEA and MEA also buy directly from very small power producers (VSPPs). The Energy Regulatory Commission (ERC), set up under the Energy Industry Act B.E. 2550 (2007), licenses operators, sets tariffs and runs renewable procurement. In August 2025 the NEPC dropped the plan to split the system operator out of EGAT.
- **Policy is set by committee resolution rather than by law.** The National Energy Policy Council (NEPC, กพช., chaired by the Prime Minister) and its executive arm, the Energy Policy Administration Committee (EPAC, กบง.), take the decisions that matter: plans, feed-in tariff rates, the Direct PPA pilot, the Utility Green Tariff and rooftop solar quotas. The ERC then turns them into regulations and notifications. The framework law has not been amended since 2007.
- **Main moves since 2017:**
  - PDP2018 (2019) and PDP2018 Rev.1 (2020), which is still the plan in force. The draft PDP2024 was never adopted. The draft PDP2026 (2026-2050) went to public hearing on 8 Sep 2026.
  - A 2022-2030 feed-in tariff of up to 5,203 MW, and a contested second round of 3,668.5 MW.
  - The Utility Green Tariff, approved by the NEPC in 2022 and launched in January 2025 at THB 4.21/kWh.
  - A Direct PPA pilot over third-party access (TPA): 2,000 MW for data centres approved in June 2024, then opened to all industry with the cap removed in July 2026. The final ERC rules are still not confirmed.
  - Rooftop solar: factory licences no longer needed (Dec 2024), a tax deduction (Royal Decree 805, Mar 2026), and a 500 MW household net-billing round at THB 2.20/kWh (Apr 2026).
  - A Climate Change Bill approved in principle by Cabinet (Dec 2025) but not enacted.
  - A carbon price in fuel excise approved by Cabinet (Jan 2025). Its gazettal is not confirmed.
- **Tracking will be hard, harder than Indonesia or Vietnam.**
  - Most decisive acts are resolutions, which our schema treats as second class.
  - The texts are almost all in Thai only, with Buddhist Era (B.E.) dates.
  - The Royal Gazette, the ERC and the Council of State sites blocked or reset our requests. The Ministry of Energy sites sit behind bot challenges.
  - Final ERC regulations often appear months after the NEPC decision. Implementing documents (ERC notifications, utility announcements) are numerous and rarely numbered.
- **The best single source is the EPPO resolutions database** ([reso.eppo.go.th](https://reso.eppo.go.th/main)). It is server-rendered, paginated and lists every NEPC and EPAC resolution since about 2012 with its date and title, and it returned HTTP 200. It is Thai-only, and its PDFs sit behind JavaScript actions without stable URLs.
- **Recommendation: go ahead with Thailand, but only with a Thai-reading reviewer and a scope rule decided first.** We need to decide how NEPC and EPAC resolutions are recorded and what to do with drafts. Start with about 30 rows built around the NEPC resolution chain plus the ERC regulations that implement it, and verify each against the Gazette with a reviewer in Thailand. Expect a lower share of `document` source links than for Indonesia or Vietnam at first.

## Legal hierarchy and document types

From highest to lowest. Thai names are given in brackets.

| Level | Type | Issued by | Numbering and identity | Our `doc_type` |
| --- | --- | --- | --- | --- |
| 1 | Constitution (รัฐธรรมนูญ) | — | By B.E. year (current: B.E. 2560 / 2017) | (not tracked) |
| 2 | Act (พระราชบัญญัติ, *Phra Ratchabanyat*); Emergency Decree (พระราชกำหนด, *Phra Ratchakamnot*) has the force of an Act | Parliament, then royal assent; Cabinet for emergency decrees | No running number. Identified by title and B.E. year, e.g. "Energy Industry Act B.E. 2550". Amendments are titled "(No. 2)", "(No. 3)" and so on | law |
| 3 | Royal Decree (พระราชกฤษฎีกา, *Phra Ratchakrit-sadika*) | King, on Cabinet advice, under an Act | Title and B.E. year. Tax decrees under the Revenue Code carry running numbers (e.g. No. 805 B.E. 2569) | decree |
| 4 | Ministerial Regulation (กฎกระทรวง, *Kot Krasuang*) | Minister, under an Act | Title and B.E. year, with "(No. x)" for amendments | ministerial regulation |
| 5 | Ministry notification (ประกาศกระทรวง) | Minister or department | Title and B.E. year | ministerial regulation (or decision) |
| 6 | ERC regulation (ระเบียบ กกพ.) and ERC notification (ประกาศ กกพ.) | Energy Regulatory Commission, under the Energy Industry Act | Title and B.E. year, sometimes "(No. 2)". There is no serial number, so the same subject can have several near-identical titles across rounds | decision |
| policy | Cabinet resolution (มติคณะรัฐมนตรี) | Cabinet | Identified by meeting date only | decision |
| policy | NEPC resolution (มติ กพช.) and EPAC resolution (มติ กบง.) | National Energy Policy Council (under the National Energy Policy Council Act B.E. 2535 / 1992) and its Energy Policy Administration Committee | Meeting "x/B.E. year (running meeting count)", e.g. กพช. 2/2569 (176). One meeting decides many agenda items, so an id needs the meeting plus a subject | decision |
| plan | PDP, AEDP, EEP, Gas Plan, Oil Plan, under a National Energy Plan | Drafted by EPPO and EGAT; approved by NEPC; Cabinet acknowledges or approves | Name and base year (PDP2018 Rev.1, PDP2026) | plan |

**Notes on how this works in practice**

- NEPC and Cabinet resolutions are not legislation, but they decide prices, quotas and who may sign which contract. The ERC then gives them legal effect through regulations and notifications. Courts have also intervened: the Central Administrative Court suspended part of the 2022-2030 wind procurement.
- **Royal Gazette citation.** A Gazette citation reads "Vol. (เล่ม) 124, Part (ตอน) 89 ก". The letter ก (Kor) is the legislation section; ข, ค and ง carry other announcements. Acts usually take effect the day after Gazette publication. ERC regulations usually take effect on publication or the day after. So a row usually has three dates: signing, Gazette publication and entry into force.
- **Buddhist Era dates.** Thai documents use the Buddhist Era: Gregorian year = B.E. year − 543. For example, B.E. 2550 = 2007, B.E. 2565 = 2022 and B.E. 2569 = 2026. Since 1941 the Thai year begins on 1 January, so the conversion is a straight subtraction for all modern rules. Months are often abbreviated: ม.ค. Jan, ก.พ. Feb, มี.ค. Mar, เม.ย. Apr, พ.ค. May, มิ.ย. Jun, ก.ค. Jul, ส.ค. Aug, ก.ย. Sep, ต.ค. Oct, พ.ย. Nov, ธ.ค. Dec. Thai digits (๐-๙) appear in Gazette PDFs. The government fiscal year runs from October to September and is also labelled in B.E. (e.g. FY2568).
- Drafts carry a placeholder year, e.g. the draft Climate Change Act is titled "B.E. ...".

## Official sources

All tests were run on 2026-11-04 from a cloud container outside Thailand through a proxy, using curl with a browser user agent and the WebFetch tool. Some blocks may be geographic or web-application-firewall rules that a Thailand-based runner or a real browser would pass.

| Portal | URL | What it holds | Search / listing | Language | Scrapeability (status we got) |
| --- | --- | --- | --- | --- | --- |
| Royal Thai Government Gazette (ราชกิจจานุเบกษา) | https://ratchakitcha.soc.go.th/ | Every Act, Royal Decree, Ministerial Regulation and ERC regulation, as published. The authoritative date source | Search by title, volume, part and date | Thai | **403** (curl and WebFetch, also on `/search-result` and the `www.` host). Needs a browser or a Thai runner |
| Energy Regulatory Commission (ERC / OERC) | https://www.erc.or.th/ (English at /en) | ERC regulations, notifications, public hearings, UGT documents, tariff (Ft) decisions; PDFs under `/web-upload/…` | Section listings; search engines index many PDFs | Thai, partly English | **Connection reset** during the TLS handshake (curl 000); WebFetch got **503**. Direct PDF links found through search may work from elsewhere |
| EPPO resolutions database (NEPC/EPAC) | https://reso.eppo.go.th/main | 2,269 resolution entries (NEPC and EPAC), each with meeting label, B.E. date, government, title, PDF and detail | Filter by committee, government, meeting number, date range and category; keyword search. **`?page=N` works** (25 per page, 91 pages) | Thai | **200**. Server-rendered HTML (Laravel Filament). Pages 1-50 parsed cleanly (back to 2012). PDFs open through a Livewire action (`mountTableAction('pdf', id)`), so there are no stable document URLs |
| Energy Policy and Planning Office (EPPO) | https://www.eppo.go.th/ (English at /en) | PDP, AEDP, EEP and smart grid plans; laws by level (national, committee, agency) | Menus | Thai, limited English | **200** |
| Ministry of Energy | https://www.energy.go.th/ | Ministry news and notifications | — | Thai | 200, but redirected to a WAF challenge page (`pds-cwaf.pttdigital.com`) |
| Ministry of Energy legal database | https://law.energy.go.th/ | Energy laws and regulations as PDFs (search results point here for the Energy Industry Act) | Listing by law | Thai | **303** to a Radware bot-challenge page |
| Office of the Council of State (Krisdika) | https://www.krisdika.go.th/ ; https://www.ocs.go.th/ | Consolidated texts of Acts, some official English translations, bill review status | Search | Thai, some English | **Connection failed** (000) on both hosts |
| Central law system | https://www.law.go.th/ | Draft laws and public hearings (we believe it is run by the Council of State; not confirmed) | Search | Thai | **403** |
| Cabinet resolutions (Secretariat of the Cabinet) | https://resolution.soc.go.th/ ; https://www.soc.go.th/ | Cabinet resolutions by date | Search by date and keyword | Thai | **403** on all three hosts tried |
| EGAT | https://www.egat.co.th/home/en/ | PDP documents, purchase announcements | Menus | Thai and English | 200 |
| PEA / MEA | https://www.pea.co.th/ ; https://www.mea.or.th/ | VSPP, rooftop and community solar announcements, UGT | Menus | Thai | 200 |
| Department of Alternative Energy Development and Efficiency (DEDE) | https://www.dede.go.th/ | AEDP, renewable statistics | — | Thai | Connection failed (000) |
| Dept. of Climate Change and Environment (DCCE) | https://www.dcce.go.th/ | Climate Change Bill drafts and hearings | — | Thai | Connection failed (000). The ministry hub https://hub.mnre.go.th/ is reachable through search |
| Thailand Greenhouse Gas Management Organization (TGO) | https://www.tgo.or.th/ | Offsets (T-VER), carbon market | — | Thai, English | 200 (the English path returned 500) |
| Excise Department | https://www.excise.go.th/ | Fuel excise and carbon price | — | Thai | 200 (not explored) |
| Parliament | https://www.parliament.go.th/ | Bills before the House | — | Thai | 200 (not explored) |

Unofficial English translations of key Acts are on the ADB Law and Policy Reform portal (https://lpr.adb.org/resource/energy-industry-act-be-2550-2007-thailand) and the UN ESCAP Asia Pacific Energy Portal (https://policy.asiapacificenergy.org/).

## Key rules since about 2017, by topic

Dates are Gregorian. "NEPC x/yyyy" gives the B.E. meeting label from the EPPO database. Confidence is **high** when the date and effect appear in an official listing and a credible secondary source, **medium** when one credible source supports it, and **low** when we have only a title or a single weak source. Row ids refer to the candidate CSV.

### framework-law

| Rule | Issuer | Date | Effect | Amends / revokes | Status | Source | Conf. |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Energy Industry Act B.E. 2550 (2007) — `TH-ACT-2007-ENERGY-INDUSTRY` | King / National Legislative Assembly | Given 2007-12-09; Gazette Vol. 124 Part 89 Kor, 2007-12-10; in force 2007-12-11 | Separates policy, regulation and operation. Creates the ERC and the Power Development Fund, sets the licence regime (s.47, exemptions by Royal Decree) and obliges network owners to allow access under published codes (s.81) | — | In force; no enacted amendment found (amendment proposals exist) | [ADB translation](https://lpr.adb.org/resource/energy-industry-act-be-2550-2007-thailand) | high |
| National Energy Policy Council Act B.E. 2535 (1992), amended up to (No. 3) B.E. 2551 | Parliament | 1992; 2008 | Creates the NEPC that approves plans and pricing policy | — | In force | [APEP listing](https://policy.asiapacificenergy.org/node?page=217) | medium (not a CSV row; pre-2017 but needed to explain NEPC) |

### captive-power

| Rule | Issuer | Date | Effect | Status | Source | Conf. |
| --- | --- | --- | --- | --- | --- | --- |
| Royal Decree exempting small energy operations from licensing B.E. 2552 — `TH-DECREE-2009-LICENCE-EXEMPTION` | King | 2009 | Generation under 1,000 kVA exempt from the ERC licence, but must notify the ERC | In force? | [WFW guide 2018](https://www.wfw.com/wp-content/uploads/2019/11/Global-Renewable-Energy-Guide-2018-Thailand.pdf) | low |
| Ministerial Regulation on types, kinds and sizes of factories (No. 3) B.E. 2567 — `TH-MR-2024-FACTORY-3` | Ministry of Industry | In force 2024-12-28 | Rooftop and building-mounted solar is no longer a "factory" at any size (before: licence above 1 MW) | In force | [Tilleke & Gibbins](https://www.tilleke.com/insights/thailand-removes-factory-license-requirement-for-solar-rooftop-installations) | medium |
| NEPC 4/2568 (174): guidelines for users who self-generate or sell private-to-private (IPS) | NEPC | 2025-11-28 | Unknown; title only | ? | [EPPO resolutions](https://reso.eppo.go.th/main) | low (not a CSV row) |

### wheeling-dppa

| Rule | Issuer | Date | Effect | Amends | Status | Source | Conf. |
| --- | --- | --- | --- | --- | --- | --- | --- |
| NEPC 1/2567 (167): measures for Direct PPA — `TH-NEPC-2024-1-DIRECT-PPA` | NEPC | 2024-06-25 | Pilot: data centres may buy renewable power directly over the grid through third-party access, up to 2,000 MW | — | Amended | [Hunton](https://www.hunton.com/insights/legal/thailands-draft-regulation-on-direct-power-purchase-agreements-via-third-party-access-for-data-centers) | high |
| ERC draft Direct PPA Regulation and draft TPA Code | ERC | Published 2025-10-03 | Eligibility (BOI-promoted data centre, at least 50 MW IT load; new renewable plant of at least 1,000 kVA without an existing PPA); grid service agreements; TPA connection, service and operation codes | — | **Draft**; final issue not confirmed | Hunton (above); [Chambers 2026](https://practiceguides.chambers.com/practice-guides/renewable-energy-2026/thailand/trends-and-developments) | high (draft) |
| NEPC 2/2569 (176): criteria for pilot Direct PPA via TPA — `TH-NEPC-2026-2-DIRECT-PPA-TPA` | NEPC | 2026-07-15 | Opens Direct PPA to industry generally and removes the 2,000 MW cap; EPAC to select and supervise; grid-use security deposits for data centres. EPAC approved principles on 3 Aug 2026; the ERC then consulted | Amends the 2024 resolution | In force (policy); ERC rules pending | [Nagashima Ohno & Tsunematsu](https://www.nagashima.com/en/publications/publication20260925-1/), [The Nation](https://www.nationthailand.com/news/general/40069791), [The Nation](https://www.nationthailand.com/news/40070384) | high |
| ERC draft amendment to the licensing regulation B.E. 2551: data-centre electricity distribution licence | ERC | Hearing 2026-09-19 to 2026-10-18 | New licence category for supplying data centres | Would amend the ERC licensing regulation B.E. 2551 (2008) | **Draft** | [Baker McKenzie](https://bakermckenzie.com/en/insight/publications/2026/09/thailand-erc-proposes-data-center-licensing) | high (draft; not a CSV row) |

### rooftop-solar

| Rule | Issuer | Date | Effect | Amends | Status | Source | Conf. |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2019 "Solar for Thai People" household net billing (ERC regulation, title not confirmed) | ERC / NEPC | 2019 | Up to 10 kW, exports bought at THB 1.68/kWh for 10 years, 100 MW quota | — | Replaced or quota exhausted | [pv magazine 2019](https://pv-magazine.com/2019/05/24/thailand-launches-net-metering-scheme-for-residential-pv), [IEEFA 2026](https://ieefa.org/sites/default/files/2026-08/IEEFA%20Report_Reforming%20Thailand's%20rooftop%20solar%20policy%20framework%20to%20reduce%20gas%20dependence_August%202026.pdf) | medium (no CSV row until the ERC title is found) |
| NEPC 3/2563 (152): guidelines for promoting rooftop solar — `TH-NEPC-2020-3-ROOFTOP` | NEPC | 2020-12-25 | Probably raised the buy-back rate to THB 2.20/kWh from 2021 (IEEFA); 90 MW residential quota to 2030 | — | Amended | EPPO resolutions; IEEFA | low |
| Ministerial Regulation on factory types (No. 3) B.E. 2567 | Ministry of Industry | 2024-12-28 | See captive-power | — | In force | Tilleke | medium |
| Royal Decree No. 805 B.E. 2569 — `TH-DECREE-2026-805` | King (Revenue Code) | Gazette 2026-03-02 | Personal income tax deduction up to THB 200,000 for on-grid home solar up to 10 kW, to 2028-12-31 | — | In force | [The Nation](https://www.nationthailand.com/news/policy/40063299) | high |
| NEPC 1/2569 (175): promoting household rooftop solar — `TH-NEPC-2026-1-ROOFTOP` | NEPC | 2026-04-29 | THB 2.20/kWh net billing, 10 years, 500 MW quota, 5 kW per meter, households only | Amends the 2020 resolution | In force (policy); ERC notification reported pending in Aug 2026 | [pv magazine](https://www.pv-magazine.com/2026/09/10/thailand-paves-the-way-for-10-gw-of-rooftop-solar/), IEEFA | high |

### tariffs-ppa

| Rule | Issuer | Date | Effect | Amends / revokes | Status | Source | Conf. |
| --- | --- | --- | --- | --- | --- | --- | --- |
| NEPC 1/2564 (153): tariff structure policy 2021-2025 — `TH-NEPC-2021-1-TARIFF-POLICY` | NEPC | 2021-04-01 | Framework for ERC base tariffs and Ft | — | Replaced | EPPO resolutions | medium |
| NEPC 7/2565 (162): UGT guidelines — `TH-NEPC-2022-7-UGT` | NEPC | 2022-11-07 | Creates green tariffs: UGT1 (pooled, no specified source) and UGT2 (named plants) | — | In force | [ERC deck via BOI](https://www.boi.go.th/upload/content/20240730%20EN%20UGT.pdf) | high |
| ERC approval of UGT1 rate — `TH-ERC-2024-UGT1` | ERC | 2024-02 (approval); launched 2025-01 | THB 4.21/kWh, one-year contracts with EGAT, MEA or PEA; 2 billion kWh offered in Q1 2025 | — | In force; 2026 premium revised | ERC deck; [Reccessary](https://reccessary.com/en/news/thailand-launches-utility-green-tariff-for-business); [Argus](https://www.argusmedia.com/en/news-and-insights/latest-market-news/2773175-thailand-floats-lower-2026-green-utility-tariff-rate) | medium |
| EPAC 5/2569 (81): UGT2 rate — `TH-EPAC-2026-5-UGT2` | EPAC | 2026-05-28 | Sets the UGT2 rate (figure not confirmed; 2024 drafts were about THB 4.55-4.56) | — | In force? | EPPO resolutions; Chambers | medium |
| NEPC 2/2569 (176): tariff structure policy 2026-2030 — `TH-NEPC-2026-2-TARIFF-POLICY` | NEPC | 2026-07-15 | Cost-reflective data-centre tariff (reported THB 5-6/kWh); first 200 kWh for homes at THB 3; Direct PPA buyers may pay into the Power Development Fund | Replaces the 2021-2025 policy | In force | [JETRO](https://www.jetro.go.jp/biznews/2026/08/5a28eb74d17ee4e0.html), [Eco-Business](https://www.eco-business.com/news/thailand-tightens-data-centre-rules-as-ai-boom-strains-power-grid/) | high |
| NEPC 4/2568 (174): amend the Royal Decree so data centres can be EGAT direct customers — `TH-NEPC-2025-4-DATA-CENTRE-EGAT` | NEPC | 2025-11-28 | Title only | — | ? | EPPO resolutions | low |

### re-pricing

| Rule | Issuer | Date | Effect | Amends | Status | Source | Conf. |
| --- | --- | --- | --- | --- | --- | --- | --- |
| NEPC 3/2565 (158): FiT rates 2022-2030 — `TH-NEPC-2022-3-FIT-RATES` | NEPC | 2022-05-06 | THB/kWh: biogas 2.0724, ground solar 2.1679, solar+BESS 2.8331, wind 3.1014 (+0.50 in the southern border provinces) | — | In force | [WFW](https://www.wfw.com/articles/thailands-5-gw-renewable-ppa-fit-scheme-2022-2030/) | high |
| ERC Regulation on RE procurement under FiT 2022-2030, no-fuel-cost group, B.E. 2565 — `TH-ERC-2022-FIT-2022-2030` | ERC | Gazette 2022-09-27 | Up to 5,203 MW (biogas 335, wind 1,500, solar 2,368, solar+BESS 1,000). First round: 175 projects, about 4,852 MW | — | In force | WFW; [Baker McKenzie via GCN](https://www.globalcompliancenews.com/2022/11/09/https-insightplus-bakermckenzie-com-bm-energy-mining-infrastructure_1-here_11022022/); [ERRA](https://erranet.org/wp-content/uploads/2024/04/ERRA_Newsletter_2024_Spring-1.pdf) | high |
| NEPC 2/2566 (165): additional FiT, 3,668.5 MW — `TH-NEPC-2023-2-FIT-ADDITIONAL` | NEPC | 2023-03-09 | Second round under the same rates | — | Amended | EPPO resolutions; [The Nation](https://www.nationthailand.com/news/policy/40044516) | high |
| NEPC 4/2567 (170): deferral of the 3,668.5 MW round | NEPC | 2024-12-25 | Suspends procurement after the shortlist (16 Dec 2024); sets up a fact-finding committee | Amends 2023 | Superseded | WFW; The Nation | medium (folded into notes) |
| NEPC 1/2568 (171): resume the remaining additional procurement — `TH-NEPC-2025-1-FIT-ADDITIONAL` | NEPC | 2025-05-06 | Utilities to negotiate with selected applicants | Amends 2023 | In force | [WFW 2025](https://www.wfw.com/articles/thailands-erc-revises-ppa-timeline-for-renewable-procurement-under-fit-scheme/) | medium |
| ERC Notification (No. 2) B.E. 2568 — `TH-ERC-2025-FIT-NOTIFICATION-2` | ERC | 2025 (before 29 Jul) | Moves the PPA deadline for SCOD-2026 projects to 29 Jul 2025 | Amends a 2024 ERC notification (no row yet) | In force | WFW 2025 | medium |
| NEPC 3/2568 (173): community-based solar — `TH-NEPC-2025-3-COMMUNITY-SOLAR` | NEPC | 2025-10-27 | 1,500 MW, up to 10 MW per site (VSPP), sold to MEA or PEA | — | In force | [Hunton](https://www.hunton.com/insights/legal/thailand-launches-community-solar-power-initiative) | high |
| ERC Regulation on community-based solar procurement B.E. 2569 — `TH-ERC-2026-COMMUNITY-SOLAR` | ERC | Gazette 2026-09-22; in force 2026-09-23 | 25-year non-firm PPA at THB 2.1679/kWh; 10 MW per project; foreign shareholding at most 49% | — | In force | [Mori Hamada (PDF)](https://chandler.morihamada.com/sites/default/files/Thailand%20Issues%20New%20Framework%20for%201.5%20GW%20Community-Based%20Solar%20Power%20Procurement%2023%20September%202026.pdf) (403 to our fetch; details from search summaries) | medium |

### coal-phase-out

| Rule | Issuer | Date | Effect | Amends | Status | Source | Conf. |
| --- | --- | --- | --- | --- | --- | --- | --- |
| NEPC 4/2565 (159): postpone retirement of Mae Moh units 8-11 — `TH-NEPC-2022-4-MAE-MOH` | NEPC | 2022-06-22 | Units kept running to end-2025 because of LNG prices | — | Amended | EPPO resolutions; [The Nation](https://www.nationthailand.com/in-focus/40016964) | medium |
| NEPC 2/2568 (172): Mae Moh management — `TH-NEPC-2025-2-MAE-MOH` | NEPC | 2025-08-21 | Units 8 and 11 to 2031; units 12-13 refurbished to 2048 | Amends 2022 | In force | [Pattaya Mail](https://www.pattayamail.com/thailandnews/nepc-approves-renewable-energy-progress-power-plant-extensions-and-temporary-electricity-tariff-cuts-515641), [Mongabay](https://news.mongabay.com/2025/10/anguish-for-residents-as-thailands-most-polluting-coal-plant-gets-new-lease-of-life/) | high |

Thailand has no coal phase-out rule as such. Coal policy shows up as unit-by-unit life extensions and as the coal share in each PDP.

### power-plans

| Rule | Issuer | Date | Effect | Status | Source | Conf. |
| --- | --- | --- | --- | --- | --- | --- |
| PDP2018 (2018-2037) — `TH-PLAN-2019-PDP2018` | NEPC (Cabinet approval reported May 2019) | 2019-01-24 | 77,211 MW by 2037, about 56 GW new | Replaced | EPPO resolutions; [Powerline](https://powerline.net.in/2019/05/13/thailands-cabinet-approves-pdp-2018-2037/) | high |
| PDP2018 Rev.1 — `TH-PLAN-2020-PDP2018-REV1` | NEPC 1/2563 (150) | 2020-03-19 | Current plan; about 20,766 MW renewables by 2037 (Chambers) | In force | EPPO resolutions; [IEA 2023](https://iea.blob.core.windows.net/assets/dd5b10b2-b655-4c7d-8c09-d3d7efe6bd50/ThailandsCleanElectricityTransition.pdf); Chambers | high |
| AEDP2018 (with EEP2018 and Gas Plan 2018) — `TH-PLAN-2020-AEDP2018` | NEPC 1/2563 (150) | 2020-03-19 | Renewable targets that go with the PDP | In force? | EPPO resolutions | medium |
| Draft PDP2024 (2024-2037) | EPPO / Ministry of Energy | Hearing 2024-06 (sources give 12-19 or 12-23 June) | 51% renewables by 2037 | **Draft, never adopted**; superseded by the PDP2026 drafting decided by NEPC on 2025-05-06 | [Thaiger](https://thethaiger.com/news/national/thailand-eyes-cleaner-energy-with-new-power-plan-for-2024-to-2037), [Bangkok Post](https://www.bangkokpost.com/thailand/general/2922462/ministry-eyes-tweaks-to-2024-power-plan) | medium (not a CSV row) |
| Draft PDP2026 (2026-2050) | EPPO / Ministry of Energy | Hearing 2026-09-08; comments to 2026-09-15 | Four cases with 65-89% clean power by 2050 (EPPO prefers Case 4, about 73%); 300 MW SMR by 2037; 10 GW rooftop | **Draft**; due to NEPC late 2026 | [Nagashima](https://www.nagashima.com/en/publications/publication20260925-1/), [pv magazine](https://www.pv-magazine.com/2026/09/10/thailand-paves-the-way-for-10-gw-of-rooftop-solar/) | high (draft; not a CSV row) |

### grid-market-rules

| Rule | Issuer | Date | Effect | Status | Source | Conf. |
| --- | --- | --- | --- | --- | --- | --- |
| NEPC 2/2568 (172): revoke the resolution to separate the system operator — `TH-NEPC-2025-2-SYSTEM-OPERATOR` | NEPC | 2025-08-21 (Pattaya Mail: 23 Aug) | System operator stays inside EGAT, ring-fenced | In force | EPPO resolutions; Pattaya Mail | high |
| Draft TPA Code (service, connection and operation codes) | ERC | Consultation 2025 | Basis for wheeling charges | **Draft** | Chambers; Hunton | high (draft) |
| ERC Regulation on mergers and cross-shareholdings in the energy industry B.E. 2565 | ERC | In force 2022-12-20 | Merger control in the energy industry | In force | Chambers; [Tilleke](https://www.tilleke.com/insights/new-competition-regulations-for-thailands-energy-sector) | medium (not a CSV row; outside our topics) |

### carbon-pricing

| Rule | Issuer | Date | Effect | Status | Source | Conf. |
| --- | --- | --- | --- | --- | --- | --- |
| Cabinet resolution on a carbon price in fuel excise — `TH-CAB-2025-CARBON-TAX` | Cabinet | 2025-01-21 | THB 200/tCO2e built into existing excise on oil products; no change at the pump | Cabinet decision confirmed; Ministry of Finance ministerial regulation's gazettal and effective date **not confirmed** | [Baker McKenzie](https://insightplus.bakermckenzie.com/bm/tax/thailand-thai-cabinet-approves-carbon-tax-on-oil-and-oil-products), [EY](https://globaltaxnews.ey.com/news/2025-0433-thailand-set-to-implement-carbon-tax-on-oil-and-petroleum-products), [Forvis Mazars](https://www.forvismazars.com/th/en/insights/doing-business-in-thailand/tax/carbon-pricing-in-excise-tax-rates) | medium |
| Draft Climate Change Act — Cabinet approval in principle `TH-CAB-2025-CLIMATE-BILL` | Cabinet; DCCE drafting | 2025-12-02 | Framework for GHG reporting (MRV), carbon tax, a possible ETS and a Climate Fund; 205 sections in 14 chapters | **Not enacted.** Council of State review under way in May 2026. The House was dissolved on 12 Dec 2025, 10 days after Cabinet approval; how far the bill has got since the 2026 election is not confirmed | [MNRE hub](https://hub.mnre.go.th/en/knowledge/detail/66378), [Thailand Business News / PRD](https://www.thailand-business-news.com/national/305914-thailand-pushes-forward-landmark-climate-change-legislation-to-combat-global-warming), [Wikipedia](https://en.wikipedia.org/wiki/Climate_Change_Bill_(Thailand)), Chambers | high (status), medium (contents) |

### energy-strategy

| Rule | Issuer | Date | Effect | Status | Source | Conf. |
| --- | --- | --- | --- | --- | --- | --- |
| NEPC 2/2564 (154): National Energy Plan framework | NEPC | 2021-08-04 | Framework for the umbrella plan that the PDP, AEDP, EEP, Gas and Oil plans sit under | National Energy Plan itself not confirmed as adopted | EPPO resolutions | medium (not a CSV row) |
| Carbon neutrality by 2050, net zero GHG by 2065 (COP26 pledge) | Government | 2021 | Target that plans refer to | Policy | IEA 2023 | high (not a CSV row) |

## Fit with our schema

**Where it fits**

- Acts, Royal Decrees and Ministerial Regulations map cleanly to `law`, `decree` and `ministerial regulation`. ERC regulations and notifications fit `decision`. The PDP and AEDP fit `plan`.
- The `amends` / `revokes` model works for plan chains (PDP2018 → Rev.1 → PDP2026) and resolution chains (Direct PPA 2024 → 2026; rooftop 2020 → 2026; Mae Moh 2022 → 2025).
- All our topics apply. `mineral-downstreaming` and `coal-supply` matter less in Thailand: Thailand uses lignite from EGAT's own Mae Moh mine and imports coal, and has no DMO-style rules that we found.

**Where it does not fit**

1. **Resolutions are the main instrument.** NEPC, EPAC and Cabinet resolutions all collapse into `decision`, which loses the difference between a policy resolution and an ERC regulation with legal force. Suggestion: add `doc_type` values `cabinet resolution` and `committee resolution`, or add an `instrument_force` field (binding / policy).
2. **No natural id or number.** A resolution is "meeting 2/2569 (176), agenda item n". One meeting decides several items, so ids need a subject suffix (we used `TH-NEPC-2026-2-DIRECT-PPA-TPA`). ERC regulations have no serial number at all. `number` will often be just "B.E. 2565", which does not identify the document.
3. **Dates.**
   - Everything is printed in B.E. with Thai month abbreviations, and sometimes Thai digits. The conversion (−543) is trivial, but it must be done during review, and we should store the original B.E. string (perhaps in `title_original`).
   - For Gazette documents, the signing date, Gazette date and entry-into-force date differ. Often only the Gazette date is easy to find; in this scouting `date_signed` sometimes holds the Gazette date, as flagged in `notes`.
   - For resolutions, the only date is the meeting date.
4. **Drafts and pending rules.** Thai policy spends a long time as drafts (Climate Change Act, PDP2024, PDP2026, TPA Code, Direct PPA regulation). Our `status` list has no `draft` or `pending` value. For now we included the resolutions that exist (e.g. Cabinet approval in principle) and left pure drafts out of the CSV. A `draft` status, or a separate watch list, would serve Thailand (and the Philippines) better.
5. **Thai-only texts and no stable URLs.**
   - There are no official English texts for most items.
   - The EPPO resolution PDFs have no permanent links, so `source_url` will often have to point at the portal.
   - The Gazette and the ERC blocked us. `source_type: portal-search` will be common at first.
   - We should archive PDFs (PLAN phase 2, item 3) from the start.
6. **Implicit supersession.** A new FiT round, Ft tariff period or UGT rate often silently replaces the last one without saying so. Court suspensions (Central Administrative Court on wind) change a rule's effect without any document from the issuer.
7. **Cross-sector channels.** Tax measures (Royal Decree 805, carbon excise) and Ministry of Industry factory rules come from outside the energy sector. `origin_sector` handles this; reviewers just need to know which ministries to watch.

## Candidate partner institutes and reviewers

Listed by organisation only; no individuals approached.

- **Thailand Development Research Institute (TDRI)**, a leading independent policy think tank with energy and regulatory work: https://tdri.or.th/en/ (200).
- **Energy Research Institute, Chulalongkorn University** (author of rooftop FiT progress studies): https://www.eri.chula.ac.th/ (connection failed from here; reachable through search). Chulalongkorn's law faculty journal has published on amending the Energy Industry Act (https://so01.tci-thaijo.org/index.php/lawchulajournal/article/view/274184).
- **Joint Graduate School of Energy and Environment (JGSEE), King Mongkut's University of Technology Thonburi**: https://www.jgsee.kmutt.ac.th/ (200).
- **Stockholm Environment Institute (SEI) Asia Centre, Bangkok**: https://www.sei.org/centres/asia/ (403 to bots).
- **Asian Institute of Technology (AIT)**, energy programmes: https://www.ait.ac.th/ (403 to bots).
- **Thai-German Cooperation / GIZ energy programme** (works with the ERC and DCCE, including on the Climate Change Act hearings): https://www.thai-german-cooperation.info/ (200).
- **Law firms for spot checks** (they publish detailed English summaries with B.E. titles): Tilleke & Gibbins (https://www.tilleke.com/), Hunton (https://www.hunton.com/), Watson Farley & Williams (https://www.wfw.com/), Baker McKenzie (https://www.bakermckenzie.com/), Nagashima Ohno & Tsunematsu (https://www.nagashima.com/), Mori Hamada / Chandler (https://chandler.morihamada.com/).
- **International analysts**: IEEFA (https://ieefa.org/), Ember (https://ember-energy.org/countries-and-regions/thailand/), IEA (https://www.iea.org/countries/thailand).

## Risks and open questions

1. **Access.** The Gazette, ERC, Council of State and Cabinet portals blocked or reset us. We need a Thai-based or browser-based fetcher, or a reviewer who downloads the PDFs by hand. This must be solved before the phase 4 weekly scan.
2. **Language.** Every binding text is in Thai. Without a Thai-reading reviewer we would be repeating law-firm summaries, which conflict on dates. Examples: the UGT2 effective date (1 May 2026 per Chambers, against an EPAC resolution of 28 May 2026); the NEPC meeting date of 21 or 23 August 2025; whether the UGT was approved in February or July 2024.
3. **Unconfirmed items:**
   - Whether the carbon price ministerial regulation was gazetted, and when.
   - Whether the final ERC Direct PPA regulation and TPA Code were issued. One unverified post claims Gazette publication on 14 Aug 2026.
   - The title and date of the 2019 household rooftop regulation and of the 2024 ERC regulation for the 3,668.5 MW round.
   - The exact effect of the NEPC 28 Nov 2025 resolutions (IPS; data centres as EGAT direct customers).
   - Whether the 2009 licence-exemption Royal Decree has been amended.
   - The AEDP2018 approval outcome.
4. **Political churn.** There were three governments in 2023-2026 (Srettha, Paetongtarn, Anutin), the House was dissolved in Dec 2025, and an election followed in 2026. Resolutions get revisited (the 3,668.5 MW round was deferred, then resumed; the system operator decision was reversed). Status checks will need to be frequent.
5. **Volume.** Electricity tariff (Ft) decisions every four months, oil fund and LPG resolutions, and many ERC procurement notices could swamp the tracker. We need a scope rule, for example: track tariff structure policies but not each Ft period.
6. **Litigation.** Administrative court cases on the FiT rounds affect status but are not "rules". We need to decide how to record them (notes only?).
7. **Coordination.** Check whether SIPET, NewClimate or the Climate Policy Radar already cover Thai climate laws (Climate Policy Radar lists the PDP2018: https://app.climatepolicyradar.org/document/thailand-power-development-plan-2018-2037_110d) to avoid duplicating them.

## Sources

Official or quasi-official
- https://reso.eppo.go.th/main (NEPC/EPAC resolutions database; pages 1-50 read on 2026-11-04)
- https://www.eppo.go.th/ and https://www.eppo.go.th/en
- https://ratchakitcha.soc.go.th/ (403)
- https://www.erc.or.th/ (connection reset / 503)
- https://law.energy.go.th/ (bot challenge)
- https://www.krisdika.go.th/ , https://www.ocs.go.th/ (connection failed)
- https://resolution.soc.go.th/ , https://www.soc.go.th/ , https://www.law.go.th/ (403)
- https://www.energy.go.th/ , https://www.egat.co.th/home/en/ , https://www.pea.co.th/ , https://www.mea.or.th/ , https://www.dede.go.th/ , https://www.dcce.go.th/ , https://www.tgo.or.th/ , https://www.excise.go.th/ , https://www.parliament.go.th/ , https://www.mnre.go.th/ , https://www.onep.go.th/ , https://www.boi.go.th/
- https://www.boi.go.th/upload/content/20240730%20EN%20UGT.pdf (ERC presentation on UGT, 30 Jul 2024)
- https://hub.mnre.go.th/en/knowledge/detail/66378 (MNRE on Cabinet approval of the Climate Change Bill)
- https://lpr.adb.org/resource/energy-industry-act-be-2550-2007-thailand and https://lpr.adb.org/sites/default/files/resource/398/thailand-energy-industry-act.pdf.pdf (unofficial translation, read in full)
- https://policy.asiapacificenergy.org/node?page=217

Law firms and practice guides
- https://www.hunton.com/insights/legal/thailands-draft-regulation-on-direct-power-purchase-agreements-via-third-party-access-for-data-centers
- https://www.hunton.com/insights/legal/thailand-launches-community-solar-power-initiative
- https://bakermckenzie.com/en/insight/publications/2026/09/thailand-erc-proposes-data-center-licensing
- https://insightplus.bakermckenzie.com/bm/tax/thailand-thai-cabinet-approves-carbon-tax-on-oil-and-oil-products
- https://www.globalcompliancenews.com/2022/11/09/https-insightplus-bakermckenzie-com-bm-energy-mining-infrastructure_1-here_11022022/
- https://practiceguides.chambers.com/practice-guides/renewable-energy-2026/thailand/trends-and-developments
- https://www.nagashima.com/en/publications/publication20260925-1/
- https://www.wfw.com/articles/thailands-5-gw-renewable-ppa-fit-scheme-2022-2030/
- https://www.wfw.com/articles/thailands-erc-revises-ppa-timeline-for-renewable-procurement-under-fit-scheme/
- https://www.wfw.com/articles/unlocking-solar-potential-thailands-regulatory-shift-on-rooftop-solar-systems/
- https://www.wfw.com/wp-content/uploads/2019/11/Global-Renewable-Energy-Guide-2018-Thailand.pdf
- https://www.tilleke.com/insights/thailand-removes-factory-license-requirement-for-solar-rooftop-installations
- https://www.tilleke.com/insights/new-competition-regulations-for-thailands-energy-sector
- https://chandler.morihamada.com/sites/default/files/Thailand%20Issues%20New%20Framework%20for%201.5%20GW%20Community-Based%20Solar%20Power%20Procurement%2023%20September%202026.pdf (403 to our fetch)
- https://www.dentons.com/en/insights/alerts/2026/august/14/thailands-direct-ppa-pilot-for-data-centres-what-has-changed-since-early-2026 (403 to our fetch)
- https://globaltaxnews.ey.com/news/2025-0433-thailand-set-to-implement-carbon-tax-on-oil-and-petroleum-products
- https://www.forvismazars.com/th/en/insights/doing-business-in-thailand/tax/carbon-pricing-in-excise-tax-rates
- https://erranet.org/wp-content/uploads/2024/04/ERRA_Newsletter_2024_Spring-1.pdf

Think tanks and agencies
- https://iea.blob.core.windows.net/assets/dd5b10b2-b655-4c7d-8c09-d3d7efe6bd50/ThailandsCleanElectricityTransition.pdf (IEA, 2023)
- https://ieefa.org/sites/default/files/2026-08/IEEFA%20Report_Reforming%20Thailand's%20rooftop%20solar%20policy%20framework%20to%20reduce%20gas%20dependence_August%202026.pdf
- https://www.jetro.go.jp/biznews/2026/08/5a28eb74d17ee4e0.html
- https://www.iea.org/policies/25997
- https://app.climatepolicyradar.org/document/thailand-power-development-plan-2018-2037_110d

News
- https://www.nationthailand.com/news/general/40069791
- https://www.nationthailand.com/news/40070384
- https://www.nationthailand.com/news/policy/40063299
- https://www.nationthailand.com/news/policy/40044516
- https://www.nationthailand.com/in-focus/40016964
- https://www.pv-magazine.com/2026/09/10/thailand-paves-the-way-for-10-gw-of-rooftop-solar/
- https://pv-magazine.com/2019/05/24/thailand-launches-net-metering-scheme-for-residential-pv
- https://www.eco-business.com/news/thailand-tightens-data-centre-rules-as-ai-boom-strains-power-grid/
- https://reccessary.com/en/news/thailand-launches-utility-green-tariff-for-business
- https://www.argusmedia.com/en/news-and-insights/latest-market-news/2773175-thailand-floats-lower-2026-green-utility-tariff-rate
- https://www.pattayamail.com/thailandnews/nepc-approves-renewable-energy-progress-power-plant-extensions-and-temporary-electricity-tariff-cuts-515641
- https://news.mongabay.com/2025/10/anguish-for-residents-as-thailands-most-polluting-coal-plant-gets-new-lease-of-life/
- https://powerline.net.in/2019/05/13/thailands-cabinet-approves-pdp-2018-2037/
- https://thethaiger.com/news/national/thailand-eyes-cleaner-energy-with-new-power-plan-for-2024-to-2037
- https://www.bangkokpost.com/thailand/general/2922462/ministry-eyes-tweaks-to-2024-power-plan
- https://www.thailand-business-news.com/national/305914-thailand-pushes-forward-landmark-climate-change-legislation-to-combat-global-warming
- https://en.wikipedia.org/wiki/Climate_Change_Bill_(Thailand)
- https://www.thestar.com.my/aseanplus/aseanplus-news/2025/12/12/royal-gazette-has-published-a-royal-decree-dissolving-thailand039s-house-of-representatives
