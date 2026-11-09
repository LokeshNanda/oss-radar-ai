---
title: govijr/terminal-mac
source: https://github.com/govijr/terminal-mac
stars: 2470
category: Developer Tools
---

# govijr/terminal-mac

- **URL**: https://github.com/govijr/terminal-mac
- **Stars**: 2470
- **Language**: Swift
- **Category**: Developer Tools
- **Topics**: cli, gui, macos, shell, swift, terminal, tui

## What it does
`terminal-mac` allows users to run a separate macOS environment within their terminal on Apple silicon Macs. It utilizes Apple Virtualization to create a virtual Mac that can be controlled and viewed through terminal commands, providing a unique way to interact with macOS applications and files.

## Why it's interesting
This project stands out because it enables a full macOS experience directly in the terminal, which is not commonly available in other virtualization solutions. It allows for seamless interaction with a virtual Mac without affecting the host system, making it useful for developers and testers who need isolated environments.

## How it works
The architecture relies on Apple Virtualization to run a macOS guest, with a helper application capturing the screen and handling input events. The terminal viewer streams the guest's screen using Kitty or iTerm2 graphics. The setup requires a compatible macOS restore image and involves a guided installation process to configure the guest environment. The README indicates that the project is still in an early release candidate stage, and some features, such as tmux passthrough, are not yet implemented.

## Get started in 5 minutes
To try it, run the following command in your terminal:
```sh
curl -fsSL https://github.com/govijr/terminal-mac/releases/latest/download/get.sh | bash
```
This will download and install the latest release, after which you can start the virtual Mac with `terminal-mac up`.

## Watch out for
The project is labeled as an early release candidate, meaning it may have stability issues and lacks Apple notarization for its releases. Users should be cautious about the self-signed nature of the application and the need for specific permissions within the guest macOS environment. Additionally, features like VM cloning and unattended guest setups are still in development.
