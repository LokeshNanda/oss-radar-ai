---
title: Minireel/HGhub
source: https://github.com/Minireel/HGhub
stars: 5077
category: Other
---

# Minireel/HGhub

- **URL**: https://github.com/Minireel/HGhub
- **Stars**: 5077
- **Language**: TypeScript
- **Category**: Other
- **Topics**: android, drama, free, movie-web-app, reels, windows

## What it does
HGhub is a third-party client for accessing short drama content from the YellowFruit platform. It is designed for multiple platforms including Windows, macOS, and Android, focusing on UI/UX and immersive vertical playback.

## Why it's interesting
Unlike many media clients, HGhub emphasizes non-commercial use and has a strict licensing policy (PolyForm Noncommercial 1.0.0) that prohibits any form of monetization or distribution of content. This focus on ethical usage and respect for copyright sets it apart from typical media applications that may not have such clear guidelines.

## How it works
HGhub is built using Tauri (Rust) for the backend and React with TypeScript for the frontend. It utilizes a custom protocol for media playback and caching, and it handles content through a single API endpoint to minimize overhead. The architecture includes a clear separation between the frontend and backend, with specific files for API handling, state management, and media processing. However, the README does not provide detailed information on how the content is sourced or any potential legal implications of its usage.

## Get started in 5 minutes
To get started, clone the repository and run the following commands:
```bash
pnpm install          # Install dependencies
pnpm app:dev          # Start the application in development mode
```
Ensure you have the necessary tools installed for your target platform (e.g., Xcode for macOS, Android SDK for Android).

## Watch out for
The project is not actively maintained for upstream data retrieval, which may limit its functionality over time. Additionally, it has a strict licensing policy that prohibits commercial use, and users must comply with local laws regarding content usage. The README warns against using unofficial versions of the software, which may pose security risks.
