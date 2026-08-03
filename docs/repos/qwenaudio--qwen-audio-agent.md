---
title: QwenAudio/qwen-audio-agent
source: https://github.com/QwenAudio/qwen-audio-agent
stars: 1752
category: AI & Agents
---

# QwenAudio/qwen-audio-agent

- **URL**: https://github.com/QwenAudio/qwen-audio-agent
- **Stars**: 1752
- **Language**: JavaScript
- **Category**: AI & Agents
- **Topics**: agent, agentic-ai, voice-agent, voice-ai, voice-chat

## What it does
Qwen Audio Agent is a real-time voice runtime designed for AI agents, enabling continuous conversation and task execution without interruptions. It supports multi-turn dialogues and integrates various backend agents for enhanced functionality.

## Why it's interesting
Unlike traditional voice assistants that pause for processing, Qwen Audio Agent allows for seamless interaction by keeping the agent engaged during background tasks. This continuous presence is aimed at improving user experience in voice interactions.

## How it works
The architecture includes a frontend for real-time voice interaction and a backend for executing tasks asynchronously. It supports multiple backend agents, which can be configured through environment variables. The system requires Node.js 22.22.2+ or 24.15.0+ and utilizes a DashScope API Key for certain functionalities. The README provides detailed instructions on installation, configuration, and usage, but lacks specifics on the underlying algorithms or technologies used in the voice processing.

## Get started in 5 minutes
1. Install the package using npm: `npm install -g qwen-audio-agent`
2. Create a configuration file: `qwenaudio config`
3. Fill in the DashScope API Key in `config.env`.
4. Start the service: `qwenaudio`
5. Optionally, launch the TUI or WebUI: `qwenaudio tui` or `qwenaudio webui`.

## Watch out for
The project is relatively new, having been created in July 2026, and is currently in testing phases for some features (e.g., speech-to-speech integration). Users should be cautious about privacy, as audio data is sent to configured services. The README advises against storing sensitive information in user profiles or conversations.
