---
title: gnipbao/story-to-handdrawn-video
source: https://github.com/gnipbao/story-to-handdrawn-video
stars: 655
category: AI & Agents
---

# gnipbao/story-to-handdrawn-video

- **URL**: https://github.com/gnipbao/story-to-handdrawn-video
- **Stars**: 655
- **Language**: JavaScript
- **Category**: AI & Agents
- **Topics**: None

## What it does
This repository provides a tool to convert Chinese story text or ordered images into a hand-drawn diary-comic animation. It outputs a silent MP4 video track that can be used for post-production voiceover.

## Why it's interesting
Unlike typical animation tools, this project leverages natural language processing to automate the storyboarding and rendering process, allowing users to create animations without manual scripting. It specifically targets Chinese narratives and integrates with agent frameworks like Codex for seamless interaction.

## How it works
The project consists of two main components: a Remotion-based renderer for creating animations and a skill package that allows interaction via natural language commands. Users can input story text or image sequences, and the tool handles sentence splitting, image generation, and rendering. It requires Node.js, Python, FFmpeg, and a compatible agent runtime for operation. The README does not specify how the image generation process works in detail or the specific capabilities of the Codex integration, leaving some uncertainty.

## Get started in 5 minutes
1. Clone the repository:
   ```bash
   git clone https://github.com/gnipbao/story-to-handdrawn-video.git
   cd story-to-handdrawn-video
   npm ci
   npm run check
   ```
2. Install the skill into your agent's skills directory:
   ```bash
   cp -R skill-package/story-to-handdrawn-video ~/.codex/skills/
   ```
3. Set the project path for the skill:
   ```bash
   export STORY_VIDEO_PROJECT=/absolute/path/to/story-to-handdrawn-video
   ```

## Watch out for
The project is relatively new, created in July 2026, and may not have extensive community support or documentation. Users should be aware of the dependencies on specific versions of Node.js and Python, as well as the need for FFmpeg. Additionally, the output is a silent video track, requiring post-production for audio, which may not be suitable for all use cases.
