"""Tests for the data loader and render helpers.  Run: python3 -m unittest discover tests"""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import build  # noqa: E402
import render  # noqa: E402


class DataTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = build.load()

    def test_data_is_valid(self):
        self.assertEqual(self.data.errors, [])

    def test_back_links_are_derived(self):
        r = self.data.rules["ID-PERMEN-ESDM-2021-26"]
        self.assertEqual(r["revoked_by"], ["ID-PERMEN-ESDM-2024-02"])
        self.assertIn("ID-PERMEN-ESDM-2018-49", r["revokes"])

    def test_generated_is_a_data_date(self):
        dates = {r["status_checked"] for r in self.data.rules.values()}
        self.assertIn(self.data.generated, dates)


class HelperTests(unittest.TestCase):
    def test_partial_dates_sit_mid_period(self):
        self.assertAlmostEqual(render.to_year("2020"), 2020.5, delta=0.05)
        self.assertAlmostEqual(render.to_year("2020-01"), 2020.04, delta=0.02)
        self.assertEqual(render.to_year(""), None)

    def test_fmt_date(self):
        self.assertEqual(render.fmt_date("2024-01-29"), "29 Jan 2024")
        self.assertEqual(render.fmt_date("2024-05"), "May 2024")
        self.assertEqual(render.fmt_date(""), "—")

    def test_component_walks_both_directions(self):
        data = build.load()
        ids = [r["id"] for r in render.component(data, data.rules["ID-PERMEN-ESDM-2019-13"])]
        self.assertEqual(ids[0], "ID-PERMEN-ESDM-2018-49")
        self.assertEqual(ids[-1], "ID-PERMEN-ESDM-2024-02")
        self.assertEqual(len(ids), 5)

    def test_amendments_fold_under_their_parent(self):
        data = build.load()
        rs = [data.rules[i] for i in ("ID-PERMEN-ESDM-2017-50", "ID-PERMEN-ESDM-2018-53", "ID-PERMEN-ESDM-2020-04")]
        grouped = render.group_current(data, rs)
        self.assertEqual([r["id"] for r, _ in grouped], ["ID-PERMEN-ESDM-2017-50"])
        self.assertEqual({a["id"] for a in grouped[0][1]}, {"ID-PERMEN-ESDM-2018-53", "ID-PERMEN-ESDM-2020-04"})

    def test_amendment_stays_visible_without_parent(self):
        data = build.load()
        grouped = render.group_current(data, [data.rules["ID-PERMEN-ESDM-2020-04"]])
        self.assertEqual([r["id"] for r, _ in grouped], ["ID-PERMEN-ESDM-2020-04"])


if __name__ == "__main__":
    unittest.main()


