---
title: feder-cr/dots
source: https://github.com/feder-cr/dots
stars: 2610
category: AI & Agents
---

# feder-cr/dots

- **URL**: https://github.com/feder-cr/dots
- **Stars**: 2610
- **Language**: Python
- **Category**: AI & Agents
- **Topics**: ai-agent, ai-agents, ai-browser, anti-detect-browser, browser-agent, browser-automation, chatgpt, dotfiles, dots, firefox, llm-agent, mcp, open-source-alternative, openai, openai-dots, openrouter, playwright, stealth-browser, web-agent, web-automation

## What it does
`dots` is an AI agent that integrates a real Firefox engine for web browsing, allowing users to interact with websites while maintaining a unique identity and avoiding detection. It enables the execution of tasks like web scraping or automated interactions by leveraging AI models from OpenRouter.

## Why it's interesting
Unlike traditional automation tools that may expose their nature through WebDriver flags or other detectable patterns, `dots` aims to mimic human behavior more closely by using a patched Firefox engine and providing a unique identity for each session. This approach helps in bypassing anti-bot measures that websites may employ.

## How it works
The architecture is built around a modified Firefox engine that handles browser interactions directly, ensuring that the fingerprint is generated within the engine itself. It supports features like maintaining user profiles across sessions, using proxies to change geographic identity, and simulating human-like interactions by sending events one at a time. The README does not specify how the AI model interacts with the browser or the underlying implementation details of the Firefox engine modifications, leaving some uncertainty about those aspects.

## Get started in 5 minutes
To get started, run the installation script for your OS (PowerShell for Windows or curl for Linux) to install the necessary components. Then, execute the command `uvx --from git+https://github.com/feder-cr/dots dots --openrouter-key sk-or-...` and open your browser at `http://127.0.0.1:8765` to start using the AI agent.

## Watch out for
The repository is relatively new, created in September 2026, which may indicate that it is still in active development and could have undiscovered bugs or incomplete features. Additionally, while it is MIT licensed, users should be cautious about the ethical implications of using an AI agent for web scraping or automated interactions, especially regarding compliance with website terms of service.
