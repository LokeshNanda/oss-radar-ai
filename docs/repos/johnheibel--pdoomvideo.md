---
title: JohnHeibel/PDoomVideo
source: https://github.com/JohnHeibel/PDoomVideo
stars: 1349
category: Other
---

# JohnHeibel/PDoomVideo

- **URL**: https://github.com/JohnHeibel/PDoomVideo
- **Stars**: 1349
- **Language**: JavaScript
- **Category**: Other
- **Topics**: None

## What it does
This repository contains the source code for a music video titled "I'm Upping My P(doom)" created using Claude Opus 5.5. It generates animations based on lyrics and visual transitions without pre-defined scene ideas, relying instead on the AI model's capabilities.

## Why it's interesting
The project showcases the use of AI-generated content in creative media, specifically in music videos, which is a relatively novel application. It emphasizes a fully automated generation process, where the AI model creates both visuals and transitions based solely on lyrical input.

## How it works
The video is produced through two generations of animation using Claude Opus 5.5, with the first generation stored in the `legacy/` directory. The repository includes various components such as chapter files in `src/ch/`, shared code in `src/`, and rendering scripts in `render.mjs`. The rendering process requires Node.js, Google Chrome, and ffmpeg, and involves painting frames and encoding them into an MP4 format. The README does not specify the exact architecture of Claude Opus 5.5 or how it generates visuals, leaving some uncertainty about the underlying AI model's workings.

## Get started in 5 minutes
To try it out, clone the repository, ensure you have Node.js, Google Chrome, and ffmpeg installed, then run:
```bash
npm install
node render.mjs --frames=0:156.6 --workers=4
node render.mjs --encode --out=out/pdoom.mp4
```
Make sure the song file is present in `assets/pdoom.mp3`.

## Watch out for
The repository does not mention licensing details, which could be a concern for reuse or distribution. Additionally, the reliance on specific software (Node.js, Chrome, ffmpeg) may introduce compatibility issues depending on the user's environment. The project appears to be in early stages, as indicated by its recent creation date in September 2026, and may lack extensive documentation or community support.
