---
title: Gathin23/cleanyourtv
source: https://github.com/Gathin23/cleanyourtv
stars: 3264
category: Developer Tools
---

# Gathin23/cleanyourtv

- **URL**: https://github.com/Gathin23/cleanyourtv
- **Stars**: 3264
- **Language**: Java
- **Category**: Developer Tools
- **Topics**: ad-free, adb, android-tv, android-tv-launcher, bloatware-removal, claude-code, debloat, google-tv, hisense, home-screen, launcher, nvidia-shield, open-source, smart-tv, sony-bravia, tcl, xiaomi

## What it does
This repository provides a tool to debloat Android TV and Google TV devices over Wi-Fi, allowing users to remove unwanted ads and replace the default home screen with a custom launcher that resembles Apple TV's interface. The process is reversible, requiring no rooting of the device.

## Why it's interesting
Unlike typical launcher apps, this tool leverages ADB (Android Debug Bridge) to disable bloatware and telemetry without uninstalling any apps, making it a safer and more user-friendly option for users who want to customize their TV experience without deep system modifications.

## How it works
The tool operates by connecting to the TV via ADB after enabling USB debugging. It backs up installed packages, disables unwanted services using `pm disable-user`, and installs a lightweight custom launcher. The repository includes scripts and a Python-based ADB client to facilitate these operations, and it supports a wide range of Android TV devices. However, it does not support Samsung and LG TVs, and certain restrictions apply to specific models, particularly those from TCL with stricter firmware.

## Get started in 5 minutes
1. Enable USB debugging on your Android TV.
2. On your computer, ensure it's on the same Wi-Fi network as the TV.
3. Use the provided prompt in `PROMPT.md` with a coding assistant like Claude Code to initiate the debloating process.

## Watch out for
The repository is relatively new, created in October 2026, and while it has garnered a significant number of stars (3264), the maturity of the tool may still be in question. Users should be cautious about potential compatibility issues with specific TV models and ensure they follow the instructions carefully to avoid any unintended consequences. Licensing details are not explicitly mentioned in the README, so users should verify the licensing terms before use.
