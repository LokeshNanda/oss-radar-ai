---
title: bookwjitchieni1986/blender-ai-mcp-addon
source: https://github.com/bookwjitchieni1986/blender-ai-mcp-addon
stars: 2763
category: AI & Agents
---

# bookwjitchieni1986/blender-ai-mcp-addon

- **URL**: https://github.com/bookwjitchieni1986/blender-ai-mcp-addon
- **Stars**: 2763
- **Language**: Unknown
- **Category**: AI & Agents
- **Topics**: ai-agents, ai-assistant, blender, blender-addon, blender-ai, blender-automation, blender-mcp, blender-plugin, blender-scripting, bpy, chatgpt, claude, gemini, llm, mcp, mcp-for-blender, mcp-server, model-context-protocol, ollama, opencode

## What it does
This repository provides an AI assistant for Blender that can interact with 3D scenes, perform object creation and editing, and facilitate multi-agent workflows through a visual chat interface. It integrates various AI models, allowing users to automate tasks and manage scene operations efficiently.

## Why it's interesting
Unlike typical Blender addons, this tool combines AI capabilities with a structured workflow system, enabling both individual and team-based interactions. It supports multiple AI providers, allowing users to choose the model that best fits their needs, which is not commonly found in standard Blender plugins.

## How it works
The addon operates as a built-in Model Context Protocol (MCP) server, facilitating communication between Blender and various AI models like OpenAI and Anthropic Claude. Users can install the addon, connect to their preferred AI models, and utilize a range of scene tools for tasks such as object inspection, material editing, and asset management. The architecture allows for both single assistant and team configurations, with tasks running sequentially and a task board for tracking progress. However, the README does not specify the underlying technical architecture or any dependencies beyond Blender and the supported AI models.

## Get started in 5 minutes
1. Download `mcp-for-blender-pro.zip` from the [Releases](https://github.com/bookwjitchieni1986/blender-ai-mcp-addon/releases/latest).
2. In Blender, navigate to **Edit → Preferences → Get Extensions → menu → Install from Disk** and select the ZIP file.
3. Enable the addon and open **3D Viewport → N → MCP Pro** to configure your AI model connection.
4. Start interacting with the assistant by sending messages or opening the Studio Window.

## Watch out for
The addon is currently targeted at Windows x64 with Blender 4.2 or later, which may limit accessibility for users on other platforms. The README does not mention any security measures beyond Python tool validation, which may not provide comprehensive protection against disallowed operations. Additionally, it is an independent project not affiliated with the Blender Foundation or the listed AI providers, which could affect support and updates.
