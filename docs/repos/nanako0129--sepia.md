---
title: Nanako0129/sepia
source: https://github.com/Nanako0129/sepia
stars: 1329
category: AI & Agents
---

# Nanako0129/sepia

- **URL**: https://github.com/Nanako0129/sepia
- **Stars**: 1329
- **Language**: Unknown
- **Category**: AI & Agents
- **Topics**: agent-skills, ai-writing, antigravity, claude-code, codex, developer-tools, fiction, grok, humanizer, llm, prompt-engineering, writing-tools

## What it does
sepia is an Agent Skill designed to enhance writing by addressing narrative architecture and discourse flow, particularly for fiction and professional documents. It provides four operations: write, review, refactor, and recreate, which can be executed across various AI agents using the Skills CLI.

## Why it's interesting
Unlike traditional writing tools that focus on surface-level edits, sepia emphasizes structural improvements in writing, aiming to reduce AI-generated text detection by modifying narrative elements rather than just word choice. Its approach is backed by research, including findings from StoryScope, which highlight the importance of narrative structure in distinguishing human from AI writing.

## How it works
sepia operates through a three-pass writing and revision protocol that targets narrative architecture, discourse flow, and surface style. It includes a 30-feature diagnosis rubric and per-model fingerprint corrections for various AI models. The skill is packaged as a single markdown file under the Agent Skills standard, allowing it to be installed on 77+ compatible agents via the Skills CLI. However, the README does not specify the primary programming language used in the repository, which leaves some uncertainty regarding its implementation details.

## Get started in 5 minutes
To install sepia, run the following command using the Skills CLI:
```bash
npx skills add Nanako0129/sepia -g
```
This command installs sepia globally, making it available for use across all projects.

## Watch out for
The repository is relatively new, created in August 2026, which may indicate that it is still in development or lacks extensive user feedback. Additionally, while it supports multiple agents, the README notes that runtime behavior outside the four specified platforms (Claude Code, Codex, Grok Build, Antigravity) has not been tested, which could lead to potential issues. The project is licensed under MIT, which is permissive but does not provide warranty or liability coverage.
