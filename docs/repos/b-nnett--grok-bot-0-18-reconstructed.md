---
title: b-nnett/grok-bot-0.18-reconstructed
source: https://github.com/b-nnett/grok-bot-0.18-reconstructed
stars: 1165
category: AI & Agents
---

# b-nnett/grok-bot-0.18-reconstructed

- **URL**: https://github.com/b-nnett/grok-bot-0.18-reconstructed
- **Stars**: 1165
- **Language**: TypeScript
- **Category**: AI & Agents
- **Topics**: None

## What it does
Grok Bot 0.18 Reconstructed is an unofficial reconstruction and extension of the Grok Bot 0.18.0 macOS application. It provides a TypeScript implementation of the original app's architecture, including an inference router for various AI providers and a local Docker sandbox for execution.

## Why it's interesting
This project stands out because it not only reconstructs the original Grok Bot but also extends its functionality with new features like local usage tracking and a customizable inference router. It serves as a research tool for understanding the original app's structure while maintaining compatibility with existing Grok Bot sessions.

## How it works
The architecture includes several components: a polished renderer from the original app, an Electron main process for lifecycle management, and a coordinator for routing inference requests. The project uses Git LFS to manage large files, including original installers, and employs a deterministic toolchain to assemble the macOS application. The README notes that the project is experimental and targets a specific version of the original app, which may limit future compatibility.

## Get started in 5 minutes
1. Clone the repository: `git clone <your-repository-url>`  
2. Navigate to the directory: `cd grok-bot-0.18-reconstructed`  
3. Install Git LFS: `git lfs install`  
4. Pull LFS files: `git lfs pull`  
5. Install dependencies: `npm ci`  
6. Build and run the app: `npm run bootstrap && npm run package && open "dist/Grok Bot 0.18 Reconstructed.app"`

## Watch out for
The project is still experimental, meaning it may have stability issues and is not guaranteed to work with future versions of Grok Bot. It requires macOS on Apple Silicon and specific versions of Node.js and Docker. Additionally, the original frontend source is not included, which may limit customization options.
