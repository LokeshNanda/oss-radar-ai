---
title: storytold/craft-anything
source: https://github.com/storytold/craft-anything
stars: 2567
category: AI & Agents
---

# storytold/craft-anything

- **URL**: https://github.com/storytold/craft-anything
- **Stars**: 2567
- **Language**: Rust
- **Category**: AI & Agents
- **Topics**: None

## What it does
Craft Anything is a tool that allows users to analyze existing software (websites, apps, games) and generate new versions based on their specifications. It employs a coding agent to build projects in Rust, comparing the results with the original to ensure accuracy.

## Why it's interesting
Unlike traditional development tools, Craft Anything combines reverse engineering with AI-driven code generation, enabling users to recreate software without needing to understand the underlying code. Its clean-room approach allows for ethical software recreation by focusing on observable elements rather than proprietary code.

## How it works
The tool operates in four main steps: Study, Build, Check, and Ready. Users point Craft Anything at a target, specify what they want, and the tool inspects the original software using various inspection tools. It then generates a new project, checks it against the original, and refines it based on discrepancies. The architecture is built in pure Rust and includes 314 tools for various software types, but details on how these tools interact are not fully specified in the README.

## Get started in 5 minutes
1. Ensure you have Rust 1.97 or newer installed.
2. Clone the repository:
   ```sh
   git clone https://github.com/storytold/craft-anything && cd craft-anything
   ```
3. Run the desktop app:
   ```sh
   cargo run --release -p craft-anything
   ```
4. Alternatively, install the CLI:
   ```sh
   cargo install --path apps/craft-anything-cli
   ```
5. Use the CLI to rebuild a website:
   ```sh
   craft-anything-cli rebuild https://example.com "Recreate this website"
   ```

## Watch out for
Craft Anything is currently in early alpha, meaning features may be incomplete or unstable. Users should be cautious about its capabilities, especially regarding the use of coding agents and the handling of proprietary software. The README emphasizes responsible use, stating that it should only be used on software that users own or have permission to analyze.
