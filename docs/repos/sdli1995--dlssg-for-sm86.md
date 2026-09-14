---
title: sdli1995/dlssg_for_sm86
source: https://github.com/sdli1995/dlssg_for_sm86
stars: 2570
category: Other
---

# sdli1995/dlssg_for_sm86

- **URL**: https://github.com/sdli1995/dlssg_for_sm86
- **Stars**: 2570
- **Language**: Unknown
- **Category**: Other
- **Topics**: None

## What it does
This repository provides a proxy for enabling NVIDIA DLSS frame generation (DLSS-G) specifically for RTX 30 Series GPUs (SM86) on Windows x64 using D3D12. It includes a DLL and configuration file that allow games to utilize DLSS frame generation without modifying the original game code.

## Why it's interesting
Unlike native implementations that may cause compatibility issues with certain games, this project uses a proxy DLL that embeds the unmodified original runtime, improving compatibility across a wider range of games. It also supports up to 6X frame generation in games that allow it, which is a notable enhancement over standard implementations.

## How it works
The project operates by replacing the game's original DLL with a custom `version.dll` that facilitates frame generation through a proxy mechanism. It includes performance optimizations and configuration options for frame generation limits. The README details specific requirements for system configuration, including supported NVIDIA drivers and GPU models, and provides performance benchmarks comparing original and optimized kernel performance. However, it does not clarify how the proxy interacts with different game engines or the specifics of its internal architecture beyond the proxying mechanism.

## Get started in 5 minutes
1. Exit the game completely.
2. Navigate to the game's executable directory.
3. Copy `version.dll` and `dlssg_sm86.ini` into this directory, backing up any existing `version.dll` first.
4. Launch the game and enable DLSS frame generation in the graphics settings.

## Watch out for
The project is in version 0.3.0, indicating it may still be in development and could have unresolved issues. It requires specific NVIDIA drivers and may not work with all games, particularly those that do not support the required frame generation features. The repository is licensed under GPLv3, which may impose restrictions on redistribution and modification.
