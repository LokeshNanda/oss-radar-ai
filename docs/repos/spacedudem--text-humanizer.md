---
title: SpaceDudem/text-humanizer
source: https://github.com/SpaceDudem/text-humanizer
stars: 743
category: AI & Agents
---

# SpaceDudem/text-humanizer

- **URL**: https://github.com/SpaceDudem/text-humanizer
- **Stars**: 743
- **Language**: Python
- **Category**: AI & Agents
- **Topics**: ai-humanizer, gpt-zero, text-humanizer

## What it does
text-humanizer is an open-source tool that converts AI-generated text into a more human-like version. It aims to bypass AI detection systems while preserving the original meaning of the text.

## Why it's interesting
Unlike standard text rewriting tools, text-humanizer employs a multi-step process involving different translation engines and large language models (LLMs) to enhance linguistic diversity and naturalness, which may help it evade detection by systems like Turnitin or GPTZero.

## How it works
The process consists of four main steps: 1) rewriting the text using the DeepSeek LLM, 2) translating the output into Turkish via Google Translate, 3) optionally translating the Turkish text into Japanese using the DeepL API, and 4) reconstructing the final text back into the original language with DeepSeek. The README does not specify the exact models or methods used in the DeepSeek LLM, leaving some uncertainty about its architecture.

## Get started in 5 minutes
1. Clone the repository: `git clone https://github.com/SpaceDudem/text-humanizer.git`
2. Navigate to the directory: `cd text-humanizer`
3. Install dependencies: `pip install -r requirements.txt`
4. Create a configuration file: `copy .\config\config.example.toml .\config.toml`
5. Run the application: `python main.py`

## Watch out for
The project is relatively new (created in September 2026) and has not been extensively tested in various environments. Users should be cautious about the effectiveness of the tool in bypassing AI detectors, as the README does not provide empirical evidence or benchmarks. The licensing is MIT, which is permissive, but users should ensure compliance with any API usage terms for DeepSeek and DeepL.
