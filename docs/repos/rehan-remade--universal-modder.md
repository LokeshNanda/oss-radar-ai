---
title: rehan-remade/universal-modder
source: https://github.com/rehan-remade/universal-modder
stars: 3538
category: Developer Tools
---

# rehan-remade/universal-modder

- **URL**: https://github.com/rehan-remade/universal-modder
- **Stars**: 3538
- **Language**: Python
- **Category**: Developer Tools
- **Topics**: age-of-empires, claude-code, claude-code-plugin, fal, game-assets, game-modding, mcp, modding, reverse-engineering, tmodloader

## What it does
Universal Modder allows users to create mods for various PC games by leveraging AI coding agents. It provides a framework for modding that includes skills for reverse engineering, asset generation, and in-game testing.

## Why it's interesting
Unlike traditional modding tools, Universal Modder integrates AI capabilities to automate the modding process, making it accessible for users who may not have extensive programming knowledge. It also emphasizes community contributions through a knowledge base where agents can share their findings and experiences.

## How it works
The tool operates through a command-line interface (CLI) and supports multiple AI agents like Claude Code and Codex. Users can install the modder as a plugin for these agents, which then utilize a series of predefined skills to mod games. The workflow involves searching a knowledge base, recon, building mods, generating assets, and documenting the process for future agents. The README details various skills and commands available, but it does not provide specific information on the internal architecture or how the AI agents interact with the modding process.

## Get started in 5 minutes
To get started, clone the repository and install the desired agent plugin. For example, for Claude Code, run:
```bash
/plugin marketplace add rehan-remade/universal-modder
/plugin install universal-modder@universal-modder
```
Ensure you have Python 3.10+, ffmpeg, and a fal API key for asset generation.

## Watch out for
The repository is relatively new (created in September 2026), so it may lack maturity and extensive documentation. Users should be cautious about the potential for bugs and the evolving nature of the tool. Additionally, the licensing is MIT, which allows for modification and redistribution, but users should ensure compliance with any game-specific modding policies.
