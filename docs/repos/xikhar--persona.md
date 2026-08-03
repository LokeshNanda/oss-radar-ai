---
title: xikhar/persona
source: https://github.com/xikhar/persona
stars: 796
category: AI & Agents
---

# xikhar/persona

- **URL**: https://github.com/xikhar/persona
- **Stars**: 796
- **Language**: JavaScript
- **Category**: AI & Agents
- **Topics**: None

## What it does
Persona is a cross-platform desktop application that provides a visual avatar for real-time voice conversations, enhancing voice experiences with expressive character animations. It supports multiple platforms including Linux, Windows, and macOS, and allows users to customize character models and animations.

## Why it's interesting
Unlike typical voice assistants that rely solely on audio output, Persona adds a visual component that can enhance user engagement and interaction. It allows for the integration of custom character models and animations, providing a unique way to represent voice interactions visually.

## How it works
Persona captures audio output from various applications using platform-specific methods (e.g., PipeWire for Linux, WASAPI for Windows, Core Audio for macOS). It does not capture microphone input or transmit audio over the network. Users can customize the experience by adding their own `.vrm` and `.vrma` files for character models and animations. The application uses a local MCP server for integration with other applications, allowing for control over the avatar's animations and visibility. The README provides detailed instructions on setting up the environment, building the application, and managing character assets.

## Get started in 5 minutes
1. Ensure you have Node.js 24 or newer and npm installed.
2. Clone the repository and navigate to the project directory.
3. Run `npm install` to install dependencies.
4. Copy the example configuration files: `cp public/assets/library.json.example public/assets/library.json` and `cp public/assets/manifest.json.example public/assets/manifest.json`.
5. Start the demo with `npm run demo`.

## Watch out for
The project is relatively new, created in July 2026, and may not have extensive documentation or community support yet. It requires specific platform capabilities (e.g., Windows 10 build 20348 or newer) and permissions (e.g., audio recording on macOS). The character assets are subject to their own licensing terms, which are separate from the MIT License that applies to the source code.
