---
title: jev-chat/jev-chat-jarvis
source: https://github.com/jev-chat/jev-chat-jarvis
stars: 6856
category: AI & Agents
---

# jev-chat/jev-chat-jarvis

- **URL**: https://github.com/jev-chat/jev-chat-jarvis
- **Stars**: 6856
- **Language**: Kotlin
- **Category**: AI & Agents
- **Topics**: accessibility-service, android, chat-assistant, llm, qq

## What it does
Jev Chat Jarvis is an Android chat assistant that analyzes conversations in supported messaging platforms (QQ, X/Twitter, and Feishu) and provides suggested replies without sending messages automatically. It operates using accessibility services to read on-screen text and offers a local knowledge base for context-aware responses.

## Why it's interesting
Unlike many chatbots that directly send messages, Jev Chat Jarvis maintains user control by only filling in suggested replies without sending them automatically. It also does not modify the chat applications, ensuring a non-intrusive experience. The ability to adapt to multiple platforms with minimal configuration is a notable feature.

## How it works
The application reads chat messages using Android's accessibility services and employs OCR for platforms where text is not directly accessible (like Feishu). It processes the text through user-configured AI models to generate response suggestions, which are displayed in a floating window. The architecture includes a modular adapter system for different chat applications, and it relies on local storage for user data, with no external data transmission unless configured by the user.

## Get started in 5 minutes
1. Download the APK from the [release page](https://raw.githubusercontent.com/jev-chat/jev-chat-jarvis/main/apk/jev-assistant-v1.4-release.apk).
2. Install the APK using `adb install -r apk/jev-assistant-v1.4-release.apk`.
3. Open the app, enter your API key in the settings, and enable accessibility permissions as guided.

## Watch out for
The project is relatively new (created in September 2026) and may have stability issues. It does not support WeChat due to policy changes. Users should be aware of privacy implications when using third-party model services for processing chat data, as the application sends data to these services based on user configuration. Additionally, the app may face limitations on certain devices, particularly those with aggressive battery management settings.
