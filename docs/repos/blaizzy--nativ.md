---
title: Blaizzy/nativ
source: https://github.com/Blaizzy/nativ
stars: 840
category: AI & Agents
---

# Blaizzy/nativ

- **URL**: https://github.com/Blaizzy/nativ
- **Stars**: 840
- **Language**: Swift
- **Category**: AI & Agents
- **Topics**: None

## What it does
Nativ is a macOS application designed for running AI models locally on Apple silicon. It provides functionalities such as a chat interface, model management, performance analytics, and local API endpoints compatible with OpenAI and Anthropic models.

## Why it's interesting
Nativ stands out by offering a fully integrated local environment for AI model inference on macOS, leveraging Apple silicon's capabilities. Unlike cloud-based solutions, it allows users to run models directly on their machines, ensuring privacy and potentially reducing latency.

## How it works
Nativ consists of a SwiftUI application that interfaces with an embedded server (`mlx-vlm`) for model management and inference. The architecture includes components for model discovery, chat functionality, and performance tracking, all running locally. The app requires macOS 26 or newer and sufficient unified memory for the selected models. It also utilizes a Python distribution for server operations, which is bundled within the application. Uncertainty exists regarding the specific models supported beyond those mentioned, as the README does not provide a comprehensive list.

## Get started in 5 minutes
To try Nativ, download the latest DMG from [GitHub Releases](https://github.com/Blaizzy/nativ/releases/latest), drag it to Applications, and launch it. On first launch, select or download a language model, optionally generate an API key, and start using the chat or analytics features.

## Watch out for
The repository is relatively new, created in July 2026, which may indicate that it is still in active development. Users should be cautious about potential bugs or incomplete features, especially since some functionalities, like dedicated audio and image generation support, are marked as "coming soon." Additionally, the README does not specify the licensing terms, which could be a concern for developers looking to use or contribute to the project.
