---
title: Run your own radar
---

# 🍴 Run your own radar

This project is a template for building an automated, AI-curated radar of new GitHub repositories in **any niche you care about** — a Rust radar, an AI-agents radar, a security radar. Setup takes about 10 minutes and runs itself weekly after that.

## 1. Fork the repository

Fork [LokeshNanda/oss-radar-ai](https://github.com/LokeshNanda/oss-radar-ai) on GitHub.

## 2. Add your LLM API key

In your fork: **Settings → Secrets and variables → Actions → New repository secret**

- Name: `OPENAI_API_KEY`
- Value: your API key

**Cost:** roughly **$0.05/week** with the default `gpt-4o-mini`. You can also use any OpenAI-compatible provider — OpenRouter, Groq, or a self-hosted Ollama — by setting `OPENAI_BASE_URL` and `OPENAI_MODEL` (see step 4).

## 3. Enable GitHub Pages

**Settings → Pages → Build and deployment → Source: GitHub Actions**

## 4. Scope your radar (optional)

Add repository **variables** (Settings → Secrets and variables → Actions → Variables tab) to customize your radar:

| Variable | Example | Effect |
| --- | --- | --- |
| `RADAR_SEARCH_QUERY` | `topic:rust language:rust` | Only track new Rust repos |
| `RADAR_SITE_NAME` | `Rust Radar` | Site title |
| `RADAR_SITE_DESCRIPTION` | `New Rust repos, analyzed weekly` | Site description / SEO |
| `RADAR_SITE_URL` | `https://you.github.io/oss-radar-ai/` | Used in feeds and links |

More query ideas: `topic:ai language:python`, `topic:security`, `topic:kubernetes`, `stars:>100 topic:llm`. Any [GitHub search qualifier](https://docs.github.com/en/search-github/searching-on-github/searching-for-repositories) works.

Then wire them into the workflow's env block in `.github/workflows/trending.yml`:

```yaml
      - name: Run radar pipeline
        env:
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          RADAR_LOG_LEVEL: INFO
          RADAR_SEARCH_QUERY: ${{ vars.RADAR_SEARCH_QUERY }}
          RADAR_SITE_NAME: ${{ vars.RADAR_SITE_NAME }}
          RADAR_SITE_DESCRIPTION: ${{ vars.RADAR_SITE_DESCRIPTION }}
          RADAR_SITE_URL: ${{ vars.RADAR_SITE_URL }}
        run: |
          radar-run

      - name: Build MkDocs site
        env:
          RADAR_SITE_NAME: ${{ vars.RADAR_SITE_NAME }}
          RADAR_SITE_DESCRIPTION: ${{ vars.RADAR_SITE_DESCRIPTION }}
        run: |
          mkdocs build --strict
```

Also reset the state and reports from the original radar so yours starts fresh:

```bash
rm -f .radar_state/*.json docs/repos/*.md docs/reports/*.md docs/categories/*.md
```

### Using a different LLM provider

Set these as repository secrets/variables and pass them into the pipeline env:

```
# OpenRouter
OPENAI_BASE_URL=https://openrouter.ai/api/v1
OPENAI_MODEL=openai/gpt-4o-mini

# Groq
OPENAI_BASE_URL=https://api.groq.com/openai/v1
OPENAI_MODEL=llama-3.3-70b-versatile
```

## 5. Run it

**Actions → Open Source Radar → Run workflow.** Your radar site publishes to `https://<you>.github.io/oss-radar-ai/` and re-runs automatically every Monday.

---

Questions or improvements? [Open an issue](https://github.com/LokeshNanda/oss-radar-ai/issues) or see [CONTRIBUTING](https://github.com/LokeshNanda/oss-radar-ai/blob/main/CONTRIBUTING.md).
