---
title: wide-trace/open-higgsfield
source: https://github.com/wide-trace/open-higgsfield
stars: 1177
category: AI & Agents
---

# wide-trace/open-higgsfield

- **URL**: https://github.com/wide-trace/open-higgsfield
- **Stars**: 1177
- **Language**: TypeScript
- **Category**: AI & Agents
- **Topics**: None

## What it does
OpenHiggsfield AI is an open-source platform for generating images and videos using 40 different models through a single prompt interface. It allows users to customize settings for each model and view generated outputs in a gallery format.

## Why it's interesting
Unlike proprietary solutions like Higgsfield AI, OpenHiggsfield AI is free and self-hosted, providing users with the flexibility to modify the code and avoid vendor lock-in. It supports a wide range of models for both image and video generation, which is not commonly found in similar tools.

## How it works
The application is built using Next.js and React, with a focus on a clean user interface that integrates various models for media generation. It utilizes server actions to handle requests, ensuring that the browser does not directly communicate with the generation API. The catalog serves as the source of truth for model settings, and uploads are managed through Vercel Blob. However, the README does not specify how the models are sourced or their licensing details, leaving some uncertainty regarding the legal use of the models.

## Get started in 5 minutes
1. Clone the repository.
2. Run `pnpm install` to install dependencies.
3. Start the development server with `pnpm dev`.
4. Open the studio in your browser and add your platform key in the format `id:secret`.

## Watch out for
The repository was created recently in August 2026, which may indicate that it is still in early development stages. There are no stated licensing details for the models used, which could pose legal risks. Additionally, the README does not mention any security measures beyond storing the platform key in an httpOnly cookie, which may require further scrutiny.
