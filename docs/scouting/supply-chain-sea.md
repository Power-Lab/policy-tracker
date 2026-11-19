# Scouting report: supply-chain, trade and EV instruments in Indonesia, Viet Nam, Thailand, the Philippines and Malaysia

Prepared 2026-11-19 for the Power Transformation Lab policy tracker. It comes with [`sc-rules.csv`](sc-rules.csv), which has 57 candidate rows in the 32-column schema (ID 16, VN 12, PH 12, TH 9, MY 8), and [`sc-sources.csv`](sc-sources.csv), which has 14 sources not already in `data/search/sources.csv`. Everything here is a lead for reviewers, not checked data. Every row is `unverified`.

**Scope.** Only these topics: local-content, manufacturing-incentives, investment-rules, mineral-downstreaming, import-tariffs, trade-remedies, import-standards, export-restrictions and ev-adoption, from 2015. Two older Indonesian instruments are included because later rows amend or revoke them. The electricity-sector rows already in `data/rules.csv` are not repeated. Indonesia's nickel ore export ban rows (ID-PERMEN-ESDM-2018-25 and ID-PERMEN-ESDM-2019-11) are mentioned only in notes.

**How this was checked.**
- Web searches identified and dated the instruments.
- Official pages were fetched where the proxy allowed it: Lawphil, BOI, MOIT, Kemenkeu JDIH and Kemenkoinfra JDIH.
- PDFs were read through their text layer with `pdftotext`: the PMK 10/2024 abstract, BOI Sor. 8/2564, BOI 6/2568 and BOI press release 20/2567.
- Where a fact rests only on news or a law-firm note, the row's notes say so.
- HTTP codes in the source tables come from `curl` with a desktop user agent through the session proxy.

---

## Indonesia

### Summary

- **Local content (TKDN) is the main supply-chain instrument.** It is set in sector rules and calculated under the Ministry of Industry's general method.
  - Electricity infrastructure: from 2012 to 2024 Permenperin 54/2012 set the rules, and Permenperin 5/2017 added solar modules.
  - In 2024 the Ministry of Industry revoked both (Permenperin 33/2024). Electricity-project TKDN moved to the energy ministry (Permen ESDM 11/2024, which also allowed temporary relaxation for solar). Module calculation moved to Permenperin 34/2024.
  - Permenperin 35/2025 replaced the general TKDN certification rules from 2025-12-11.
- **The EV regime rests on Perpres 55/2019 as amended by Perpres 79/2023.** It sets the TKDN schedule. From 2024 to 2025 it also offered CBU/CKD import relief to firms that committed to produce locally. The relief was implemented by Permen Investasi 6/2023 and PMK 10/2024 (0% duty to 2025-12-31). The VAT borne by the government (PPN DTP) was renewed each year: PMK 8/2024, then PMK 12/2025. Most of these incentives ended on 2025-12-31.
- **Mineral downstreaming.** The 2020 Minerba amendment (UU 3/2020) is the statutory basis for ending unrefined mineral exports, including bauxite from 2023-06-10. Kepmen ESDM 296.K/2023 lists 47 critical minerals.
- **Investment rules.** The Positive Investment List (Perpres 10/2021, amended by Perpres 49/2021) governs foreign ownership.

### Legal hierarchy and document types

| Rank | Type | Example | `doc_type` |
| --- | --- | --- | --- |
| 1 | Undang-Undang (law) | UU 3/2020 | law |
| 2 | Peraturan Pemerintah (government regulation) | (none in this set) | government regulation |
| 3 | Peraturan Presiden (Perpres) | Perpres 55/2019, 79/2023, 10/2021 | presidential regulation |
| 4 | Peraturan Menteri: Permenperin, Permen ESDM, PMK, Permen Investasi | Permenperin 34/2024, PMK 10/2024 | ministerial regulation |
| 5 | Keputusan Menteri (Kepmen) | Kepmen ESDM 296.K/MB.01/MEM.B/2023 | decision |

The ministries number their regulations differently. Industry used `NN/M-IND/PER/M/YYYY` until about 2020 and `NN Tahun YYYY` after that. Finance uses `NN/PMK.010/YYYY` or `NN Tahun YYYY`. ESDM decisions carry suffixes (`.K/MB.01/MEM.B/`).

### Official sources

