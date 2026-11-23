---
title: iamajmeena/neonclipping
source: https://github.com/iamajmeena/neonclipping
stars: 2265
category: AI & Agents
---

# iamajmeena/neonclipping

- **URL**: https://github.com/iamajmeena/neonclipping
- **Stars**: 2265
- **Language**: Python
- **Category**: AI & Agents
- **Topics**: ai-video-clipper, clipping, faster-whisper, ffmpeg, gameplay-clipper, local-llm, ollama, open-source-video-editor, opusclip-alternative, shorts, twitch-clips, vertical-video, video, whisper, youtube-shorts-generator, yt-dlp

## What it does
NeonClipping is a local, open-source tool that converts long YouTube, Twitch, or Kick videos into 9:16 vertical clips with captions. It operates entirely on the user's machine, requiring no uploads or subscriptions, and can generate clips in approximately two minutes.

## Why it's interesting
Unlike cloud-based alternatives like OpusClip, NeonClipping runs locally, ensuring user privacy and eliminating API costs. It features an audio-first approach to identify key moments in videos, leveraging local machine learning models for enhanced performance and customization.

## How it works
NeonClipping employs a two-mode system for moment detection: a Fast mode that analyzes audio for sudden loudness changes and a Deep mode that evaluates the entire video for additional context. It uses local models for transcription and scoring, and the architecture includes a FastAPI server for handling requests. The README does not specify the exact dependencies for the local LLM, which may introduce uncertainty regarding setup requirements.

## Get started in 5 minutes
To quickly try NeonClipping, download the `NeonClipping-Setup.bat` file from the Releases page, run it to install dependencies, and then open your browser to `http://127.0.0.1:8770` to start making clips by pasting a video link.

## Watch out for
The project is relatively new (created in November 2026), so there may be undiscovered bugs or performance issues. The README mentions that the Mac/Linux installer has not been fully tested, which could lead to installation challenges. Additionally, users should ensure they have the required Python version and FFmpeg installed, as these are necessary for operation.
