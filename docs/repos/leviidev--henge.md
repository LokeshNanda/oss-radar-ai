---
title: Leviidev/Henge
source: https://github.com/Leviidev/Henge
stars: 1442
category: Other
---

# Leviidev/Henge

- **URL**: https://github.com/Leviidev/Henge
- **Stars**: 1442
- **Language**: C
- **Category**: Other
- **Topics**: None

## What it does
Henge is an emulator that allows users to run macOS on iOS and iPadOS devices, specifically targeting A14 and M1 chips or newer. It enables the installation of macOS without needing a Mac, utilizing its own Just-In-Time (JIT) compilation and memory management unit (MMU).

## Why it's interesting
Henge stands out because it does not rely on existing virtualization frameworks like QEMU, instead implementing its own JIT and virtual GPU to render macOS applications. This approach allows for a unique emulation experience on mobile devices, which is not commonly available in other solutions.

## How it works
Henge downloads Apple's restore image and installs it directly on the device, emulating macOS's arm64 code through its own JIT. It uses Metal for graphics rendering and allows for touch input as a trackpad. The README notes that it has only been tested on an iPhone 17 Pro, and iPad support is new and untested on actual hardware, creating some uncertainty about performance across devices. Additionally, it mentions limitations such as a failure to sign in to an Apple Account and slower performance compared to a real Mac.

## Get started in 5 minutes
To try Henge, download `Henge.ipa` from the [Releases](https://github.com/Leviidev/Henge/releases) page and sideload it using SideStore or AltStore. Ensure you have iOS or iPadOS 17 or later on an A14 or M1 chip or newer, and follow the installation instructions provided in the README.

## Watch out for
Henge is still in development, with known issues such as graphics rendering problems in non-tested applications and limitations in keyboard shortcuts on iPadOS. It is licensed under GPL-2.0-or-later, which restricts its distribution on the App Store. Additionally, it has only been tested on a limited set of devices, raising concerns about its maturity and reliability across the broader iOS/iPadOS ecosystem.