| Name | URL | Tier | Languages | What it holds | Access observed |
| --- | --- | --- | --- | --- | --- |
| BPK legal database | https://peraturan.bpk.go.id/ | 1 | id | All levels, metadata and PDFs | 403 (curl); readable through search snippets |
| peraturan.go.id | https://peraturan.go.id/ | 1 | id | State Gazette and Berita Negara texts | connection reset |
| JDIH Kemenkeu | https://jdih.kemenkeu.go.id/ | 2 | id | PMK with abstracts | 307 home page; PDF downloaded |
| JDIH Kemenperin | https://jdih.kemenperin.go.id/ | 2 | id | Permenperin (TKDN, EV) | connection reset |
| JDIH ESDM | https://jdih.esdm.go.id/ | 2 | id | Permen and Kepmen ESDM | not tried (already listed) |
| JDIH Kemenko Infrastruktur | https://jdih.kemenkoinfra.go.id/ | 2 | id | Metadata for investment and EV rules | 200 (WebFetch) |

### Key instruments by category

- **local-content:**
  - Permenperin 54/2012 (revoked)
  - Permenperin 5/2017 (solar; revoked)
  - Permenperin 33/2024 (revocation)
  - Permenperin 34/2024 (solar module TKDN)
  - Permen ESDM 11/2024 (electricity projects; temporary solar relaxation)
  - Permenperin 35/2025 (general TKDN certification)
  - Permenperin 6/2022 (EV TKDN roadmap)
- **ev-adoption and manufacturing-incentives:**
  - Perpres 55/2019 and Perpres 79/2023
  - Permen Investasi 6/2023 (expired; amended by 1/2024, no row)
  - PMK 12/2025 (VAT relief for 2025; PMK 8/2024, the 2024 version, has no row)
- **import-tariffs:** PMK 10/2024 (0% duty on programme BEVs to 2025-12-31).
- **investment-rules:** Perpres 10/2021 and Perpres 49/2021.
- **mineral-downstreaming and export-restrictions:** UU 3/2020 (Art. 170A, the end of unrefined exports including bauxite on 2023-06-10) and Kepmen ESDM 296.K/2023.

### Fit with the schema

These instruments fit the schema well. Every row has a number and an official listing. The amend and revoke chains are clear, for example 54/2012 ← 5/2017 ← 33/2024. Fiscal incentives that are renewed each year (PPN DTP) need one row per year. A reviewer should decide whether to add PMK 8/2024 and any 2026 successor.

### Risks and open questions

- BPK, peraturan.go.id and JDIH Kemenperin blocked automated access. Dates rest on search snippets of those pages.
- The Kemenkeu page for Perpres 55/2019 gives 28 and 29 March 2019. BPK and Setkab give 8 and 12 August 2019. The row uses August.
- The signing date and full title of Permenperin 33/2024 were not found.
- The task brief cited the critical minerals decree as 296.K/HK.02/…, but the official file reads 296.K/MB.01/MEM.B/2023. Its three-year term ends about 2026-09, so a replacement list may exist.
- The 2025 amendment of the Minerba law is reported in press but was not confirmed, and it has no row.
- Whether any 2026 EV incentive replaced the expired 2025 incentives was not checked.

### Sources

- https://peraturan.bpk.go.id/Details/116973/perpres-no-55-tahun-2019
- https://peraturan.bpk.go.id/Details/273447/perpres-no-79-tahun-2023
- https://jdih.kemenkeu.go.id/dok/perpres-55-tahun-2019
- https://setkab.go.id/inilah-perpres-no-55-2019-tentang-program-kendaraan-bermotor-listrik-berbasis-baterai/
- https://peraturan.bpk.go.id/Details/227541/permenperin-no-6-tahun-2022
- https://jdih.kemenkoinfra.go.id/permen-investasi-no-6-tahun-2023
- https://peraturan.bpk.go.id/Details/323555/permeninvesbkpm-no-1-tahun-2024
- https://industri.kontan.co.id/news/pelaku-usaha-dapat-insentif-impor-cbu-mobil-listrik-sampai-2025
- https://jdih.kemenkeu.go.id/download/6234644d-4879-466c-b53b-70c5acb29819/2024pmkeuangan010abs.pdf
- https://jdih.kemenkeu.go.id/api/download/5058714c-0925-4100-9039-8a7e070a901d/12%20Tahun%202025.pdf
- https://www.pajak.go.id/sites/default/files/2024-02/SP-10%20PEMERINTAH%20KEMBALI%20BERIKAN%20INSENTIF%20PPN%20DTP%20KENDARAAN%20BERMOTOR%20LISTRIK.pdf
- https://ekonomi.bisnis.com/read/20250219/259/1840828/sah-insentif-ppn-dan-ppnbm-kendaraan-listrik-hybrid-diperpanjang
- https://otodriver.com/berita/2025/insentif-mobil-listrik-dicabut-akhir-tahun-ini-enam-brand-kena-imbas-insecgicbas
- https://peraturan.bpk.go.id/Details/268784
- https://peraturan.go.id/files/permenperin-no-33-tahun-2024.pdf
- https://peraturan.bpk.go.id/Details/296131/permenperin-no-34-tahun-2024
- https://esdm.go.id/id/media-center/arsip-berita/beri-relaksasi-tkdn-plts-ini-batas-waktunya
- https://ekonomi.bisnis.com/read/20240805/44/1788364/menteri-esdm-rilis-aturan-relaksasi-tkdn-untuk-plts
- https://www.industry.co.id/read/135224/sah-begini-penjelasan-permenperin-no-34-tahun-2024-dan-permen-esdm-no-11-tahun-2024-terkait-aturan-tkdn-dalam-pembangunan-infrastruktur-ketenagalistrikan-plts
- https://berkas.dpr.go.id/pusaka/files/isu_sepekan/Isu%20Sepekan---II-PUSLIT-Januari-2024-245.pdf
- https://peraturan.bpk.go.id/Details/333003/permenperin-no-35-tahun-2025
- https://ekonomi.bisnis.com/read/20250913/257/1910960/ini-perubahan-utama-aturan-deregulasi-tkdn-ada-insentif-hingga-sanksi
- https://peraturan.bpk.go.id/Details/161806/perpres-no-10-tahun-2021
- https://peraturan.bpk.go.id/Details/168534/perpres-no-49-tahun-2021
- https://jdih.kemenkoinfra.go.id/id/peraturan-presiden-republik-indonesia-no-10-tahun-2021
- https://ekonomi.bisnis.com/read/20230609/44/1663878/jokowi-setop-ekspor-bauksit-10-juni-potensi-cuan-rp117-triliun-lenyap
- https://www.liputan6.com/bisnis/read/5315467/bauksit-haram-diekspor-mulai-hari-ini
- https://jdih.esdm.go.id/storage/document/Kepmen%20ESDM%20No%20296K_MB_01_MEM_B_2023.pdf
- https://industri.kontan.co.id/news/pemerintah-terbitkan-aturan-klasifikasi-mineral-kritis-berikut-daftar-lengkapnya

