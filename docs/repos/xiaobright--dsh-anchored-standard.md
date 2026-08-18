---
title: xiaobright/dsh-anchored-standard
source: https://github.com/xiaobright/dsh-anchored-standard
stars: 3467
category: AI & Agents
---

# xiaobright/dsh-anchored-standard

- **URL**: https://github.com/xiaobright/dsh-anchored-standard
- **Stars**: 3467
- **Language**: JavaScript
- **Category**: AI & Agents
- **Topics**: deepseek, deepseek-harness, dsh-plugin, llm-agent

## What it does
This repository provides experimental presets for the DeepSeek Harness, focusing on a two-phase approach that starts with a minimal toolset and transitions to a more comprehensive set of tools based on session durability. It includes various modes that dictate how the model interacts with tools and manages context during a session.

## Why it's interesting
Unlike standard presets, this project aims to optimize the initial interaction phase by anchoring the model's trajectory to a minimal condition, which can lead to better performance in specific scenarios. It also allows users to explore different interaction modes, making it a flexible tool for developers working with AI agents.

## How it works
The repository defines several modes that dictate the model's behavior during its first request and subsequent interactions. Each mode has specific configurations for tool availability, context management, and promotion signals that trigger the transition from a minimal to a more extensive toolset. The README notes that active development has ceased due to cost constraints, and the repository is now in maintenance mode, which raises uncertainty about future updates or support.

## Get started in 5 minutes
To get started, clone the repository and follow the installation instructions in the README. Each mode is self-contained and can be installed independently by copying the desired mode's directory to your workspace.

## Watch out for
The project is currently in maintenance mode, with no active development due to rising costs associated with the DeepSeek API. This means that while bug fixes may be provided, new features or significant updates are unlikely. Additionally, the repository is not officially affiliated with DeepSeek, which may affect support and reliability.
