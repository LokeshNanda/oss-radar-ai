---
title: Vincentwei1021/anything2explainer
source: https://github.com/Vincentwei1021/anything2explainer
stars: 1256
category: AI & Agents
---

# Vincentwei1021/anything2explainer

- **URL**: https://github.com/Vincentwei1021/anything2explainer
- **Stars**: 1256
- **Language**: TypeScript
- **Category**: AI & Agents
- **Topics**: agent-skills, ai-agents, ai-video, claude-code, claude-code-skill, codex, edge-tts, educational-video, explainer-video, kokoro, motion-graphics, multi-agent, react, remotion, text-to-video, tts, typescript, video-generation

## What it does
This repository provides a method to generate narrated explainer videos from any given topic using AI coding agents like Claude Code and Codex. The output includes a 1280×720 MP4 video with synchronized voiceover, subtitles, and a chapter progress bar, all created through a structured pipeline involving research, narration, and rendering.

## Why it's interesting
Unlike traditional video generation tools that rely on stock footage or generative models, anything2explainer produces deterministic videos where every frame is drawn in code. This ensures that all visual elements are original and sourced, providing a clear traceability of information presented in the videos.

## How it works
The process involves nine stages, starting from topic input to video rendering, with checkpoints for user input at critical stages. It utilizes Remotion for rendering, and the architecture includes multiple agents for research, narration, and quality control. The README does not specify how the AI agents are implemented or their exact capabilities beyond integration with Claude Code and Codex, leaving some uncertainty about extensibility with other agents.

## Get started in 5 minutes
To get started, clone the repository and set up the environment as follows:
```bash
git clone https://github.com/Vincentwei1021/anything2explainer.git
ln -s "$PWD/anything2explainer" ~/.claude/skills/anything2explainer   # Claude Code
ln -s "$PWD/anything2explainer" ~/.codex/skills/anything2explainer    # Codex
```
Ensure you have Node.js and the required Python packages installed as outlined in the README.

## Watch out for
The toolkit is licensed under PolyForm Noncommercial, meaning it can only be used for noncommercial purposes without prior authorization. Additionally, the README notes that while it has been verified on macOS and Linux, Windows support is untested. There may also be limitations in terms of visual style customization, as it only supports one visual style with two backdrop options.
