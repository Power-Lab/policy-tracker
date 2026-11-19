# Scouting report: Malaysia

Prepared 2026-11-04 for the phase 5 expansion. This is desk research from web sources, but unlike the Thailand and Philippines scouting, most of it rests on official PDFs we downloaded and read: Energy Commission guidelines, Acts from the Attorney General's Chambers, SEDA orders and Sabah enactments. No row has been through a reviewer. The candidate rows are in [my-candidates.csv](my-candidates.csv) (30 rows).

## Summary

- **Structure: a regulated single-buyer model, with three separate systems.**
  - **Peninsular Malaysia (and the Federal Territory of Labuan for regulation).** Tenaga Nasional Berhad (TNB) is the vertically integrated utility. It owns the grid and distribution, and it owns much of the generation. Two ring-fenced units inside TNB do the market work. The **Single Buyer** buys from TNB's own plants and from independent power producers (IPPs) and settles the market. The **Grid System Operator (GSO)** dispatches. Both units were given a legal basis by the Electricity Supply (Amendment) Act 2015 (Act A1501).
  - **Federal bodies.** The **Energy Commission** (Suruhanjaya Tenaga, ST) is the regulator: it handles licences, tariff setting under incentive-based regulation (IBR), codes and guidelines. The **Sustainable Energy Development Authority (SEDA)** runs the feed-in tariff under the Renewable Energy Act 2011 and is the implementing agency for rooftop solar. Policy sits with the **Ministry of Energy Transition and Water Transformation (PETRA)**: formed in December 2023, renamed in February 2024. **MyPOWER Corporation**, an agency under PETRA, coordinates electricity supply industry reform and the nuclear programme.
  - **Sabah.** Since 3 January 2024 the state's own **Energy Commission of Sabah (ECoS)** regulates electricity and renewable energy under the state Electricity Supply Enactment 2024 and the Sabah Renewable Energy Enactment 2024. Sabah Electricity Sdn Bhd (SESB) is still the utility.
  - **Sarawak.** Sarawak has never been under the federal Electricity Supply Act: its operation there was suspended from 1 September 1990. The state Electricity Ordinance (Cap. 50) governs instead, and Sarawak Energy Berhad (SEB) is the utility and, since a 2023 amendment, the statutory Single Buyer.
- **Most rules that matter are Energy Commission guidelines, not regulations.** Under section 50C of the Electricity Supply Act 1990 the Commission issues registered guidelines (numbered `GP/ST/No.x/yyyy`), and failing to comply with them is an offence. Every recent programme is a guideline of this kind: third-party access (CRESS), community solar (CREAM), rooftop solar (NEM Rakyat, NOVA, SELCO, Solar ATAP), the green tariff (GET), the NEDA market and the IBR tariff method. The Minister makes subsidiary legislation (P.U.(A)) far less often. Programme launches, quotas and charges are announced in PETRA press releases, which then flow into guideline revisions.
- **Main moves since 2017:**
  - **Legislation.** The NEDA merchant dispatch arrangement (2017). Electricity Supply Act amendments in 2024 (Act A1739: energy efficiency moved to a new Act) and 2025 (Act A1775: import and export licences, green attributes, a Market Operator). Commencement of the 2025 Act is not confirmed.
  - **Corporate and community supply.** The Corporate Green Power Programme, a virtual PPA scheme (2022-2023, 800 MW). CRESS third-party access (September 2024), with the system access charge cut in August 2025 and a fixed 14 sen/kWh "CRESS Acceleration Package" in September 2026. CREAM community solar (2025).
  - **Rooftop solar.** NEM 3.0 (2021-June 2025), followed by Solar ATAP from 1 January 2026, which credits exports at the energy charge for homes and at the average system marginal price for businesses.
  - **Tariffs and procurement.** The RP4 tariff reset: 45.40 sen/kWh average base tariff from 1 July 2025, with a monthly Automatic Fuel Adjustment replacing ICPT. Large Scale Solar rounds up to LSS6 (July 2026: 2,650 MW solar plus 1,250 MW/6,000 MWh of storage).
  - **Policy.** The National Energy Policy 2022-2040 and the National Energy Transition Roadmap (NETR, 2023): 70% renewable installed capacity by 2050 and no new coal plants. Ministers have since said coal generation will end by 2044.
  - **Carbon tax.** A carbon tax on iron, steel and energy was announced for 2026. In June 2026 the bill was still being drafted.
- **Tracking difficulty: moderate, the easiest country scouted so far.**
  - The Energy Commission's new site lists every Act, regulation, gazette notice, guideline and code in one filterable, paginated listing (HTTP 200), with PDFs in English. Most guidelines carry a registration record that lists each revision and its date, which is exactly the amendment chain we need.
  - The hard parts:
    - Each guideline is revised in place ("Pindaan 2024", "Pin.1/2026"), often several times a year, and the PDF at the URL is overwritten.
    - Many decisions (charges, quotas, procurement rounds) exist only as press releases, often in Malay only.
    - Old Energy Commission URLs (`/contents/…` and the `e-aset.st.gov.my` file host) are dead or unreachable, though search engines still return them.
    - The Federal Gazette portal and the Sarawak LawNet were unreachable from our runner.
    - Sabah and Sarawak need their own tracks.
- **Recommendation: go ahead with Malaysia now, Peninsular first.**
  - Start with the 30 candidate rows, which are mostly sourced to official PDFs. Verify them with a reviewer who reads Malay, since gazette texts are bilingual and the Malay text is generally the authoritative one.
  - Decide two schema points first: how to record guideline revisions, and whether a sub-national segment goes in the id (see "Fit with our schema").
  - Add Sabah (ECoS has a clean listing) in the same pass. Treat Sarawak as low-confidence until LawNet or Sarawak Energy can be read.

## Legal hierarchy and document types

From highest to lowest. Malay names are given in brackets.

| Level | Type | Issued by | Numbering and identity | Our `doc_type` |
| --- | --- | --- | --- | --- |
| 1 | Federal Constitution (Perlembagaan Persekutuan) | — | Electricity is on the concurrent list. Sabah and Sarawak legislate their own supply | (not tracked) |
| 2 | Act of Parliament (Akta) | Parliament, with Royal Assent by the Yang di-Pertuan Agong | Principal Acts have a running number ("Act 447"). Amending Acts have an "A" number ("Act A1775"). Each carries a Royal Assent date and a Gazette publication date, and most start on a date the Minister sets by Gazette notification, so there are three dates | law |
| 2s | State Enactment (Sabah) / Ordinance (Sarawak) | State Legislative Assembly, with assent by the Yang di-Pertua Negeri | Sabah: "No. 17 of 2023" (the Electricity Supply Enactment 2024 carries the 2023 number). Sarawak: chapter numbers ("Cap. 50") and amending "Cap. A…" numbers | law (state) |
| 3 | Subsidiary legislation (perundangan subsidiari): regulations (peraturan), orders (perintah), rules (kaedah-kaedah) | Minister, under an Act (e.g. s.53 of Act 447, s.63 of Act 725) | Federal Gazette **P.U.(A) n/yyyy** (e.g. P.U.(A) 335/2025, the Licensee Supply (Amendment) Regulations 2025) | government regulation |
| 3b | Gazette notifications (pemberitahuan), including licence exemptions under s.54 and commencement dates | Minister | **P.U.(B) n/yyyy** (e.g. P.U.(B) 297/2024, the EV-charging licence exemption; P.U.(B) 520/2024, the commencement of Act A1739) | decision |
| 4 | Energy Commission codes (kod) | Energy Commission under s.50A, approved by the Minister | `KOD/ST/No.x/yyyy` (e.g. the Grid Code for Peninsular Malaysia, KOD/ST/No.8/2025) | circular (see notes) |
| 4 | Energy Commission guidelines (garis panduan) | Energy Commission under s.50C (tariff guidelines also under s.26). Non-compliance is an offence (s.50E, added in 2015) | `GP/ST/No.x/yyyy`, with revisions marked "(Pindaan yyyy)" or "(Pin. n/yyyy)" and listed in a registration record on page 1 | circular |
| 4 | Energy Commission directions (arahan) and circulars (pekeliling) | Energy Commission | Mostly safety and service standards | circular |
| policy | Cabinet and ministry decisions: tariff approvals under s.26, programme launches, charges, procurement rounds | Cabinet, PETRA (earlier KeTTHA, KeTSA, NRECC), announced by PETRA or ST press release or "notis makluman" | Press release date and a file reference (e.g. PETRA.100-9/1/4 JLD.2 (34)) | decision |
| plan | National policies and roadmaps (NEP 2022-2040, NETR 2023, Malaysia Plans); generation development plans approved by the JPPPET planning committee | Ministry of Economy (formerly EPU); PETRA and ST for generation plans | Name and period | plan |