---

## Viet Nam

### Summary

- **EV demand-side policy works mainly through fees and taxes.**
  - Registration fees: Decree 10/2022 set a 0% first registration fee for battery EVs from 2022-03-01. Decree 51/2025 kept it at 0% to 2027-02-28. A further Decree 202/2026 is reported but not verified.
  - Special consumption tax: preferential BEV rates, first under Law 03/2022, now under the new SCT Law 66/2025, in force 2026-01-01. Press reports that Law 09/2026 extends the preferential rates to 2030.
  - Plans and directives: the transport transition programme (Decision 876/2022) sets targets. Directive 20/2025 targets fossil-fuelled motorcycles in central Hanoi from 2026-07-01.
- **Supply-side incentives come from supporting-industry policy.** Decree 111/2015 was amended by Decree 205/2025 (in force 2025-09-01).
- **Minerals.** The 2024 Law on Geology and Minerals took effect 2025-07-01. Its December 2025 amendment (Law 147/2025) adds a rare-earth chapter and bans raw rare-earth exports from 2026-01-01.
- **Trade remedies.** MOIT's AD20 case put final duties on Chinese hot-rolled steel from 2025-07-06. This is an indirect input to clean tech. No Vietnamese remedies on solar or battery goods were found; Vietnam is mostly the target of other countries' cases.

### Legal hierarchy and document types

| Rank | Type | Example | `doc_type` |
| --- | --- | --- | --- |
| 1 | Luật (law) of the National Assembly | 66/2025/QH15, 147/2025/QH15 | law |
| 2 | Nghị định (decree) of the Government | 10/2022/NĐ-CP, 205/2025/NĐ-CP | decree |
| 3 | Quyết định (decision) and Chỉ thị (directive) of the Prime Minister | 876/QĐ-TTg, 20/CT-TTg | decision / directive |
| 4 | Thông tư (circular) and Quyết định of ministries | 1959/QĐ-BCT | circular / decision |

Numbers carry the issuer suffix: `QH15` or `QH16` (the legislature), `NĐ-CP`, `QĐ-TTg`, `CT-TTg`, `QĐ-BCT`. Amending laws often bundle several laws, as Law 03/2022 does.

### Official sources

| Name | URL | Tier | Languages | What it holds | Access observed |
| --- | --- | --- | --- | --- | --- |
| vbpl.vn | https://vbpl.vn/ | 1 | vi | National legal database | not tried (already listed) |
| Government portal | https://chinhphu.vn/ | 1 | vi | Decrees, decisions, consolidated texts | 200 |
| MOIT | https://moit.gov.vn/ | 2 | vi | MOIT legal documents and trade remedy decisions | 200 |
| Thư viện Pháp luật | https://thuvienphapluat.vn/ | 3 | vi, en | Register with status and dates | 403 |
| LuatVietnam | https://luatvietnam.vn/ | 3 | vi, en | Register | 403 |

