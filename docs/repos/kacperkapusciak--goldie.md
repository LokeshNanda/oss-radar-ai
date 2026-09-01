---
title: kacperkapusciak/goldie
source: https://github.com/kacperkapusciak/goldie
stars: 1117
category: Developer Tools
---

# kacperkapusciak/goldie

- **URL**: https://github.com/kacperkapusciak/goldie
- **Stars**: 1117
- **Language**: TypeScript
- **Category**: Developer Tools
- **Topics**: None

## What it does
Goldie is a tool for generating App Store and Google Play screenshots and preview videos for mobile applications. It utilizes an iOS simulator or Android emulator to capture app flows and frames the outputs with device bezels, backgrounds, and headlines, while ensuring compliance with store upload rules.

## Why it's interesting
Goldie is framework agnostic, meaning it can work with various mobile development frameworks such as SwiftUI, UIKit, Jetpack Compose, Flutter, React Native, and Kotlin Multiplatform. This flexibility allows developers to use it regardless of their tech stack, which is not common in similar tools that often target specific frameworks.

## How it works
Goldie operates by integrating with the Argent tool to replay user flows on simulators or emulators. It requires macOS, Node.js (version 20 or newer), and ffmpeg for installation. The CLI commands allow users to configure their app's screenshot generation by specifying device types and app paths in a configuration file. The output is organized into directories based on device and locale. The tool also includes a studio for previewing and tweaking assets. However, the README does not provide detailed information on the internal architecture or how the tool manages interactions with the simulators/emulators.

## Get started in 5 minutes
1. Ensure you have macOS, Node.js (20+), and ffmpeg installed.
2. Install Goldie globally using `npm i -g goldie`.
3. Copy the example configuration file with `cp goldie.config.example.ts goldie.config.ts` and configure it to point to your app's Argent flows.
4. Run `goldie all` to capture screenshots and generate previews.

## Watch out for
The repository is relatively new (created in August 2026), so it may not have extensive community support or documentation yet. Users should be cautious about potential bugs, especially since flows can fail if the app changes. Additionally, the README mentions that debug builds may interfere with captures, suggesting that only release builds should be used. There are no explicit licensing details provided in the README.
