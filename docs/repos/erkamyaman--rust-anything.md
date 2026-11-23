---
title: erkamyaman/rust-anything
source: https://github.com/erkamyaman/rust-anything
stars: 8568
category: Developer Tools
---

# erkamyaman/rust-anything

- **URL**: https://github.com/erkamyaman/rust-anything
- **Stars**: 8568
- **Language**: Rust
- **Category**: Developer Tools
- **Topics**: agent-skills, claude-code, cli, code-migration, codex, ffi, golang, java, javascript, mcp, migration, napi, performance, porting, pyo3, python, rewrite, ruby, rust, typescript

## What it does
`rust-anything` allows developers to incrementally rewrite applications in Rust while ensuring that the new code behaves identically to the original. It supports various programming languages including TypeScript, Python, C, Go, Ruby, and Java, and verifies the correctness of each piece of rewritten code against recorded behavior from the original application.

## Why it's interesting
This tool stands out by not just translating code but by proving that the rewritten Rust code matches the original application's behavior through a recording and verification process. This approach mitigates risks associated with code migration, making it suitable for performance-critical applications where safety and correctness are paramount.

## How it works
The tool operates by recording the behavior of the original application using the `record` command, which captures outputs for various inputs. Developers can then use the `bridge` command to generate Rust code, which is checked against the recorded behavior using the `diff` command. The process continues until the entire application is rewritten in Rust, with the original code untouched until the migration is complete. It utilizes libraries like `napi-rs`, `PyO3`, and `wasm-bindgen` for cross-language functionality. However, the README does not specify how it handles edge cases or what limitations exist in the recording process, leaving some uncertainty.

## Get started in 5 minutes
To quickly get started, run the following commands:
```sh
cargo install rust-anything
rust-anything setup
```
This installs the tool and sets it up for use with various coding agents. Alternatively, prebuilt binaries are available for macOS, Linux, and Windows, which can be installed via npm with `npm install -g rust-anything`.

## Watch out for
The repository is relatively new, created in November 2026, which may imply that it is still maturing. Users should be cautious about potential bugs or incomplete features. Additionally, the README warns that the recording and replaying processes should be conducted on a copy of the project to avoid affecting production environments. The tool is licensed under the MIT license.