Notes:

- **Authoritative language.** Acts and P.U. instruments are published in Malay and English. The Malay text is generally authoritative. The Energy Commission writes most guidelines in English, though a few, such as the AFA claims guideline and the meter guidelines, are in Malay only. PETRA press releases are often Malay only (the September 2026 CRESS Acceleration Package release is one).
- **Ministry names change often.** The energy ministry has been KeTTHA (to 2018), MESTECC (2018-2020), KeTSA (2020-2022), NRECC (2022-2023), KPTDGA (December 2023) and PETRA (renamed February 2024). The issuing body field should use the name at the time of signing.
- **Two guideline "dates".** The Energy Commission's listing shows a "Diterbitkan/Issued" date that is often only the upload date: dozens of documents show February or March 2026 because the site was migrated then. Take the registration and revision dates from the registration record inside each PDF.

## Official sources

All tests were run on 2026-11-04 from a cloud container outside Malaysia through a proxy, using curl with a browser user agent and the WebFetch tool.

| Portal | URL | What it holds | Search / listing | Language | Scrapeability (status we got) |
| --- | --- | --- | --- | --- | --- |
| Energy Commission (ST): legislation library | https://www.st.gov.my/ms/tentang-kami/perundangan | Acts, regulations, Gazette notifications, guidelines, codes, directions, circulars, prosecution reports; PDFs under `/sites/default/files/yyyy-mm/` | Category filter `?resource_branch_parent_tid=` (389 Acts, 397 regulations, 393 Gazette notifications, 32 guidelines, 348 codes, 392 directions, 390 circulars) plus `&page=N`. About 23 pages in all; we listed 117 items | English and Malay | **200**. Server-rendered Drupal, easy to parse. Each item gives title, category and upload date. Old `/contents/…` URLs return **404** |
| Energy Commission: programme pages | https://www.st.gov.my/sustainability/energy-transition-programmes | One page each for CRESS (plus the Acceleration Package), CREAM, GET, SELCO, CGPP and Solar ATAP, with guideline PDFs, charge notices and FAQs; also the Electricity Market and IBR pages | Static pages | English | **200** |
| Energy Commission: legacy file host | https://e-aset.st.gov.my/ | Older PDFs (Act A1739 copy, P.U.(B) 520/2024, LSS PETRA 5+ notice, generation development plan reports) that search engines still index | — | — | **Connection failed (000)**. Treat these links as dead and use the `www.st.gov.my/sites/default/files/` copies |
| Laws of Malaysia (Attorney General's Chambers) | https://lom.agc.gov.my/ | Principal and amending Acts, P.U.(A) and P.U.(B) | Navigation uses tokenised `processFile.php?token=…` links (base64-encoded internal URLs), so it is hard to crawl | Malay and English | **200** for the home page. Direct PDF paths under `/ilims/upload/portal/akta/outputaktap/` work (Act 447 and A1739 returned 200, A1775 returned 200 with the full text). The A1501 path returned **500** |
| Federal Gazette (e-Warta) | https://www.federalgazette.agc.gov.my/ | The Gazette as published | — | Malay and English | **Connection failed (000)** |
| Ministry of Energy Transition and Water Transformation (PETRA) | https://www.petra.gov.my/ | Press releases, policy statements | — | Malay, some English | **200**, but the page is a JavaScript single-page app with no server-rendered links. PETRA press releases are easier to get as copies on st.gov.my |
| SEDA Malaysia | https://www.seda.gov.my/ and the RE portal https://www.seda.gov.my/reportal/ | Renewable Energy Act 2011 and its P.U.(A) orders and rules (PDFs in `/wp-content/uploads/`); FiT, NEM, Solar ATAP, LSS and SELCO pages; quota results | WordPress pages and announcements; `/feed/` RSS | English and Malay | **200** |
| Single Buyer | https://www.singlebuyer.com.my/ | NEDA, CRESS, CREAM and cross-border (ENEGEM) registration, templates, average SMP | Menus | English | **200** |
| Grid System Operator | https://www.gso.org.my/ | System data, grid code materials | — | English | **200** once, then **connection failed (000)**: intermittent |
| TNB / myTNB | https://www.tnb.com.my/ ; https://www.mytnb.com.my/ | Tariff tables, GET, connection rules | Menus | English and Malay | **200** |
| MyPOWER Corporation | https://www.mypower.gov.my/ | Electricity supply industry reform (third-party access, tariffs), nuclear programme office | Static | English | **200** |
| Ministry of Economy | https://www.ekonomi.gov.my/ | NETR, NEP 2022-2040, Malaysia Plans (PDFs) | — | English and Malay | **200** (NETR and NEP PDFs downloaded) |
| Energy Commission of Sabah (ECoS) | https://ecos.gov.my/ (pages `/content/enactment`, `/content/regulations`, `/content/guidelines`) | Sabah enactments, regulations and guidelines in Malay and English | Static lists of PDFs | English and Malay | **200** (www redirects with 301) |
| Sabah State Attorney-General's Chambers | https://sagc.sabah.gov.my/ | Reference copies of Sabah enactments | — | English | **200** (PDF) |
| Sabah Electricity (SESB) | https://www.sesb.com.my/ | Utility | — | — | **Connection failed (000)** |
| Sarawak LawNet | https://lawnet.sarawak.gov.my/ | Consolidated Sarawak ordinances (Cap. 50 reprint as at 2024) | — | English | **Connection failed (000)** |
| Sarawak Energy | https://www.sarawakenergy.com/ | Media releases on the 2023 Electricity (Amendment) | — | English | **403** (curl and WebFetch) |
| Parliament | https://www.parlimen.gov.my/ | Bills and Hansard | — | Malay | **Connection failed (000)** |

Secondary aggregators: the ESCAP Asia Pacific Energy Portal (https://policy.asiapacificenergy.org/) has summaries of Malaysian Acts. Law-firm alerts (Skrine, Rahmat Lim, Christopher & Lee Ong, LHAG, Baker McKenzie/Wong & Partners) reliably report each new guideline within days.

## Key rules since about 2017, by topic

Confidence is **high** when we read the official PDF, **medium** when one credible secondary source supports it, and **low** when the source was unreachable or weak. Row ids refer to the candidate CSV. "Peninsular" means Peninsular Malaysia; most federal guidelines also cover Labuan.

### framework-law

| Rule | Issuer | Date | Effect | Amends / revokes | Status | Source | Conf. |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Electricity Supply Act 1990 (Act 447) — MY-ACT-1990-447 | Parliament | Royal Assent 22 Aug 1990; Gazette 30 Aug 1990 | The framework law. s.9 licences for every installation (public and private); s.26 tariffs; s.50A codes; s.50C guidelines; s.54 exemptions. Suspended in Sarawak from 1 Sep 1990 (P.U.(A) 272/1990) | — | amended | [LOM PDF](https://lom.agc.gov.my/ilims/upload/portal/akta/outputaktap/459_BI/447%20ELECTRIC%201990%20BI.pdf) | high |
| Electricity Supply (Amendment) Act 2015 (Act A1501) — MY-ACT-2015-A1501 | Parliament | Royal Assent 30 Oct 2015; Gazette 5 Nov 2015; in force 1 Jan 2016 | Created the Single Buyer (s.22B) and System Operator (s.22A) with ring-fencing; codes (s.50A); binding guidelines and directions (s.50C), with an offence for non-compliance; Electricity Industry Fund | amends Act 447 | in force | [ESCAP summary](https://policy.asiapacificenergy.org/ru/node/1204) | high |
| Electricity Supply (Amendment) Act 2024 (Act A1739) — MY-ACT-2024-A1739 | Parliament | Royal Assent 2 Jul 2024; Gazette 26 Nov 2024; in force 1 Jan 2025 (P.U.(B) 520/2024) | Removes "efficient use of electricity" (Part VA) from Act 447; that moves to the Energy Efficiency and Conservation Act 2024 (Act 861) | amends Act 447 | in force | [ST PDF](https://www.st.gov.my/sites/default/files/2026-02/Electricity-Supply-%28Amendment%29-Act-2024---Act-A1739.pdf) | high |
| Electricity Supply (Amendment) Act 2025 (Act A1775) — MY-ACT-2025-A1775 | Parliament (Dewan Rakyat 30 Jul 2025, Dewan Negara 9 Sep 2025) | Royal Assent 31 Oct 2025; Gazette 18 Nov 2025 | Licences for importing and exporting electricity (new s.22D); defines "green attributes"; creates a "Market Operator" (s.22C). Commencement is by ministerial notification, possibly in stages. **No commencement notice found** | amends Act 447 | in force? (see notes) | [LOM PDF](https://lom.agc.gov.my/ilims/upload/portal/akta/outputaktap/3181495_BI/Act%20A1775%20-%20ELECTRICITY%20SUPPLY%20(AMENDMENT)%20ACT%202025.pdf) | high (text); low (in-force date) |
| Energy Commission (Amendment) Act 2025 (Act A1776) — MY-ACT-2025-A1776 | Parliament | Gazette 18 Nov 2025 | Gives the Energy Commission regulatory functions over electricity imports and exports | amends Act 610 (not a row) | in force? | ST performance booklet (via search) | medium |
| Sabah Electricity Supply Enactment 2024 (No. 17 of 2023) — MY-SBH-ENACT-2023-17 | Sabah Legislative Assembly | Assent and in force 3 Jan 2024 | Sabah's own licensing (s.8), tariffs and fund; ECoS takes over from ST | (displaces Act 447 in Sabah; instrument not located) | in force | [ECoS PDF](https://ecos.gov.my/sites/default/files/uploads/para/attachments/2024-01/8.%20Electricity%20Supply%20Enactment%202024.pdf) | high |
| Sarawak Electricity (Amendment) Ordinance 2023 (cited as Cap. A210/2023) — MY-SWK-ORD-2023-A210 | Sarawak Legislative Assembly | Passed 21 Nov 2023 | Puts the Single Buyer (Sarawak Energy) into law; solar up to 50 kW may be installed without a licence and can sell surplus; special agreements above 5 MW | amends Cap. 50 (not a row) | in force (assumed) | [The Star](https://thestar.com.my/news/nation/2023/11/21/sarawak-assembly-passes-electricity-bill) | low |

Not rows yet: the Electricity Supply (Amendment) Act 2001 (Act A1116); the Energy Commission Act 2001 (Act 610); the Energy Efficiency and Conservation Act 2024 (Act 861, in force by P.U.(B) 521/2024); the Licensee Supply (Amendment) Regulations 2025 (P.U.(A) 335/2025, in force 1 Oct 2025: voltage definitions and supply-request procedures).

### captive-power

| Rule | Issuer | Date | Effect | Status | Source | Conf. |
| --- | --- | --- | --- | --- | --- | --- |
| Guidelines on Licence Application under the ESA 1990, 2nd ed. (GP/ST/No.52/2024) — MY-GP-2024-52 | ST | 2024 (listed 27 Jan 2025) | Splits licences into **public** (selling to utilities; NEM and NOVA own use with export; own use where a third party owns the asset under a lease or PPA) and **private** (own use with a consumer-owned asset, e.g. diesel or solar). Lists the s.54 exemptions (P.U.(B) 156/1994, 342/2008, 307/2012, 297/2024) | in force | [ST PDF](https://www.st.gov.my/sites/default/files/2026-02/GUIDELINES-ON-LICENCE-APPLICATION.pdf) | high |
| SELCO guidelines (GP/ST/No.51/2024) — MY-GP-2024-51 | ST | in force 1 Jan 2025; revised 27 Mar 2025 and 15 Jun 2026 (signed 21 Jul 2026) | Self-consumption solar without export credit. Revokes GP/ST/No.13/2017 (Pin.2023). 31 Dec 2025 notice: the standby charge of RM12/kWp and the battery requirement now apply above 1 MWac (the battery rule used to apply above 72 kWp) | amended | [ST PDF](https://www.st.gov.my/sites/default/files/2026-07/Guidelines-for-Solar-Photovoltaic-for-Self-Consumption-In-Peninsular-Malaysia.pdf) | high |

P.U.(B) 297/2024 (1 Aug 2024) exempts low-voltage EV-charging installations (100 A or less) from s.9 licensing. It sits on the edge of scope and is not a row.

### wheeling-dppa

| Rule | Issuer | Date | Effect | Status | Source | Conf. |
| --- | --- | --- | --- | --- | --- | --- |
| Corporate Green Power Programme (CGPP) — MY-DEC-2022-CGPP | ST, for the ministry (NRECC) | Launched 7 Nov 2022 (600 MW). Applications 9 May-31 Dec 2023 (800 MW) | Virtual PPA between a corporate consumer and a new solar producer, settled through NEDA; target commercial operation in 2025. 22 producers (563.42 MW) announced in August 2023 | expired (window closed) | [ST information guide](https://www.st.gov.my/sites/default/files/2026-03/Information_Guide_For_Corporate_Green_Power_Programme_%28For_Solar_PV_Plant%29_April_2023ii.pdf); [ST award notice](https://www.st.gov.my/sites/default/files/2026-03/070823--Announcement-of-Successful-SPP-For-CGPP.pdf) | medium (launch date); high (2023 round) |
| CRESS guidelines (GP/ST/No.40/2024) — MY-GP-2024-40 | ST | First version 20 Sep 2024; revised 1 Mar 2025 and 29 Dec 2025 (signed 26 Dec 2025) | Third-party access: a renewable developer supplies a green consumer over TNB's network in the Peninsula and pays the Single Buyer a system access charge (SAC). 51% local ownership is a licence condition. SAC: 25/45 sen/kWh (firm/non-firm) at launch, cut to 20/40 sen for RP4 by PETRA on 29 Aug 2025 | amended | [ST PDF](https://www.st.gov.my/sites/default/files/2026-04/Guidelines-for-CRESS_2.pdf); [PETRA SAC release](https://www.st.gov.my/sites/default/files/2026-03/siaran_mediaeng_2.pdf) | high |
| CRESS Acceleration Package — MY-DEC-2026-CAP | PETRA | 18 Sep 2026 | Fixed SAC of 14 sen/kWh (firm) for developers and 4.02 sen/kWh for green consumers, for 10 years from COD; minimum 10-year contract; only for projects at COD by 31 Dec 2028. 11 developers and 8 consumers (3,148 MW) were registered under CRESS by then. The SAC method changes from RP5 (2028) | in force | [ST CAP SAC PDF](https://www.st.gov.my/sites/default/files/2026-10/System-Access-Charge-%28SAC%29---CRESS-Acceleration-Package_1.pdf); [ST CAP page](https://www.st.gov.my/sustainability/energy-transition-programmes/corporate-renewable-energy-supply-scheme/cress-acceleration-package) | high |
| CREAM guidelines (GP/ST/No.55/2025) — MY-GP-2025-55 | ST | 2025 (applications from 1 Jun 2025) | Community solar plants (100 kWp-2 MWp per 11 kV feeder) supply local green consumers through the network; community access charge 15 sen, cut to 9 sen/kWh on 29 Aug 2025 | in force | [ST PDF](https://www.st.gov.my/sites/default/files/2026-03/CREAM-GUIDELINE_FINAL_2.pdf) | high |

The NEDA guidelines (grid-market-rules) are also the settlement layer for CGPP, CRESS and CREAM. In Sarawak, the 2023 amendment reportedly lets solar producers sell to another consumer when the Single Buyer does not need the power (low confidence).

### rooftop-solar

| Rule | Issuer | Date | Effect | Status | Source | Conf. |
| --- | --- | --- | --- | --- | --- | --- |
| NEM Rakyat and NEM GoMEn guidelines (GP/ST/No.27/2021) — MY-GP-2021-27 | ST | 29 Jan 2021; 8 versions to 19 Aug 2026 | NEM 3.0 (announced by KeTSA on 29 Dec 2020, 2021-2025, up to 2,500 MW in all): one-for-one offset for 10 years for homes and government buildings. Quota top-ups 2023-2025 were each a revision; the 2026 revision follows the new tariff structure. New applications ended 30 Jun 2025 (SEDA) | amended | [ST PDF](https://www.st.gov.my/sites/default/files/2026-08/GUIDELINES-FOR-SOLAR-PHOTOVOLTAIC-INSTALLATION-UNDER-THE-PROGRAMME-OF-NEM-RAKYAT-AND-NEM-GOMEN-IN-PENINSULAR-MALAYSIA_Rev.1_2026_.pdf) | high |
| NOVA guidelines (GP/ST/No.28/2021) — MY-GP-2021-28 | ST | 29 Jan 2021; revised 2023, 2024 (twice), 2025, and 23 Jul 2026 | Net offset virtual aggregation for non-domestic consumers, up to 1,000 kW; exports credited at the average SMP. Quota top-ups of 500/300/300/300 MW | amended | [ST PDF](https://www.st.gov.my/sites/default/files/2026-07/Guidelines-for-Solar-Photovoltaic-Installation-Under-Net-Offset-Virtual-Aggregations-%28NOVA%29-Programme-For-Peninsular-Malaysia.pdf) | high |
| Solar ATAP guidelines (GP/ST/No.60/2025) — MY-GP-2025-60 | ST (PETRA policy; SEDA implementing) | Registered 30 Dec 2025; in force 1 Jan 2026 | Replaces NEM for new applicants. Homes are credited at the energy charge and businesses at the average SMP, on energy only. Caps of 5 kW (single phase) and 15 kW (three phase) for homes and 1,000 kW otherwise. NEM participants may switch only by ending their NEM contract | in force | [ST PDF](https://www.st.gov.my/sites/default/files/2026-03/GUIDELINES-FOR-SOLAR-ACCELERATED_0.pdf); [SEDA Solar ATAP page](https://www.seda.gov.my/reportal/atap/) | high |

For context: NEM 1.0 started in November 2016 (500 MW to 2020) and NEM 2.0 on 1 Jan 2019, both before the NEM 3.0 guideline numbers. SELCO is covered under captive-power. Sabah runs its own "Solar Rakyat Sabah" scheme under ECoS (not researched).

### tariffs-ppa

| Rule | Issuer | Date | Effect | Status | Source | Conf. |
| --- | --- | --- | --- | --- | --- | --- |
| RP4 tariff schedule — MY-DEC-2025-RP4 | Government (s.26 approval), announced by ST | 20 Jun 2025; in force 1 Jul 2025-31 Dec 2027 | Average base tariff of 45.40 sen/kWh (against 45.62 sen approved in Dec 2024). New categories by voltage; separate energy, capacity, network and retail charges; energy-efficiency incentive for homes using 1,000 kWh or less; wider ToU off-peak. Automatic Fuel Adjustment (AFA) replaces ICPT, published monthly | in force | [ST media statement](https://www.st.gov.my/sites/default/files/2026-09/Kenyataan-Media---Jadual-Tarif-RP4.pdf) | high |
| IBR tariff guidelines for Peninsular Malaysia 2025 (GP/ST/No.56/2025) — MY-GP-2025-56 | ST (ss.26 and 50C) | Listed 28 Jul 2025 | Regulatory implementation guidelines for RP4: revenue cap, base tariff, AFA method (section 7), WACC, efficiency carry-over | in force | [ST PDF](https://www.st.gov.my/sites/default/files/2026-02/REGULATORY_IMPLEMENTATION_GUIDELINES.pdf) | high (date medium) |
| Guidelines on Green Electricity Tariff (GP/ST/No.38/2023) — MY-GP-2023-38 | ST | 2023; revised 25 Nov 2024, 31 Jan 2025 and 14 Jul 2025 | TNB's green tariff (consumers pay a premium for renewable supply, with mREC transfer from 2025). Revokes GP/ST/No.31/2022 | amended | [ST PDF](https://www.st.gov.my/sites/default/files/2026-02/GUIDELINES_ON_ELECTRICITY_TARIFF.pdf) | high |

Also found: earlier IBR guidelines for RP2 and RP3 (2018, 2021 and 2022 editions, plus Sabah and Labuan 2023). The 3 Nov 2025 AFA claims guideline (GP/ST/No.53/2024 (Pindaan 2025), Malay only) is a candidate for phase 2. The 3 sen/kWh monthly AFA cap is reported by the press, not confirmed in an official text. PPA terms for IPPs are not public.

### re-pricing

| Rule | Issuer | Date | Effect | Status | Source | Conf. |
| --- | --- | --- | --- | --- | --- | --- |
| Renewable Energy Act 2011 (Act 725) — MY-ACT-2011-725 | Parliament | 2011 (exact dates not confirmed) | Feed-in tariff system run by SEDA, paid from the RE fund, for the Peninsula and Labuan (Sabah left in 2024) | amended | [SEDA page](https://www.seda.gov.my/policies/renewable-energy-act-2011/) | medium |
| Renewable Energy (Amendment) Act 2023 (Act A1689) — MY-ACT-2023-A1689 | Parliament | Royal Assent 22 Jul 2023; Gazette 28 Jul 2023 | Among other things, lets the Minister suspend the Act in parts of Malaysia (new s.1(3)), which appears to prepare for Sabah's own RE enactment. Commencement not confirmed | in force? | [SEDA PDF](https://www.seda.gov.my/wp-content/uploads/2023/08/RENEWABLE-ENERGY-AMENDMENT-ACT-2023-ACT-A1689-BI.pdf) | high (text) |
| RE (Amendment of Schedule) Order 2025, P.U.(A) 251/2025 — MY-PUA-2025-251 | Minister (PETRA), s.63 Act 725 | Made 1 Aug 2025; deemed in force 28 Jan 2019 | Extends the FiT period for biogas from 16 to 21 years | in force | [SEDA PDF](https://www.seda.gov.my/wp-content/uploads/2025/08/Perintah-Tenaga-Boleh-Baharu-Pindaan-Jadual-2025-P.U.-A-251_2025.pdf) | high |
| Guidelines on LSS PV plants for connection (GP/ST/No.1/2016) — MY-GP-2016-1 | ST | 28 Apr 2016; revised 20 Dec 2018, 20 May 2020 and 2 Apr 2024 | Framework and grid-connection rules for Large Scale Solar auction plants | amended | [ST PDF](https://www.st.gov.my/sites/default/files/2026-02/Guidelines-on-Large-Scale-Solar-PV-Plant-for-Connection-to-Electricity-Network.pdf) | high |
| LSS6 RFP notice — MY-DEC-2026-LSS6 | PETRA through ST | 24 Jul 2026 | Sixth LSS round in the Peninsula: 2,650 MW solar and 1,250 MW/6,000 MWh BESS in three packages (2,200 MW + 1,100 MW BESS open; 300 MW + 150 MW BESS Bumiputera; 150 MW Bumiputera solar only) | in force | [ST notice](https://www.st.gov.my/sites/default/files/2026-07/Notis-Makluman-Pengapungan-Dokumen-Request-For-Proposal-Bagi-Program-Bidaan-Terbuka-Large-Scale-Solar.pdf) | high |
| Sabah Renewable Energy Enactment 2024 (No. 18 of 2023) — MY-SBH-ENACT-2023-18 | Sabah Legislative Assembly | Assent and in force 3 Jan 2024 | Sabah's own FiT system under ECoS (replaces SEDA there) | in force | [ECoS PDF](https://ecos.gov.my/sites/default/files/uploads/para/attachments/2024-01/10.%20Sabah%20Renewable%20Energy%20Enactment%202024.pdf) | high |

Not rows yet, and needing primary sources:
- Earlier LSS rounds: LSS4 (2020); LSS5 (RFP April 2024, 2 GW); LSS PETRA 5+ (notice 17 Jan 2025 on the dead e-aset host; 13 projects totalling 1,975 MWac reported).
- FiT 2.0 (SEDA, 17 Oct 2024): a fixed rate for 10 years, then bids between a floor and a ceiling for the remaining 11 years. The amendments to the FiT rules, P.U.(A) 385/2011, that it relies on are not identified; SEDA ran a regulatory impact analysis consultation on amending them.
- P.U.(A) 131/2022: raised the biogas eligibility cap from 5 MW to 30 MW and revised biomass items.
- P.U.(A) 439/2025: administrative fees.

### coal-phase-out

No legal instrument. The commitments are in plans and ministerial statements:
- **Twelfth Malaysia Plan.** Tabled on 27 Sep 2021, it included a pledge to build no new coal plants (press reports).
- **NETR (2023).** It sets "Target 2: No new coal power plant" and has coal "close to fully phased-out" from power generation by 2050 (NETR text). Row: MY-PLAN-2023-NETR.
- **The 2044 date.** At London Climate Action Week in June 2024, Deputy Prime Minister Fadillah Yusof said coal would be halved by 2035 and fully retired by 2044. He reaffirmed this in July 2026 and mentioned a proposed National Coal Site Repurposing Framework (press reports). Neither statement is a legal instrument. Track them in the NETR row notes, or as a "decision" if a Cabinet decision is found.

### power-plans

Peninsular generation plans are prepared by ST and approved by the JPPPET committee. They are published only as "Report on Peninsular Malaysia Generation Development Plan" documents, and only some editions are public: the 2019 edition (2020-2030) and the 2020 edition (2021-2039). A 2024-2050 projection was approved by JPPPET, according to Malay Mail on 27 Feb 2025, but we found no public document, so there is no row yet. New capacity is procured by RFP, such as the NEWGEN25 RFP for new generation capacity in 2025-2029, listed on ST. The NETR is tagged power-plans in the meantime. Sabah's JPPPET approved its own generation plan in August 2023 (press).

### grid-market-rules

| Rule | Issuer | Date | Effect | Status | Source | Conf. |
| --- | --- | --- | --- | --- | --- | --- |
| NEDA guidelines (GP/ST/No.12/2017) — MY-GP-2017-12 | ST | 17 Apr 2017; revised 28 May 2019, 5 Dec 2019, 22 Nov 2024 and 26 Dec 2025 | New Enhanced Dispatch Arrangement: generators without PPAs (and, from 2019, solar producers) bid into Single Buyer dispatch at the system marginal price. The 2024 revision added CRESS, CGPP and LSS; the 2025 revision added CREAM | amended | [ST PDF](https://www.st.gov.my/sites/default/files/2026-02/NEDA-Guideline-2025-final.pdf) | high |
| Guidelines for Single Buyer Market (Peninsular Malaysia) 2018 (GP/ST/No.16/2018) — MY-GP-2018-16 | ST | 18 Apr 2018; revised 1 Nov 2024 (signed 18 Nov 2024) | Rules for the Single Buyer's planning, scheduling, procurement and settlement, with ring-fencing practices | amended | [ST PDF](https://www.st.gov.my/sites/default/files/2026-02/%5BPindaan-2024%5D-Guidelines-for-Single-Buyer-Market-%28Peninsular-Malaysia%29-2018.pdf) | high |
| Grid Code for Peninsular Malaysia – Main Code (KOD/ST/No.8/2025) — MY-KOD-2025-8 | ST under s.50A, approved by the PETRA Minister | Dated 28 Mar 2025; in force 1 Jan 2026 | New grid code (Main Code plus Additional Code). It appears to replace the Grid Code KOD/ST/No.2/2010, but we did not find a revocation clause | in force | [ST PDF](https://www.st.gov.my/sites/default/files/2026-02/01-MainCode.pdf) | high |

Also listed by ST: the Guidelines for Ring-Fencing of the System Operator (Peninsular Malaysia) 2016 (revised 2024); the Single Buyer and System Operator guidelines for Labuan (2023); the Distribution Code for Peninsular Malaysia, Sabah and Labuan (2017); the Sabah and Labuan Grid Code (2017, now superseded in Sabah by the ECoS Sabah Grid Code); and ENEGEM, the cross-border energy exchange run by the Single Buyer.

### carbon-pricing

No enacted instrument, so there are no rows.
- **Announcements.** Budget 2025 (October 2024) and Budget 2026 (10 Oct 2025) announced a carbon tax from 2026, first on iron, steel and energy, tied to a National Carbon Market Policy and a Climate Change Bill.
- **Status in June 2026.** On 24 Jun 2026 the government told the Dewan Rakyat that the Carbon Tax Bill was in its final drafting stage, with the mechanism and rate not decided. An RM15/tonne figure appears in some reports but is unconfirmed.
- **Since then.** We found nothing after June 2026 showing the bill was tabled. Bursa Carbon Exchange (voluntary market, 2022-2023) is out of scope for now.

### energy-strategy

| Rule | Issuer | Date | Effect | Status | Source | Conf. |
| --- | --- | --- | --- | --- | --- | --- |
| National Energy Policy 2022-2040 (Dasar Tenaga Negara) — MY-PLAN-2022-NEP | Economic Planning Unit, Prime Minister's Department | Launched 19 Sep 2022 | Low Carbon Nation Aspiration 2040; a living document reviewed every three years by a National Energy Council | in force | [Ministry of Economy PDF](https://www.ekonomi.gov.my/sites/default/files/2022-09/National%20Energy%20Policy_2022_2040.pdf) | high |
| National Energy Transition Roadmap (NETR) — MY-PLAN-2023-NETR | Ministry of Economy | Phase 1 27 Jul 2023; Phase 2 29 Aug 2023 | 70% RE installed capacity by 2050 (up from 40% by 2040); no new coal plants; coal "close to fully phased-out" of the power mix by 2050; 10 flagship catalyst projects (Phase 1); signals a third-party access framework for the power sector | in force | [Ministry of Economy PDF](https://www.ekonomi.gov.my/sites/default/files/2023-09/National%20Energy%20Transition%20Roadmap_0.pdf) | high |

Also relevant but not rows: the National Renewable Energy Policy and Action Plan 2009 (SEDA is procuring the drafting of NREPAP 2.0, tender SEDASH 09/2026); the National Energy Efficiency Action Plan 2.0 (2026-2035) on ST; Sarawak's PCDS 2030; and the NETR progress reports.

## Fit with our schema

- **Guidelines carry most of the weight, and `circular` is the nearest `doc_type`.** An ST guideline is issued by the regulator under a statutory power (s.50C), is binding (s.50E) and has a registered number, so it behaves like Vietnam's ministry circulars. We map guidelines and codes to `circular` and explain this in the notes. Codes (KOD/ST) could have their own type later. Gazette-level ministerial rules (P.U.(A)) map to `government regulation`. Ministerial and Cabinet programme decisions (tariff approval, CAP, LSS rounds, CGPP) map to `decision`.
- **Revisions in place.** Each guideline keeps its base number through many revisions ("Pindaan 2024", "Pin.1/2026"), and the PDF at the URL is replaced. Options:
  - (a) one row per base number with status `amended` and the revision history in the notes (what the CSV does now);
  - (b) one row per substantive revision, each linked to the base by `amends`. This suits the CRESS SAC changes and the Solar ATAP and NEM quota steps.

  Recommendation: (a) by default and (b) only when a revision changes prices, quotas or eligibility. We should also record the registration date of each revision, since the listing's upload date is unreliable. A change history (phase 2 item 4) would fit well here.
- **Programmes are announced, then codified.** CRESS, CREAM, Solar ATAP and the SAC cuts all start as PETRA press releases and only later become guideline text ("Caveat to be updated" on the CAP page). The tracker needs a way to link a `decision` row to the guideline revision that implements it.
- **Status gaps.** Act A1775 (and possibly A1689) have been gazetted but have no commencement notice we could find. The schema has no "enacted, not yet in force" or "partly in force" status, so these rows are marked `in force` with a warning in the notes. We suggest adding `pending`. Closed programmes whose contracts continue (CGPP, NEM 3.0 for existing participants) do not fit `expired` well either.
- **Sub-national law.** Sabah enactments and Sarawak ordinances are full `law`s but apply to one state only. The id format has no place for that, so we used `MY-SBH-…` and `MY-SWK-…`, which breaks the strict country-type-year-number pattern. We need either a `jurisdiction` field or an agreed id segment. Sabah's enactment numbers also do not match their titles: the Electricity Supply Enactment **2024** is **No. 17 of 2023**.
- **Proposed `countries.csv` row.** Hierarchy: `Akta (Act of Parliament);Enakmen/Ordinan (Sabah or Sarawak state law);Peraturan/Perintah, P.U.(A) (subsidiary legislation);Pemberitahuan, P.U.(B) (Gazette notification);Garis Panduan and Kod ST (Energy Commission guideline or code)`. Sources: `Energy Commission legislation library|https://www.st.gov.my/ms/tentang-kami/perundangan;Laws of Malaysia (AGC)|https://lom.agc.gov.my/;SEDA|https://www.seda.gov.my/;Energy Commission of Sabah|https://ecos.gov.my/`.

## Candidate partner institutes and reviewers

Names from desk research only; none has been contacted.

| Institution | Why | URL |
| --- | --- | --- |
| Institute of Energy Policy and Research (IEPRe), Universiti Tenaga Nasional | Energy policy and economics unit; works with ST (the Energy Commission funds a Chair in Energy Economics there); tariff, NEM and market research | https://uniten.edu.my/research/institute-energy-policy-and-research-iepre |
| Institute of Strategic and International Studies (ISIS) Malaysia | Leading policy think tank, publishes on energy transition and climate policy | https://www.isis.org.my/ |
| Khazanah Research Institute | Independent research on economic policy, including energy and utilities | https://www.krinstitute.org/ |
| Institute for Democracy and Economic Affairs (IDEAS) | Policy institute that has published on energy market reform | https://www.ideas.org.my/ |
| UM Power Energy Dedicated Advanced Centre (UMPEDAC), Universiti Malaya | Technical research on solar and grids; could review rooftop and grid rows | https://umpedac.um.edu.my/ |
| Malaysian Photovoltaic Industry Association (MPIA) | Industry view on NEM, Solar ATAP, SELCO, CRESS and LSS; tracks every revision | https://www.mpia.org.my/ |
| ASEAN Centre for Energy | Published a CRESS policy insight (January 2025); regional partner | https://aseanenergy.org/ |
| Law firms with regular Malaysian energy alerts: Skrine; Rahmat Lim & Partners; Christopher & Lee Ong (Rajah & Tann Asia); Lee Hishammuddin Allen & Gledhill | Fast, dated summaries of each guideline; possible pro bono reviewers | https://www.skrine.com/ ; https://www.rahmatlim.com/ ; https://www.christopherleeong.com/ ; https://lh-ag.com/ |
| MyPOWER Corporation (government agency) | Official contact point for reform questions (third-party access, market operator) | https://www.mypower.gov.my/ |

## Risks and open questions

- **Commencement of Acts A1775 and A1776.** Both were gazetted on 18 Nov 2025, but we found no P.U.(B) commencement notice, and the Federal Gazette portal was unreachable. The Energy Commission said in early 2026 that rule-making would follow commencement. A1689 (2023) has the same problem.
- **Overwritten PDFs.** ST replaces guideline PDFs in place (e.g. `Guidelines-for-CRESS_2.pdf`, `..._0.pdf`), and old links rot: the whole `/contents/` tree and `e-aset.st.gov.my` are gone. Archiving each PDF as we fetch it (phase 2 item 3) matters more here than for Indonesia or Vietnam.
- **Upload dates are not issue dates.** The listing's "Issued" date is often the February-March 2026 migration date. Always take dates from the registration record.
- **Press-release governance.** Charges and quotas (SAC, CAC, CAP, LSS packages) are set by PETRA announcement before any guideline text, and the releases are often Malay only. Whether these are "rules" is a scope decision.
- **Sabah and Sarawak.** The legal basis for the federal Act ceasing to apply in Sabah (a suspension order?) was not located. Sarawak sources (LawNet, Sarawak Energy) were unreachable, and the Cap. A210/2023 citation comes from a search snippet only. Sarawak's rules on solar sales, the Single Buyer and exports to Sabah, Brunei, Kalimantan and Singapore need a separate pass.
- **Tariff instruments.** The RP4 tariff schedule is approved by the government under s.26 and published by TNB and ST. We did not find a gazetted instrument, so the row's legal form is a `decision`. Sabah (SESB) tariffs are set by ECoS under the 2024 Enactment and were not researched.
- **Coal and carbon.** Both are commitments without instruments (2044 coal exit; 2026 carbon tax). The topic pages may look empty for Malaysia unless we accept plan and statement rows.
- **Not yet researched:** IPP PPA terms and the NEWGEN25 RFP; the Gas Framework Agreement for power; the Energy Exchange Malaysia (ENEGEM) rules; the Labuan instruments; ECoS guidelines (Sabah Grid Code, Single Buyer Sabah 2024, Sabah IBR); the RE fund (KWTBB) levy changes.

## Sources

Official (fetched and read unless noted):
- https://www.st.gov.my/ms/tentang-kami/perundangan (listing; all category pages)
- https://www.st.gov.my/sustainability/energy-transition-programmes
- https://www.st.gov.my/sustainability/energy-transition-programmes/corporate-renewable-energy-supply-scheme/cress
- https://www.st.gov.my/sustainability/energy-transition-programmes/corporate-renewable-energy-supply-scheme/cress-acceleration-package
- https://www.st.gov.my/sustainability/energy-transition-programmes/solar-accelerated-transition-action-programme-solar
- https://www.st.gov.my/sustainability/energy-transition-programmes/self-consumption-selco
- https://www.st.gov.my/sustainability/energy-transition-programmes/corporate-green-power-programme
- https://www.st.gov.my/sustainability/energy-transition-programmes/green-electricity-tariff-get
- https://www.st.gov.my/sustainability/energy-transition-programmes/community-renewable-energy-aggregation-mechanism-cream
- https://www.st.gov.my/sustainability/market-structure-access/electricity-market
- https://www.st.gov.my/pricing/electricity-pricing-framework/incentive-based-regulation-ibr
- https://www.st.gov.my/ms/struktur-harga/fakta-tarif-elektrik-anda
- https://www.st.gov.my/notis-kadar-afa-bagi-bulan-november-2026
- https://www.st.gov.my/sites/default/files/2026-04/Guidelines-for-CRESS_2.pdf
- https://www.st.gov.my/sites/default/files/2026-03/GUIDELINES-FOR-SOLAR-ACCELERATED_0.pdf
- https://www.st.gov.my/sites/default/files/2026-07/Guidelines-for-Solar-Photovoltaic-for-Self-Consumption-In-Peninsular-Malaysia.pdf
- https://www.st.gov.my/sites/default/files/2026-03/CREAM-GUIDELINE_FINAL_2.pdf
- https://www.st.gov.my/sites/default/files/2026-02/GUIDELINES_ON_ELECTRICITY_TARIFF.pdf
- https://www.st.gov.my/sites/default/files/2026-10/System-Access-Charge-%28SAC%29---CRESS-Acceleration-Package_1.pdf
- https://www.st.gov.my/sites/default/files/2026-10/CRESS-Acceleration-Package-Criteria.pdf
- https://www.st.gov.my/sites/default/files/2026-03/siaran_mediaeng_2.pdf
- https://www.st.gov.my/sites/default/files/2026-03/Notis-Makluman-31.12.2025.pdf
- https://www.st.gov.my/sites/default/files/2026-03/Information_Guide_For_Corporate_Green_Power_Programme_%28For_Solar_PV_Plant%29_April_2023ii.pdf
- https://www.st.gov.my/sites/default/files/2026-03/070823--Announcement-of-Successful-SPP-For-CGPP.pdf
- https://www.st.gov.my/sites/default/files/2026-02/NEDA-Guideline-2025-final.pdf
- https://www.st.gov.my/sites/default/files/2026-02/%5BPindaan-2024%5D-Guidelines-for-Single-Buyer-Market-%28Peninsular-Malaysia%29-2018.pdf
- https://www.st.gov.my/sites/default/files/2026-02/01-MainCode.pdf
- https://www.st.gov.my/sites/default/files/2026-02/REGULATORY_IMPLEMENTATION_GUIDELINES.pdf
- https://www.st.gov.my/sites/default/files/2026-02/GUIDELINES-ON-LICENCE-APPLICATION.pdf
- https://www.st.gov.my/sites/default/files/2026-07/Guidelines-for-Solar-Photovoltaic-Installation-Under-Net-Offset-Virtual-Aggregations-%28NOVA%29-Programme-For-Peninsular-Malaysia.pdf
- https://www.st.gov.my/sites/default/files/2026-08/GUIDELINES-FOR-SOLAR-PHOTOVOLTAIC-INSTALLATION-UNDER-THE-PROGRAMME-OF-NEM-RAKYAT-AND-NEM-GOMEN-IN-PENINSULAR-MALAYSIA_Rev.1_2026_.pdf
- https://www.st.gov.my/sites/default/files/2026-02/Guidelines-on-Large-Scale-Solar-PV-Plant-for-Connection-to-Electricity-Network.pdf
- https://www.st.gov.my/sites/default/files/2026-07/Notis-Makluman-Pengapungan-Dokumen-Request-For-Proposal-Bagi-Program-Bidaan-Terbuka-Large-Scale-Solar.pdf
- https://www.st.gov.my/sites/default/files/2026-02/PERATURAN-PERATURAN_BEKALAN_PEMEGANG_LESEN_PINDAAN_2025_PUA335-2025.pdf
- https://www.st.gov.my/sites/default/files/2026-03/PUB297_PEMBERITAHUAN_SEKSYEN_54.pdf
- https://www.st.gov.my/sites/default/files/2026-02/Electricity-Supply-%28Amendment%29-Act-2024---Act-A1739.pdf
- https://www.st.gov.my/sites/default/files/2026-02/Act-447---Electricity-Supply-Act-1990.pdf
- https://www.st.gov.my/sites/default/files/2026-02/Garis-Panduan-Tuntutan-Melalui-Mekanisme-Pelarasan-Tarif-Elektrik-bagi-Pemegang-LAP.pdf
- https://www.st.gov.my/sites/default/files/2026-09/Kenyataan-Media---Jadual-Tarif-RP4.pdf
- https://st.gov.my/sites/default/files/2026-03/ST_Performance-Booklet_v2i-%28ZM%29.pdf (seen in search results only)
- https://e-aset.st.gov.my/contents/2024/EECA/P.U.%20(B)%20520%202024%20Penetapan%20Tarikh%20Permulaan%20Kuat%20Kuasa%20Akta%20Bekalan%20Elektrik%20(Pindaan)%202024.pdf (search snippet only; host unreachable)
- https://lom.agc.gov.my/principal.php
- https://lom.agc.gov.my/ilims/upload/portal/akta/outputaktap/459_BI/447%20ELECTRIC%201990%20BI.pdf
- https://lom.agc.gov.my/ilims/upload/portal/akta/outputaktap/3181495_BI/Act%20A1775%20-%20ELECTRICITY%20SUPPLY%20(AMENDMENT)%20ACT%202025.pdf
- https://lom.agc.gov.my/ilims/upload/portal/akta/outputaktap/2200928_BI/Electricity%20Supply%20(Amendment)%20Act%202024%20-%20Act%20A1739.pdf
- https://www.seda.gov.my/policies/renewable-energy-act-2011/
- https://www.seda.gov.my/reportal/nem/
- https://www.seda.gov.my/reportal/atap/
- https://www.seda.gov.my/reportal/fit/
- https://www.seda.gov.my/reportal/large-scale-solar/
- https://www.seda.gov.my/wp-content/uploads/2023/08/RENEWABLE-ENERGY-AMENDMENT-ACT-2023-ACT-A1689-BI.pdf
- https://www.seda.gov.my/wp-content/uploads/2025/08/Perintah-Tenaga-Boleh-Baharu-Pindaan-Jadual-2025-P.U.-A-251_2025.pdf
- https://www.seda.gov.my/wp-content/uploads/2023/03/PUA-131-2022.pdf
- https://www.ekonomi.gov.my/sites/default/files/2023-09/National%20Energy%20Transition%20Roadmap_0.pdf
- https://www.ekonomi.gov.my/sites/default/files/2023-07/NETR_Part1_0.pdf
- https://www.ekonomi.gov.my/sites/default/files/2022-09/National%20Energy%20Policy_2022_2040.pdf
- https://www.mypower.gov.my/
- https://www.petra.gov.my/
- https://ecos.gov.my/announcement/energy-commission-sabah-ecos-regulator-energy-electricity-supply-renewable-energy-and
- https://ecos.gov.my/content/enactment ; https://ecos.gov.my/content/regulations ; https://ecos.gov.my/content/guidelines ; https://ecos.gov.my/content/electricity-supply-and-renewable-energy
- https://ecos.gov.my/sites/default/files/uploads/para/attachments/2024-01/8.%20Electricity%20Supply%20Enactment%202024.pdf
- https://ecos.gov.my/sites/default/files/uploads/para/attachments/2024-01/10.%20Sabah%20Renewable%20Energy%20Enactment%202024.pdf
- https://sagc.sabah.gov.my/sites/default/files/law/Sabah%20Renewable%20Energy%20Enactment%202024.pdf
- https://lawnet.sarawak.gov.my/lawnet_file/Ordinance/ORD_CAP.%2050%20Electricity%20LawNet%202024%20(1).pdf (unreachable; cited from search result)

Secondary:
- https://policy.asiapacificenergy.org/ru/node/1204 (Act A1501 summary)
- https://www.skrine.com/insights/alerts/september-2024/cress-guidelines-regulatory-framework-and-requirem
- https://www.rajahtannasia.com/viewpoints/malaysias-corporate-renewable-energy-supply-scheme-cress-key-features-of-the-framework-under-the-guidelines/
- https://www.rahmatlim.com/publication/articles/22679/introduces-corporate-green-power-programme
- https://www.thestar.com.my/business/business-news/2023/08/08/cgpp-allocation-still-has-a-balance-of-about-30
- https://www.thestar.com.my/business/business-news/2026/10/15/cress-charges-fixed-at-14-senkwh-for-developers-4-sen-for-green-consumers
- https://www.thestar.com.my/news/nation/2026/09/18/govt-strengthens-cress-with-14-senkwh-firm-supply-rate
- https://www.thestar.com.my/news/nation/2025/07/30/dewan-rakyat-passes-electricity-supply-bill-and-energy-commission-bill
- https://thesun.my/malaysia-news/dewan-negara-passes-key-bills-on-electricity-trade-and-cross-border-insolvency-FL14861730
- https://www.edgeprop.my/content/1914711/energy-commission-begin-drafting-rules-cross-border-power-trading-early-2026-says-ceo
- https://www.malaymail.com/news/malaysia/2025/06/20/energy-commission-up-to-19pc-reduction-as-putrajaya-unveils-progressive-electricity-tariff-new-rebates-for-low-use-households/181076
- https://www.thestar.com.my/business/business-news/2025/10/10/budget-2026-carbon-tax-to-be-introduced-next-year
- https://www.thestar.com.my/news/nation/2026/06/24/carbon-tax-bill-in-final-stage-of-drafting-dewan-rakyat-heard
- https://www.nst.com.my/amp/news/nation/2026/06/1471495/carbon-tax-bill-final-drafting-phase-dewan-rakyat-told
- https://www.thevibes.com/articles/news/124574/govt-to-end-coal-fired-power-generation-by-2044-fadillah
- https://www.thevibes.com/articles/news/114443/deputy-prime-minister-ii-coal-power-to-be-halved-by-2035-and-fully-retired-by-2044
- https://theedgemalaysia.com/article/12mp-malaysia-committed-becoming-carbonneutral-nation-2050-says-pm
- https://www.businesstoday.com.my/2022/09/19/national-energy-policy-nep-2022-2040-launched-today-as-a-new-narrative-for-energy-transition/
- https://lh-ag.com/energy-projects-infrastructure-national-energy-transition-roadmap-netr-phase-2/
- https://www.pv-magazine.com/2026/07/16/malaysia-unveils-sixth-large-scale-solar-tender/
- https://www.malaymail.com/news/malaysia/2025/02/27/putrajaya-data-centres-could-need-more-power-by-2040-than-malaysia-uses-annually-now/168145
- https://repoemc.ukm.my/items/92398bdd-a7fe-47f3-9bc8-d40661781915/full (Generation Development Plan 2020 report)
- https://www.freemalaysiatoday.com/category/nation/2024/02/08/its-now-the-energy-transition-and-water-transformation-ministry
- https://thestar.com.my/news/nation/2024/01/05/handover-of-electricity-powers-begin-in-sabah
- https://thestar.com.my/news/nation/2023/11/21/sarawak-assembly-passes-electricity-bill
- https://www.malaymail.com/news/malaysia/2023/11/22/premier-amended-sarawak-electricity-ordinance-allow-homeowners-to-sell-excess-power/103566
- https://enlit-asia.com/news-renewables/sarawak-strengthens-commitment-renewable-energy-through-electricity-amendment-act-2023 (search snippet; page returned 503)
- https://www.sarawakenergy.com/electricity-amendment-act-2023-strengthening-sarawaks-commitment-to-renewable-energy (403)
- https://aseanenergy.org/wp-content/uploads/2025/01/Policy-Insight_Malaysia-CRESS2.pdf (seen in search results)
- https://uniten.edu.my/research/institute-energy-policy-and-research-iepre
