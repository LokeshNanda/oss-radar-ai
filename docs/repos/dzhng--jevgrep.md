---
title: dzhng/jevgrep
source: https://github.com/dzhng/jevgrep
stars: 1084
category: Developer Tools
---

# dzhng/jevgrep

- **URL**: https://github.com/dzhng/jevgrep
- **Stars**: 1084
- **Language**: TypeScript
- **Category**: Developer Tools
- **Topics**: ai-sdk, claude-code, cli, code-search, codex, coding-agents, context-retrieval, developer-tools, jev, semantic-search, typescript, vercel-ai-gateway

## What it does
Jevgrep is a command-line interface (CLI) tool that helps developers find relevant code files and source context by asking natural language questions about what the code does. It leverages the Jev AI model to assess relevance across a repository's structure and returns pertinent files, leads, and excerpts in a single output.

## Why it's interesting
Unlike traditional code search tools that rely on keyword matching, Jevgrep uses semantic understanding to interpret developer queries, potentially improving the efficiency of navigating large codebases. It claims to achieve similar task completion rates as baseline models while reducing costs by approximately 30%.

## How it works
Jevgrep operates by sending queries to the Jev model, which evaluates the relevance of files based on the provided context. It supports Node.js environments and requires authentication with a key from Vercel AI Gateway or other providers. The tool filters out irrelevant files and caches results locally, but it does not guarantee that all sensitive information is excluded from searches. The architecture is built using TypeScript, Bun workspaces, and Turborepo, with specific commands for installation and usage detailed in the README.

## Get started in 5 minutes
1. Install the CLI globally using `npm install -g @dzhng/jevgrep`.
2. Authenticate with your provider using `jg auth`.
3. Install the required agent skill with `jg skill`.
4. Start querying your codebase with commands like `jg "How are telemetry events recorded and sent?" ./my-project`.

## Watch out for
The repository is relatively new, created in September 2026, and may still be evolving. There is no built-in command for upgrading the CLI; users must manually reinstall the latest version. Additionally, while it claims to filter out sensitive information, there is no guarantee that all such data is excluded, so users should be cautious about the search root they select.
