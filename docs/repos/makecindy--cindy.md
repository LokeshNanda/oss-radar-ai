---
title: makecindy/cindy
source: https://github.com/makecindy/cindy
stars: 611
category: AI & Agents
---

# makecindy/cindy

- **URL**: https://github.com/makecindy/cindy
- **Stars**: 611
- **Language**: TypeScript
- **Category**: AI & Agents
- **Topics**: agent, ai-agent, ai-assistant, android, claude-code, codex, electron, ios, llm, macos, react-native, typescript, windows

## What it does
Cindy is an open-source AI agent that operates locally on your machine, integrating various models and tools to automate tasks in your projects and applications. It supports multiple harnesses, including Claude Code and Codex, allowing for flexible task execution and management.

## Why it's interesting
Cindy differentiates itself by offering a local execution environment that can seamlessly switch between models and harnesses mid-task, maintaining continuity in workspace and memory. This flexibility, combined with the ability to integrate with existing applications and services, positions it as a versatile tool for developers looking to enhance productivity.

## How it works
Cindy is structured as a pnpm monorepo containing a desktop client (built with Electron), a mobile client (using Expo/React Native), and shared packages for authentication and agent orchestration. The repository does not include the backend service, which is hosted separately. Users can operate in either a hosted mode (requiring a Cindy cloud account) or a local mode (no sign-in required), but server-backed capabilities are unavailable in local mode. The architecture supports plugin development and customization, although details on the specific implementation of the harnesses and models are not fully detailed in the README.

## Get started in 5 minutes
1. Clone the repository: `git clone https://github.com/makecindy/cindy.git`
2. Navigate to the directory: `cd cindy`
3. Initialize submodules: `git submodule update --init --recursive cindy-protocol`
4. Pull Git LFS files: `git lfs pull`
5. Install dependencies: `pnpm install`

## Watch out for
The repository is relatively new (created in July 2026), which may imply that it is still in development and could have stability issues. The README mentions that some features, such as the open marketplace for plugins, are still in the making. Additionally, while the client can operate without a cloud account, many features may be limited in local mode. Security practices are emphasized, particularly regarding the handling of credentials and analytics, but users should be cautious about the implications of using cloud services.