### Key instruments by category

- **ev-adoption:**
  - Decree 10/2022 and Decree 51/2025 (registration fee)
  - Law 03/2022 (replaced), Law 66/2025 and Law 09/2026 (special consumption tax)
  - Decision 876/2022 and Directive 20/2025
- **manufacturing-incentives:** Decree 111/2015 and Decree 205/2025.
- **mineral-downstreaming and export-restrictions:** Law 54/2024 and Law 147/2025 (raw rare-earth export ban).
- **trade-remedies:** MOIT Decision 1959/QĐ-BCT (hot-rolled steel, China).
- **import-tariffs and import-standards:** no EV-specific instrument was confirmed. A reviewer should check whether the preferential import duty programme for auto components (Decree 57/2020 and successors) belongs here.

### Fit with the schema

The fit is good. One problem is that omnibus amending laws (Law 03/2022) touch several topics, so the row covers only the SCT part. Another is that some rows rely on vbpl.vn or chinhphu.vn as portal-search URLs because the documents themselves were not opened.

### Risks and open questions

- Law 03/2022 and Law 09/2026 are low confidence. The rates and dates come from memory and press, so check them against the official texts.
- Sources differ on the adoption date of Law 66/2025 (2025-06-14 or 2025-06-24).
- Decree 202/2026 (registration fee) is unverified.
- Whether Law 147/2025 also restricts refined rare-earth exports needs checking in Chapter VIIa.
- Thư viện Pháp luật and LuatVietnam block automated access.

### Sources

- https://luatvietnam.vn/thue-phi-le-phi/o-to-dien-tiep-tuc-duoc-mien-le-phi-truoc-ba-den-28-2-2027-565-101356-article.html
- https://thuvienphapluat.vn/phap-luat-nha-dat/nghi-dinh-512025ndcp-ve-le-phi-truoc-ba-doi-voi-o-to-dien-tu-01032025-1024.html
- https://thuvienphapluat.vn/van-ban/thue-phi-le-phi/nghi-dinh-10-2022-nd-cp-quy-dinh-ve-le-phi-truoc-ba-484768.aspx
- https://luatvietnam.vn/tin-van-ban-moi/tu-01-3-2022-o-to-dien-duoc-mien-le-phi-truoc-ba-trong-3-nam-186-34994-article.html
- https://thuvienphapluat.vn/van-ban/Thue-Phi-Le-Phi/Luat-thue-tieu-thu-dac-biet-2025-so-66-2025-QH15-621225.aspx
- https://datafiles.chinhphu.vn/cpp/files/duthaovbpl/2026/Thang4/phu-luc-2.-ban-danh-gia-tac-dong.pdf
- https://nguoiquansat.vn/vi-sao-quoc-hoi-chot-giu-thue-tieu-thu-dac-biet-voi-xe-dien-3-den-het-2030-288739.html
- https://lsvn.vn/du-kien-gia-han-uu-dai-thue-tieu-thu-dac-biet-cho-xe-dien-den-2030-a171575.html
- https://moit.gov.vn/van-ban-phap-luat/nghi-dinh-sua-doi-bo-sung-mot-so-dieu-cua-nghi-dinh-so-111-2015-nd-cp-ngay-3-11-2025-cua-chinh-phu-ve-phat-trien-cong-ng.html
- https://tapchicongthuong.vn/bo-sung-chinh-sach-ho-tro-kinh-phi-cho-doanh-nghiep-cong-nghiep-ho-tro-142888.htm
- https://english.luatvietnam.vn/giao-thong/decision-876-qd-ttg-2022-program-on-green-energy-transition-reduction-of-carbon-and-methane-emissions-in-transport-sector-226589-d1.html
- https://tapchitoaan.vn/thu-tuong-chi-dao-ha-noi-cam-xe-may-chay-xang-dau-trong-vanh-dai-1-tu-thang-7202613742.html
- https://vbpl.vn/TW/Lists/vbpq/Attachments/174000/Luat%20Dia%20chat%20va%20khoang%20san.docx
- https://thuvienphapluat.vn/van-ban/Tai-nguyen-Moi-truong/Luat-Dia-chat-va-Khoang-san-2024-so-54-2024-QH15-578531.aspx
- https://thuvienphapluat.vn/phap-luat-nha-dat/luat-dia-chat-va-khoang-san-sua-doi-2025-luat-so-1472025qh15-13824.html
- https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/10/149-vbhn-vpqh.signed.pdf
- https://e.vnexpress.net/news/news/environment/vietnam-bans-raw-rare-earth-export-in-new-mineral-law-4992790.html
- https://www.mining.com/web/vietnam-curbs-exports-of-refined-rare-earths-reaffirms-ban-on-ore-trade/
- https://moit.gov.vn/tin-tuc/ap-dung-thue-chong-ban-pha-gia-chinh-thuc-doi-voi-mot-so-san-pham-thep-can-nong-co-xuat-xu-tu-cong-hoa-nhan-dan-trung-ho.html
- https://luatvietnam.vn/thue/quyet-dinh-1959-qd-bct-2025-ap-dung-thue-chong-ban-pha-gia-thep-can-nong-tu-trung-quoc-va-cham-dut-dieu-tra-tu-an-do-405185-d1.html
- https://chinhphu.vn/
- https://vbpl.vn/

