---
title: storytold/gridcraft
source: https://github.com/storytold/gridcraft
stars: 3391
category: Developer Tools
---

# storytold/gridcraft

- **URL**: https://github.com/storytold/gridcraft
- **Stars**: 3391
- **Language**: Rust
- **Category**: Developer Tools
- **Topics**: None

## What it does
GridCraft is an open-source spreadsheet application implemented in pure Rust, designed to replicate the functionality of Microsoft Excel. It supports multiple platforms, including macOS, Windows, Linux, BSD, and the web via WebAssembly.

## Why it's interesting
GridCraft differentiates itself by being a clean-room reimplementation of Excel, focusing on performance with features like copy-on-write workbooks and incremental recalculation. It also aims for high compatibility with Excel's file formats, including XLSX, while being entirely built in Rust, which may appeal to developers interested in systems programming and performance.

## How it works
The architecture consists of a layered Cargo workspace, with separate crates for core functionalities, formulas, models, and the user interface. The application uses a dependency-graph calculation engine and supports over 500 worksheet functions. It also features an MCP server for agent-driven commands, allowing for automation and control via a JSON channel. The README indicates that the project is in alpha, with ongoing work to improve fidelity and compatibility with Excel files.

## Get started in 5 minutes
To quickly try GridCraft, clone the repository and run the following commands:
```sh
cargo run --release -p gridcraft -- --sample sales
```
This command opens a sample workbook. For web usage, navigate to the `apps/gridcraft-web` directory and run:
```sh
trunk serve --release
```
This will serve the application at `http://127.0.0.1:8771`.

## Watch out for
GridCraft is currently in alpha, meaning it may not be fully stable or feature-complete. The README notes that while it covers 89% of Excel's ribbon commands and 513 of 523 worksheet functions, it is estimated to be about 50% ready for real work. Users should be cautious about potential bugs and incomplete features, especially regarding file compatibility and performance on older hardware.
