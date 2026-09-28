---
title: mikehasa/golive-skill
source: https://github.com/mikehasa/golive-skill
stars: 1029
category: Developer Tools
---

# mikehasa/golive-skill

- **URL**: https://github.com/mikehasa/golive-skill
- **Stars**: 1029
- **Language**: TypeScript
- **Category**: Developer Tools
- **Topics**: agent-skill, agent-skills, ai-agents, claude-code, cloudflare, codex, database, deployment, developer-tools, devops, dns, godaddy, hosting, infrastructure, neon, netlify, porkbun, skills, supabase, vercel

## What it does
GoLive is an open-source tool that automates the deployment of agent-built applications, managing hosting, databases, domains, email, and payments on the user's accounts. It detects the necessary resources, plans the deployment, requires user approval, applies the changes, and verifies the outcome.

## Why it's interesting
Unlike traditional deployment tools, GoLive integrates directly with coding agents, allowing for a conversational interface to manage deployments. It emphasizes user control by requiring approval for every action and provides a teardown process to clean up resources, which is not commonly found in similar tools.

## How it works
GoLive operates as a Node CLI that interacts with various service providers (e.g., Vercel, Netlify, Supabase) to provision resources based on user input. It uses a series of commands to detect requirements, create deployment plans, and execute them only after user approval. The architecture is designed to ensure that no changes are made without explicit consent, and it includes features for rollback and resource teardown. However, the README mentions that some features are still in alpha and may not be fully validated.

## Get started in 5 minutes
To install GoLive, run the following command in your terminal:
```bash
npx skills add https://github.com/mikehasa/golive-skill --skill golive --global
```
After installation, you can use it by prompting your coding agent with a command like:
```text
Use the golive skill to take this app live.
```

## Watch out for
GoLive is currently in early alpha (version 0.1.0-alpha.5), which indicates that it may have incomplete features and stability issues. Users should be cautious about using it in production environments until it matures. Additionally, the README notes that some integrations and functionalities are not fully validated, and there are security considerations regarding credential management.
