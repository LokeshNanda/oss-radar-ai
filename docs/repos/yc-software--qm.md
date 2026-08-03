---
title: yc-software/qm
source: https://github.com/yc-software/qm
stars: 7598
category: AI & Agents
---

# yc-software/qm

- **URL**: https://github.com/yc-software/qm
- **Stars**: 7598
- **Language**: TypeScript
- **Category**: AI & Agents
- **Topics**: None

## What it does
QM is a multiplayer agent harness designed for startups, allowing employees to work independently in isolated workspaces while collaborating with the agent in Slack and web channels. It supports various AI models and provides features like scoped memory, file management, and custom internal apps.

## Why it's interesting
Unlike traditional personal assistants, QM is built for organizational use, enabling multiple users to customize their agents while maintaining collaboration. Its architecture allows for easy switching between different AI models and harnesses, promoting flexibility and open-source principles.

## How it works
QM operates with a central core that uses a Postgres database for persistence and runs on TypeScript with Node.js. It features a headless core that interacts with various plugins (Slack, web UI) and employs a scoped sandbox for each user. The README outlines a deployment process that does not require source checkout, but specifics on deployment workflows or CI integration are not detailed.

## Get started in 5 minutes
To initialize a deployment, run the following command:
```bash
npm exec --yes --package=@yc-software/qm@latest -- \
  qm init . --org <slug> --target <fly-or-aws>
npm install
```
This command sets up the necessary configuration for your organization.

## Watch out for
The repository is relatively new, created in July 2026, which may indicate limited maturity or community support. The README mentions a lack of production deployment workflows, and security practices depend on the chosen security posture, which could introduce risks if not properly managed.
