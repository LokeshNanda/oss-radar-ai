---
title: MeteorNOX/DeepSeek-Balance-Whale-Widget
source: https://github.com/MeteorNOX/DeepSeek-Balance-Whale-Widget
stars: 842
category: Developer Tools
---

# MeteorNOX/DeepSeek-Balance-Whale-Widget

- **URL**: https://github.com/MeteorNOX/DeepSeek-Balance-Whale-Widget
- **Stars**: 842
- **Language**: JavaScript
- **Category**: Developer Tools
- **Topics**: cordis, deepseek, deepseek-harness, developer-tools, dsh, dsh-plugin, dsh-plugins, floating-widget, plugin

## What it does
The DeepSeek Balance Whale Widget is a plugin for the DeepSeek Harness (DSH) that displays a floating widget in the bottom right corner of the DSH web interface. It provides real-time balance updates, daily usage statistics, and interactive features like animations and sound effects.

## Why it's interesting
This widget stands out due to its automatic balance tracking capabilities without requiring a session token for basic functionality, making it user-friendly. It also offers customizable features such as drag-and-drop positioning, sound effects, and a unique visual design that enhances user engagement.

## How it works
The widget operates as a standard DSH plugin, utilizing the DeepSeek API to fetch balance information and usage statistics. It supports two modes for tracking usage: a simple mode that records balance changes without requiring additional tokens, and a real-time mode that uses a session token for more precise tracking. The architecture includes a main JavaScript file (`lib/index.js`), configuration files, and assets for visuals and sounds, all structured within the repository.

## Get started in 5 minutes
To install the widget, clone the repository and run the following command in the root directory:
```powershell
dsh plugin --profile web add link:.
```
After installation, restart the DSH web interface and refresh your browser to see the widget in action.

## Watch out for
The project is relatively new, created in August 2026, and may not have extensive community support yet. Users should ensure they have the required `DEEPSEEK_API_KEY` configured for the widget to function correctly. Additionally, there are specific instructions for upgrading from older installations that must be followed to avoid conflicts.
