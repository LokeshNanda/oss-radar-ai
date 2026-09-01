---
title: crmne/fastpotify
source: https://github.com/crmne/fastpotify
stars: 1205
category: Other
---

# crmne/fastpotify

- **URL**: https://github.com/crmne/fastpotify
- **Stars**: 1205
- **Language**: Rust
- **Category**: Other
- **Topics**: audio, cross-platform, desktop-app, egui, gui, librespot, linux, macos, mpris, music, music-player, rust, spotify, spotify-client, spotify-connect, windows

## What it does
Fastpotify is a lightweight Spotify client written in Rust that allows users to play music locally and control playback on other devices via Spotify Connect. It supports features like gapless playback, a customizable library, and a Winamp mini player, while consuming significantly less memory than the official Spotify app.

## Why it's interesting
Fastpotify differentiates itself from the official Spotify client by being a native application that runs on multiple platforms (Linux, macOS, Windows) with a focus on performance and resource efficiency. It also offers unique features like MilkDrop visualizations and a keyboard-first interface, appealing to users who prefer a more customizable and responsive music player experience.

## How it works
The application utilizes the librespot library for playback and Spotify Connect functionality, and it employs the egui framework for its user interface. The architecture includes modules for handling playback, API interactions, and UI rendering, with a focus on maintaining a single instance across platforms. The README does not specify the exact internal architecture beyond the mentioned modules, leaving some details about the implementation uncertain.

## Get started in 5 minutes
To install Fastpotify, on Arch Linux, run `yay -S fastpotify-bin`. For macOS, use Homebrew with `brew install --cask crmne/tap/fastpotify`. Alternatively, you can build it from source using `cargo install --path .` with Rust 1.95 or newer. After installation, sign in with Spotify to start using the app.

## Watch out for
Fastpotify requires a Spotify Premium account for music playback, while free accounts can only browse and search. The application is still relatively new (created in August 2026) and may have undiscovered bugs or limitations. Additionally, it is not affiliated with Spotify, and users should be aware of the potential risks associated with using third-party clients.
