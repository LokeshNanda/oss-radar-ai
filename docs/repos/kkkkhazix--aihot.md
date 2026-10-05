---
title: KKKKhazix/AIHOT
source: https://github.com/KKKKhazix/AIHOT
stars: 5914
category: AI & Agents
---

# KKKKhazix/AIHOT

- **URL**: https://github.com/KKKKhazix/AIHOT
- **Stars**: 5914
- **Language**: TypeScript
- **Category**: AI & Agents
- **Topics**: ai, chinese, content-curation, daily-digest, docker-compose, llm, mcp, news-aggregator, postgresql, rss, self-hosted, typescript

## What it does
AIHOT is a framework for creating personalized news aggregation sites that utilize AI to collect, filter, and summarize news articles from various sources. It generates daily, weekly, and monthly reports based on the aggregated content, allowing users to customize the sources and selection criteria according to their industry needs.

## Why it's interesting
Unlike typical news aggregators, AIHOT leverages AI models to not only filter content but also to cluster related articles into single events and rank them based on their popularity across different sources. This approach allows for a more nuanced understanding of news trends and enables users to tailor the platform to specific industries without needing extensive coding knowledge.

## How it works
AIHOT operates by ingesting data from multiple sources, which are then processed through a series of AI-driven steps: deduplication, scoring, summarization, and clustering. The architecture includes Node.js, TypeScript, PostgreSQL, and Docker for deployment. The README indicates that the core engine is the same as the live site, but it lacks detailed information on the internal data flow or specific AI models used, leaving some uncertainty about the implementation details.

## Get started in 5 minutes
To quickly set up AIHOT, clone the repository and run the following commands:
```bash
git clone https://github.com/KKKKhazix/AIHOT.git myhot
cd myhot
node scripts/init-env.ts --llm-key <你的模型 API Key>
docker compose up -d --build
```
After a few minutes, access the site at `http://localhost:3000`.

## Watch out for
The project is relatively new, created in September 2026, and while it has garnered significant interest with over 5,900 stars, it may still have unresolved issues or incomplete features. The README also notes that the author is not a professional developer, which could imply potential code quality concerns. Additionally, users are advised not to use the AIHOT name and logo, as they are not included in the MIT license.
