# Scouting report: Australia

Prepared 2026-11-19 for the Power Transformation Lab policy tracker. It comes with `au-rules.csv` (20 candidate rows), `au-country.csv` and `au-sources.csv`. Everything here is a lead for reviewers, not checked data. Where a fact rests only on news, a law-firm note or general knowledge, the row's notes say so.

How this was checked: Commonwealth Acts and instruments were looked up through the Federal Register of Legislation (FRL) public API (`api.prod.legislation.gov.au/v1/titles/search(...)`), which returned the register id, Act number, making date and in-force status for each title. Our page fetcher only saw tables of contents on FRL text pages, so the substance of each Act comes from those tables of contents plus secondary sources. ARENA program pages were read directly (HTTP 200). The DCCEEW, DISR (industry.gov.au, which also hosts the Anti-Dumping Commission) and FIRB sites did not respond to our client (HTTP 000 or 503).

## 1. Summary

- **Structure.** Australia is a federation. The Commonwealth legislates on tax, customs, foreign investment, emissions reporting and national programs. The states own or regulate most networks and run planning approvals and their own renewable schemes (e.g. the NSW Electricity Infrastructure Roadmap). The eastern and southern grids form the National Electricity Market (NEM), operated by AEMO under the National Electricity Law, with the AEMC making rules and the AER regulating networks. State instruments were not scouted; use `jurisdiction` = AU-NSW, AU-VIC etc. if added.
- **Supply-chain policy** sits under the *Future Made in Australia* (FMIA) agenda:
  - the **Future Made in Australia Act 2024** (No. 119 of 2024, 2024-12-10), which creates the National Interest Framework and community benefit principles and bars support for coal, oil and gas;
  - the **Production Tax Credits Act 2025** (No. 9 of 2025, 2025-02-14): the Hydrogen Production Tax Incentive and the Critical Minerals Production Tax Incentive, with a 2026 grid-matching instrument for hydrogen;
  - **ARENA programs**: Solar Sunshot (now up to A$850 million, three rounds open or closed), Battery Breakthrough Initiative (cut to A$142 million in the 2026 Budget and closed to new applications), Hydrogen Headstart (A$2 billion revenue support; Round 1 awarded to Murchison and Orica);
  - the **National Reconstruction Fund** (2023) and the **Critical Minerals Strategy 2023-2030** (2026 update), plus the **Critical Minerals Strategic Reserve**, given legal footing by the EFIC Amendment (Strategic Reserve) Act 2026 (No. 21 of 2026).
