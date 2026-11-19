# Scouting report: China

Prepared 2026-11-19 for the Power Transformation Lab policy tracker. It comes with `cn-rules.csv` (35 candidate rules, 32-column schema), `cn-country.csv`, `cn-sources.csv` and `cn-vocabulary.csv` (24 draft Chinese term rows). Everything here is a lead for reviewers, not checked data. Where a fact rests only on news, a law-firm note or a local government copy, the row's `notes` say so.

How this was checked: official portals were requested with `curl` (desktop user agent, through the session proxy); the status codes below come from those requests. Four official pages were read directly with WebFetch (NDRC Document 136, MOFCOM announcements 2025 No. 62 and 2026 No. 58, the MEE copy of the carbon trading regulations). Web searches filled the remaining gaps, mostly via official URLs (gov.cn, ndrc.gov.cn, mofcom.gov.cn, mee.gov.cn, miit.gov.cn, mof.gov.cn) and Xinhua. The national laws database (flk.npc.gov.cn) did not answer, so no law was read in its consolidated official copy.

---

## 1. Summary

- **Structure.** Laws are passed by the National People's Congress (NPC) or its Standing Committee (NPCSC) and promulgated by numbered presidential order; the State Council issues administrative regulations by numbered State Council order. Most operational energy policy is made by the **National Development and Reform Commission (NDRC)** and the **National Energy Administration (NEA)** through notices and guiding opinions with document numbers such as 发改价格〔2025〕136号. Carbon markets sit with the **Ministry of Ecology and Environment (MEE)**.
- **Electricity.** The Electricity Law (1995, last amended 2018) is dated; the **Energy Law** (Presidential Order No. 37, in force 2025-01-01) is now the umbrella law. Renewable pricing has moved from feed-in tariffs (to 2020) to grid parity (2021) and, with **Document 136** (signed 2025-01-27), to full market participation with a contract-for-difference-like "mechanism price" for new projects commissioned from 2025-06-01. The **Distributed PV Measures** (国能发新能规〔2025〕7号) replaced the 2013 rules. A **full revision of the Renewable Energy Law** had its first NPCSC reading on 2026-11-02.
- **Carbon pricing.** The national ETS runs under MEE's 2020 trial measures and the State Council's **Interim Regulations** (Order No. 775, in force 2024-05-01; amended by Order No. 843 of 2026-08-08). Steel, cement and aluminium were added from the 2024 compliance year (work plan of 2025-03-26).
- **Supply chain.** China's tools are mostly **upstream control and industry discipline**: a revised **Mineral Resources Law** (in force 2025-07-01), the **Rare Earth Management Regulations** (Order No. 785, in force 2024-10-01) with rare-earth quota measures (Order No. 71, 2025), MIIT's **PV manufacturing standard conditions** (2024 edition, non-binding), and VAT **export-rebate cuts** for PV and batteries (13% to 9% from 2024-12-01; PV rebate removed from 2026-04-01; battery rebate 6% in April-December 2026 and removed from 2027-01-01). Foreign investment is under the **Foreign Investment Law** (2020) and a negative list whose 2024 edition removed all manufacturing restrictions.
- **Trade: the densest category.** Under the **Export Control Law** (2020) and the **Dual-Use Items Regulations** (Order No. 792, in force 2024-12-01), MOFCOM and Customs have issued licensing controls on gallium and germanium (2023 No. 23), graphite (2023 No. 39), antimony (2024 No. 33), seven medium and heavy rare earths (2025 No. 18), and on 2025-10-09 a package covering lithium batteries and graphite anodes (No. 58), extraterritorial rare-earth items (No. 61) and rare-earth technologies (No. 62). That package was **suspended** on 2025-11-07 until 2026-11-10 and, by announcement 2026 No. 58, **until 2027-01-10**. The technology export catalogue restricts battery cathode and lithium extraction technology (2025 No. 28). Battery electric cars need an **export licence** from 2026-01-01. On imports, anti-dumping duties on US and Korean polysilicon were continued for five years from 2026-01-14.
- **Tracking difficulty: moderate.** Official portals are mostly open and server-rendered, and document numbers are regular. The difficulties are volume, frequent short-term suspensions and extensions (which the schema does not model directly), the national laws database being unreachable from this environment, and the gap between signing date and publication date for many notices.
- **Recommendation: worth adding, starting with the trade and supply-chain modules.** China is the reference case for export restrictions on clean-tech inputs, and the instruments are well documented in official Chinese sources.

