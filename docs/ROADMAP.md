# Roadmap

Status: ✅ done · ⏳ next · 💭 later

## Objective

A public dataset, with a website, from which a user can determine which instrument governs a given issue in a given economy, what its legal status is, and which earlier instruments it amended or replaced, across electricity, energy, clean technology supply chains and trade. The dataset supports the Power Transformation Lab's research on clean energy deployment, manufacturing and trade in Asia-Pacific, and should remain inexpensive to keep current.

## Principles

1. **One page per instrument**, with a stable address that can be cited.
2. **The CSV files in `data/` are the single source of truth.** Pages, downloads and charts are generated from them.
3. **Verification is reported explicitly.** Every entry shows its status and verification level.
4. **No server.** Python and Jinja2 generate static files hosted on GitHub Pages, which keeps maintenance and transfer simple.
5. **Lab presentation.** The site follows the Power Transformation Lab's visual identity (pwrlab.org).

## Status

### Site and data model ✅
- Pages per instrument, country, topic and category; explore with filters; country comparison; timeline; updates log and Atom feed; data downloads.
- Four categories (electricity; energy and climate; supply chain and industrial policy; trade) with 24 topics, and a technology field.
- Schema for amendment, revocation, implementation and partial override; draft and pending statuses; jurisdiction for sub-national law ([SCHEMA-NOTES.md](SCHEMA-NOTES.md)).

### Review workflow ✅
- Reviewer view; review issues become pull requests automatically; multi-rule reviews; change history per instrument ([REVIEWING.md](REVIEWING.md)).

### Search framework ✅
- Search and inclusion protocol, source registry, multilingual vocabulary, search-plan generator, weekly portal scan with optional model-drafted entries ([SEARCH-PROTOCOL.md](SEARCH-PROTOCOL.md)).

### Coverage
- ✅ Electricity and selected cross-sector instruments: Indonesia, Viet Nam, Thailand, the Philippines, Malaysia (all unverified).
- ✅ Supply chain, trade and EV adoption instruments for the same five economies (57, unverified).
- ⏳ India, Australia, Pakistan and Bangladesh, completing the nine economies of the lab's 2026 Asia-Pacific green economic transition brief.
- 💭 Singapore, Cambodia, Lao PDR, Brunei, Timor-Leste and Myanmar ([scouting/rest-of-asean.md](scouting/rest-of-asean.md)); China as the main reference economy for supply chains.

### Next
- ⏳ Country reviewers, beginning with verification of existing entries.
- ⏳ Native-speaker review of the search vocabulary; vocabulary for Hindi, Bengali, Urdu and other languages as needed.
- ⏳ Portal adapters for open tier 1–2 sources (EPPO resolutions, DOE Philippines, Energy Commission Malaysia, and sources for the new economies).
- 💭 Archived copies of source documents; a quarterly written summary of changes.

## Open questions
- Whether to include utility-issued rules and sub-national rules beyond the cases already covered.
- Custom domain under pwrlab.org, and a link from the lab website.
- Analytics: none at present; a privacy-preserving option could be added if usage statistics are needed.
