---
title: CopilotKit/OpenDots
source: https://github.com/CopilotKit/OpenDots
stars: 3425
category: AI & Agents
---

# CopilotKit/OpenDots

- **URL**: https://github.com/CopilotKit/OpenDots
- **Stars**: 3425
- **Language**: TypeScript
- **Category**: AI & Agents
- **Topics**: None

## What it does
OpenDots is an open-source template for creating persistent AI agents that can interact through text, calls, and Slack. It allows users to define custom agents (Dots) that can perform tasks, manage documents, and facilitate conversations in a workspace environment.

## Why it's interesting
Unlike typical AI chatbots, OpenDots provides a framework for building customizable agents that operate in a persistent environment, maintaining state and context across interactions. It integrates with various services, including Slack and WebRTC for calls, and emphasizes a self-hosted approach, giving developers control over their deployments.

## How it works
OpenDots is built using TypeScript and relies on the CopilotKit and AG-UI frameworks for its architecture. It features a modular design where each Dot can have its own computer environment, allowing for isolated execution of tasks. The application supports a range of functionalities, including document management, conversation threads, and integration with external services. However, some features, such as connected-service verification for Slack and speech capabilities, are still pending confirmation.

## Get started in 5 minutes
To get started, clone the repository:
```sh
git clone https://github.com/CopilotKit/OpenDots.git
cd OpenDots
npm ci
cp .env.example .env
npm run dev
```
Then, open your browser at `http://127.0.0.1:5173` to begin configuring your agents and creating Spaces.

## Watch out for
The project is currently in an alpha state, indicating that it may have incomplete features and potential instability. Some functionalities, such as multi-user support and richer content management, are not yet implemented. Additionally, while the license is MIT, developers should be cautious about the security implications of self-hosting AI agents and managing sensitive data.
