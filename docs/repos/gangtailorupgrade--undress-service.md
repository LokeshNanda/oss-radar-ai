---
title: GangTailorUpgrade/undress-service
source: https://github.com/GangTailorUpgrade/undress-service
stars: 1151
category: AI & Agents
---

# GangTailorUpgrade/undress-service

- **URL**: https://github.com/GangTailorUpgrade/undress-service
- **Stars**: 1151
- **Language**: Python
- **Category**: AI & Agents
- **Topics**: 18comic, coomer, coomer-downloader, coomer-party, coomer-porn, coomer-su, doujin-moe, ehviewer, ex-hentai, explicit-content, hitomi-la, kemono, kemono-downloader, kemono-oarty, kemono-party, kemono-porn, kemono-su, nudity, sex, unrestricted-ai

## What it does
The Dress AI Service is an open-source, self-hosted platform that allows users to digitize their wardrobe, receive AI-generated outfit recommendations, and visualize outfits using generative AI. It integrates real-time weather data to suggest appropriate clothing combinations based on occasion and personal style.

## Why it's interesting
Unlike typical fashion apps that rely on cloud services, Dress AI Service prioritizes user privacy by being fully self-hosted, ensuring that all data remains on the user's machine. It combines advanced AI techniques for tagging and visualization, making it a comprehensive tool for fashion enthusiasts and developers alike.

## How it works
The architecture consists of a FastAPI backend that handles wardrobe uploads, outfit generation, and AI visualization using models like CLIP and Stable Diffusion. Users can upload clothing images, which are processed to extract metadata and generate outfit recommendations based on a hybrid approach of rule-based logic and AI embeddings. The system also supports optional local LLM reasoning via Ollama for enhanced outfit descriptions. The README does not specify the exact performance or limitations of the AI models used, leaving some uncertainty regarding their effectiveness.

## Get started in 5 minutes
To quickly set up the service, clone the repository, navigate to the directory, and run the following commands:
```bash
cp .env.example .env
docker-compose up --build
```
Then, visit `http://localhost:8080` to access the service.

## Watch out for
The repository was created in August 2026, so it may still be in early development stages. Users should be cautious about potential bugs or incomplete features. Additionally, while the project is licensed under the MIT License, there may be concerns regarding the use of AI models and their licensing, which are not fully detailed in the README.