- **Investment screening** runs through the Foreign Acquisitions and Takeovers Act 1975 as amended by the Foreign Investment Reform (Protecting Australia's National Security) Act 2020. Critical-minerals-specific screening practice is in FIRB guidance and Treasurer statements, which we could not reach.
- **Trade.** No clean-tech-specific tariff instrument was found. The only trade remedy located is the anti-dumping measure on **wind towers** from China (2014, continued 2019 to 2024-04-16); whether it was continued after Inquiry 621 is unresolved.
- **Demand side and electricity.** Electric Car Discount FBT exemption (2022), New Vehicle Efficiency Standard (2024, from 2025-01-01), Capacity Investment Scheme (2023 instrument), Cheaper Home Batteries Program (2025), the 2015 LRET reduction, the Climate Change Act 2022 targets and the Safeguard Mechanism (2015 Rule, 2023 reforms).
- **Tracking difficulty: low for Commonwealth law, high for programs.** FRL is complete, structured and has an open API with ids, dates and status history. Programs (ARENA, CIS tenders, FMIA) are run through grant guidelines and agency web pages rather than legislative instruments, and several agency sites block automated clients.

## 2. Legal hierarchy and document types

| Rank | Type | Issuer | Numbering | Our `doc_type` |
| --- | --- | --- | --- | --- |
| 1 | Constitution | People | Sections (s. 51 heads of power) | (not tracked) |
| 2 | Act of Parliament | Parliament, Royal Assent | "Act No. N of YYYY"; FRL id C{YYYY}A{NNNNN} | law |
| 3 | Regulations (Governor-General) | Governor-General in Council | FRL id F{YYYY}L{NNNNN} | government regulation |
| 3 | Rules, determinations, instruments | Minister or agency | FRL id F{YYYY}L{NNNNN}; notifiable instruments F{YYYY}N{NNNNN} | ministerial regulation |
| 4 | Program guidelines, strategies | ARENA, departments | unnumbered | decision / plan |
| 4 | Anti-dumping notices | Minister / ADC | ADN YYYY/NNN | decision |
| - | State Acts and instruments | State parliaments and ministers | state registers | law / regulation with `jurisdiction` |

Amending instruments are shown on FRL as "Repealed" once spent (automatic repeal after commencement); rows for such instruments keep `in force` and say so in notes.

## 3. Official sources

| Name | URL | Tier | Languages | What it holds | Access observed |
| --- | --- | --- | --- | --- | --- |
| Federal Register of Legislation | https://www.legislation.gov.au/ | 1 | en | All Commonwealth Acts and instruments, compilations, status | HTTP 200; API open |
| ARENA funding pages | https://arena.gov.au/funding/ | 2 | en | Solar Sunshot, BBI, Hydrogen Headstart guidelines and dates | HTTP 200 |
| Clean Energy Regulator | https://www.cer.gov.au/ | 2 | en | Safeguard, RET, NGER | HTTP 200 |
| PM&C Critical Minerals Strategic Reserve | https://www.pmc.gov.au/domestic-policy/critical-minerals-strategic-reserve | 2 | en | Reserve design and legislation | HTTP 200 |
| DCCEEW | https://www.dcceew.gov.au/ | 2 | en | CIS, energy policy | unreachable (HTTP/2 stream error) |
| DISR (industry.gov.au) | https://www.industry.gov.au/ | 2 | en | Critical Minerals Strategy, battery strategy | unreachable (000 / 503) |
| Anti-Dumping Commission | https://www.industry.gov.au/anti-dumping-commission | 2 | en | Dumping Commodity Register, public record | unreachable (000 / 503) |
| FIRB | https://firb.gov.au/ | 2 | en | Foreign investment guidance | unreachable (000) |
| Future Made in Australia portal | https://futuremadeinaustralia.gov.au/ | 4 | en | Program summaries | HTTP 426 |
| Parliament (APH) | https://www.aph.gov.au/ | 4 | en | Bills, estimates documents | 403 on a tabled PDF |

## 4. Key instruments by category

**Electricity**
- Renewable Energy (Electricity) Amendment Act 2015 (No. 90 of 2015): LRET cut to 33,000 GWh (re-pricing).
- Capacity Investment Scheme Program Instrument 2023 (F2023L01481, amended 2024): revenue underwriting tenders for renewables and dispatchable capacity (re-pricing, energy-storage).
- Cheaper Home Batteries Program Regulations 2025 (F2025L00765): STC support for small-scale batteries from 2025-07-01 (rooftop-solar, energy-storage).

**Energy**
- Climate Change Act 2022 (No. 37 of 2022): 43% by 2030, net zero by 2050.
- Safeguard Mechanism: 2015 Rule (F2015L01637), Crediting Amendment Act 2023 (No. 14 of 2023), Reforms Rules 2023 (F2023L00528) (carbon-pricing).
- Electric Car Discount Act 2022 (No. 86 of 2022) and New Vehicle Efficiency Standard Act 2024 (No. 34 of 2024) (ev-adoption).

**Supply chain**
- Future Made in Australia Act 2024; Production Tax Credits Act 2025; HPTI grid matching instrument 2026 (manufacturing-incentives, mineral-downstreaming).
- Solar Sunshot, Battery Breakthrough Initiative, Hydrogen Headstart (manufacturing-incentives).
- National Reconstruction Fund Corporation Act 2023.
- Critical Minerals Strategy 2023-2030; EFIC Amendment (Strategic Reserve) Act 2026 (mineral-downstreaming).
- Foreign Investment Reform (Protecting Australia's National Security) Act 2020 (investment-rules).

**Trade**
- Wind towers from China: anti-dumping continuation ADN 2019/33 (trade-remedies). No import-tariff, import-standard or export-restriction instrument specific to clean tech was found.

## 5. Fit with the schema

- Commonwealth Acts and instruments map cleanly to `law`, `government regulation` and `ministerial regulation`; FRL ids make stable `number` values and could become an adapter.
- Grant programs (ARENA rounds, CIS tenders) have no legislative number; they are coded `decision` with "unnumbered (...)". The legal basis for spending is often a generic Industry Research and Development instrument (as for CIS and the Cheaper Home Batteries Program), which could be tracked instead.
- Spent amending instruments show as "Repealed" on FRL; we kept `in force` for amendments whose effect continues. The tracker needs a convention on this.
- Federal/state split: `jurisdiction` is needed for any state scheme (NSW Roadmap LTESAs, VIC renewable targets).
- `technologies` works well here (hydrogen, batteries, solar-pv are explicit in program names).

## 6. Risks and open questions

- Wind towers anti-dumping: the Minister's 2024 decision on Inquiry 621 was not found; `expired` is unconfirmed.
- Production tax incentive rates and periods (reported A$2/kg; 10% of processing costs; 2027-28 to 2039-40) were not read from the Act and were left out of summaries.
- FIRB critical minerals policy (2023-24 statements on investments in critical minerals by non-like-minded investors) not captured; FIRB site unreachable.
- Critical Minerals Strategy 2026 update and NVES amendment determination (F2026L01248) could be separate rows.
- Hydrogen Headstart Round 2 resizing and Solar Sunshot funding changes come partly from news.
- Commencement dates given only to month where s. 2 was not read.

## 7. Sources

- https://www.legislation.gov.au/ and API https://api.prod.legislation.gov.au/v1/titles/search
- https://www.legislation.gov.au/C2024A00119/asmade/text
- https://www.legislation.gov.au/C2025A00009/asmade/text
- https://www.legislation.gov.au/F2026L01000/asmade/text
- https://www.legislation.gov.au/C2026A00021/asmade/text
- https://www.legislation.gov.au/C2020A00114/asmade/text
- https://www.legislation.gov.au/C2023A00012/asmade/text
- https://www.legislation.gov.au/C2022A00037/asmade/text
- https://www.legislation.gov.au/F2015L01637/latest/text
- https://www.legislation.gov.au/C2023A00014/asmade/text
- https://www.legislation.gov.au/F2023L00528/asmade/text
- https://www.legislation.gov.au/C2022A00086/asmade/text
- https://www.legislation.gov.au/C2024A00034/asmade/text
- https://www.legislation.gov.au/F2023L01481/latest/text
- https://www.legislation.gov.au/C2015A00090/asmade/text
- https://www.legislation.gov.au/F2025L00765/asmade/text
- https://arena.gov.au/funding/solar-sunshot/
- https://arena.gov.au/funding/battery-breakthrough-initiative/
- https://arena.gov.au/funding/hydrogen-headstart/
- https://arena.gov.au/assets/2024/08/ARENA-Media-Release_Solar-Sunshot-Opening_3108024.pdf
- https://www.pmc.gov.au/domestic-policy/critical-minerals-strategic-reserve
- https://www.industry.gov.au/publications/critical-minerals-strategy-2023-2030
- https://www.industry.gov.au/sites/default/files/2026-10/critical-minerals-strategy-2023-2030-update-2026.pdf
- https://www.minister.industry.gov.au/ministers/king/media-releases/seizing-opportunities-australias-critical-minerals
- https://www.hsfkramer.com/es/notes/mining/2023-06/everything-you-need-to-know-about-australias-2023-critical-minerals-strategy
- https://www.mining.com/web/australia-passes-law-to-trade-stock-fuel-alongside-rare-earths
- https://www.industry.gov.au/node/87567
- https://www.industry.gov.au/sites/default/files/adrp/2019_100_report_combined_-_public.pdf
- https://www.industry.gov.au/sites/default/files/adc/public-record/2024-03/621_-_16_-_report_-_rep_621_-_final_report_-_rep_621.pdf
- https://www.industry.gov.au/sites/default/files/adc/public-record/2023-12/621_-_12_-_submission_-_applicant_-_kepple_prince_engineering_pty_ltd_-_response_to_statement_of_essential_facts.pdf
- https://www.energy-storage.news/arena-opens-consultation-into-au523-million-battery-breakthrough-initiative-in-australia
- https://arena.gov.au/news/murchison-green-hydrogen-project-given-a-headstart
- https://arena.gov.au/news/arena-backs-hunter-valley-renewable-hydrogen-project-with-432-million
- https://www.cer.gov.au/schemes/safeguard-mechanism
