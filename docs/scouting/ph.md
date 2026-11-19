# Scouting report: Philippines

Prepared 2026-11-04 for the Southeast Asia Energy Policy Tracker. It comes with [`ph-candidates.csv`](ph-candidates.csv), which has 30 candidate rules in a subset of our schema. Everything here is a lead for reviewers, not checked data. Where a fact rests only on news or a law-firm note, the text says so.

How this was checked: official portals were fetched with `curl` where they allowed it. The HTTP status codes in the tables below come from those fetches. DOE circular PDFs were downloaded and read through their text layer, or through OCR (Tesseract) when they were scanned images. Dates in the CSV come from the document itself, the UP Law Center register (NARO), or a recital in a later DOE circular, unless the notes say otherwise. Web searches filled the gaps.

---

## 1. Summary

- **Structure.** The Electric Power Industry Reform Act of 2001 (EPIRA, RA 9136, approved 2001-06-08) restructured the sector:
  - It split up the state utility NPC. Generation and supply are competitive and need no franchise. Transmission and distribution stay regulated, franchised monopolies.
  - Transmission is owned by the state's TransCo and run under concession by the private **NGCP**.
  - Distribution is done by private utilities (Meralco is the largest) and about 120 electric cooperatives supervised by NEA. The cooperative count is from general knowledge and was not checked.
  - The **WESM** spot market is run by **IEMOP** and governed by PEMC. It now covers Luzon, the Visayas and, since 2023-01-26, Mindanao.
  - EPIRA Sec. 31 provides for **retail competition and open access** (RCOA). It started in 2012 for large users and extended to Mindanao on 2024-03-26.
- **Two rule-makers.** The **DOE** makes policy through Department Circulars, which also adopt the WESM Rules. The independent, quasi-judicial **ERC** turns policy into binding regulation and prices through Resolutions, and decides cases (rates, PSAs, licences). Most topics therefore have a pair of rules, a DOE circular and an ERC resolution, and the tracker needs both.
- **Renewables** sit under the RE Act (RA 9513, 2008-12-16). Its main instruments are:
  - Renewable Portfolio Standards (DC2017-12-0015, increment raised to 2.52% from 2023)
  - the Green Energy Auction (DC2021-11-0036 and amendments; ERC sets ceiling "GEAR" prices for each round)
  - the Green Energy Option, rewritten in 2026 with a 50 kW threshold
  - net metering (ERC rules plus DOE circulars of 2020, 2024 and 2025)
  - virtual PPAs (DC2025-10-0024)

  Since a 2022 DOE circular, foreign owners may hold 100% of solar, wind, hydro and ocean projects.
- **Coal.** A DOE moratorium on endorsing new greenfield coal plants was announced on 2020-10-27. It is a DOE *advisory*, not a circular. A 2025-10-14 advisory widened the exemptions. The DOE said in 2026-05 that the moratorium stays.
- **Plans.** The Philippine Energy Plan (PEP) 2023-2050 and the Power Development Plan (PDP) 2023-2050 set targets of 35% renewables in generation by 2030 and 50% by 2040. Their exact adoption dates are not clear from what we could reach. DC2026-02-0005 now governs how the PDP is prepared.
- **Tracking difficulty: moderate.** Everything is in English and numbering is regular (DC*YYYY-MM-NNNN*, "Resolution No. N, s. YYYY"). The DOE's new site has server-rendered listings by year and was easy to scrape. The UP Law Center register (NARO) gives issue and filing dates for DOE and ERC rules. Lawphil and the Supreme Court E-Library cover laws and executive orders. The obstacles:
  - The ERC site, Official Gazette, Congress and NGCP all returned 403 (Cloudflare challenges).
  - Most DOE PDFs are scans and need OCR.
  - The DOE's 2025-26 site migration broke old links.
  - The volume is high, with roughly 25 to 40 DOE circulars a year, many of them WESM rule amendments.
- **Recommendation: yes, make the Philippines the next country.** Its rules map onto our schema with fewer gaps than Vietnam's. Language costs nothing. The topics line up closely with Indonesia's and Vietnam's (rooftop solar, direct PPAs, RE auctions, coal limits, national plans), so the Compare page gains a lot. Plan for two things: a way into ERC documents (manual download, NARO, or partner help), and OCR in the phase 4 portal scan.

## 2. Legal hierarchy and document types

From highest to lowest rank. The numbering formats come from the documents we read.

