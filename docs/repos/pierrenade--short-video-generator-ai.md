---
title: pierrenade/short-video-generator-AI
source: https://github.com/pierrenade/short-video-generator-AI
stars: 1139
category: AI & Agents
---

# pierrenade/short-video-generator-AI

- **URL**: https://github.com/pierrenade/short-video-generator-AI
- **Stars**: 1139
- **Language**: Python
- **Category**: AI & Agents
- **Topics**: ai, ai-video, python, short-video-maker, video-generation

## What it does
This repository provides a tool for converting YouTube videos into short, shareable clips, focusing on highlight detection, subtitles, translation, and voiceover. It allows users to generate 9:16 formatted videos suitable for platforms like TikTok or Instagram.

## Why it's interesting
Unlike many SaaS tools that charge for similar functionalities, this project is open-source and free to use. It offers a local web interface and a command-line interface, allowing for flexibility in how users interact with the tool.

## How it works
The tool fetches a YouTube video or uses a local file, transcribes it using the `faster-whisper` model, and then employs a chosen LLM (OpenAI, Gemini, or MuAPI) to analyze the transcript for highlight moments. It ranks these moments based on a virality framework and allows users to customize the output through various CLI flags. The README does not specify how the highlight ranking algorithm works in detail, leaving some uncertainty about its effectiveness.

## Get started in 5 minutes
1. Clone the repository: `git clone https://github.com/pierrenade/short-video-generator-AI.git`
2. Navigate to the directory: `cd short-video-generator-AI`
3. Create and activate a virtual environment:
   - Windows: `python -m venv venv && venv\Scripts\activate`
   - Linux/MacOS: `python -m venv venv && source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Set up your `.env` file with your LLM provider API key and run the command: `python main.py "https://www.youtube.com/watch?v=video_id"`.

## Watch out for
The project is relatively new, created in September 2026, and may not have extensive community support or documentation. Users need to manage API keys for the LLM providers, which may involve costs depending on usage. The README does not provide information on the performance or limitations of the highlight detection algorithm, which could affect the quality of generated clips.