class ReviewTests(unittest.TestCase):
    """The review applier treats issue bodies as untrusted input."""

    def setUp(self):
        import apply_review
        import rules_diff
        self.ar = apply_review
        raw = build.DATA.joinpath("rules.csv").read_text(encoding="utf-8")
        self.columns, self.rows = rules_diff.read_rows(raw)

    def body(self, payload):
        import json
        return "text\n```json review\n" + json.dumps(payload) + "\n```\n"

    def test_applies_edits_and_sets_verification(self):
        r = self.rows["VN-DECREE-2024-80"]
        p = self.ar.parse_payload(self.body({"v": 1, "reviewer": "A", "rules": [
            {"id": "VN-DECREE-2024-80", "base": {"notes": r["notes"]}, "set": {"notes": "checked"},
             "checks": {k: True for k in self.ar.CHECKS}}]}))
        errors, conflicts = self.ar.apply(p, self.rows, "someone", "2026-11-04")
        self.assertEqual((errors, conflicts), ([], []))
        self.assertEqual(r["notes"], "checked")
        self.assertEqual(r["verification"], "verified")
        self.assertEqual(r["reviewed_by"], "A (@someone)")

    def test_refuses_stale_base(self):
        p = self.ar.parse_payload(self.body({"v": 1, "rules": [
            {"id": "VN-DECREE-2024-80", "base": {"status": "in force"}, "set": {"status": "revoked"}}]}))
        _, conflicts = self.ar.apply(p, self.rows, "x", "2026-11-04")
        self.assertEqual(len(conflicts), 1)
        self.assertEqual(self.rows["VN-DECREE-2024-80"]["status"], "replaced")

    def test_rejects_protected_fields_and_unknown_ids(self):
        p = self.ar.parse_payload(self.body({"v": 1, "rules": [
            {"id": "VN-DECREE-2024-80", "set": {"verification": "verified", "id": "X"}},
            {"id": "NOPE", "set": {"notes": "x"}}]}))
        errors, _ = self.ar.apply(p, self.rows, "x", "2026-11-04")
        self.assertEqual(len(errors), 3)
        self.assertEqual(self.rows["VN-DECREE-2024-80"]["verification"], "unverified")

    def test_missing_or_bad_block(self):
        with self.assertRaises(self.ar.ReviewError):
            self.ar.parse_payload("no block here")
        with self.assertRaises(self.ar.ReviewError):
            self.ar.parse_payload("```json review\n{not json\n```")

    def test_multi_rule_limit(self):
        many = {"v": 1, "rules": [{"id": i, "set": {}} for i in list(self.rows)[:20]]}
        with self.assertRaises(self.ar.ReviewError):
            self.ar.parse_payload(self.body(many))

    def test_csv_round_trips_unchanged(self):
        raw = build.DATA.joinpath("rules.csv").read_bytes().decode("utf-8")
        nl = "\r\n" if "\r\n" in raw else "\n"
        self.assertEqual(self.ar.write_rows(self.columns, self.rows, nl), raw)


class ScanTests(unittest.TestCase):
    ROW = """<tr><td><a href='/?pageid=27160&docid={id}'><span class="code">{code}</span></a></td>
    <td><span class="issued-date">31/10/2026</span></td>
    <td><a href='/?pageid=27160&docid={id}'><span class="substract">{title}</span></a></td></tr>"""

    def test_chinhphu_rows_and_keywords(self):
        import scan_portals as sp
        page = "<table>" + "".join(self.ROW.format(**r) for r in [
            {"id": 1, "code": "70/2026/TT-BCT", "title": "Quy định kiểm toán năng lượng"},
            {"id": 2, "code": "11066/VPCP-CN", "title": "thu phí điện tử đường bộ"},
            {"id": 3, "code": "567/TB-VPCP", "title": "Phó Thủ tướng Phạm Thị Thanh Trà"},
        ]) + "</table>"
        items = sp.parse({"adapter": "chinhphu", "url": "https://vanban.chinhphu.vn/"}, page)
        self.assertEqual([i["key"] for i in items], ["1", "2", "3"])
        self.assertEqual(items[0]["date"], "2026-10-31")
        self.assertTrue(items[0]["url"].startswith("https://vanban.chinhphu.vn/?pageid=27160&docid=1"))
        words, excl = ["năng lượng", "điện", "than"], ["điện tử"]
        self.assertEqual(sp.relevant(items[0], words, excl), ["năng lượng"])
        self.assertEqual(sp.relevant(items[1], words, excl), [])  # "điện tử" = electronic
        self.assertEqual(sp.relevant(items[2], words, excl), [])  # "Thanh" is not "than" (coal)

    def test_esdm_cards_and_source_filters(self):
        import scan_portals as sp
        card = ('<div class="newsbar-card"><h6 class="newsbar-card-title" title="{t}"><a href="/dokumen/view?id={i}">{t}</a></h6>'
                '<p><a href="/dokumen/download?id={i}.pdf">x</a></p></div>')
        page = "".join(card.format(i=i, t=t) for i, t in [
            (1, "Peraturan Menteri Energi dan Sumber Daya Mineral Nomor 12 Tahun 2026 tentang Perubahan"),
            (2, "Keputusan Menteri Energi dan Sumber Daya Mineral Nomor 409.K/MB.01/MEM.B/2026 tentang Harga Mineral Logam Acuan"),
            (3, "Dari Ruang Sidang ke Meja Perancangan: artikel"),
        ])
        src = {"adapter": "esdm", "url": "https://jdih.esdm.go.id/", "language": "id", "match_all": True,
               "require": "^(Peraturan|Keputusan)", "skip": ["Harga (Mineral )?(Logam )?Acuan"]}
        items = sp.parse(src, page)
        self.assertEqual([i["key"] for i in items], ["1"])
        self.assertEqual(items[0]["code"], "12/2026")
        self.assertTrue(items[0]["file"].endswith("/dokumen/download?id=1.pdf"))
        self.assertTrue(sp.hits_for(src, items[0], {"keywords": {}}))


