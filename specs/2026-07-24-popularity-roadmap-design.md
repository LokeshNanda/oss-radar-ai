# Popularity Roadmap — Design Spec

**Date:** 2026-07-24
**Status:** Approved
**Goal:** Grow readership of the Open Source Radar site first, and grow repo stars by making the project an easy-to-fork "build your own radar" template. All growth mechanisms must be fully automated and low cost (no manual weekly obligations, no paid distribution APIs).
**Audience:** General developers (broadened from the current enterprise-architect tone). Analytical, no-hype voice is retained.

## Current state (analysis summary)

- Weekly GitHub Actions pipeline (Mondays, `trending.yml`): searches GitHub for the top 10 most-starred repos created in the last 7 days, generates one LLM analysis per repo from **metadata only** (name, description, stars, language, topics), writes MkDocs pages, deploys to GitHub Pages. Dedupe state in `.radar_state/processed_repos.json`.
- ~20 weekly reports, ~230 repo pages since 2026-02.
- Codebase is modular (`fetch` / `summarize` / `generator` / `pipeline`) and easy to extend.

**Popularity blockers identified:**
1. Repo has no LICENSE, no GitHub topics, no homepage URL, minimal README → near-zero discoverability, and unlicensed code deters sharing/forking.
2. LLM analysis never sees the README → output is generic and hedged ("likely…", "suggests…"), which limits shareability and return visits.
3. No subscription or syndication surface (no RSS, no JSON feed, no social cards, no SEO basics like `site_url`/sitemap).
4. No categorization, no trend data, no reason to browse beyond the latest report.
5. Radar scope is hardcoded → forks can't easily become "Rust Radar" / "AI Agent Radar".

## Strategy

Content-quality first, then distribution, then the fork-template angle:
distribution amplifies whatever exists, so the analysis must be genuinely good before pointing new eyeballs at it. The template angle is the strongest repo-star driver and follows once the flagship site demonstrates the concept.

## Phases

### Phase 0 — Discoverability quick wins
- Add MIT `LICENSE`.
- Set GitHub repo topics (`github-trending`, `llm`, `ai`, `open-source`, `mkdocs`, `github-actions`, `developer-tools`) and homepage URL → the Pages site.
- README overhaul: one-line pitch, live-site link, screenshot, badges (build status, license, site), "how it works" diagram, "run your own radar" teaser.
- MkDocs SEO basics: `site_url`, sitemap, meta descriptions.

### Phase 1 — Content quality (core bet)
- **README-aware analysis:** fetch each repo's README via the GitHub API, truncate to a token budget (~4–6k tokens), include in the prompt. Use a mini-tier model to keep weekly cost in the $0.01–0.05 range.
- **New prompt for general devs**, sections: What it does · Why it's interesting · How it works under the hood · Get started in 5 minutes · Watch out for (maturity/caveats). Honest about uncertainty; no marketing tone.
- **Auto-categorization:** the same LLM call returns structured output including one category from a fixed set (AI/Agents, DevTools, Web, Data, Infra, Security, Languages, Other). Categories render as tags on repo/report pages and get per-category index pages.
- **Star-growth tracking:** extend `.radar_state` to store star snapshots per run; pages show weekly deltas; reports flag the biggest risers.

### Phase 2 — Zero-manual distribution
- **RSS/Atom feed** for weekly reports.
- **JSON feed** (`/api/latest.json` + per-week JSON) so others can build on the data (backlinks, integrations).
- **Social cards** via mkdocs-material's social plugin (generated in CI) so shared links render OG images.
- **Auto-updating repo README:** pipeline writes the current week's top 10 into the GitHub README each run.
- **Copy-paste social drafts:** each weekly report page includes a pre-written LinkedIn/X post block (no posting automation, no obligation).

### Phase 3 — "Fork your own radar" template
- Config-driven radar scope: topic/language/query filters via config so a fork becomes a niche radar in minutes.
- OpenAI-compatible `base_url` support (OpenRouter, Groq, Ollama, …) so forkers aren't locked to one provider.
- GitHub template-repo setup + "deploy your own in 5 minutes" docs, `CONTRIBUTING.md`, seeded good-first-issues.

### Phase 4 — Stickiness (later)
- Trends dashboard page (languages/categories over time from accumulated state).
- "Biggest risers" / hall-of-fame page.
- Tag filtering, archive improvements.

## Out of scope (YAGNI)
Newsletter infrastructure, paid social APIs, databases, daily cadence, comment systems, analytics backends.

## Error handling & constraints
- README fetch failures degrade gracefully to metadata-only analysis (current behavior).
- All generation stays deterministic/idempotent per existing design principles; feeds and README updates are regenerated, not appended.
- Secrets stay in env vars; no new secret types required until Phase 3 (optional alternate LLM keys).

## Success criteria
- Phase 0: repo is licensed, topic-tagged, and the site is indexed by search engines.
- Phase 1: repo pages contain concrete, README-grounded specifics (no hedging boilerplate); every repo has a category.
- Phase 2: a reader can subscribe (RSS) and a developer can consume the data (JSON) with zero manual steps per week.
- Phase 3: a stranger can fork and have their own themed radar live in under 15 minutes.