## 2. Legal hierarchy and document types

| Rank | Type | Issuer | How it is numbered and cited | Our `doc_type` |
| --- | --- | --- | --- | --- |
| 1 | Constitution | NPC | Articles | (not tracked) |
| 2 | **法律 Law** | NPC or NPCSC, promulgated by presidential order | "中华人民共和国主席令第三十七号"; amending decisions "全国人民代表大会常务委员会关于修改《...》的决定" | `law` |
| 3 | **行政法规 Administrative regulation** | State Council | "国务院令第775号"; usually 条例 (regulations) or 暂行条例 (interim regulations) | `government regulation` |
| 4 | **部门规章 Departmental rules** | Ministries, alone or jointly, by numbered order | "生态环境部令第19号", "国家发展改革委 商务部令第23号", "工业和信息化部 ... 令第71号"; usually 办法 (measures) | `ministerial regulation` |
| 5 | **规范性文件 Normative documents** | NDRC, NEA and other ministries | Notices and guiding opinions numbered like 发改价格〔2025〕136号, 国能发新能规〔2025〕7号 (规 marks a normative document) | `circular` (notices, opinions); `ministerial regulation` where the document is a set of measures (办法) |
| 6 | **公告 Announcements** | MOFCOM with GAC, MOF with STA, MIIT | "商务部 海关总署公告2023年第23号"; numbered per issuer per year; export controls, tax rates, industry conditions | `decision` |
| 7 | **规划 Plans** | State Council, General Office, NDRC/NEA | Five-year plans and sector plans, issued by a numbered notice (国办发〔2020〕39号) | `plan` |
| 8 | **Party and State Council opinions** | CPC Central Committee and State Council | "中发〔2015〕9号" | `party resolution` (none recorded in this pass) |

Validity notes: laws and regulations state their own commencement date. Many NDRC/NEA notices state no effective date: we used the publication date and explained this in notes. Signing (成文) and publication (发布) dates often differ by one to six weeks (Document 136: signed 2025-01-27, published 2025-02-09). The 规 in a document number (发改能源规, 国能发新能规) marks a normative document, which usually has a validity period (often five years).

## 3. Official sources

Requested 2026-11-19 with `curl` through the session proxy (desktop user agent), unless stated.

| Name | URL | Tier | Languages | What it holds | Access result |
| --- | --- | --- | --- | --- | --- |
| State Council policy library and Gazette | https://www.gov.cn/zhengce/ | 1 | zh | State Council orders, Gazette, ministry document library | **200** (home page, server-rendered) |
| National Laws and Regulations Database | https://flk.npc.gov.cn/ | 1 | zh | Consolidated laws and regulations | **Failed**: no response within 20 s |
| National People's Congress | http://www.npc.gov.cn/ | 1 | zh, en | Laws, presidential orders, drafts | **200** home; WebFetch of an order page **503** |
| National administrative regulations database (MoJ) | https://xzfg.moj.gov.cn/ | 1 | zh | Current texts of regulations | not tried |
| NDRC | https://www.ndrc.gov.cn/ | 2 | zh | Pricing and energy notices, plans | **200**; notice page read |
| NEA | https://www.nea.gov.cn/ | 2 | zh | NEA normative documents | **200** |
| MOFCOM (and sub-sites aqygzj, exportcontrol, xkzj, policy) | https://www.mofcom.gov.cn/ | 2 | zh, en | Export control and trade announcements | **200**; two announcement pages read |
| MIIT | https://www.miit.gov.cn/ | 2 | zh | Orders, industry standard conditions | **200** |
| MEE | https://www.mee.gov.cn/ | 2 | zh | ETS rules, rules database | **200**; regulation page read |
| State Taxation Administration | https://www.chinatax.gov.cn/ | 2 | zh | Tax announcements | **200** |
| Ministry of Finance | https://www.mof.gov.cn/ | 2 | zh | Tax policy, tariff commission | gss.mof.gov.cn **502**; szs.mof.gov.cn not tried |
| General Administration of Customs | http://www.customs.gov.cn/ | 2 | zh | Customs announcements, tariff | **412** (bot protection) |
| Ministry of Natural Resources | http://www.mnr.gov.cn/ | 2 | zh | Mining rules | **503** |
| Ministry of Science and Technology | https://www.most.gov.cn/ | 2 | zh | Technology export catalogue | **200** but 157-byte response |
| IEA Policies database | https://www.iea.org/policies | 4 | en | Policy summaries | **403** |

