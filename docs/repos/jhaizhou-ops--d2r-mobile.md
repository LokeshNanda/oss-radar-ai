---
title: jhaizhou-ops/d2r-mobile
source: https://github.com/jhaizhou-ops/d2r-mobile
stars: 3991
category: Other
---

# jhaizhou-ops/d2r-mobile

- **URL**: https://github.com/jhaizhou-ops/d2r-mobile
- **Stars**: 3991
- **Language**: C
- **Category**: Other
- **Topics**: compatibility-layer, diablo-2-resurrected, diablo2, game-port, ios, ipad, iphone, mac, macos, metal, reign-of-the-warlock

## What it does
D2R Mobile is an open-source compatibility layer that allows users to run Diablo II: Resurrected (with the Reign of the Warlock expansion) natively on iOS and macOS devices. It enables full touch controls, maintains a steady 60 fps, and requires users to provide their own game files from the Nintendo Switch version.

## Why it's interesting
Unlike traditional emulators, D2R Mobile executes the original game code directly on Apple devices without any emulation, which results in a more efficient and responsive gaming experience. It also includes a complete touch control scheme and additional endgame content not present in the original game, enhancing the overall gameplay experience.

## How it works
The compatibility layer operates by rewriting only a few instructions of the original aarch64 program to run on Apple's kernel, while the rest of the game code remains unchanged. It utilizes Apple's Metal for graphics rendering, translating shaders offline to avoid runtime compilation. The README does not provide detailed architectural diagrams or specific components of the codebase, leaving some uncertainty about the internal workings.

## Get started in 5 minutes
To try D2R Mobile, clone the repository, follow the instructions in the [docs/GAME_FILES.md](https://github.com/jhaizhou-ops/d2r-mobile/docs/GAME_FILES.md) to prepare your game files, and install the app on your iOS or macOS device. Ensure your device meets the specified requirements for compatibility.

## Watch out for
The project is in a developer preview stage for Apple TV 4K, and there is no multiplayer support; the game runs fully offline. Users must bring their own game files, as the repository does not contain any game content. The license is MIT, which allows for modification and redistribution, but users should be aware of the legal implications of using their own game files.
