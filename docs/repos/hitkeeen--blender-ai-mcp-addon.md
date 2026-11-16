---
title: hitkeeen/blender-ai-mcp-addon
source: https://github.com/hitkeeen/blender-ai-mcp-addon
stars: 1929
category: AI & Agents
---

# hitkeeen/blender-ai-mcp-addon

- **URL**: https://github.com/hitkeeen/blender-ai-mcp-addon
- **Stars**: 1929
- **Language**: Unknown
- **Category**: AI & Agents
- **Topics**: ai-agents, ai-assistant, blender, blender-addon, blender-ai, blender-automation, blender-mcp, blender-plugin, blender-scripting, bpy, chatgpt, claude, gemini, llm, mcp, mcp-for-blender, mcp-server, model-context-protocol, ollama, opencode

## What it does
This repository provides an AI assistant for Blender that can inspect scenes, create objects, edit materials, and manage multi-agent workflows through a visual chat interface. It integrates with various AI models, including ChatGPT and Claude, to facilitate creative tasks in 3D modeling.

## Why it's interesting
Unlike standard Blender plugins, this addon combines AI-driven assistance with a multi-agent workflow, allowing for collaborative scene management and automation of repetitive tasks. It supports a range of AI models and provides a built-in Model Context Protocol (MCP) server for enhanced integration.

## How it works
The addon operates within Blender, leveraging a visual chat workspace to interact with users and manage scene operations. It connects to various AI providers and allows users to configure single or multi-agent setups for task management. The architecture includes a local MCP server for communication with external clients, though specific implementation details are not fully outlined in the README.

## Get started in 5 minutes
1. Download `mcp-for-blender-pro.zip` from the [Releases](https://github.com/hitkeeen/blender-ai-mcp-addon/releases/latest).
2. In Blender, navigate to **Edit → Preferences → Get Extensions → menu → Install from Disk** and select the ZIP file.
3. Enable the addon and open **3D Viewport → N → MCP Pro** to configure your AI provider and model.
4. Start interacting with the assistant by sending messages or opening the Studio Window.

## Watch out for
The addon is currently targeted at Windows x64 with Blender 4.2 or later, which may limit its accessibility for users on other platforms. The README does not specify the maturity of the project or any known issues, and while it uses the MIT license, users should be aware of the independent nature of the project, which is not affiliated with the Blender Foundation.
