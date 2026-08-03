---
title: trycompai/crm
source: https://github.com/trycompai/crm
stars: 1925
category: AI & Agents
---

# trycompai/crm

- **URL**: https://github.com/trycompai/crm
- **Stars**: 1925
- **Language**: TypeScript
- **Category**: AI & Agents
- **Topics**: None

## What it does
This repository hosts a CRM (Customer Relationship Management) system that integrates an AI research agent designed to autonomously manage and record customer interactions. Unlike traditional CRMs, which rely heavily on user input, this system allows the agent to operate independently, making decisions about follow-ups and data collection.

## Why it's interesting
The CRM is built around the concept of an 'agentic-first' approach, where the AI agent is the core functionality rather than an add-on feature. It emphasizes a strict policy against guessing or inferring data about individuals, focusing instead on recording observed facts, which could reduce misinformation in customer records.

## How it works
The architecture is a monorepo using Turborepo with a stack that includes Bun for runtime, Next.js for the front end, and NestJS for the API. The agent operates independently, processing tasks from a queue and interacting with various data sources only when configured to do so. It uses a unique sandbox environment to ensure security, preventing unauthorized data access. The README does not specify how the agent's decision-making process is implemented beyond its operational independence, leaving some details about its internal logic uncertain.

## Get started in 5 minutes
1. Clone the repository: `git clone https://github.com/trycompai/crm.git && cd crm`
2. Install dependencies: `bun install`
3. Start the Postgres database: `docker compose up -d`
4. Set up the environment variables by copying `.env.example` to `.env` and filling in the required values.
5. Run the application: `bun run dev` and access it at [localhost:3000](http://localhost:3000).

## Watch out for
The project is relatively new, created in July 2026, and has not yet established a large user base (1925 stars). The authorization model is very simplistic, relying solely on Google sign-in, which may not suit all use cases. Additionally, the README advises caution when pointing the CRM at real customer data, highlighting potential security concerns.
