---
title: storytold/wordcraft
source: https://github.com/storytold/wordcraft
stars: 7771
category: Developer Tools
---

# storytold/wordcraft

- **URL**: https://github.com/storytold/wordcraft
- **Stars**: 7771
- **Language**: Rust
- **Category**: Developer Tools
- **Topics**: None

## What it does
WordCraft is an open-source word processor that reimplements Microsoft Word using pure Rust. It supports reading and writing .docx files and offers features like track changes, styles, tables, and mail merge, running natively on multiple operating systems and in the browser via WebAssembly.

## Why it's interesting
Unlike typical alternatives, WordCraft is built from the ground up in Rust, emphasizing performance and privacy by functioning offline. It aims to replicate the familiar Microsoft Word interface and workflow without relying on frameworks like Electron or Tauri, thus providing a native experience across platforms.

## How it works
The architecture is layered, with various crates handling different aspects of the application, such as document editing, layout, rendering, and user interface. The core functionality is driven by a command system, allowing both user and agent interactions. The README indicates that WordCraft is in alpha, covering 88% of Word's ribbon features, but it is uncertain how complete the implementation is in terms of stability and fidelity to Word's features.

## Get started in 5 minutes
To try WordCraft, clone the repository and run the following commands:
```sh
git clone https://github.com/storytold/wordcraft
cd wordcraft
cargo run --release -p wordcraft -- --sample        # the desktop app with the sample document
```

## Watch out for
WordCraft is currently in alpha, with about 60% of the functionality needed for real work compared to Microsoft Word. Users should be aware of potential gaps in feature parity, especially with complex documents, and the README suggests that testing against real-world .docx files is needed for further development. Licensing is under MIT or Apache-2.0, which is permissive but should be reviewed for specific use cases.