class DraftTests(unittest.TestCase):
    def test_draft_rows_are_validated(self):
        import draft_entries as de
        data = build.load()
        hit = {"country": "ID", "language": "id", "url": "https://jdih.esdm.go.id/dokumen/view?id=1", "code": "12/2026",
               "title": "Peraturan Menteri ... Nomor 12 Tahun 2026", "file": "x.pdf"}
        d = {"in_scope": True, "scope_reason": "", "doc_type": "ministerial regulation", "number": "12/2026",
             "short_name": "Permen ESDM 12/2026", "issuing_body": "ESDM", "origin_sector": "energy",
             "energy_channel": ["supply"], "date_signed": "2026-10-20", "date_in_force": "next month",
             "title_original": "x", "title_english": "MEMR Regulation 12/2026", "summary_english": "Does things.",
             "topics": ["captive-power"], "amends": ["ID-PERMEN-ESDM-2021-11", "ID-MADE-UP"], "revokes": [],
             "status": "in force", "confidence": "medium", "notes": "check dates"}
        row, problems = de.to_row(data, hit, d)
        self.assertEqual(row["id"], "ID-PERMEN-ESDM-2026-12")
        self.assertEqual(row["amends"], "ID-PERMEN-ESDM-2021-11")
        self.assertEqual(row["date_in_force"], "")
        self.assertEqual(row["verification"], "unverified")
        self.assertEqual(len(problems), 2)

    def test_schema_enums_match_vocabularies(self):
        import draft_entries as de
        sch = de.schema(build.load())
        self.assertEqual(set(sch["required"]), set(sch["properties"]))
        self.assertIn("rooftop-solar", sch["properties"]["topics"]["items"]["enum"])

    def test_only_https_documents_are_fetched(self):
        import draft_entries as de
        for bad in ("file:///etc/passwd", "http://example.com/a.pdf", "ftp://x/y.pdf"):
            with self.assertRaises(ValueError):
                de.fetch_pdf(bad)


class AcceptDraftTests(unittest.TestCase):
    def test_parses_ids_and_csv_blocks(self):
        import accept_draft as ad
        cols = ["id", "country", "notes"]
        body = "x\n```csv\nID-A,ID,\"a, b\"\n```\n```csv\nid,country,notes\nID-B,ID,c\n```"
        self.assertEqual(ad.requested_ids("/accept ID-A, ID-B\nthanks"), ["ID-A", "ID-B"])
        self.assertEqual(ad.requested_ids("looks good"), [])
        rows = ad.drafted_rows(body, cols)
        self.assertEqual(set(rows), {"ID-A", "ID-B"})
        self.assertEqual(rows["ID-A"]["notes"], "a, b")


