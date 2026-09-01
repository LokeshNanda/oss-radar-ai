---
title: XiaoDuoYa/codex-with-chatgpt
source: https://github.com/XiaoDuoYa/codex-with-chatgpt
stars: 2068
category: AI & Agents
---

# XiaoDuoYa/codex-with-chatgpt

- **URL**: https://github.com/XiaoDuoYa/codex-with-chatgpt
- **Stars**: 2068
- **Language**: TypeScript
- **Category**: AI & Agents
- **Topics**: ai-agents, chatgpt, codex, mcp, model-context-protocol, oauth

## What it does
This repository allows users to leverage ChatGPT as a planning and review tool while using Codex for execution. It connects the ChatGPT web app to Codex through a secure, read-only MCP (Model Context Protocol) bridge, enabling efficient coding sessions without the need for API keys or reverse proxies.

## Why it's interesting
Unlike traditional setups that require API keys and direct integration with Codex, this project utilizes the existing ChatGPT web subscription to handle planning and review tasks, effectively reducing the consumption of Codex API tokens. This approach also emphasizes security by ensuring that sensitive files never leave the local environment.

## How it works
The architecture consists of a loopback HTTP server that manages a secure connection between ChatGPT and Codex. It employs OAuth 2.1 for authentication and uses a read-only MCP to allow ChatGPT to access only the necessary lines of code from the local workspace. The system operates with a clear separation of control and data planes, ensuring that no sensitive data is exposed during the process. However, the README does not specify how the system handles potential errors or failures during the connection setup.

## Get started in 5 minutes
1. Ensure you have Node.js (>= 20) and git installed.
2. Copy the provided installation command into Codex to automatically set up the project.
3. Follow the prompts to complete the first-time setup, which includes logging into ChatGPT and configuring the connection.

## Watch out for
The project is marked as an unofficial community effort, which may imply potential instability or lack of support. Additionally, while it claims to have a verified end-to-end setup, the README does not provide extensive documentation on troubleshooting or error handling, which could be a concern for less experienced users.