Not tried: trb.mofcom.gov.cn (trade remedies), gss.mof.gov.cn tariff notices beyond the home page, provincial portals.

## 4. Key instruments by category

Row ids refer to `cn-rules.csv`.

### Electricity
- **framework-law**: Electricity Law, recorded through its 2018 amending decision (`CN-LAW-2018-23`); Renewable Energy Law 2009 amendment (`CN-LAW-2009-RE-AMEND`); revision draft 2026 (`CN-BILL-2026-RE`, draft). The Energy Law (`CN-LAW-2024-37`) is also tagged framework-law.
- **re-pricing**: Document 136 (`CN-CIRC-NDRC-2025-136`). Not recorded: grid-parity notice 发改价格〔2021〕833号 (2021-06, in force 2021-08-01); renewable consumption responsibility weights 发改能源〔2019〕807号 (2019-05-10).
- **rooftop-solar**: Distributed PV Measures 2025 (`CN-MR-NEA-2025-7`).
- **wheeling-dppa**: green certificate full coverage (`CN-CIRC-NDRC-2023-1044`); NEA certificate issuance and trading rules 国能发新能规〔2024〕67号 (2024-08-26) not recorded.
- **energy-storage**: guiding opinion on new-type storage (`CN-CIRC-NDRC-2021-1051`).
- **power-plans**: 14th FYP Modern Energy System Plan (`CN-PLAN-NDRC-2022-210`).
- Not recorded: electricity spot market basic rules 发改能源规〔2023〕1217号 (a 2026 replacement was reported in draft); coal capacity price 发改价格〔2023〕1501号 (in force 2024-01-01); 中发〔2015〕9号 power sector reform opinion (2015-03-15).

### Energy and climate
- **energy-strategy**: Energy Law (`CN-LAW-2024-37`); Modern Energy System Plan.
- **carbon-pricing**: Interim Regulations (`CN-GR-2024-775`, amended); ETS extension work plan (`CN-PLAN-MEE-2025-ETS-EXPANSION`). Not recorded: MEE Order No. 19 (2020 trial measures); CCER measures (MEE-SAMR Order No. 31, 2023-10-19, amended 2026-09-20); State Council Order No. 843 (2026).
- **ev-adoption**: NEV purchase tax 2023 No. 10 (`CN-DEC-MOF-2023-10`); NEV Industry Development Plan 2021-2035 (`CN-PLAN-SC-2020-39`). Not recorded: dual-credit measures (MIIT Order No. 53 of 2020, amended 2023-06-29); hydrogen industry plan 2021-2035 (2022-03-23).

### Supply chain
- **mineral-downstreaming**: Mineral Resources Law 2024 (`CN-LAW-2024-36`); Rare Earth Regulations (`CN-GR-2024-785`); rare earth quota measures (`CN-MR-MIIT-2025-71`); rare-earth and lithium items in the export control rows.
- **manufacturing-incentives**: PV standard conditions (`CN-DEC-MIIT-2024-33`, binding = no); export rebate rows (`CN-DEC-MOF-2024-15`, `CN-DEC-MOF-2026-2`); NEV plan. The lithium battery industry standard conditions (2024 edition) were found only as a draft and a local copy of the management measures; not recorded.
- **investment-rules**: Foreign Investment Law (`CN-LAW-2019-26`); negative list 2024 (`CN-MR-NDRC-2024-23`).
- **local-content**: none found at national level in this pass.