class SchemaTests(unittest.TestCase):
    def test_new_links_are_derived(self):
        data = build.load()
        self.assertIn("ID-PERPRES-2022-112", data.rules["ID-PERMEN-ESDM-2017-50"]["overridden_by"])
        self.assertIn("VN-DECREE-2025-57", data.rules["VN-LAW-2024-61"]["implemented_by"])
        self.assertEqual(data.rules["ID-UU-2020-11"]["revoked_by"], ["ID-PERPPU-2022-02"])

    def test_overrides_join_the_chain_but_implements_do_not(self):
        data = build.load()
        chain = {r["id"] for r in render.component(data, data.rules["ID-PERMEN-ESDM-2017-50"])}
        self.assertIn("ID-PERPRES-2022-112", chain)
        law_chain = {r["id"] for r in render.component(data, data.rules["VN-LAW-2024-61"])}
        self.assertNotIn("VN-DECREE-2025-57", law_chain)

    def test_validator_catches_new_field_errors(self):
        import shutil
        import tempfile
        tmp = Path(tempfile.mkdtemp())
        for f in build.DATA.glob("*.csv"):
            shutil.copy(f, tmp / f.name)
        text = (tmp / "rules.csv").read_text(encoding="utf-8")
        text = text.replace("ID-PERMEN-ESDM-2024-02,ID,,", "ID-PERMEN-ESDM-2024-02,ID,VN-XX,", 1)
        text = text.replace(",2024-01-29,2024-01-29,", ",2567-01-29,2024-01-29,", 1)
        (tmp / "rules.csv").write_text(text, encoding="utf-8")
        old = build.DATA
        try:
            build.DATA = tmp
            errors = build.load().errors
        finally:
            build.DATA = old
            shutil.rmtree(tmp)
        self.assertTrue(any("Buddhist Era" in e for e in errors))
        self.assertTrue(any("jurisdiction" in e for e in errors))

    def test_statuses_and_doc_types(self):
        for s in ("draft", "pending"):
            self.assertIn(s, build.STATUSES)
            self.assertNotIn(s, build.CURRENT)
        for d in ("emergency regulation", "advisory", "regulator determination", "code"):
            self.assertIn(d, build.DOC_TYPES)


class SearchFrameworkTests(unittest.TestCase):
    def test_framework_is_consistent(self):
        import search
        topics = set(build.load().topics)
        known = {r["code"] for r in build.read_csv(build.DATA / "countries.csv")[0]}
        known |= {r["code"] for r in build.read_csv(build.DATA / "pipeline.csv")[0]}
        errors, _ = search.validate(search.load(), topics, known)
        self.assertEqual(errors, [])

    def test_scan_config_comes_from_the_registry(self):
        import scan_portals as sp
        cfg = sp.load_config()
        self.assertEqual({s["id"] for s in cfg["sources"]}, {"vn-chinhphu", "id-esdm-jdih"})
        esdm = next(s for s in cfg["sources"] if s["id"] == "id-esdm-jdih")
        self.assertTrue(esdm["match_all"])
        self.assertIn("điện tử", cfg["exclude"]["vi"])

    def test_topics_are_suggested(self):
        import scan_portals as sp
        cfg = sp.load_config()
        item = {"code": "70/2026/TT-BCT", "title": "Quy định định mức kiểm toán năng lượng"}
        self.assertIn("energy-efficiency", sp.topics_for(item, cfg, "vi"))

    def test_search_plan_lists_sources_and_queries(self):
        import search
        import search_plan
        fw = search.load()
        module = next(m for m in fw["modules"] if m["id"] == "power-core")
        text = search_plan.plan(module, fw, build.load(), "ID", "rooftop-solar")
        self.assertIn("JDIH ESDM", text)
        self.assertIn('"PLTS atap"', text)
        self.assertIn("site:jdih.esdm.go.id", text)


class CategoryTests(unittest.TestCase):
    def test_every_topic_has_a_known_category(self):
        data = build.load()
        self.assertEqual(list(data.categories), ["electricity", "energy", "supply-chain", "trade"])
        for t in data.topics.values():
            self.assertIn(t["category"], data.categories)

    def test_rule_categories_follow_topics(self):
        data = build.load()
        r = data.rules["ID-PERMEN-ESDM-2019-11"]  # nickel ore export ban: mineral downstreaming + captive power
        self.assertEqual(r["categories"], ["electricity", "supply-chain"])

    def test_technologies_are_validated(self):
        data = build.load()
        self.assertIn("solar-pv", data.rules["ID-PERMEN-ESDM-2024-02"]["technologies"])
        for r in data.rules.values():
            for t in r["technologies"]:
                self.assertIn(t, build.TECHNOLOGIES)

    def test_undated_instruments_fall_back_to_date_in_force(self):
        self.assertEqual(render.plot_date({"date_signed": "", "date_in_force": "2020"}), "2020")
        self.assertEqual(render.plot_date({"date_signed": "2019-05", "date_in_force": "2020"}), "2019-05")
        svg = render.chain_svg([{"id": "A", "slug": "a", "short_name": "A", "status": "in force", "date_signed": "",
                                 "date_in_force": "", "amends": [], "revokes": [], "overrides": []}], "A", "")
        self.assertIn("<svg", svg)
