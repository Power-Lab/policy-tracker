# Research brief: compiling a new economy

A reusable specification for compiling the scouting report and first entries for a new economy, by a person or an AI research assistant. See [../ADDING-A-COUNTRY.md](../ADDING-A-COUNTRY.md) for the full procedure. Replace `<cc>` with the ISO code and `<output directory>` with a working directory outside the repository.

The tracker records legal and policy instruments (laws, regulations, decrees, decisions, circulars, plans, notifications) in four categories. Read `data/rules.csv` for tone, `docs/SEARCH-PROTOCOL.md` for eligibility criteria and source tiers, and `docs/scouting/ph.md` for the report structure.

## Categories and topic ids (use only these ids)

| category | topic id | covers |
| --- | --- | --- |
| electricity | framework-law | principal electricity law and its amendments |
| electricity | power-plans | national power / generation / transmission plans |
| electricity | grid-market-rules | grid codes, network access, wholesale market rules |
| electricity | tariffs-ppa | retail tariffs, standard PPA terms |
| electricity | re-pricing | renewable pricing and procurement: FiTs, auctions, ceiling prices, RPS |
| electricity | rooftop-solar | rooftop and distributed solar, net metering |
| electricity | wheeling-dppa | wheeling, open access, direct and virtual PPAs, green tariffs |
| electricity | captive-power | own-use generation and its licensing |
| electricity | coal-phase-out | limits on new coal plants, early retirement |
| electricity | energy-storage | storage licensing, procurement, requirements |
| electricity | cross-border-trade | electricity imports/exports and interconnectors |
| energy | energy-strategy | economy-wide energy strategies and master plans |
| energy | energy-efficiency | efficiency standards, audits, demand-side programmes |
| energy | carbon-pricing | carbon tax, ETS, offsets, GHG reporting |
| energy | coal-supply | coal supply obligations and price caps |
| energy | ev-adoption | demand-side EV policy: purchase incentives, targets, charging rules |
| supply-chain | mineral-downstreaming | critical minerals: processing requirements, ore export bans, mineral strategies |
| supply-chain | local-content | local content requirements (e.g. TKDN, domestic content in auctions) |
| supply-chain | manufacturing-incentives | subsidies, tax incentives, production-linked incentives for clean-tech manufacturing |
| supply-chain | investment-rules | foreign investment rules, screening, ownership caps, investment approval |
| trade | import-tariffs | customs duties on clean-tech goods and inputs |
| trade | trade-remedies | anti-dumping, countervailing and safeguard duties |
| trade | import-standards | import approvals, approved lists, mandatory standards/certification (e.g. India ALMM, BIS) |
| trade | export-restrictions | export bans, quotas, licensing and controls |

## technologies field (optional, ";"-separated)

solar-pv, wind, batteries, electric-vehicles, grid-equipment, hydrogen. Leave empty when the instrument is not technology-specific.

## Output files (write to `<output directory>`)

1. `<cc>.md` per country: scouting report with sections: Summary; Legal hierarchy and document types; Official sources (table: name, URL, tier 1-4, languages, what it holds, access result you observed: HTTP status or "not tried"); Key instruments by category; Fit with the schema; Risks and open questions; Sources (every URL used).
2. `<cc>-rules.csv` per country, header exactly (32 columns):
   id,country,jurisdiction,doc_type,number,short_name,issuing_body,origin_sector,energy_channel,date_signed,date_in_force,title_original,title_english,summary_english,topics,technologies,amends,revokes,implements,overrides,link_basis,binding,grandfathered,status,status_checked,source_url,source_type,language,verification,reviewed_by,reviewed_on,notes
   Rules: id = COUNTRY-TYPE-YEAR-NUMBER uppercase (e.g. IN-NOTIF-MNRE-2019-ALMM). doc_type one of: law, emergency regulation, government regulation, presidential regulation, ministerial regulation, decree, decision, circular, advisory, code, regulator determination, directive, plan, regional plan, MoU, party resolution. origin_sector one of energy, mining, industry-trade, finance-fiscal, environment. energy_channel one or more of demand, supply, prices, investment, grid-access, emissions. Dates YYYY-MM-DD (or YYYY-MM / YYYY if that is all you can confirm). status one of in force, amended, pending, draft, replaced, revoked, expired; a row amended by another row in your file must be "amended", one revoked must be "revoked" or "replaced". amends/revokes/implements/overrides reference ids in your own file only. link_basis for rows with amends/revokes: express clause | implied by successor | expired. binding empty or "no". status_checked = the date of the research. source_type "document" if the URL is the instrument or its official page, else "portal-search". language = language of the binding text (en, hi, bn, ur, id, vi, th, ms). verification = unverified; reviewed_by/reviewed_on empty. summary_english: 2-3 neutral sentences on what it does, no evaluative language, no speculation. notes: start "Scouted from desk research (high|medium|low confidence)." then what a reviewer must check.
   Write the CSV with Python's csv module (QUOTE_MINIMAL, "\n" line endings).
3. `<cc>-country.csv`: header code,name,language,status,hierarchy,sources,intro (hierarchy ";"-separated highest to lowest, e.g. "Act of Parliament (law);Rules (government regulation)"; sources "Name|https://url;Name|https://url"; intro: 2-3 neutral sentences on how the power sector and industrial policy are organised; status "Scouted, unverified").
4. `<cc>-sources.csv`: header id,country,name,url,tier,kind,languages,access,checked,adapter,notes (id = lowercase cc-short-name; tier 1 gazette/official legal database, 2 issuing body listing, 3 legal register, 4 secondary; kind one of gazette, legal database, agency listing, legal register, secondary; access open|partial|restricted|unreachable|unknown from what you observed; checked = date if you tried it; adapter empty).

## Standards

- Since 2015 (the period of the lab's supply-chain brief), plus earlier instruments that recorded ones amend or depend on.
- Prefer official sources; secondary sources (law firms, think tanks, IEA policy database, news) may identify and date an instrument but say so in notes.
- Never invent numbers, dates or URLs. If unsure, leave the field empty (only date_in_force, number may not be empty: use "unnumbered (...)" when there is no number) and say so in notes.
- Run this check on each rules file and fix all problems before finishing:
  python3 -c "import csv,sys; sys.path.insert(0,'scripts'); import build; r=list(csv.DictReader(open(sys.argv[1],encoding='utf-8'))); ids={x['id'] for x in r}; print(len(r),'rows'); [print('BAD',x['id'],f,x[f]) for x in r for f,ok in [('doc_type',build.DOC_TYPES),('status',set(build.STATUSES)),('origin_sector',build.ORIGIN_SECTORS)] if x[f] not in ok]; [print('LINK',x['id'],t) for x in r for f in ('amends','revokes','implements','overrides') for t in build.split(x[f]) if t not in ids]; [print('EMPTY',x['id'],f) for x in r for f in build.REQUIRED if not x.get(f,'').strip()]" <output directory>/<cc>-rules.csv
- Run the check from the repository root. Write outputs outside the repository; they are merged after review (ADDING-A-COUNTRY.md steps 2, 3 and 7).
