---
title: paipiange/nvzhuang
source: https://github.com/paipiange/nvzhuang
stars: 2028
category: AI & Agents
---

# paipiange/nvzhuang

- **URL**: https://github.com/paipiange/nvzhuang
- **Stars**: 2028
- **Language**: Go
- **Category**: AI & Agents
- **Topics**: None

## What it does
This repository provides a web-based AI fashion reference gallery featuring 1,407 AI-generated clothing images. It supports bilingual browsing (Chinese and English) and includes a virtual try-on feature that allows users to upload their photos and apply selected clothing items.

## Why it's interesting
Unlike typical fashion galleries, this project integrates AI-driven virtual try-on capabilities, allowing users to see how clothing would look on them without needing physical samples. It also offers a fully open-source solution with commercial use rights under the MIT License, making it accessible for developers and businesses.

## How it works
The front end is a static site that interacts with a backend service built using Go (GoFrame). Users can browse the clothing gallery, search using keywords in both languages, and utilize the AI try-on feature by configuring their backend with various AI models (e.g., OpenAI, Gemini). The backend can be deployed using Docker, and it supports multiple AI models for clothing transfer.

## Get started in 5 minutes
To quickly try it out, clone the repository, navigate to the `backend` directory, and run `docker compose up -d` to start the backend service. Then, open `index.html` in a browser to access the front end.

## Watch out for
The project is relatively new (created in October 2026), so it may have stability issues or incomplete features. Users need to set up their backend for the AI try-on functionality, which requires API keys for the respective models. Ensure compliance with the licensing terms when using the generated images for commercial purposes.
