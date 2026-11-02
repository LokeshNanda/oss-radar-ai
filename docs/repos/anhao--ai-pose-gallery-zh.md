---
title: anhao/ai-pose-gallery-zh
source: https://github.com/anhao/ai-pose-gallery-zh
stars: 5424
category: AI & Agents
---

# anhao/ai-pose-gallery-zh

- **URL**: https://github.com/anhao/ai-pose-gallery-zh
- **Stars**: 5424
- **Language**: TypeScript
- **Category**: AI & Agents
- **Topics**: ai-art, chinese, cloudflare-pages, gallery, i18n, pose, reference-images, static-site

## What it does
This repository provides a comprehensive Chinese-language gallery of AI-generated reference images for poses, costumes, and portraits, totaling over 11,500 images. It integrates a web-based studio for character synthesis, allowing users to combine references and generate images using various AI protocols.

## Why it's interesting
Unlike typical image galleries, this project combines multiple datasets into a single interface, fully localized in Chinese, and offers a unique synthesis tool that connects to several AI image generation APIs. It also includes a plugin for ComfyUI, enhancing its usability within that ecosystem.

## How it works
The application is built using React, TypeScript, and Tailwind CSS, with a backend that supports multiple AI image generation protocols (e.g., Google Gemini, OpenAI GPT Image). It features a local storage mechanism using IndexedDB for managing user-generated content and historical data. The repository includes a structured directory for images and metadata, and it provides scripts for data maintenance and image downloading. However, the README does not specify how the AI protocols are implemented or their specific configurations.

## Get started in 5 minutes
1. Clone the repository: `git clone --depth 1 https://github.com/anhao/ai-pose-gallery-zh.git`
2. Navigate to the directory: `cd ai-pose-gallery-zh`
3. Install dependencies: `pnpm install`
4. Start the local server: `pnpm dev`
5. Access the application at `http://localhost:5173`.

## Watch out for
The repository is relatively new (created in October 2026), which may imply potential stability issues. It contains adult content, and users must comply with legal and ethical guidelines regarding image usage. Licensing is under MIT for the code, but the images and original data are not covered by this license, which may restrict their use in commercial applications.
