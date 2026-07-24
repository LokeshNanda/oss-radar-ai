# Roadmap

Goal: grow readership of the radar site and make the repo an easy-to-fork
"build your own radar" template — fully automated, low cost.
Full design: [specs/2026-07-24-popularity-roadmap-design.md](specs/2026-07-24-popularity-roadmap-design.md)

## Phase 0 — Discoverability quick wins
- [ ] MIT LICENSE
- [ ] GitHub repo topics + homepage URL → Pages site
- [ ] README overhaul (pitch, live-site link, screenshot, badges, how-it-works)
- [ ] MkDocs SEO basics: `site_url`, sitemap, meta descriptions

## Phase 1 — Content quality
- [ ] README-aware LLM analysis (fetch + truncate repo READMEs)
- [ ] New general-developer prompt (what it does / why interesting / how it works / get started / watch out for)
- [ ] Auto-categorization with per-category index pages
- [ ] Star-growth tracking with weekly deltas and biggest risers

## Phase 2 — Zero-manual distribution
- [ ] RSS/Atom feed
- [ ] JSON feed (`/api/latest.json`)
- [ ] Social cards (OG images) in CI
- [ ] Auto-updating repo README with the week's top 10
- [ ] Copy-paste social post drafts in each weekly report

## Phase 3 — Fork-your-own-radar template
- [ ] Config-driven radar scope (topic/language/query filters)
- [ ] OpenAI-compatible `base_url` support (OpenRouter, Groq, Ollama, …)
- [ ] Template-repo setup + 5-minute deploy docs, CONTRIBUTING.md, good-first-issues

## Phase 4 — Stickiness
- [ ] Trends dashboard (languages/categories over time)
- [ ] Biggest risers / hall-of-fame page
- [ ] Tag filtering + archive improvements

## Out of scope (for now)
Newsletter infrastructure, paid social APIs, databases, daily cadence, comments.
