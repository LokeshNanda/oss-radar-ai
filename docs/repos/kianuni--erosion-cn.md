---
title: Kianuni/Erosion-CN
source: https://github.com/Kianuni/Erosion-CN
stars: 2177
category: Developer Tools
---

# Kianuni/Erosion-CN

- **URL**: https://github.com/Kianuni/Erosion-CN
- **Stars**: 2177
- **Language**: Swift
- **Category**: Developer Tools
- **Topics**: None

## What it does
Erosion-CN is a toolbox for iOS/iPadOS system configuration and MobileGestalt research, designed to enhance device capabilities while ensuring safety against bootloop issues. It supports iOS/iPadOS versions 27.0 to 27.2.1 and partially supports 26.x, offering features like dynamic cache data management and dual backup systems.

## Why it's interesting
Unlike standard configuration tools, Erosion-CN provides a bilingual interface (English and Chinese) and focuses on security enhancements, such as preventing bootloop and ensuring safe writes to system files. It also addresses specific regional limitations for Chinese devices, making it particularly useful for users in China.

## How it works
Erosion-CN builds on the upstream project Erosion and incorporates various safety mechanisms, including real-time parsing of `libMobileGestalt.dylib` for dynamic cache management and a dual backup system using SHA-256. The README details specific technical implementations, such as using `pwrite` with `F_FULLFSYNC` for safe writes and maintaining original system file integrity. However, the exact architecture of the underlying system modifications is not fully detailed, leaving some uncertainty about the implementation specifics.

## Get started in 5 minutes
To try Erosion-CN, download the latest IPA from the [Releases page](https://github.com/Kianuni/Erosion-CN/releases/latest) and install it using a signing tool like SideStore or AltStore. Ensure you have a valid App Group container permission for installation.

## Watch out for
The project is intended for research and educational purposes, with a warning about potential risks when modifying system configurations. Users should back up their devices before use, as changes can lead to unexpected behavior. The licensing is under GPLv3, which may impose restrictions on commercial use.
