---
title: tobi/disktree
source: https://github.com/tobi/disktree
stars: 1744
category: Developer Tools
---

# tobi/disktree

- **URL**: https://github.com/tobi/disktree
- **Stars**: 1744
- **Language**: Rust
- **Category**: Developer Tools
- **Topics**: None

## What it does
`disktree` is a disk usage visualization tool that represents directories as a treemap, allowing users to identify and remove files that occupy significant disk space. It scans the user's home directory by default and provides a graphical interface for marking files for deletion while displaying available free space.

## Why it's interesting
Unlike traditional disk usage tools that present data in lists or simple graphs, `disktree` offers an interactive treemap visualization that allows users to navigate through their file system visually. This approach can make it easier to identify large files and directories at a glance, and it integrates with the Omarchy desktop environment, maintaining a consistent theme.

## How it works
The application is built using Rust and the GPUI framework, which allows it to leverage GPU acceleration for rendering. It scans directories to calculate disk usage, presenting the data in a nested mosaic format. Users can interact with the interface using keyboard and mouse controls to mark files for deletion, which are then reviewed before any action is taken. The README details specific behaviors on different operating systems, including handling of hidden files and permissions.

## Get started in 5 minutes
To try `disktree`, download the appropriate release binary for your OS from the [latest release page](https://github.com/tobi/disktree/releases/latest). For Linux, unpack the tar.gz file and run `./install.sh`, or clone the repository and run `make install`. For macOS, unzip the downloaded file and drag `disktree.app` into Applications. On Windows, unpack the zip file and run `disktree.exe` directly.

## Watch out for
The repository is relatively new, created in September 2026, which may imply limited community support or maturity. Users need Rust 1.97 or newer, and the application requires a compatible GPU for rendering. There are specific instructions for macOS regarding permissions and notarization that may be necessary for proper functionality. Additionally, the README does not specify a license, which could be a concern for some users.
