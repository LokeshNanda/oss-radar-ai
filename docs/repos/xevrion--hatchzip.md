---
title: xevrion/hatchzip
source: https://github.com/xevrion/hatchzip
stars: 2001
category: Developer Tools
---

# xevrion/hatchzip

- **URL**: https://github.com/xevrion/hatchzip
- **Stars**: 2001
- **Language**: Rust
- **Category**: Developer Tools
- **Topics**: 7z, 7zip, archive, archive-extractor, cli, crash-safe, disk-space, extract, extractor, gui, in-place, linux, macos, rar, rust, tar, unrar, unzip, windows, zip

## What it does
HatchZip is an open-source archive extractor that supports ZIP, 7z, RAR, tar, and split archives. It extracts files in place, meaning it only requires enough disk space for the extracted files, not the original archive and the extracted files simultaneously.

## Why it's interesting
Unlike traditional extractors that require additional space for both the archive and the extracted files, HatchZip allows for extraction even when disk space is limited. It does this by removing parts of the archive as files are extracted, making it particularly useful for large archives on nearly full disks.

## How it works
HatchZip reads the archive from the end and cuts off finished parts as files are extracted, which allows it to reuse disk space. It checks available disk space before extraction, maintains a safety margin, and can resume interrupted extractions. The tool is built in Rust and provides both a desktop app and a command-line interface (CLI).

## Get started in 5 minutes
To quickly try HatchZip, download the appropriate installer for your OS from the [latest release](https://github.com/xevrion/hatchzip/releases/latest). For command-line usage, you can install it via a package manager like Homebrew or Scoop, or run the installation script directly from the terminal. For example, on Linux:
```sh
curl -fsSL https://raw.githubusercontent.com/xevrion/hatchzip/main/install.sh | sh
```

## Watch out for
The project is relatively new, created in October 2026, and may not have the maturity of established tools like 7-Zip or WinRAR. It is not yet code-signed, which may trigger security warnings on Windows. Additionally, while it supports multiple archive formats, RAR support requires additional compilation steps and a C++ compiler.
