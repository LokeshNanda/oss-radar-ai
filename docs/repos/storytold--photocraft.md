---
title: storytold/photocraft
source: https://github.com/storytold/photocraft
stars: 1439
category: Other
---

# storytold/photocraft

- **URL**: https://github.com/storytold/photocraft
- **Stars**: 1439
- **Language**: Rust
- **Category**: Other
- **Topics**: adobe, adobe-photoshop-2026, adobe-photoshop-2026-ai, art, image-editing, image-editing-software, image-editor, images, photo-editing, photoshop, psd, rust

## What it does
PhotoCraft is an open-source image editing application that reimplements Adobe Photoshop using pure Rust. It supports features like layers, masks, adjustment layers, and real PSD file handling, allowing users to edit images offline without relying on proprietary software.

## Why it's interesting
Unlike traditional image editing software, PhotoCraft is built entirely in Rust, which may offer performance benefits and a more modern architecture. It aims for high fidelity in PSD file compatibility, claiming to round-trip 134 out of 135 real-world PSD files byte-for-byte, which is a significant achievement for open-source alternatives.

## How it works
PhotoCraft uses a pure-data document model and a command engine, with a user interface built on top of the `egui` library. It features a dual compositor system (CPU and GPU) for rendering, and employs a clean-room approach, meaning it was developed without using any proprietary code or assets. The application is structured across 24 crates, and it includes a command registry of over 500 commands that can be accessed via the UI, CLI, or control channels. The README does not specify the exact architecture details beyond this, leaving some uncertainty about the internal workings.

## Get started in 5 minutes
To try PhotoCraft, clone the repository using the command:
```sh
git clone https://github.com/storytold/photocraft.git
```
Further instructions for building and running the application are not provided in the truncated README, so additional steps may be required.

## Watch out for
The project is in an early alpha stage, which suggests that it may have stability issues or incomplete features. The README does not provide extensive documentation or a clear roadmap, so users should be cautious about relying on it for production use. Licensing is under MIT or Apache-2.0, which is permissive but should be reviewed for compliance in commercial contexts.
