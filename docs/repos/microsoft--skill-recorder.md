---
title: microsoft/skill-recorder
source: https://github.com/microsoft/skill-recorder
stars: 907
category: AI & Agents
---

# microsoft/skill-recorder

- **URL**: https://github.com/microsoft/skill-recorder
- **Stars**: 907
- **Language**: TypeScript
- **Category**: AI & Agents
- **Topics**: agent-skills, ai-agents, automation, copilot, copilot-cli, copilot-cowork, copilot-studio, electron, microsoft-scout, screen-recording

## What it does
Skill Recorder is a desktop application that records on-screen work sessions, capturing user actions and optional narration. It then utilizes the GitHub Copilot CLI to reconstruct these actions into a structured intent and ordered steps, allowing users to create reusable skills or automations for AI agents.

## Why it's interesting
Unlike traditional screen recording tools, Skill Recorder not only captures video but also analyzes user interactions to generate actionable insights for AI agents. This enables the creation of skills that can generalize from a single recorded session, making it a unique tool for automating repetitive tasks.

## How it works
The application captures screen activity and user actions locally, including window switches and optional narration. Once recording is complete, users can analyze the session, which sends data to GitHub's cloud for processing by Copilot. The output is a clear intent and a list of steps that can be turned into a skill or automation. The README does not specify the underlying architecture beyond the use of Electron and Node.js, leaving some uncertainty about the detailed implementation.

## Get started in 5 minutes
1. Download the latest release from the [releases page](https://github.com/microsoft/skill-recorder/releases/latest).
2. Run the installation command for your platform as specified in the README.
3. Grant screen recording permissions on first launch, then start recording your task.

## Watch out for
The project is relatively new, created in July 2026, and may still be maturing. Users should be cautious about recording sensitive information, as the application sends data to GitHub's cloud during analysis. Additionally, a GitHub account with Copilot access is required to use the application effectively.
