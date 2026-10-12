---
title: zhongerxin/iPhone-use
source: https://github.com/zhongerxin/iPhone-use
stars: 3305
category: Developer Tools
---

# zhongerxin/iPhone-use

- **URL**: https://github.com/zhongerxin/iPhone-use
- **Stars**: 3305
- **Language**: Python
- **Category**: Developer Tools
- **Topics**: None

## What it does
This repository allows users to control a real iPhone via USB using natural language commands processed by Codex. It facilitates tasks such as app navigation, screen reading, and input automation, while providing real-time screen previews.

## Why it's interesting
Unlike traditional automation tools that require extensive setup or separate server instances, this tool integrates directly with Codex and leverages WebDriverAgent for seamless communication with the iPhone. It offers a unique approach by allowing users to interact with their devices using conversational prompts, making automation more accessible.

## How it works
The tool operates by establishing a local Python MCP service that communicates with the iPhone through WebDriverAgent (WDA). It requires a macOS environment with Xcode and a connected iPhone, where users must install and sign WDA Runner using their Apple developer account. The setup process is guided by Codex, which helps users through installation and configuration steps. The tool also sends anonymous usage statistics to PostHog unless disabled by specific environment variables.

## Get started in 5 minutes
1. Ensure you have macOS, Xcode, and a USB-connected iPhone.
2. Install WDA Runner on your iPhone by following the setup instructions provided in the README.
3. Clone the repository and run the installation script:
   ```sh
   git clone https://github.com/zhongerxin/iPhone-use.git
   cd iPhone-use
   sh scripts/install.sh
   ```
4. Use the provided prompt to configure Codex for your iPhone.

## Watch out for
The repository is currently private, requiring GitHub access permissions or a source code package to use. Users need to handle Apple account login, device trust, and developer mode manually during setup. Additionally, the tool's performance may depend on the state of the iPhone and the responsiveness of the Codex model. The project is licensed under MIT, and users should review third-party dependencies for compliance.
