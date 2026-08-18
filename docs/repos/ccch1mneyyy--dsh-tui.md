---
title: ccch1mneyyy/dsh-TUI
source: https://github.com/ccch1mneyyy/dsh-TUI
stars: 1877
category: Developer Tools
---

# ccch1mneyyy/dsh-TUI

- **URL**: https://github.com/ccch1mneyyy/dsh-TUI
- **Stars**: 1877
- **Language**: TypeScript
- **Category**: Developer Tools
- **Topics**: claude-code, coding-agent, deepseek, deepseek-harness, dsh-plugin, ink, react, terminal, tui

## What it does
`dsh-TUI` is a terminal user interface (TUI) plugin designed for the DeepSeek Harness (DSH) framework, offering features like a pixel whale top bar, real-time status updates, and session management capabilities such as time rewind and context progress bars. It integrates seamlessly with existing DSH installations without modifying core components.

## Why it's interesting
This plugin stands out by providing a visually appealing and functional interface for terminal interactions, specifically tailored for users of the DSH framework. Its focus on a zero-core change installation and extensive command set makes it a robust tool for developers looking to enhance their terminal experience without significant overhead.

## How it works
The architecture of `dsh-TUI` relies on a combination of React components and the Ink library for rendering in terminal environments. It operates by mounting as a plugin to the DSH CLI, utilizing existing DSH services for session management and command execution. The plugin supports various interactive features, including real-time updates and customizable themes, while maintaining performance through event-driven rendering and layout virtualization. However, specific details about the underlying data handling and session persistence mechanisms are not fully detailed in the README.

## Get started in 5 minutes
To quickly set up `dsh-TUI`, ensure you have a compatible terminal and the DSH CLI installed. Run the following commands:
```sh
npm install -g @deepseek-ai/dsh @deepseek-harness-tui/dsh-tui
dsh-tui
```
This will install the plugin and start the TUI interface, initializing your profile automatically.

## Watch out for
The plugin is currently in public beta, which may imply potential instability or incomplete features. Additionally, there are known limitations regarding clipboard handling and session management that users should be aware of, particularly in environments with sensitive data. The licensing is under MIT, which is permissive but does not provide warranty or liability coverage.
