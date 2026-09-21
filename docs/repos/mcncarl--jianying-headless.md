---
title: mcncarl/jianying-headless
source: https://github.com/mcncarl/jianying-headless
stars: 2235
category: Developer Tools
---

# mcncarl/jianying-headless

- **URL**: https://github.com/mcncarl/jianying-headless
- **Stars**: 2235
- **Language**: Python
- **Category**: Developer Tools
- **Topics**: None

## What it does
Jianying Headless is a local automation tool designed for the Jianying (剪映) professional version on macOS. It allows users to generate editable drafts from structured editing plans, modify multi-track projects in isolation, and export videos using the native Jianying engine.

## Why it's interesting
This tool provides a unique workflow for AI video production, enabling batch draft generation and project handoff without relying on the official Jianying SDK. It supports specific versions of Jianying and integrates tightly with the macOS environment, which may appeal to developers working in video editing automation.

## How it works
The tool operates by taking video materials and editing plans to create editable drafts that can be exported as MP4 files using the native Jianying engine. It requires a compatible version of Jianying (11.5.0 or 11.4.2) and Python 3.9+, along with other dependencies like FFmpeg and Xcode Command Line Tools. The README outlines a core process involving material and editing plans leading to draft creation and native engine export, but it also notes that modifications made in Jianying after draft creation do not sync back to the original plans. There are specific checks for environment compatibility and project structure, but the README does not clarify the extent of testing across different macOS versions or hardware configurations.

## Get started in 5 minutes
1. Clone the repository: `git clone https://github.com/mcncarl/jianying-headless.git`
2. Navigate to the directory: `cd jianying-headless`
3. Build the native codec: `python3 tools/build_native_codec.py`
4. Run the environment check: `python3 skills/yichen-jianying-edit/scripts/headless_draft.py doctor`
5. Prepare your JSON plan and execute the build and export commands as detailed in the README.

## Watch out for
The project is not guaranteed to work on any macOS machine due to specific version dependencies and environment checks. It does not support all versions of Jianying or all effects, and there are known limitations regarding the editing of complex clips and certain media formats. The licensing is restrictive, allowing only personal and non-commercial use without explicit permission for commercial applications. Additionally, the README indicates that the project is still under development, with ongoing issues and limitations that may affect usability.
