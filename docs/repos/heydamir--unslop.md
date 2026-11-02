---
title: heydamir/unslop
source: https://github.com/heydamir/unslop
stars: 5564
category: AI & Agents
---

# heydamir/unslop

- **URL**: https://github.com/heydamir/unslop
- **Stars**: 5564
- **Language**: JavaScript
- **Category**: AI & Agents
- **Topics**: None

## What it does
unslop is a skill for Claude Code and Codex that transforms poorly designed, AI-generated user interfaces into polished designs. It audits the UI for issues, proposes improvements, and can generate a short video showcasing the transformation.

## Why it's interesting
Unlike traditional design tools, unslop automates the process of UI refinement by leveraging AI to identify design flaws and suggest enhancements, making it accessible for developers who may not have design expertise. It integrates seamlessly with various frameworks and can operate on live sites.

## How it works
unslop operates by first auditing the UI to identify design flaws ('slop'), then proposes a direction for improvement based on the product's character. It processes the UI in multiple passes, addressing aspects like spacing, color, and layout. The README does not provide detailed information on the underlying algorithms or AI models used, leaving some uncertainty about its technical implementation.

## Get started in 5 minutes
Clone the repository and copy the skill to your Claude or Codex skills folder:
```bash
git clone https://github.com/heydamir/unslop
mkdir -p ~/.claude/skills && cp -r unslop/skills/unslop ~/.claude/skills/
```
Then, use the command `/unslop` or `$unslop` followed by the target UI to begin.

## Watch out for
The repository has a high star count, indicating interest, but it was created recently (October 2026), which may imply it is still in early development. Users should be cautious about relying on it for production use until it matures. Additionally, it requires external dependencies like Playwright and ffmpeg for certain features, which may complicate setup.
