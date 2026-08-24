---
title: CopilotKit/OpenBot
source: https://github.com/CopilotKit/OpenBot
stars: 2593
category: AI & Agents
---

# CopilotKit/OpenBot

- **URL**: https://github.com/CopilotKit/OpenBot
- **Stars**: 2593
- **Language**: TypeScript
- **Category**: AI & Agents
- **Topics**: ag-ui, agent-governance, ai-agents, browser-automation, copilotkit, generative-ui, mcp

## What it does
OpenBot is an agent platform that allows users to create AI coworkers, each with its own isolated environment, including a browser and files. It enables these agents to perform tasks while ensuring that all actions are governed and recorded for security and compliance.

## Why it's interesting
OpenBot differentiates itself by providing a comprehensive governance model for AI agents, allowing for fine-grained control over what each agent can do. It supports any AG-UI compliant agent, making it versatile and adaptable to various frameworks and custom implementations.

## How it works
OpenBot runs on Docker and uses PostgreSQL for data storage. Each agent operates in its own container, ensuring isolation and security. The platform employs a gateway that evaluates actions against defined policies before execution, maintaining an audit trail of all interactions. Configuration is managed through a `.env` file, and it requires integration with CopilotKit Intelligence for functionality. The README does not specify how the agents are trained or the specifics of the underlying AI models used, which leaves some uncertainty regarding their capabilities.

## Get started in 5 minutes
1. Clone the repository and create a `.env` file from `.env.example`.
2. Obtain CopilotKit Intelligence credentials and fill in the required values in `.env`.
3. Run the following commands:
   ```sh
   bun install
   bash scripts/start.sh
   ```
4. Access the application at <http://localhost:3010>.

## Watch out for
The project is currently in alpha status, indicating that it may have rough edges and bugs. Users should be cautious about deploying it in production environments. Additionally, it requires a CopilotKit Intelligence license, which may have associated costs depending on usage.
