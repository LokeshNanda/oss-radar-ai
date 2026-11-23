---
title: omonkeyz/xbox-emulator
source: https://github.com/omonkeyz/xbox-emulator
stars: 1535
category: Other
---

# omonkeyz/xbox-emulator

- **URL**: https://github.com/omonkeyz/xbox-emulator
- **Stars**: 1535
- **Language**: Rust
- **Category**: Other
- **Topics**: None

## What it does
The Xbox Emulator allows users to run Xbox Series X|S games on a PC by reimplementing the console's platform layer, including Direct3D 12 and system libraries. It tracks progress on compatibility with various titles and provides a Rust-based workspace for development.

## Why it's interesting
This project is a continuation of the TomBox emulator, focusing specifically on Xbox Series X|S compatibility, which is less common compared to emulators for older consoles. It emphasizes legal use of already-decrypted game dumps and aims for broad compatibility across multiple titles rather than being tied to a single game.

## How it works
The emulator's architecture includes a Rust workspace with directories for crates and tools, and it implements Xbox-specific Direct3D 12 methods, shader translations, and system library functions. Progress is tracked through various metrics, including system function coverage and shader translations, with detailed documentation on the status of each component. However, the README does not specify the exact architecture or design patterns used in the codebase, leaving some uncertainty about the internal workings.

## Get started in 5 minutes
To get started, clone the repository and navigate to the `crates/` and `tools/` directories for the source code. Follow the instructions in the `CONTRIBUTING.md` for building and contributing, as the README does not provide explicit setup instructions for running the emulator locally.

## Watch out for
The project is still in progress, with many features marked as incomplete, such as certain shader stages and audio functionality. It is licensed under GPL-3.0-or-later, which may impose restrictions on commercial use. Additionally, the README indicates that while some titles are playable, others may have significant issues, such as crashes or incomplete rendering.