| Rank | Type | Issuer | How it is numbered and cited | Our `doc_type` |
| --- | --- | --- | --- | --- |
| 1 | **1987 Constitution** | People | Article and section. Art. XII Sec. 2 (natural resources, 60% Filipino ownership) drives the RE foreign-ownership question. | (not tracked) |
| 2 | **Republic Act (RA)** | Congress (Senate and House), signed by the President | One running series across years: "Republic Act No. 9136", cited "RA 9136". Older laws with the same force: Presidential Decrees (e.g. PD 269 on electrification, PD 1096 Building Code) and Commonwealth Acts (CA 146, the Public Service Act). Many RAs are just franchises for one distribution utility or cooperative (e.g. RA 12146, Meralco's renewal, 2025-04-11). | `law` |
| 3 | **Executive Order (EO)** and other presidential issuances (Administrative Orders, Proclamations, Memorandum Circulars) | President | Numbering restarts with each president: "Executive Order No. 21, s. 2023". | `presidential regulation` |
| 4a | **DOE Department Circular (DC)** | Secretary of Energy | `DCYYYY-MM-NNNN`: year, month, then a sequence number that runs through the year (e.g. DC2023-06-0021). Suffixes such as `-1` mark re-issued copies (DC2021-06-0015-1). Implementing rules (IRRs) of laws are issued as DCs (RE Act IRR = DC2009-05-0008). WESM Rules and Market Manuals are adopted and amended by DC. | `circular` |
| 4b | **ERC Resolution** | ERC (collegial body) | "Resolution No. 13, Series of 2024" (cited "Res. 13 s.2024"). Adopts rules, codes (Grid Code, Distribution Code), price methods and ceiling prices. | `decision` |
| 4c | **DOE Department Order (DO)** | Secretary of Energy | `DOYYYY-MM-NNNN`. Mostly internal (committees, delegations), but some direct NEA or utilities (e.g. DO2023-10-0022 on joint CSP for gas supply). | probably `decision` |
| 4d | Joint circulars and resolutions (DOE-ERC-NEA, DOE-DENR), NEA Memoranda, DENR Administrative Orders | Several agencies | Own series, e.g. NEA Memo No. 2023-57; DENR AO 2024-02 (offshore wind ECCs). | `circular` / `decision` |
| 5 | **DOE Advisories**, notices, FAQs | DOE | Usually unnumbered and dated (e.g. the 2020 and 2025 coal moratorium advisories). | none fits well (see section 5) |
| (other) | **ERC Decisions and Orders** in docketed cases | ERC | "ERC Case No. YYYY-NNN RC" (format from general knowledge, not checked). Approves PSAs, rates and GEA prices for specific parties. | out of scope for now |
| (other) | **DOJ Opinions**, Supreme Court decisions | DOJ / SC | "DOJ Opinion No. 21, s. 2022"; "G.R. No. …" | out of scope; mention in notes |

Notes on validity. Under the Administrative Code of 1987, agency rules take effect only after filing with the UP Law Center's **Office of the National Administrative Register (ONAR)** and publication. The DOE circulars we read nearly all say "fifteen (15) days after publication in at least two newspapers of general circulation" and require filing with ONAR. Since 2025 several have been published in the Official Gazette. Two consequences:

- The signing date and the date in force always differ.
- NARO, the online version of the register, is a useful check that we have not missed a rule.

## 3. Official sources

Fetched 2026-11-04 with a desktop user agent through the session proxy. A 403 here may be bot protection rather than a real block; most of these sites will open in a normal browser.

| Portal | URL | What it holds | Listing or search | Language | Fetch result |
| --- | --- | --- | --- | --- | --- |
| **DOE (new site)** | https://doe.gov.ph/laws-and-issuances/issuances | Department Circulars (year pages for 2013 and 2020 to 2026) and Department Orders (2002 to 2026). A detail page for each circular holds part of the text, where it was published, the publication date and the PDF. | Year listings at `/laws-and-issuances/issuances/{year}?page=N`, rendered on the server. Detail pages at `/circular-no-dc-YYYY-MM-NNNN`. PDFs on a CloudFront domain (`d24qbtp4vooyzi.cloudfront.net/api/media/file/...`). Site search runs in the browser (empty HTML). | English | **200**, scrapeable. Problems: (a) 16 of 23 PDFs we downloaded had no text layer and needed OCR. (b) No year pages for 2014-2019, so most 2017-2019 circulars (RPS, GEOP, CSP) are missing. (c) The 2022 and 2023 listings look incomplete (we saw 17 of the 38 numbers in 2023). (d) Some detail pages carry another circular's title (DC2024-03-0009, DC2023-12-0035). (e) Old `/node/NNNN` links return a "Page Not Found" page with HTTP **200**, so link checkers will not catch them. |
| DOE (old site) | https://legacy.doe.gov.ph/ | Pre-2025 site: circulars from before 2020, advisories, PEP and PDP PDFs, drafts for comment. Search engines still index it heavily. | Drupal nodes and tag pages | English | Could not connect (**proxy CONNECT 502**). It may be down or blocked only for us; try from a browser. |
| DOE document store | https://prod-cms.doe.gov.ph/ | Drafts and attachments | none seen | English | **403** |
| **UP Law Center NARO** (official register of administrative rules) | https://naro.law.upd.edu.ph/ | Rules filed with ONAR: DOE DCs, **ERC Resolutions**, NEA, DENR and others. Each record has the number, title, agency, **date issued**, **date filed**, a registration number and the official copy. | Search at `/search?q=…`, records at `/issuances/{id}`; agency directory and bulletins | English | **200**, scrapeable. Our searches found only 2023-2025 issuances ("8,233 issuances, 3 volumes"), so older rules may not be there. It is our best way into ERC resolutions while the ERC site is blocked. |
| **ERC** | https://www.erc.gov.ph/ | Resolutions, decisions, orders, case dockets, rates | Has issuance pages (not seen) | English | **403** (Cloudflare "Just a moment" challenge) |
| **Lawphil** (Arellano Law Foundation, not government but the standard reference) | https://lawphil.net/ | RAs, EOs, SC decisions | Year indexes: `/statutes/repacts/raYYYY/raYYYY.html`; RA pages `ra_NNNN_YYYY.html`; EOs `/executive/execord/eoYYYY/eo_NN_YYYY.html` | English | **200**, scrapeable; approval dates in the text |
| **Supreme Court E-Library** | https://elibrary.judiciary.gov.ph/ | RAs, executive issuances (including some DOE circulars and joint resolutions, e.g. DC2017-12-0015 at `showdocs/10/89908`), SC decisions | Browsing ("bookshelf"); no search tried | English | **200** |
| Official Gazette | https://www.officialgazette.gov.ph/ | Official publication of laws, EOs and (since 2025) some DCs | Date-based URLs | English | **403** |
| Senate legislative records | https://ldr.senate.gov.ph/ | Bills, such as the EPIRA amendment bills | Search | English | **403** |
| House of Representatives | https://www.congress.gov.ph/ | Bills | Search | English | **403** |
| IEMOP (WESM market operator) | https://www.iemop.ph/ | WESM Rules and Manuals, market reports, copies of DOE and ERC issuances (e.g. DC2023-01-0004 and ERC Res. 08 s.2021 PDFs) | Yes | English | **200** |
| WESM / PEMC | https://www.wesm.ph/ | Market governance | not explored | English | **200** |
| NGCP | https://www.ngcp.ph/ | Transmission Development Plan, grid data | not explored | English | **403** |
| TransCo | https://www.transco.ph/ | Transmission asset owner | not explored | English | **200** |
| NEA | https://www.nea.gov.ph/ | Electric cooperative rules and memos | not explored | English | **403** |
| FOI portal | https://www.foi.gov.ph/agencies/doe/ | Requests to the DOE (useful for missing texts) | Yes | English | not fetched |

Secondary sources we leaned on, which also serve as a check during review:

- News: Manila Bulletin, BusinessWorld, Inquirer, Philstar, PowerPhilippines
- Law firms: Baker McKenzie, DFDL, Cruz Marcelo
- Unofficial legal databases: Lawyerly, jur.ph (rate-limited, 429)
- Legal databases kept by ADB and Climate Change Laws of the World

## 4. Key rules since about 2017, by topic

Format for each rule: number · title · issuer · date · what it does · what it amends or revokes · status · source · confidence. ★ marks rules that are in the CSV. Rules without a ★ are worth adding but were not confirmed well enough, or were cut to keep the CSV to 30 rows.

### framework-law

- ★ **RA 9136** · Electric Power Industry Reform Act (EPIRA) · Congress · 2001-06-08 · Restructures the sector, creates ERC, WESM, PSALM and TransCo, opens generation and supply to competition, and sets RCOA (Sec. 31) · Status: amended (lifeline rate only) · https://lawphil.net/statutes/repacts/ra2001/ra_9136_2001.html · high
- RA 10150 · lifeline rate extension · Congress · 2011-06-21 · Amends EPIRA Sec. 73 · https://lawphil.net/statutes/repacts/ra2011/ra_10150_2011.html · high (not in CSV)
- ★ **RA 11552** · lifeline rate extension · Congress · 2021-05-27 · Amends EPIRA Sec. 73 as amended by RA 10150 · in force · https://lawphil.net/statutes/repacts/ra2021/ra_11552_2021.html · high
- ★ **RA 9513** · Renewable Energy Act of 2008 · Congress · 2008-12-16 · Basis for RPS, FIT, GEOP and net metering · in force · https://lawphil.net/statutes/repacts/ra2008/ra_9513_2008.html · high
- ★ **DC2022-11-0034** · amends Sec. 19 of the RE Act IRR (DC2009-05-0008) · DOE · 2022-11-15 · Allows 100% foreign ownership of solar, wind, hydro and ocean projects, following DOJ Opinion 21 s.2022 · in force · Baker McKenzie note; official text not reached · medium
- DC2025-09-0014 · further amendments to the RE Act IRR (new definitions, e.g. "Emerging RE Technologies") · DOE · 2025-09-04 (OCR "SEP 4 2025") · https://doe.gov.ph/circular-no-dc-2025-09-0014 · medium (not in CSV)
- RA 11659 · Public Service Act amendments (narrows what counts as a "public utility") · 2022-03-21 · https://lawphil.net/statutes/repacts/ra2022/ra_11659_2022.html · high on the date; its effect on power not analysed (not in CSV)
- Other laws that touch power (not in CSV):
  - RA 11234 EVOSS Act (one-stop permitting), 2019-03-08
  - RA 11361 Anti-Obstruction of Power Lines Act, 2019-08-08
  - RA 11646 Microgrid Systems Act, 2022-01-21
  - RA 12120 Philippine Natural Gas Industry Development Act, 2025-01-08
  - RA 12305 Philippine National Nuclear Energy Safety Act (creates PhilATOM), 2025-09-18

  All are on Lawphil; high.
- **EPIRA amendment bills:** still pending as of 2026-07. The President called again for amendments in his 2026 State of the Nation Address, and new Senate bills target system-loss charges. In 2025-03 the ERC said the House bill was at second reading and the Senate bill still in committee. No enacted amendment found, and there are no rows for drafts.

### captive-power

- ★ **DC2026-08-0017** · Policy Guidelines for Self-Generating Facility Zero-Export Solar Systems and Micro-Solar Systems for Own-Use · DOE · 2026-08 · Simpler rules for own-use solar that does not export; asks the ERC for rules within 90 days · in force · https://doe.gov.ph/circular-no-dc-2026-08-0017 · high
- EPIRA allows self-generation facilities without a generation licence; they need an ERC Certificate of Compliance. ERC Res. 14 s.2024 sets strategies for approving COCs of generation companies, self-generating facilities and distributed energy resources (NARO https://naro.law.upd.edu.ph/issuances/5690). Medium; not in CSV.
- DC2025-04-0008 · revised rules for direct connection of industrial and commercial end-users to the grid · DOE · 2025-04 · https://doe.gov.ph/circular-no-dc-2025-04-0008 · medium on content (title only); not in CSV. It appears to revise DC2020-01-0001 (same subject); the text was not checked.
- The 2025 coal advisory exempts own-use coal in some cases (see coal-phase-out).

### wheeling-dppa

There is no "wheeling" rule as such. Open access runs through **RCOA** (contestable customers choose a retail supplier and pay wheeling charges to the utility and NGCP), the **GEOP** (the renewables-only version), and now **VPPAs**.

- ★ **DC2018-07-0019** · GEOP Rules · DOE · 2018-07-18 · End-users of 100 kW and above may buy from an RE supplier · revoked by DC2026-01-0002 · secondary copy https://dev.lawyerly.ph/laws/90979 · high
- DC2020-04-0009 · operating permits for RE suppliers under GEOP · DOE · 2020-04-22 · revoked by DC2026-01-0002 · https://doe.gov.ph/circular-no-dc-2020-04-0009 · high (not in CSV)
- ERC Res. 08 s.2021 · A Resolution Adopting the Green Energy Option Program · ERC · 2021-04-22 (recital in DC2026-01-0002) · copy on IEMOP · medium (not in CSV)
- DC2023-01-0004 · WESM and Retail Rules amendments and the Retail Manual for GEOP · DOE · 2023-01-31 (NARO) · not in CSV
- ★ **DC2024-03-0009** · commercial operation of RCOA and GEOP in Mindanao · DOE · 2024-03-01 · Start date 2024-03-26 · in force · high
- ★ **ERC Res. 13 s.2024** · Omnibus Rules for Customer Choice Programs in the Retail Market · ERC · 2024-08-14 · Consolidates RCOA and GEOP rules · in force · https://naro.law.upd.edu.ph/issuances/4928 · high
- ★ **DC2026-01-0002** · Revised GEOP Rules · DOE · 2026-01 · Threshold cut to 50 kW with annual review toward lower levels · revokes DC2018-07-0019 and DC2020-04-0009 · in force · high
- ★ **DC2025-10-0024** · Guidelines on Virtual Power Purchase Agreements · DOE · 2025-10-29 · Financial contracts for voluntary RECs, recognised as PPAs for financing · in force · high
- Background: DC2012-05-0005 started RCOA on 2012-05-09 (recital in DC2024-03-0009). Current contestability thresholds not confirmed.

### rooftop-solar

- ERC Res. 9 s.2013 · original Net-Metering Rules · ERC · 2013-05-27 (recital) · not in CSV
- ★ **ERC Res. 06 s.2019** · Amended Net-Metering Rules · ERC · 2019-08-16 · amended by Res. 15 s.2025 · medium (ERC text not seen)
- ★ **DC2020-10-0022** · Enhancing the Net-Metering Program · DOE · 2020-10-22 · amended · high
- ★ **DC2024-08-0025** · further net-metering policies (credit banking, REC meter) · DOE · 2024-08-19 · amends DC2020-10-0022 · high
- ★ **ERC Res. 15 s.2025** · amending Res. 06 s.2019 · ERC · 2025-08-27 · medium (known only from the DOE recital)
- ★ **DC2025-10-0020** · net metering with REC trading and multi-site or aggregate net metering · DOE · 2025-10 · supplements DC2020-10-0022 · high
- ★ **DC2023-12-0035** · Expanded Roof-Mounted Solar Program (ERSP) · DOE · 2023-12 · Rooftop leasing and third-party business models; counts toward Energy Efficiency Act compliance · in force · high
- ★ **DC2026-08-0017** (see captive-power)
- Net metering is capped at 100 kW under the RE Act rules. A House bill to lift the cap was reported, but there is no sign it was enacted.

### tariffs-ppa

- ★ **DC2018-02-0003** · CSP for distribution utilities' PSAs for the captive market · DOE · 2018-02 · revoked by DC2023-06-0021 (once the ERC guidelines take effect) · medium
- ★ **DC2023-06-0021** · Mandatory CSP by distribution utilities · DOE · 2023-06-30 · repeals DC2015-06-0008, DC2018-02-0003, DC2021-09-0030 and DC2022-06-0027 once the ERC guidelines take effect · amended · high
- ERC Res. 16 s.2023 · the ERC's CSP and PSA guidelines that go with it (via NEA Memo 2023-57 on NARO) · medium on the number; date not found (not in CSV)
- ★ **DC2025-10-0022** · enhanced procurement by distribution utilities, amending DC2023-06-0021 · DOE · 2025-10 · high
- ERC Res. 12 s.2024 · cost recovery for distribution utilities' RPS compliance · ERC · 2024-04-23 · https://naro.law.upd.edu.ph/issuances/4927 · high (not in CSV)
- ★ **RA 11552** (lifeline rate, see framework-law)

### re-pricing

- ★ **DC2017-12-0015** · RPS On-Grid Rules · DOE · 2017-12-22 · amended · SC E-Library · high
- DC2022-09-0030 · raises the annual RPS increment from 1% to 2.52% from 2023 · DOE · 2022-09-23 (news) · medium (not in CSV)
- ★ **DC2023-05-0015** · amendments to the RPS On-Grid Rules · DOE · 2023-05-23 · NARO · high. Also DC2023-05-0014 for off-grid RPS (same date) and DC2023-12-0032 on sanctions for RPS breaches (2023-12-07).
- ★ **DC2020-07-0017** · first GEA guidelines · DOE · 2020-07 · revoked by DC2021-11-0036 · high
- ★ **DC2021-11-0036** · Revised GEAP Guidelines · DOE · 2021-11-03 · amended by DC2023-09-0027 (2023-09-26) and DC2025-03-0004 (2025-03-07) · high
- ★ **DC2023-10-0029** · GEA rules for non-FIT technologies · DOE · 2023-12-12 · amended by DC2024-03-0010 (2024-03-25) and DC2024-09-0028 (2024-09-10) · high
- ERC price rules (not in CSV):
  - Res. 06 s.2023, GEAR prices for GEA-2 (2023-06-14)
  - Res. 19 s.2024, price method for non-FIT GEA (2024-12-17)
  - Res. 06 s.2025, collection of the GEA allowance (2025-01-08)

  All from NARO; high. GEA-4 and GEA-5 GEAR prices come only from news (offshore wind PHP 11.00/kWh, 2026-02). DC2026-09-0020 resets GEA-5 for offshore wind (title only).
- Feed-in tariffs (2010s ERC FIT rates) not researched; pre-2017.

### coal-phase-out

- ★ **Coal moratorium advisory** · DOE · announced 2020-10-27; written advisory dated 2020-12-22 (news) · Stops DOE endorsements for greenfield coal plants · amended by the 2025 clarification · medium
- ★ **Clarification of coverage** · DOE advisory · 2025-10-14 · Exempts own-use, off-grid, critical-mineral and some on-grid shortfall projects · in force · medium. CEED and others criticised it; the DOE said in 2026-05 that the moratorium stays.
- DC2023-07-0022 · guidelines on decommissioning and mothballing generating units · DOE · 2023-07 · https://doe.gov.ph/circular-no-dc-2023-07-0022 · medium; content not read (not in CSV)
- No coal retirement or phase-out plan found. Climate Action Tracker notes the PEP has no coal phase-out.

### power-plans and energy-strategy

- ★ **PEP 2023-2050** · DOE · 2023 (revised edition reported 2024-07) · Clean energy scenario: 35% RE by 2030 and 50% by 2040; nuclear and offshore wind options · medium
- PDP 2023-2050 · DOE · date not confirmed · https://legacy.doe.gov.ph/node/27881 (not fetched) · low (not in CSV). EPIRA Sec. 37 requires the DOE to update the PDP every year, which raises the "plans replacing plans" question again.
- ★ **DC2026-02-0005** · categorising energy resources in the energy mix · DOE · 2026-02 · Governs how the PDP is prepared and how utilities' supply procurement plans and distribution development plans align · medium
- ★ **EO 21, s. 2023** · framework for offshore wind development · President · 2023-04-19 · high. Implemented by DC2023-06-0020 (2023-06-16, NARO).
- Also (not in CSV):
  - DC2025-10-0019, framework for adding nuclear power to the generation mix (published 2025-10-03)
  - DC2025-11-0026 and later amendments, waste-to-energy framework
  - DC2026-06-0013, mid-merit gas capacity auction
  - RA 11285 Energy Efficiency and Conservation Act, 2019-04-12
  - National Renewable Energy Program 2020-2040 (not checked)

### grid-market-rules

- ★ **DC2026-01-0001** · lets generation companies finance and build the transmission links their plants need · DOE · 2026-01-07 · high. DC2026-02-0007 does the same for TransCo.
- Market milestones, all from the DOE site (not in CSV):
  - DC2021-06-0015, start of the enhanced WESM design
  - DC2021-10-0032, Renewable Energy Market manual
  - DC2022-10-0031, preferential dispatch for all RE (2022-10-05)
  - DC2022-12-0039, WESM in Mindanao
  - DC2023-04-0008, energy storage policy (2023-04-20, NARO), amended by DC2026-02-0008
  - DC2023-09-0026, reserve market starts operating
  - DC2026-02-0006, Power Generator Accountability Policy
- The **WESM Rules and Manuals** are amended by DC several times a year (the DOE listing shows 5 WESM circulars in 2020 and at least 15 in 2021). The Grid Code and Distribution Code are ERC resolutions; not researched.

### carbon-pricing

- No carbon tax or emissions trading law found. Bills were not checked.
- EO 174, s. 2014 · Philippine GHG Inventory Management and Reporting System · 2014-11-24 · https://lawphil.net/executive/execord/eo2014/eo_174_2014.html · high (not in CSV; before 2017)
- DC2025-10-0025 · Guidelines on Energy Certificates (classes of certificates and trading, framed around the Paris Agreement, the NREP and the RPS) · DOE · 2025-10 · high on the title; not in CSV

## 5. Fit with our schema

**Where it fits:**

- Laws, EOs, DOE circulars and ERC resolutions each have a stable number, an issuer, a signing date and an English title. They also have explicit **repealing clauses** that often name the earlier rules (DC2021-11-0036 repeals DC2020-07-0017; DC2026-01-0002 repeals DC2018-07-0019 and DC2020-04-0009; DC2023-06-0021 repeals four CSP circulars). So `amends` and `revokes` can usually come from the text rather than be inferred.
- `date_signed` differs from `date_in_force`, usually by 15 days after publication. The DOE detail pages give the publication date, so `date_in_force` can be derived.
- `language` is always `en`, so no `title_original` translation is needed (`title_original` = `title_english`).

**Where it does not fit:**

1. **ERC resolutions mapped to `decision`.** This works, but it hides the fact that the ERC is an independent regulator issuing binding rules on the same level as DOE circulars. We could add a `resolution` doc_type, or rely on `issuing_body`.
2. **ERC cases and dockets.** Rate cases, PSA approvals and auction results are decisions for named parties. They matter (they set actual tariffs) but are not rules. Keep them out and link to them in notes.
3. **DOE advisories.** The coal moratorium, arguably the country's most important coal rule, exists only as unnumbered advisories. This is the same problem as party resolutions in Vietnam. We would need a new id pattern (we used `PH-ADV-DOE-2020-COAL`) and perhaps an `advisory` doc_type.
4. **Conditional repeal.** DC2023-06-0021 repeals the earlier CSP circulars only "upon the effectivity of the ERC guidelines". `revokes` has no effective date, so this needs a note or a `revoked_on` field.
5. **"Supplements" versus "amends".** Many DCs "supplement" an earlier circular without amending its text (e.g. DC2025-10-0020 on net metering). We have recorded these as `amends`; reviewers should agree a convention.
6. **WESM Rules as a living document.** One row per WESM amendment would swamp the dataset. Two options: one row for "WESM Rules (as amended)" with amendments listed in notes, or rows for milestone circulars only.
7. **Plans.** The PEP and PDP are updated often (the PDP by law every year). Their adoption dates are unclear and they are not signed instruments. This is the same "plans replacing plans" issue as RUPTL and PDP8.
8. **Drafts.** The DOE publishes many draft circulars for comment (often on the old site), and some are cited by number before they are final (e.g. the RPS amendment). They should stay out of `rules.csv`; a phase 4 scan could track them as "pending".
9. **Franchise laws.** Dozens of RAs a year grant or renew distribution franchises (e.g. RA 12146, Meralco's renewal). Include only major ones (Meralco, NGCP) or exclude them.
10. **IRR identity.** The RE Act IRR (DC2009-05-0008) is amended by later DCs. That chain works, but the IRR row would come before 2017 and before our scope.

## 6. Candidate partner institutes and reviewers

Names and URLs only; none has been contacted.

- Institute for Climate and Sustainable Cities (ICSC): https://icsc.ngo/
- Center for Energy, Ecology, and Development (CEED): https://ceedphilippines.com/
- UP Diliman Electrical and Electronics Engineering Institute: https://eee.upd.edu.ph/
- Philippine Institute for Development Studies (PIDS): https://pids.gov.ph/
- IEEFA (has published on the Philippine coal moratorium): https://ieefa.org/
- Ember (Philippines page): https://ember-energy.org/countries-and-regions/philippines/
- UP Law Center, Office of the National Administrative Register (as a data source, not a reviewer): https://naro.law.upd.edu.ph/
- Not confirmed (sites did not respond): the UP Energy Policy and Development Program (epdp.ph) and the Manila Observatory (observatory.ph).

## 7. Risks and open questions

1. **ERC access.** The ERC site is behind Cloudflare and blocks scripts. NARO covers 2023 onward; for older ERC rules we need manual downloads, IEMOP copies or help from a partner. Without this, half of each topic stays unverified.
2. **OCR.** Most DOE PDFs are scans. OCR quality was fine for dates and repeal clauses, but it garbles numbers (e.g. "DC2O24", "'15"). Every OCR-derived field needs a human check, and the phase 4 scanner needs Tesseract or similar.
3. **Link rot.** The DOE moved to a new site in 2025-26. Old `node/NNNN` URLs now return a "Page Not Found" page with HTTP 200, so our link checker would pass them. The old site was unreachable for us. We should save copies of source PDFs (phase 2 item 3) from the start.
4. **DOE metadata errors.** Some detail pages show the wrong title, and the year listings have gaps (2014-2019 missing; 2022 and 2023 incomplete). NARO and the PDFs should be the authority, not the listing.
5. **Volume.** Roughly 25 to 40 DOE circulars a year across all subsectors (highest sequence numbers seen: 26 in 2020, 36 in 2021, 38 in 2023, 30 in 2024, 29 in 2025, 22 by 2026-10), plus ERC resolutions. A scope rule is needed: power sector only, and no WESM manual tweaks.
6. **Open facts to check:**
   - the exact title and text of both coal advisories
   - signing days for the DCs where we have only the month
   - whether ERC Res. 13 s.2024 superseded Res. 08 s.2021
   - whether DC2023-06-0021's repeal of DC2018-02-0003 has taken effect (ERC Res. 16 s.2023 date and effectivity)
   - DC2024-03-0010's real title (NARO and the DOE site disagree)
   - PEP and PDP adoption dates
   - current RCOA contestability thresholds
   - GEA-4 and GEA-5 ERC resolution numbers
7. **Legal-political churn.** EPIRA amendments may pass in the 20th Congress and could change the framework, for example on system-loss charges or ERC powers. Foreign ownership in RE rests on a DOJ opinion and a DOE circular rather than a law, so it could be challenged; we found no court case.
8. **Coordination.** Check overlap with existing trackers, as with SIPET and NewClimate, and with Philippine groups such as ICSC that already publish policy timelines.

## 8. Sources

Official and primary:

- https://doe.gov.ph/
- https://doe.gov.ph/laws-and-issuances/issuances
- https://doe.gov.ph/laws-and-issuances/issuances/2013 (and the 2020 to 2026 year pages, with `?page=1` and `?page=2`)
- DOE circular pages (each also links its PDF):
  - https://doe.gov.ph/circular-no-dc-2020-04-0009
  - https://doe.gov.ph/circular-no-dc-2020-07-0017
  - https://doe.gov.ph/circular-no-dc-2020-10-0022
  - https://doe.gov.ph/circular-no-dc-2021-11-0036
  - https://doe.gov.ph/circular-no-dc-2023-06-0021
  - https://doe.gov.ph/circular-no-dc-2023-07-0022
  - https://doe.gov.ph/circular-no-dc-2023-09-0027
  - https://doe.gov.ph/circular-no-dc-2023-10-0029
  - https://doe.gov.ph/circular-no-dc-2023-12-0032
  - https://doe.gov.ph/circular-no-dc-2023-12-0035
  - https://doe.gov.ph/circular-no-dc-2024-03-0009
  - https://doe.gov.ph/circular-no-dc-2024-08-0025
  - https://doe.gov.ph/circular-no-dc-2025-03-0004
  - https://doe.gov.ph/circular-no-dc-2025-09-0014
  - https://doe.gov.ph/circular-no-dc-2025-10-0019
  - https://doe.gov.ph/circular-no-dc-2025-10-0020
  - https://doe.gov.ph/circular-no-dc-2025-10-0022
  - https://doe.gov.ph/circular-no-dc-2025-10-0024
  - https://doe.gov.ph/circular-no-dc-2025-10-0025
  - https://doe.gov.ph/circular-no-dc-2026-01-0001
  - https://doe.gov.ph/circular-no-dc-2026-01-0002
  - https://doe.gov.ph/circular-no-dc-2026-02-0005
  - https://doe.gov.ph/circular-no-dc-2026-02-0006
  - https://doe.gov.ph/circular-no-dc-2026-08-0017
- DOE PDF example: https://d24qbtp4vooyzi.cloudfront.net/api/media/file/dc2020-10-0022.pdf?prefix=dev%2Fmedia
- https://doe.gov.ph/node/26616 and https://doe.gov.ph/node/16477 (both now "Page Not Found" with HTTP 200)
- https://doe.gov.ph/PEP (also "Page Not Found")
- https://doe.gov.ph/bureaus/eppb
- https://doe.gov.ph/search?q=moratorium
- Old DOE site (indexed, not reachable for us):
  - https://legacy.doe.gov.ph/ducsp
  - https://legacy.doe.gov.ph/node/22837
  - https://legacy.doe.gov.ph/node/9134
  - https://legacy.doe.gov.ph/node/27881
  - https://legacy.doe.gov.ph/node/24251
  - https://legacy.doe.gov.ph/node/12478
  - https://legacy.doe.gov.ph/sites/default/files/pdf/pep/PEP%202023-2050%20Vol.%20I.pdf
- https://doe.gov.ph/sites/default/files/pdf/announcements/draft-dc-adopting-amendments-on-rps-on-grid-rules.pdf (draft; seen in search only)
- NARO register:
  - https://naro.law.upd.edu.ph/
  - https://naro.law.upd.edu.ph/search
  - issuance records 418, 920, 940, 1248, 1249, 1306, 1360, 1409, 1448, 2214, 2216, 2560, 2785, 2958, 3644, 3852, 4202, 4927, 4928, 5047, 5690, 5821, 6803, 7927, 7934, each at `https://naro.law.upd.edu.ph/issuances/{id}`
- Lawphil:
  - https://lawphil.net/statutes/repacts/ra2001/ra_9136_2001.html
  - https://lawphil.net/statutes/repacts/ra2008/ra_9513_2008.html
  - https://lawphil.net/statutes/repacts/ra2011/ra_10150_2011.html
  - https://lawphil.net/statutes/repacts/ra2019/ra_11234_2019.html
  - https://lawphil.net/statutes/repacts/ra2019/ra_11285_2019.html
  - https://lawphil.net/statutes/repacts/ra2019/ra_11361_2019.html
  - https://lawphil.net/statutes/repacts/ra2021/ra_11552_2021.html
  - https://lawphil.net/statutes/repacts/ra2022/ra_11646_2022.html
  - https://lawphil.net/statutes/repacts/ra2022/ra_11659_2022.html
  - https://lawphil.net/statutes/repacts/ra2025/ra_12120_2025.html
  - https://lawphil.net/statutes/repacts/ra2025/ra_12305_2025.html
  - https://lawphil.net/statutes/repacts/ra2024/ra2024.html
  - https://lawphil.net/statutes/repacts/ra2025/ra2025.html
  - https://lawphil.net/statutes/repacts/ra2026/ra2026.html
  - https://lawphil.net/executive/execord/eo2023/eo_21_2023.html
  - https://lawphil.net/executive/execord/eo2014/eo_174_2014.html
- Supreme Court E-Library:
  - https://elibrary.judiciary.gov.ph/
  - https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/10/89908
  - https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/10/91991
- Status checks only (403 or not explored):
  - https://www.erc.gov.ph/
  - https://www.erc.gov.ph/Issuances
  - https://www.erc.gov.ph/ContentPage/62
  - https://www.officialgazette.gov.ph/
  - https://www.officialgazette.gov.ph/2023/04/19/executive-order-no-21-s-2023/
  - https://ldr.senate.gov.ph/
  - https://www.congress.gov.ph/
  - https://www.ngcp.ph/
  - https://www.nea.gov.ph/
  - https://psa.gov.ph/
  - https://prod-cms.doe.gov.ph/
  - https://www.wesm.ph/
  - https://www.iemop.ph/
  - https://www.transco.ph/
- IEMOP copies:
  - https://iemop.ph/wp-content/uploads/2023/10/RCOA-GEOPP-1.0_26Feb2023_DC2023-01-0004_GEOP_fin.pdf
  - https://iemop.ph/wp-content/uploads/2023/10/Resolution-No.-08-Series-of-2021-AnnexA2020-005RM-GEOP.pdf
- https://www.foi.gov.ph/agencies/doe/

Secondary (news, law firms, databases):

- https://mb.com.ph/2020/10/27/doe-enforces-moratorium-on-new-coal-power-developments
- https://mb.com.ph/2021/01/12/doe-excludes-expansion-projects-in-coal-moratorium
- https://alpha.pna.gov.ph/articles/1119918 (seen in search; host blocked for fetching)
- https://mb.com.ph/2025/10/16/doe-eases-further-coal-moratorium-for-self-generating-critical-needs-projects
- https://context.ph/2025/10/17/doe-clarifies-exceptions-to-coal-plant-moratorium/
- https://ceedphilippines.com/think-tank-warns-vs-does-widening-of-coal-moratorium-exemptions/
- https://tribune.net.ph/2026/05/08/doe-shrugs-off-calls-to-ease-coal-ban-bets-bigger-on-re
- https://ieefa.org/resources/philippines-moratorium-coal-projects-will-attract-usd-30-billion-renewable-energy
- https://insightplus.bakermckenzie.com/bm/projects/philippines-renewable-energy-sector-is-now-open-to-full-foreign-ownership
- https://www.dfdl.com/insights/legal-and-tax-updates/philippines-doe-amends-re-act-implementing-rules-and-regulations-to-allow-full-foreign-equity-in-re-projects/
- https://mb.com.ph/2022/11/16/doe-opens-re-for-full-foreign-ownership
- https://www.bworldonline.com/economy/2023/04/20/518259/marcos-issues-order-to-expedite-rollout-of-offshore-wind-projects
- https://business.inquirer.net/?p=364989 (RPS 2.52%)
- https://context.ph/?p=5494 (RPS 2.52%)
- https://dev.lawyerly.ph/laws/90979 (DC2018-07-0019)
- https://dev.lawyerly.ph/laws/89908 (DC2017-12-0015)
- https://enviliance.com/regions/southeast-asia/ph/report_14953 (VPPA)
- https://mb.com.ph/2025/06/16/erc-sets-ceiling-prices-for-gea-4-renewable-projects
- https://mb.com.ph/2026/02/23/erc-sets-higher-11kwh-price-cap-for-offshore-wind-auction
- https://mb.com.ph/2025/09/25/marcos-signs-law-creating-nuclear-regulatory-body-bans-non-peaceful-use-of-atomic-energy
- https://www.philstar.com/business/2025/03/31/2432246/very-slim-chance-epira-amendments-year-erc/amp/
- https://mb.com.ph/2026/07/29/work-underway-on-proposed-amendments-to-epiramarcos
- https://newsinfo.inquirer.net/2272876/explainer-marcos-priority-bills-mentioned-in-his-2026-sona
- https://philstar.com/business/2023/09/01/2292834/energy-roadmap-now-includes-nuclear
- https://mbc.com.ph/2024/07/09/policy-notes-doe-philippine-energy-plan-2023-2050
- https://climateactiontracker.org/countries/philippines/policies-action/
- https://climate-laws.org/document/power-development-plan-2023-2050_06f0
- https://mb.com.ph/2023/10/9/erc-prescribes-2-tiered-review-process-for-auctioned-power-supply-deals
- https://cruzmarcelo.com/doe-eliminates-one-year-cap-on-net-metering-credit-roll-over-and-removes-renewable-energy-certificate-meter-requirement/
- Partner sites: https://icsc.ngo/, https://ceedphilippines.com/, https://eee.upd.edu.ph/, https://pids.gov.ph/, https://ieefa.org/, https://ember-energy.org/countries-and-regions/philippines/