### Trade
- **export-restrictions**: Export Control Law (`CN-LAW-2020-58`); Dual-Use Regulations (`CN-GR-2024-792`); gallium and germanium, graphite, antimony, US-specific controls, medium and heavy rare earths, lithium batteries and anodes, extraterritorial rare earths, rare earth technologies (`CN-DEC-MOFCOM-2023-23`, `-2023-39`, `-2024-33`, `-2024-46`, `-2025-18`, `-2025-58`, `-2025-61`, `-2025-62`); suspension to 2027-01-10 (`CN-DEC-MOFCOM-2026-58`); technology export catalogue 2025 (`CN-DEC-MOFCOM-2025-28`); BEV export licensing (`CN-DEC-MOFCOM-2025-54`).
- **trade-remedies**: polysilicon anti-dumping expiry review 2026 (`CN-DEC-MOFCOM-2026-3`).
- **import-tariffs / import-standards**: none recorded; China's 2025 retaliatory tariffs on US goods are general measures and were excluded under the eligibility rule for general trade instruments.

## 5. Fit with the schema

- **Suspensions.** The October 2025 export controls were suspended before or soon after taking effect, and the suspension has been extended once. We kept the suspended announcements `in force` (they are not revoked) and recorded the extension as a row that `overrides` them. The first suspension (2025 No. 70) and the suspension of paragraph 2 of 2024 No. 46 (2025 No. 72, to 2026-11-27) are described in notes only. Reviewers may want a convention, or a status, for "adopted but suspended".
- **Normative documents vs rules.** NDRC/NEA notices and opinions map to `circular`; NEA's distributed PV 办法 is a normative document but is mapped to `ministerial regulation` because it is a full set of measures. Ministry orders (令) are `ministerial regulation`.
- **Announcements.** MOFCOM-GAC and MOF-STA announcements map to `decision`. MIIT standard conditions are announcements that state they are not mandatory: `decision` with `binding = no`.
- **Amending decisions.** NPCSC amendments are separate laws ("decisions on amending"). We recorded the Electricity Law and Renewable Energy Law through their latest amending decisions, because the 1995 and 2005 base texts could not be read; reviewers may prefer one row per base law plus amendment rows.
- **Export rebates.** No topic covers export tax rebates; we used `manufacturing-incentives`. A reviewer may prefer a trade topic.
- **Technologies.** Rare-earth rows are tagged wind and electric-vehicles (permanent magnets); the gallium, germanium and antimony tags (solar-pv) are tentative.
- **Draft law.** `CN-BILL-2026-RE` has an empty `date_in_force` (not adopted), as for India's DGTR row.
- **language** is `zh` for all rows; MOFCOM publishes unofficial English versions of some announcements.

## 6. Partner institutes and possible reviewers

