---
title: deepseek-ai/chat-demo
source: https://github.com/deepseek-ai/chat-demo
stars: 3868
category: Web & Frontend
---

# deepseek-ai/chat-demo

- **URL**: https://github.com/deepseek-ai/chat-demo
- **Stars**: 3868
- **Language**: TypeScript
- **Category**: Web & Frontend
- **Topics**: None

## What it does
This repository provides a static chat demo powered by the DeepSeek API, allowing users to interact with the chat application directly in their browser without needing a backend. Users can manage multiple conversations, upload attachments, and utilize features like voice input and Markdown formatting.

## Why it's interesting
Unlike many chat applications that require a server-side component, this demo operates entirely in the browser, making it easy to deploy and use without complex setup. It also supports advanced features such as streaming replies and source citations, which may not be common in simpler chat demos.

## How it works
The application is built with TypeScript and uses a combination of local storage (for settings and API keys) and IndexedDB (for conversations and attachments). It connects directly to the DeepSeek API for message handling and supports various features like Markdown parsing and audio recording. The architecture allows for customization of the API origin and development server proxy through the `rspack.config.ts` file. However, the README does not specify the exact API capabilities or limitations, leaving some uncertainty about the full range of features supported by the backend.

## Get started in 5 minutes
1. Install Node.js 22.12+ and pnpm.
2. Clone the repository: `git clone https://github.com/deepseek-ai/chat-demo.git`
3. Navigate to the directory: `cd chat-demo`
4. Install dependencies: `pnpm install`
5. Start the development server: `pnpm dev` and open `http://localhost:8090` in your browser.

## Watch out for
The repository is relatively new, created in November 2026, which may indicate that it is still in development or lacks extensive community support. Additionally, the application relies on browser storage for sensitive data, which could raise security concerns if not handled properly. The README mentions that certain features depend on server-side validation, but it does not provide details on what those features are or how they are validated.
