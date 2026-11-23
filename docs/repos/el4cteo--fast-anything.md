---
title: EL4CTEO/fast-anything
source: https://github.com/EL4CTEO/fast-anything
stars: 2902
category: Developer Tools
---

# EL4CTEO/fast-anything

- **URL**: https://github.com/EL4CTEO/fast-anything
- **Stars**: 2902
- **Language**: Rust
- **Category**: Developer Tools
- **Topics**: agent-skills, ai-agents, claude-code, claude-code-plugin, codex, developer-tools, ffi, mcp, mcp-server, napi-rs, nodejs, optimization, performance, profiler, pyo3, python, rewrite-it-in-rust, ruby, rust, typescript

## What it does
**fast-anything** is a tool that identifies slow functions in applications written in languages like Python, Node.js, Ruby, and others, and rewrites only those functions in Rust to improve performance. It profiles the application, ports the identified functions, and verifies that the Rust version behaves the same as the original.

## Why it's interesting
Unlike traditional approaches that suggest rewriting entire applications in Rust, **fast-anything** focuses on optimizing only the performance-critical parts, which can save significant development time and reduce risks associated with large-scale rewrites. It provides a fully reversible process, allowing developers to switch between the original and optimized versions seamlessly.

## How it works
The tool operates by profiling the target application to find the slowest functions, which are then ported to Rust using a coding agent (like Claude or Codex). It verifies the correctness of the ported functions by comparing outputs from the original and Rust implementations across various test cases. The README does not specify the internal architecture or how the coding agent interacts with the tool, leaving some uncertainty about the implementation details.

## Get started in 5 minutes
To try **fast-anything**, install it using npm or Cargo with the command:
```sh
npm i -g @el4cteo/fast-anything      # or: cargo install fast-anything
```
Then, run the profiling command:
```sh
fast-anything go --agent claude -- python app.py
```
Replace `python app.py` with your application command as needed.

## Watch out for
The repository is relatively new, created in November 2026, which may imply limited community support and potential bugs. The README does not mention any specific security concerns or licensing issues beyond the MIT license, but users should be cautious about using it in production environments until it has been more thoroughly vetted.
