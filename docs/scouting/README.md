# Country scouting

Desk research on the countries after Indonesia and Vietnam, done in November 2026. Each report covers how the power sector is organised, the legal hierarchy, the official sources (and whether they can be scraped), the key rules since about 2017 by topic, how well they fit the schema, possible partner institutes, and risks.

| Country | Report | Candidate rules | Recommendation |
| --- | --- | --- | --- |
| Philippines | [ph.md](ph.md) | [30](ph-candidates.csv) | Next country. English, regular numbering, close topic fit. Needs access to ERC documents and OCR. |
| Thailand | [th.md](th.md) | [29](th-candidates.csv) | Go ahead with a Thai-reading reviewer, and decide first how to record resolutions and drafts. |
| Malaysia | [my.md](my.md) | [30](my-candidates.csv) | Peninsular Malaysia plus Sabah. Decide first how to record guideline revisions and state law. |
| Singapore, Cambodia, Lao PDR, Brunei, Timor-Leste, Myanmar | [rest-of-asean.md](rest-of-asean.md) | in the report | Singapore, then Cambodia, then Lao PDR (after its new Electricity Law), then light profiles of Brunei and Timor-Leste. Myanmar last, as a watch list. |

**These are leads, not tracker rows.** Candidates come from web research and have not been checked against the binding text. When a country's phase starts, each candidate is checked by a reviewer, converted to the full schema and added to `data/rules.csv` as `unverified` until verified.

Check the candidate files against the tracker's vocabularies with:

```bash
python3 scripts/check_candidates.py
```

The schema changes the scouting points to are collected in [../SCHEMA-NOTES.md](../SCHEMA-NOTES.md) (items 11–20).
