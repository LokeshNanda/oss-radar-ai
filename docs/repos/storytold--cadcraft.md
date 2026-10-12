---
title: storytold/cadcraft
source: https://github.com/storytold/cadcraft
stars: 3077
category: Developer Tools
---

# storytold/cadcraft

- **URL**: https://github.com/storytold/cadcraft
- **Stars**: 3077
- **Language**: Rust
- **Category**: Developer Tools
- **Topics**: None

## What it does
CADCraft is an open-source, AutoCAD-style application for computer-aided design and drafting, implemented in pure Rust. It supports native operation on multiple platforms, including macOS, Windows, Linux, FreeBSD, and offers a WebAssembly version for browser use.

## Why it's interesting
Unlike many CAD applications that rely on Electron or web views, CADCraft is built entirely in Rust, promising better performance and a more native experience. It also emphasizes a familiar AutoCAD workflow, making it easier for users transitioning from that environment.

## How it works
CADCraft's architecture separates concerns into distinct modules, such as geometry handling, DXF file processing, and rendering. The application uses a command line interface that mimics traditional CAD workflows, allowing for commands to be executed via typed input or JSON through an MCP (Multi-Channel Protocol) server. The README indicates that the application is in early development, and specific features may still be under construction or subject to change.

## Get started in 5 minutes
To try CADCraft, clone the repository and run the following commands:
```sh
git clone https://github.com/storytold/cadcraft
cd cadcraft
cargo run --release -p cadcraft -- --sample
```
This will open a sample drawing for you to interact with.

## Watch out for
CADCraft is currently in early development, which may imply incomplete features or bugs. The README mentions that not all CAD entities are modeled yet, and users should refer to the roadmap for feature parity. Additionally, it is licensed under MIT or Apache-2.0, which allows for flexibility in usage but requires attention to compliance with the chosen license.
