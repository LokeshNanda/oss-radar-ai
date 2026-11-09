---
title: NotRexed/Hookshot
source: https://github.com/NotRexed/Hookshot
stars: 3984
category: Other
---

# NotRexed/Hookshot

- **URL**: https://github.com/NotRexed/Hookshot
- **Stars**: 3984
- **Language**: C++
- **Category**: Other
- **Topics**: None

## What it does
Hookshot is a tool that allows users to run a native version of The Legend of Zelda: Ocarina of Time on Windows and Linux, using their own copy of the game. It recompiles the game's code into a format that can be executed on these operating systems without the need for an emulator.

## Why it's interesting
Unlike traditional emulators, Hookshot translates the game's code and reimplements the console's system software, providing potentially better performance and compatibility with modern hardware. It also utilizes Vulkan for graphics rendering, which can enhance visual fidelity and performance compared to older graphics APIs.

## How it works
The project uses a static recompilation approach, translating the game's code to C and compiling it into a native executable. The README details specific requirements for running the tool, including a supported version of the game, a compatible operating system, and a graphics card that supports Vulkan 1.3 and mesh shaders. The installation process involves using the Hookshot Builder to compile the game from the user's files, which can take 10 to 45 minutes depending on the hardware. The README also outlines various known issues and performance metrics across different hardware configurations.

## Get started in 5 minutes
1. Ensure you have a copy of the game at the supported version and a compatible system (64-bit Windows 10/11 or Linux with glibc 2.35+).
2. Download the latest release of `HookshotBuilder.exe` (Windows) or `Hookshot-<version>-x86_64.AppImage` (Linux) from the releases page.
3. Run the builder, select your game files, and follow the prompts to build and launch the game.

## Watch out for
The project is marked as experimental, with many features still under testing. Users have reported various issues, such as performance inconsistencies and graphical glitches, especially on AMD and Intel graphics cards. Additionally, the repository does not include the game files, and users must provide their own copy. There are warnings about false positives from antivirus software regarding the build tools, which users should be aware of.
