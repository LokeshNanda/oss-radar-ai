---
title: ly05010419/MacNativeGames
source: https://github.com/ly05010419/MacNativeGames
stars: 1281
category: Other
---

# ly05010419/MacNativeGames

- **URL**: https://github.com/ly05010419/MacNativeGames
- **Stars**: 1281
- **Language**: C
- **Category**: Other
- **Topics**: None

## What it does
This repository allows users to build a native macOS application for playing **The Legend of Zelda: Tears of the Kingdom** on Apple silicon Macs, iPhones, and iPads. It requires users to provide their own game files and keys, as it does not distribute any game content.

## Why it's interesting
Unlike traditional emulators, this project runs the game's ARM64 code directly on Apple hardware, leveraging Metal for graphics rendering. This approach aims to provide better performance and smoother gameplay compared to typical emulation methods.

## How it works
The repository contains scripts and tools to compile the game into a macOS app or an unsigned iOS IPA. Users must have the original game files (XCI or NSP) and keys, and the build process involves using Python scripts to prepare shaders and game data. The app builds a shader cache to minimize stuttering during gameplay, and it collects shader data from users to improve performance for everyone. The README does not specify how the patch code or shader list is maintained beyond user contributions.

## Get started in 5 minutes
1. Ensure you have Xcode command line tools and Homebrew installed.
2. Clone the repository and navigate to its folder in Terminal.
3. Run the build script with your game file and keys:
   ```sh
   python3.14 build_app.py ~/Games/totk.xci -k ~/keys/prod.keys
   ```
4. Open the resulting app from Finder.

## Watch out for
The project is not affiliated with Nintendo and requires users to own a copy of the game, which raises potential legal concerns. The README lacks comprehensive documentation on troubleshooting and performance guarantees, and it may not cover all edge cases in shader compilation or game compatibility. Users should also be aware that the app may require significant disk space (up to 60 GB) for the build process.
