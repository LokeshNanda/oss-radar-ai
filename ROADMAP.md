# Roadmap

Goal: grow readership of the radar site and make the repo an easy-to-fork
"build your own radar" template — fully automated, low cost.
Full design: [specs/2026-07-24-popularity-roadmap-design.md](specs/2026-07-24-popularity-roadmap-design.md)

## Phase 0 — Discoverability quick wins
- [x] MIT LICENSE
- [ ] GitHub repo topics + homepage URL → Pages site *(manual: Settings → About)*
- [x] README overhaul (pitch, live-site link, badges, how-it-works)
- [x] MkDocs SEO basics: `site_url`, sitemap, meta descriptions

## Phase 1 — Content quality
- [x] README-aware LLM analysis (fetch + truncate repo READMEs)
- [x] New general-developer prompt (what it does / why interesting / how it works / get started / watch out for)
- [x] Auto-categorization with per-category index pages
- [x] Star-growth tracking with weekly deltas and biggest risers
- [x] `radar-backfill` CLI for historical pages *(run again with an API key to LLM-categorize the 230 backfilled pages)*

## Phase 2 — Zero-manual distribution
- [x] RSS feed (`feed.xml`)
- [x] JSON API (`api/latest.json`, `api/catalog.json`)
- [x] Social cards (OG images) in CI
- [x] Auto-updating repo README with the week's top 10
- [x] Copy-paste social post drafts in each weekly report

## Phase 3 — Fork-your-own-radar template
- [x] Config-driven radar scope (`RADAR_SEARCH_QUERY`, site name/description env)
- [x] OpenAI-compatible `base_url` support (OpenRouter, Groq, Ollama)
- [x] "Run your own" 10-minute guide + CONTRIBUTING.md
- [ ] Mark repo as a GitHub template + seed good-first-issues *(manual: Settings → Template repository)*

## Phase 4 — Stickiness
- [x] Trends page (categories/languages over time)
- [x] Hall of fame (all-time top + recent risers)
- [x] Archive grouped by month

## Ideas for later
Newsletter, per-category RSS feeds, Atom feed, richer trend charts, daily cadence option.
