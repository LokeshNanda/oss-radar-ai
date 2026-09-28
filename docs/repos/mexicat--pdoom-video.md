---
title: mexicat/pdoom-video
source: https://github.com/mexicat/pdoom-video
stars: 1553
category: Web & Frontend
---

# mexicat/pdoom-video

- **URL**: https://github.com/mexicat/pdoom-video
- **Stars**: 1553
- **Language**: TypeScript
- **Category**: Web & Frontend
- **Topics**: None

## What it does
This repository provides a code-rendered music video for the song "I'm Upping My P(doom)". It features generative visuals synchronized with the lyrics, allowing for both live previews in the browser and high-quality offline exports in 1080p60 or 4K60.

## Why it's interesting
Unlike traditional video editing tools, this project uses a deterministic function based on song time to generate every frame, ensuring that the live preview matches the final rendered output. It also incorporates advanced techniques for motion blur and scene rendering, which are not commonly found in standard video production workflows.

## How it works
The project is built using TypeScript and three.js, with a structured layout that includes audio analysis tools written in Python for timing data generation. The renderer is located in the `app/` directory, while the analysis tools are in the `analysis/` directory. The rendering process involves complex calculations for motion blur and scene transitions, with specific scripts for both real-time preview and offline rendering. However, the README does not specify how the generative visuals are created beyond the mention of a conversation with Claude (Opus 5.5), leaving some uncertainty about the underlying algorithms used for visual generation.

## Get started in 5 minutes
1. Clone the repository.
2. Navigate to the `app` directory: `cd app`
3. Install dependencies: `bun install`
4. Start the preview server: `bunx vite`
5. Open your browser to `http://localhost:5173`.

## Watch out for
The project requires specific tools such as bun, Google Chrome, and ffmpeg, which may not be installed by default. Additionally, the analysis tools require a separate installation of the `uv` package and the models used for audio analysis are not included in the repository, which could complicate regeneration of timing data. The song and lyrics are not covered by the MIT License and belong to their respective authors, which may limit usage rights.