Not researched in this pass. Candidates to approach: Chinese energy policy researchers at universities or think tanks with English output (for example Tsinghua University's climate institute or the NDRC Energy Research Institute), and trade-law practitioners for the export control rows. Reviewers need to read Chinese.

## 7. Risks and open questions

1. **Suspension timing.** The October 2025 package is suspended to 2027-01-10 and paragraph 2 of 2024 No. 46 to 2026-11-27. Both dates fall within weeks of this report; check for new announcements before merging.
2. **flk.npc.gov.cn unreachable.** Law dates and order numbers rest on gov.cn listings and search summaries. The Renewable Energy Law 2009 amendment's presidential order number was not confirmed.
3. **Signing vs publication dates.** For 1044 (green certificates), the negative list and the PV standard conditions, only publication dates were confirmed.
4. **Carbon trading rules amended in 2026.** State Council Order No. 843 (2026-08-08) and an MEE decision of 2026-09-20 amended the ETS regulation and the CCER measures, apparently in connection with the new Ecological Environment Code; the Code itself was not researched.
5. **ETS work plan.** No document number found; the URL is MEE's press page.
6. **Renewable Energy Law revision.** Draft text not located on npc.gov.cn; content from Xinhua reports only.
7. **Electricity Law revision.** On the 2025 State Council legislative plan; no NPCSC submission found.
8. **Not yet recorded but likely relevant:** 2021 grid-parity notice; RCW mechanism (2019); green certificate rules (2024); spot market rules (2023, and the 2026 draft); coal capacity price (2023); MEE Order No. 19 and CCER measures; dual-credit measures; hydrogen plan; MOFCOM-GAC 2025 Nos. 55-57 and 70, MOFCOM 2025 No. 72; technology export catalogue 2023 No. 57; lithium battery industry standard conditions; 15th Five-Year Plan and sector plans (2026); any national local-content rules.

## 8. Sources

Official (tier 1-2):
- https://www.ndrc.gov.cn/xxgk/zcfb/tz/202502/t20250209_1396066.html (Document 136; read)
- https://www.ndrc.gov.cn/xxgk/jd/jd/202502/t20250209_1396070_ext.html (Document 136 interpretation)
- https://www.gov.cn/zhengce/zhengceku/202502/content_7004206.htm (Distributed PV Measures)
- https://www.nea.gov.cn/20250123/112c5b199c5f45dd8e7ac93c9f5e4eaf/c.html (Distributed PV Measures, NEA)
- https://www.ndrc.gov.cn/xxgk/zcfb/tz/202308/t20230803_1359092.html (green certificates 1044)
- https://www.gov.cn/gongbao/2024/issue_11626/202410/content_6978630.html (green certificate rules 2024)
- https://www.ndrc.gov.cn/xxgk/zcfb/ghxwj/202107/t20210723_1291321.html (storage 1051)
- https://www.gov.cn/zhengce/zhengceku/2022-03/23/content_5680759.htm (Modern Energy System Plan)
- https://www.ndrc.gov.cn/xxgk/zcfb/tz/202106/t20210611_1283088.html (2021 parity pricing 833)
- https://www.ndrc.gov.cn/xxgk/zcfb/tz/201905/t20190515_962446.html (RCW 807)
- https://www.ndrc.gov.cn/xxgk/zcfb/tz/202311/t20231110_1361897.html (coal capacity price 1501)
- https://www.mee.gov.cn/ywgz/fgbz/fl/200802/t20080202_117982.shtml (Renewable Energy Law consolidated)
- https://www.gov.cn/yaowen/liebiao/202411/content_6985719.htm (Order No. 37, Energy Law)
- https://www.gov.cn/yaowen/liebiao/202411/content_6985718.htm (Order No. 36, Mineral Resources Law)
- https://www.gov.cn/zhengce/content/202402/content_6930137.htm (Order No. 775)
- https://www.mee.gov.cn/zcwj/gwywj/202610/t20261010_1175967.shtml (Order No. 775 as revised 2026; read)
- https://www.mee.gov.cn/zcwj/gwywj/202608/t20260814_1164034.shtml (Order No. 843)
- https://www.mee.gov.cn/gzk/gz/202112/t20211213_963865.shtml (MEE Order No. 19)
- https://www.mee.gov.cn/gzk/gz/202310/t20231020_1043695.shtml (CCER measures)
- https://www.mee.gov.cn/ywdt/zbft/202503/t20250326_1104767.shtml (ETS extension)
- https://www.gov.cn/zhengce/202306/content_6889002.htm (NEV purchase tax 2023 No. 10)
- https://www.gov.cn/zhengce/content/2020-11/02/content_5556716.htm (NEV plan)
- https://www.gov.cn/zhengce/zhengceku/2020-06/22/content_5521144.htm (dual-credit measures 2020)
- https://www.ndrc.gov.cn/fggz/hjyzy/tdftzh/202203/t20220325_1320346.html (hydrogen plan)
- https://www.gov.cn/zhengce/content/202406/content_6960152.htm (Order No. 785)
- https://www.miit.gov.cn/zcfg/qtl/art/2025/art_ff508817506f4d928dd38ec4ea483b71.html (Order No. 71)
- https://www.gov.cn/gongbao/2025/issue_12286/202509/content_7041212.html (Order No. 71, Gazette)
- https://www.gov.cn/zhengce/202409/content_6973155.htm (negative list 2024)
- https://www.ndrc.gov.cn/xxgk/jd/jd/202409/t20240907_1392878.html (negative list interpretation)
- https://wap.miit.gov.cn/gyhxxhb/jgsj/dzxxs/zlgh/art/2024/art_8997116730504e5b85f97f9e63c2da3a.html (PV standard conditions interpretation)
- http://gxj.zaozhuang.gov.cn/gxwj/202411/t20241125_1971068.html (PV standard conditions, local copy)
- https://szs.mof.gov.cn/zhengcefabu/202411/t20241115_3947628.htm (export rebates 2024 No. 15)
- https://szs.mof.gov.cn/zhengcefabu/202601/t20260109_3981637.htm (export rebates 2026 No. 2)
- http://www.npc.gov.cn/npc/c30834/202010/cf4e0455f6424a38b5aecf8001712c43.shtml (Export Control Law)
- https://www.mofcom.gov.cn/zcfb/zhzc/art/2020/art_a292f549deab48c09fdff9a8c3cc5906.html (Order No. 58)
- https://www.mee.gov.cn/zcwj/gwywj/202410/t20241021_1089760.shtml (Order No. 792)
- https://aqygzj.mofcom.gov.cn/qdml/art/2023/art_c2ae3d2061e14e97ba608de1ed565f78.html (2023 No. 23)
- https://www.mofcom.gov.cn/zcfb/blgg/art/2023/art_f6b1bc49e2c8482f8eb749012bc66dec.html (2023 No. 39)
- https://www.mofcom.gov.cn/zwgk/zcfb/art/2024/art_a4711acb06364199a3c5a06d7f2be6d8.html (2024 No. 33)
- https://www.mofcom.gov.cn/zwgk/zcfb/art/2024/art_3d5e990b43424e60828030f58a547b60.html (2024 No. 46)
- https://www.mofcom.gov.cn/zwgk/zcfb/art/2025/art_5c68985a6b1a46778e2e8dbff1bb1601.html (2025 No. 72)
- https://www.mofcom.gov.cn/zcfb/zgdwjjmywg/art/2025/art_7ef0e7016e934fc9b1bde9c4b6e7e893.html (2025 No. 18)
- https://www.mofcom.gov.cn/zwgk/zcfb/art/2025/art_79646f0161564975a938fe00fee158d5.html (2025 No. 58)
- https://www.mofcom.gov.cn/zwgk/zcfb/art/2025/art_7fc9bff0fb4546ecb02f66ee77d0e5f6.html (2025 No. 61)
- https://www.mofcom.gov.cn/zwgk/zcfb/art/2025/art_6cb42957741440c6984de696b70df9ae.html (2025 No. 62; read)
- https://www.mofcom.gov.cn/zwgk/zcfb/art/2025/art_b1ec77dd3f0d4762952904df7cdaadec.html (2025 No. 70)
- https://www.mofcom.gov.cn/zwgk/zcfb/art/2026/art_91466027f465467985942a639a9485f4.html (2026 No. 58; read)
- https://www.most.gov.cn/tztg/202312/t20231221_189244.html (catalogue 2023 No. 57)
- https://www.most.gov.cn/satp/kjzc/zh/202507/t20250716_194194.html (catalogue 2025 No. 28)
- https://www.mofcom.gov.cn/syxwfb/art/2025/art_072f1b88bcb4415fae1f05bbd569fd50.html (catalogue 2025 spokesperson)
- https://www.mofcom.gov.cn/zcfb/blgg/art/2025/art_8c4374c1443f40c9bc2ac97f3a6502bd.html (BEV export licensing 2025 No. 54)

Secondary (tier 4, discovery and dating only):
- https://www.news.cn/politics/20261102/67c7cd3b61134a769fcfdd161df65e7a/c.html (Renewable Energy Law revision draft)
- https://m.gmw.cn/2026-11/02/content_1304581968.htm (same)
- https://www.news.cn/world/20260113/cb277682ebba4444bd6b3d162c7ca53d/c.html (polysilicon expiry review 2026 No. 3)
- https://www.spglobal.com/energy/en/news-research/latest-news/metals/110926-china-extends-rare-earth-export-suspension-to-january-2027 (suspension extension)
- https://paper.people.com.cn/zgnyb/pc/content/202505/19/content_30074723.html (Electricity Law revision on 2025 legislative plan)
- https://www.yicai.com/news/102845989.html (BEV export licensing)
- https://www.tid.gov.hk/en/tradecircular/files/2025/ci9772025a.pdf (Hong Kong TID copy of 2025 No. 70)
- https://junhe.com/legal-updates/2224 (dual-credit 2023 amendment)
