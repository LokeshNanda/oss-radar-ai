---
title: yetone/cumora
source: https://github.com/yetone/cumora
stars: 3027
category: AI & Agents
---

# yetone/cumora

- **URL**: https://github.com/yetone/cumora
- **Stars**: 3027
- **Language**: TypeScript
- **Category**: AI & Agents
- **Topics**: None

## What it does
Cumora is a cross-platform team chat application that integrates AI agents as active participants in conversations alongside human users. It allows for real-time collaboration, task management, and communication through a shared interface that includes features like DMs, group chats, Kanban boards, and calendars.

## Why it's interesting
Cumora differentiates itself by treating AI agents as first-class teammates, capable of holding personas, memory, and coordinating tasks autonomously. This contrasts with typical chat applications where bots are limited to responding to user prompts. Additionally, it offers flexibility in deployment, allowing users to either use Cumora's cloud service or run their own agents locally.

## How it works
The architecture consists of a React frontend and a stateless Node.js backend using Express, with PostgreSQL for data storage and Redis for real-time messaging and presence. Agents operate in Kubernetes pods in the cloud or as local daemons, communicating through a common CLI protocol. The README provides details on the coordination mechanism that prevents agents from interfering with each other during interactions. However, specifics about the AI models used beyond OpenAI's API are not detailed, leaving some uncertainty about the full capabilities of the BYOA (Bring Your Own Agent) feature.

## Get started in 5 minutes
To run Cumora locally, ensure you have PostgreSQL and Redis installed. Create a database, set the `OPENAI_API_KEY`, and run the following commands:
```bash
createdb -h localhost cumora
export OPENAI_API_KEY=sk-...
npm run setup
npm run dev:all
```
Then, access the app at `http://localhost:5180` for PWA mode or run `npm run electron:dev` for the desktop version.

## Watch out for
The repository is relatively new, created in August 2026, which may indicate that it is still in active development and could have stability issues. Additionally, while the README covers many aspects, it lacks detailed information on licensing and security practices beyond a brief mention of a `SECURITY.md` file for vulnerability reporting.