---

## Thailand

### Summary

- **The EV package is the main instrument.**
  - The Cabinet adopts each phase by resolution: EV 3.0 (2022-02-15) and EV 3.5 (2023-12-19, after the EV Board's 2023-11-01 approval).
  - The resolutions are implemented through Excise Department notifications (excise cuts and subsidies) and Ministry of Finance customs notifications under Section 12 of the Customs Tariff Decree. These cover CBU BEV duty relief for 2024-2025 and a duty exemption for nine BEV parts.
  - Production-offset obligations tie the import relief to local manufacturing. The Cabinet loosened them on 2025-12-09.
- **BOI announcements carry the supply-side incentives.**
  - Sor. 8/2564 sets the EV manufacturing promotion terms.
  - 6/2568 (2025-07-22) gives an extra tax reduction for EV and appliance projects that meet local-content thresholds (40% for BEVs, 45% for PHEVs).
- **Battery cells.** The EV Board approved cash grants on 2024-02-21, subject to Cabinet approval that was not confirmed.
- **Other topics.** No Thai export restrictions or trade remedies in scope were identified.

### Legal hierarchy and document types

| Rank | Type | Example | `doc_type` |
| --- | --- | --- | --- |
| 1 | Act (Phra Ratchabanyat) | Investment Promotion Act B.E. 2520 | law |
| 2 | Royal Decree | Customs Tariff Decree (Section 12 powers) | decree |
| 3 | Cabinet resolution | EV 3.0 and EV 3.5 | decision |
| 4 | Ministerial notification (Ministry of Finance, Excise Department) | CBU BEV duty relief | ministerial regulation |
| 5 | BOI announcement; EV Board resolution | BOI 6/2568; EV Board 2024-02-21 | decision |

BOI announcements use Buddhist-era years (2568 = 2025) and a "Sor." prefix for sector policies. Cabinet and EV Board resolutions are unnumbered.

### Official sources

| Name | URL | Tier | Languages | What it holds | Access observed |
| --- | --- | --- | --- | --- | --- |
| Royal Thai Government Gazette | https://ratchakitcha.soc.go.th/ | 1 | th | Notifications (customs, excise) | not tried (already listed) |
| BOI | https://www.boi.go.th/ | 2 | th, en | Announcements, press releases (English) | 200; PDFs downloaded |
| Excise Department | https://www.excise.go.th/ | 2 | th | EV excise notifications | 200 (home page) |
| Thai Government (thaigov) | https://www.thaigov.go.th/ | 2 | th | Cabinet resolutions | 403 |

### Key instruments by category

- **ev-adoption and import-tariffs:**
  - Cabinet EV 3.0 and EV 3.5
  - Ministry of Finance CBU BEV duty notification (2024-2025, expired)
  - BEV parts duty exemption (expired 2025-12-31)
  - 30@30 production target
- **manufacturing-incentives and local-content:**
  - BOI Sor. 8/2564
  - BOI 6/2568
  - EV Board battery-cell scheme (pending)
  - Cabinet 2025-12-09 adjustments

### Fit with the schema

The fit is acceptable but loose. Cabinet resolutions and BOI announcements are `decision`. The binding measures sit in Royal Gazette notifications, and their numbers were not found. Each Excise and customs notification probably deserves its own row linked to the Cabinet resolution through `implements`. Thai titles still need to be added. Like the existing TH rows, these use English placeholders.

### Risks and open questions

- Notification numbers and Thai titles are missing for the Ministry of Finance customs measures and the Excise EV notifications.
- The date of the Cabinet approval of the battery-cell grants is unknown. Press puts the subsidy in 2023 or 2024, and a THB 24 billion envelope is reported.
- The meeting date of the 30@30 target is unclear (2021 or 2023-05-12). RVO reports a raise to 50%, which was not verified.
- The 2024-02-21 tax deduction for buying electric trucks and buses has no row, because its implementing Royal Decree was not found.
- Thaigov returned 403.

### Sources

- https://www.boi.go.th/upload/content/Sor.8_2564_en.pdf
- https://www.boi.go.th/upload/content/6_2568EN.pdf
- https://www.boi.go.th/upload/content/PR20_2567EN.pdf
- https://www.boi.go.th/upload/content/PR119_2566EN.pdf
- https://www.boi.go.th/upload/content/PR57_2565EN.pdf
- https://www.nationthailand.com/business/40012375
- https://kpmg.com/th/en/home/insights/2022/05/th-tax-news-flash-issue-130.html
- https://www.tilleke.com/insights/thailand-approves-incentives-to-promote-electric-vehicle-adoption-and-manufacturing
- https://insightplus.bakermckenzie.com/bm/industrials-manufacturing-transportation/thailand-new-ev35-incentive-package-approved-by-the-cabinet
- https://www.ey.com/en_gl/technical/tax-alerts/thailand---subsidies--duties--excise-tax-incentives-to-encourage
- https://insightplus.bakermckenzie.com/bm/tax/thailand-extension-of-the-customs-duty-incentives-for-completely-built-up-bevs-imported-from-1-january-2024-to-31-december-2025
- https://insightplus.bakermckenzie.com/bm/industrials-manufacturing-transportation/thailand-notification-of-the-ministry-of-finance-exempting-import-duties-for-major-bev-parts
- https://www2.deloitte.com/content/dam/Deloitte/th/Documents/tax/th-customs-alert-ev-Jun2023-en.pdf
- https://www.nationthailand.com/in-focus/40015222
- https://www.nationthailand.com/thailand/general/40024599
- https://www.iea.org/policies/30546 (403)
- https://www.nationthailand.com/business/automobile/40059499
- https://www.thailand.go.th/issue-focus-detail/thailand-updates-ev3ev35-incentives-to-strengthen-position-as-regional-ev-hub
- https://www.nationthailand.com/news/40000851
- https://www.eria.org/uploads/4_Chapter-4-The-Economic-and-Greenhouse-Gas-Emission-Impacts-of-EV.pdf
- https://www.tilleke.com/insights/boi-expands-promoted-activities-for-electric-vehicle-manufacturers
- https://ratchakitcha.soc.go.th/

---

## Philippines

### Summary

- **EV policy.**
  - Law: the EV Industry Development Act (RA 11697) lapsed into law on 2022-04-15, and its DOE/DOTr/DTI IRR is dated 2022-09-02.
  - Tariffs: EO 12 (2023) cut MFN duties on BEVs and some parts to zero for five years. EO 62 (2024) widened this to hybrids, e-motorcycles and more parts until 2028.
- **Manufacturing and investment incentives.**
  - CREATE (RA 11534, 2021) and CREATE MORE (RA 12066, 2024) set the tax incentives.
  - The Strategic Investment Priority Plan decides which activities qualify. The 2022 plan (MO 61) put EVs in Tier II, and the 2026 plan (MO 47, 2026-05-21) adds critical-mineral processing.
  - EO 18 (2023) creates "green lanes" for strategic investments.
- **Critical minerals.**
  - EO 130 (2021) reopened new mineral agreements.
  - RA 12253 (2025) overhauled mining taxes.
  - EO 122 (2026-08-18) sets a critical minerals framework: a national list, priority ore access for domestic processors, and DTI-BOI promotion of downstream industries.
  - No raw-ore export ban was found.

### Legal hierarchy and document types

As in [ph.md](ph.md):

| Rank | Type | Example | `doc_type` |
| --- | --- | --- | --- |
| 1 | Republic Act | RA 11697, RA 12066 | law |
| 2 | Executive Order, Memorandum Order | EO 12 s.2023, MO 47 s.2026 | presidential regulation |
| 3 | IRR and Department Circulars | EVIDA IRR | circular |

### Official sources

| Name | URL | Tier | Languages | What it holds | Access observed |
| --- | --- | --- | --- | --- | --- |
| Lawphil | https://lawphil.net/ | 3 | en | RAs, EOs, MOs (full text) | 200 |
| Supreme Court E-Library | https://elibrary.judiciary.gov.ph/ | 1 | en | Laws, EOs, IRRs | 403 |
| DOE | https://doe.gov.ph/ | 2 | en | IRRs and circulars | 200 (page content not parsed) |
| Official Gazette | https://www.officialgazette.gov.ph/ | 1 | en | Publication dates | not tried (403 earlier per ph.md) |

All of these are already in `sources.csv`. No new Philippine source was added.

### Key instruments by category

- **ev-adoption:** RA 11697, the EVIDA IRR, EO 12 and EO 62.
- **import-tariffs:** EO 12 and EO 62.
- **manufacturing-incentives and investment-rules:** RA 11534, RA 12066, MO 61 s.2022 (replaced), MO 47 s.2026 and EO 18.
- **mineral-downstreaming:** EO 130, RA 12253 and EO 122.

### Fit with the schema

The fit is very good. Texts are in English on Lawphil, and approval dates are stated. Effectivity dates depend on publication and were mostly not found, so several rows give only the year in `date_in_force`.

### Risks and open questions

- Effectivity dates are missing for most instruments, and so is the number of the EVIDA IRR.
- Whether MO 47 expressly revokes MO 61 was not checked.
- RA 12253's fit with mineral-downstreaming is loose.
- The Critical Minerals List due under EO 122 was not checked.
- RA 11647 (Foreign Investments Act amendments) and RA 11659 (Public Service Act amendments, 2022) are candidate investment-rules rows not added.

### Sources

- https://lawphil.net/statutes/repacts/ra2022/ra_11697_2022.html
- https://doe.gov.ph/node/22449
- https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/2/96703 (403)
- https://businessmirror.com.ph/2022/09/06/irr-of-electric-vehicle-lawfinalized-signed-by-doe/
- https://lawphil.net/executive/execord/eo2023/eo_12_2023.html
- https://abs-cbn.com/business/01/19/23/electric-vehicle-tariff-rates-temporarily-cut-to-zero
- https://lawphil.net/executive/execord/eo2024/eo_62_2024.html
- https://lawphil.net/statutes/repacts/ra2021/ra_11534_2021.html
- https://lawphil.net/statutes/repacts/ra2024/ra_12066_2024.html
- https://business.inquirer.net/489358/marcos-signs-create-more-act-amending-the-law-on-corporate-income-taxes/amp
- https://lawphil.net/executive/mo/mo2022/mo_61_2022.html
- https://lawphil.net/executive/mo/mo2026/mo_47_2026.html
- https://lawphil.net/executive/execord/eo2023/eo_18_2023.html
- https://lawphil.net/executive/execord/eo2021/eo_130_2021.html
- https://lawphil.net/statutes/repacts/ra2025/ra_12253_2025.html
- https://www.pwc.com/ph/en/tax/tax-publications/tax-alerts/2025/tax-alert-35.html
- https://www.dof.gov.ph/recto-enhanced-mining-regime-transforms-ph-natural-wealth-into-investments-jobs-and-sustainable-growth-for-filipinos/
- https://lawphil.net/executive/execord/eo2026/eo_122_2026.html
- https://cruzmarcelo.com/a-new-playbook-for-critical-minerals-what-executive-order-no-122-means-for-mining-and-energy-investment-in-the-philippines/

---

## Malaysia

### Summary

- **EV policy is mostly plans and budget measures.**
  - Plans: the National Automotive Policy 2020 (2020-02-21) and the Low Carbon Mobility Blueprint 2021-2030, which targets EVs at 15% of total industry volume by 2030.
  - Tax exemptions: Budget 2022 (2021-10-29) brought in import, excise, sales-tax and road-tax exemptions. The CBU exemption ended on 2025-12-31. The CKD exemption runs to 2027-12-31.
  - Import conditions: from 2026-07-01, MITI requires new CBU EV imports to have a CIF value of at least RM200,000 and motor output of at least 180 kW.
- **Industrial policy.** NIMP 2030 (2023-09-01) sets it. The green tax incentives (GITA/GITE) were reworked into tiers in Budget 2024, for applications from 2024 to 2026.
- **Minerals.** Policy follows the Mineral Industry Transformation Plan 2021-2030. The ban on exporting raw rare earths was announced on 2023-09-11 and, according to NRES, is held as a 2025-2027 moratorium.
- **Missing legal instruments.** None of the Malaysian rows yet links to a gazetted instrument (a P.U.(A) order). Plans and budget measures stand in for them.

### Legal hierarchy and document types

| Rank | Type | Example | `doc_type` |
| --- | --- | --- | --- |
| 1 | Act of Parliament | Customs Act 1967, Excise Act 1976 | law |
| 2 | Subsidiary legislation (P.U.(A) orders) | Customs Duties (Exemption) orders | ministerial regulation |
| 3 | Cabinet and ministry policy decisions, budget measures | Budget 2022 EV exemptions; MITI CBU EV rule | decision |
| 4 | National plans and blueprints | NIMP 2030, LCMB, NAP 2020 | plan |

### Official sources

| Name | URL | Tier | Languages | What it holds | Access observed |
| --- | --- | --- | --- | --- | --- |
| Federal Gazette (AGC) | https://www.federalgazette.agc.gov.my/ | 1 | ms, en | P.U.(A) exemption orders | not tried (already listed) |
| MITI | https://www.miti.gov.my/ | 2 | en, ms | NAP 2020, NIMP, media statements | 200 |
| MIDA | https://www.mida.gov.my/ | 2 | en | Incentive guidelines | 200 |
| MOF | https://www.mof.gov.my/ | 2 | en, ms | Budget measures | 301 (redirect) |
| MGTC | https://www.mgtc.gov.my/ | 2 | en | LCMB, GITA asset | 200 |
| JMG | https://jmg.gov.my/ | 2 | ms, en | Rare earth statements | 301 (redirect) |

### Key instruments by category

- **ev-adoption:** NAP 2020, the LCMB, the Budget 2022 EV exemptions and the MITI CBU EV rule (2026).
- **import-tariffs:** the Budget 2022 EV exemptions.
- **import-standards:** the MITI CBU EV rule (2026).
- **manufacturing-incentives and investment-rules:** NAP 2020, NIMP 2030 and the Budget 2024 GITA/GITE measure.
- **mineral-downstreaming and export-restrictions:** TIM 2021-2030 and the raw rare-earth export ban.

### Fit with the schema

The fit is weak at present. Every row is a plan or a policy decision without a number. The binding measures (customs and excise exemption orders, and any export prohibition order) are P.U.(A) instruments that should become separate rows linked by `implements`. They were not located in this pass.

### Risks and open questions

- The P.U.(A) numbers for the EV duty exemption orders and their extensions are missing.
- The legal basis and start date of the rare-earth export ban are missing (2024-01-01 or 2025). A possible relaxation was reported in 2026-08.
- The adoption date of the LCMB is unclear.
- The Budget 2024 date (2023-10-13) is from general knowledge.
- The new CBU EV rule has been seen only in press.

### Sources

- https://www.miti.gov.my/index.php/pages/view/nap2020
- https://www.mondaq.com/Technology/897982/Malaysia-Launches-The-National-Automotive-Policy-2020
- https://paultan.org/2025/08/19/nap-2020-to-be-reviewed-to-ensure-relevance-miti/
- https://www.nres.gov.my/ms-my/pustakamedia/KenyataanMedia/Kenyataan%20Media%20TIM%202021-2030.pdf
- https://www.iea.org/policies/16794-national-mineral-industry-transformation-plan-2021-2030
- https://www.mgtc.gov.my/what-we-do/low-carbon-mobility-2/low-carbon-mobility-blueprint/
- https://nst.com.my/amp/business/2021/04/683754/low-carbon-mobility-blueprint-drive-larger-participation-ev-players
- https://www.iseas.edu.sg/wp-content/uploads/2024/04/ISEAS_Perspective_2024_33.pdf
- https://www.mof.gov.my/portal/en/news/press-citations/full-exemption-of-import-excise-duties-sales-tax-for-electric-vehicle
- https://paultan.org/2021/10/29/budget-2022-evs-in-malaysia-to-be-completely-tax-free-soon/
- https://paultan.org/2025/12/22/fully-imported-evs-arriving-in-malaysia-before-dec-28-will-qualify-for-excise-import-duty-exemptions-maa/
- https://www.malaymail.com/news/malaysia/2026/03/11/miti-ev-tax-exemptions-for-local-assembly-till-end-2027-as-some-chinese-auto-makers-set-to-start-this-year/212147
- https://www.mida.gov.my/launch-of-the-new-industrial-master-plan-2030-nimp-2030/
- https://www.businesstoday.com.my/2023/09/01/anwar-nimp-2030-to-drastically-enhance-malaysias-economic-trajectory/
- https://www.bloomberg.com/news/articles/2023-09-11/malaysia-seeks-to-develop-ban-on-exports-of-rare-earths
- https://jmg.gov.my/berita-artikel/moratorium-on-raw-ree-export-aimed-at-supporting-midstream-industry-development-nres
- https://www.malaymail.com/amp/news/malaysia/2025/11/14/malaysia-imposes-short-term-ban-on-raw-ree-exports-to-boost-midstream-industry-says-ministry/198298
- https://asianews.network/?p=306588
- https://www.thestar.com.my/news/nation/2026/08/03/keep-ban-on-raw-rare-earth-exports-until-local-value-chain-built-putrajaya-urged
- https://www.mida.gov.my/malaysias-2024-national-budget/
- https://www.mgtc.gov.my/services/green-investment-tax-allowance-gita/
- https://www.thestar.com.my/business/business-news/2026/05/06/miti-imported-electric-vehicles-subject-to-two-main-conditions-from-july-1-2026
- https://paultan.org/2026/05/06/miti-confirms-changes-to-cbu-ev-policy-minimum-cif-value-of-rm200k-at-least-245-ps-effective-july-1-2026/
- https://paultan.org/2026/07/15/miti-says-government-has-no-plans-to-reverse-new-cbu-ev-policy/
