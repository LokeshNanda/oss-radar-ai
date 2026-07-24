# Architecture

```
GitHub Search API → fetch → dedupe → summarize (LLM, JSON mode) → generate → MkDocs → GitHub Pages
```

## Modules (`src/open_source_radar_ai/`)

| Module | Responsibility |
| --- | --- |
| `config.py` | Env-var configuration (`AppConfig`, search scope via `RADAR_SEARCH_QUERY`) |
| `github_client.py` | GitHub REST API: trending search, README fetch, repo-by-id |
| `fetch.py` | Fetch + exclude-processed orchestration |
| `dedupe.py` | Processed-repo state (`.radar_state/processed_repos.json`) |
| `openai_client.py` | OpenAI-compatible chat client (OpenRouter/Groq/Ollama via `OPENAI_BASE_URL`) |
| `prompts.py` / `summarize.py` | README-aware structured analysis → `RepoAnalysis(markdown, category)` |
| `catalog.py` | Persistent catalog of all featured repos (`.radar_state/catalog.json`) — single data source for categories, feeds, trends |
| `stars.py` | Star-count snapshots per run (`.radar_state/star_history.json`), risers computation |
| `generator.py` | Repo pages, weekly reports (velocity, risers, social draft), index, archive |
| `category_pages.py` | Per-category index pages (`docs/categories/`) |
| `feeds.py` | RSS (`docs/feed.xml`) and JSON API (`docs/api/*.json`) |
| `readme_updater.py` | Rewrites the README radar section between `<!-- RADAR:START/END -->` markers |
| `trends.py` | `docs/trends.md` — categories/languages over time |
| `hall_of_fame.py` | `docs/hall-of-fame.md` — all-time top repos + recent risers |
| `backfill.py` | One-time `radar-backfill` CLI: catalog + categorize historical pages |
| `pipeline.py` | Orchestrates a full run |
| `cli.py` | Entry points: `radar-run`, `radar-fetch`, `radar-backfill` |

## Design principles

- Deterministic, idempotent file generation (`io_utils` atomic writes — reruns produce no diff noise)
- Graceful degradation: README/LLM/API failures log and skip, never crash the run
- No secrets in code; everything configured via env vars (see `.env.example`)
- State and generated pages are committed by CI, so every run is reproducible and diffable
