---
title: pireel/pireel
source: https://github.com/pireel/pireel
stars: 698
category: Web & Frontend
---

# pireel/pireel

- **URL**: https://github.com/pireel/pireel
- **Stars**: 698
- **Language**: TypeScript
- **Category**: Web & Frontend
- **Topics**: ai-video, capcut, captions, chatcut, openchatcut, talking-head, video-editor

## What it does
Pireel is an open-source, backend-free AI video editor designed for talking-head videos. It allows users to edit, storyboard, and export videos entirely within the browser without requiring an account or server.

## Why it's interesting
Unlike traditional video editors that often rely on backend services for processing, Pireel operates fully client-side, leveraging WebCodecs for video export. This approach enables a seamless editing experience without the need for external dependencies, making it accessible and easy to use.

## How it works
Pireel is structured as a minimal Vite application that mounts various editor packages. It supports local editing and export, with features like themes and a timeline. However, certain functionalities such as block composition and transcription require external providers, which can be injected through a defined interface in the codebase. The README does not specify the exact capabilities of the external providers or how they integrate with the core editor.

## Get started in 5 minutes
To quickly try Pireel, run the following commands:
```bash
pnpm install
pnpm dev
```
Then open the printed URL in your browser, import a video, and start editing.

## Watch out for
The project is licensed under AGPL-3.0, which may impose restrictions on usage and distribution. Additionally, while the core editing features are functional without a backend, the reliance on external providers for advanced features may limit usability for some users. The repository is relatively new, created in July 2026, which may indicate that it is still in active development and could have unresolved issues.
