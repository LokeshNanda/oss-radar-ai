---
title: tamaratran/fast-jev-compaction
source: https://github.com/tamaratran/fast-jev-compaction
stars: 5756
category: Developer Tools
---

# tamaratran/fast-jev-compaction

- **URL**: https://github.com/tamaratran/fast-jev-compaction
- **Stars**: 5756
- **Language**: TypeScript
- **Category**: Developer Tools
- **Topics**: None

## What it does
This repository provides a Claude Code plugin and an npm library that replaces the built-in compaction summary with Jev decisions, allowing for a more precise management of tool calls and results in conversations. It retains verbatim user and assistant messages while efficiently managing the state sent to Jev, ensuring that only necessary information is kept.

## Why it's interesting
Unlike traditional context compaction methods that summarize conversations (often leading to loss of important details), this tool maintains the original messages intact and only removes unnecessary tool calls and results based on Jev's scoring. This approach minimizes data loss and enhances the fidelity of the conversation history.

## How it works
The plugin pairs each tool use with its result, sending the entire conversation state to Jev for evaluation. It uses a series of truncation and abridgment techniques to fit the state within token limits, while concurrently querying Jev about which calls and results to keep. The decisions are based on a configurable threshold, and the plugin can fall back to the built-in summary if it cannot sufficiently reduce the state. The README does not specify how the plugin interacts with different versions of Claude Code beyond the requirement for version 2.1.274 or higher.

## Get started in 5 minutes
1. Install the package with `npm install fast-jev-compaction`.
2. Set your API key with `export TYPESAFE_API_KEY=...`.
3. Import and use the `compactMessages` function in your TypeScript code as shown in the README.

## Watch out for
The repository is relatively new (created in September 2026), which may imply limited community support or maturity. The README notes that token sizes are estimates and that the plugin may fail under certain conditions, requiring fallback mechanisms. Additionally, it is important to manage API keys securely and not expose them in source files.
