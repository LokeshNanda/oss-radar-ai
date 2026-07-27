# 📡 Open Source Radar AI

**AI-curated radar of GitHub's hottest new repositories — analyzed, categorized, and published automatically every week.**

[![Open Source Radar](https://github.com/LokeshNanda/oss-radar-ai/actions/workflows/trending.yml/badge.svg)](https://github.com/LokeshNanda/oss-radar-ai/actions/workflows/trending.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Live site](https://img.shields.io/badge/Live%20site-oss--radar--ai-blue)](https://lokeshnanda.github.io/oss-radar-ai/)

👉 **Read this week's radar: [lokeshnanda.github.io/oss-radar-ai](https://lokeshnanda.github.io/oss-radar-ai/)**
📶 Subscribe: [RSS feed](https://lokeshnanda.github.io/oss-radar-ai/feed.xml) · Build on it: [JSON API](https://lokeshnanda.github.io/oss-radar-ai/api/latest.json)

Every Monday, this project finds the most-starred repositories created on GitHub in the last 7 days, generates an honest developer-focused breakdown of each one with an LLM (what it does, why it's interesting, how it works, how to try it, what to watch out for), and publishes everything as a static site — with zero manual steps.

---

## 📡 This week's radar

<!-- RADAR:START -->
_Week of 2026-07-27_

- [`slvDev/esp32-ai`](https://github.com/slvDev/esp32-ai) ([analysis](https://lokeshnanda.github.io/oss-radar-ai/repos/slvdev--esp32-ai/))
- [`mikiarlo3/ai-copywriter`](https://github.com/mikiarlo3/ai-copywriter) — An AI copywriter that uses real copywriting skills + real marketing knowledge with human tone. ([analysis](https://lokeshnanda.github.io/oss-radar-ai/repos/mikiarlo3--ai-copywriter/))
- [`mshumer/Claude-of-Duty`](https://github.com/mshumer/Claude-of-Duty) — A Call of Duty-quality FPS in Three.js, built from a single prompt. ([analysis](https://lokeshnanda.github.io/oss-radar-ai/repos/mshumer--claude-of-duty/))
- [`gnipbao/story-to-handdrawn-video`](https://github.com/gnipbao/story-to-handdrawn-video) — Agent skill: convert Chinese story copy or ordered images into a hand-drawn diary-comic animation (silent MP4 picture track). ([analysis](https://lokeshnanda.github.io/oss-radar-ai/repos/gnipbao--story-to-handdrawn-video/))
- [`makecindy/cindy`](https://github.com/makecindy/cindy) — Consider it done. The open-source AI agent that works out of the box · 想到，就能做到。开源、开箱即用的 AI Agent。 ([analysis](https://lokeshnanda.github.io/oss-radar-ai/repos/makecindy--cindy/))
<!-- RADAR:END -->

---

## ⚙️ How it works

```mermaid
flowchart LR
    A[GitHub Search API<br/>top new repos of the week] --> B[Dedupe against<br/>processed state]
    B --> C[Fetch each repo's README]
    C --> D[LLM analysis<br/>structured JSON output]
    D --> E[Markdown pages<br/>reports, categories, feeds]
    E --> F[MkDocs Material build]
    F --> G[GitHub Pages deploy]
```

Everything runs in a single scheduled GitHub Actions workflow ([`trending.yml`](.github/workflows/trending.yml)). Generated pages and state are committed back to the repo, so every run is reproducible and diffable.

## ✨ Features

- **Weekly radar reports** — the top 10 new repositories, ranked by stars
- **Developer-focused AI analysis** — grounded in each repo's README, honest about uncertainty, no hype
- **Deterministic & idempotent** — same inputs produce byte-identical output; repos are never analyzed twice
- **Fully automated** — fetch → analyze → publish with no human in the loop
- **Cheap to run** — roughly $0.05/week with `gpt-4o-mini`

## 🍴 Run your own radar

This project is designed to be forked. Point it at your favorite niche — a **Rust radar**, an **AI-agents radar**, a **security radar** — by changing a couple of environment variables, adding an API key, and enabling GitHub Pages. Follow the [10-minute setup guide](https://lokeshnanda.github.io/oss-radar-ai/run-your-own/).

## 🚀 Local development

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -e ".[dev]"

# run the test suite
python -m pytest tests -q

# run the pipeline (needs OPENAI_API_KEY, optional GITHUB_TOKEN)
cp .env.example .env        # then fill in your keys
radar-run

# preview the site
mkdocs serve
```

### Configuration

| Variable | Default | Purpose |
| --- | --- | --- |
| `OPENAI_API_KEY` | — | Required. LLM API key |
| `OPENAI_MODEL` | `gpt-4o-mini` | Model used for analysis |
| `OPENAI_BASE_URL` | `https://api.openai.com` | Any OpenAI-compatible endpoint |
| `GITHUB_TOKEN` | — | Optional. Raises GitHub API rate limits |
| `GITHUB_PER_PAGE` | `10` | Repos fetched per run |
| `GITHUB_DAYS_BACK` | `7` | Lookback window in days |
| `RADAR_MAX_REPOS_PER_RUN` | `10` | Cap on repos analyzed per run |

## 🗺 Roadmap

See [ROADMAP.md](ROADMAP.md) and the [design spec](specs/2026-07-24-popularity-roadmap-design.md).

## 📄 License

[MIT](LICENSE)
