---
title: Lemxy/WinRust
source: https://github.com/Lemxy/WinRust
stars: 1336
category: Other
---

# Lemxy/WinRust

- **URL**: https://github.com/Lemxy/WinRust
- **Stars**: 1336
- **Language**: Rust
- **Category**: Other
- **Topics**: None

## What it does
WinRust is a Windows shell replacement built in Rust, offering alternatives to the taskbar, file manager, file search, task manager, and disk cleaner. It aims to provide a lightweight and fast experience compared to the default Windows shell components.

## Why it's interesting
WinRust differentiates itself by being a native application without reliance on .NET or Electron, boasting significantly lower memory usage and faster performance metrics compared to Windows' built-in tools. For example, it claims to open folder windows in 60 ms versus 420 ms for Windows Explorer and uses only 46 MB of memory compared to 366 MB for Explorer.

## How it works
The architecture consists of a main installer (plugin-launcher.exe) that manages various plugins, each responsible for different functionalities like file searching and task management. The installer modifies Windows settings and services to integrate the new components, and all changes are reversible. The README provides details on the command-line interface for managing plugins and the build process, but it does not specify how the plugins interact with the Windows API or the underlying system.

## Get started in 5 minutes
1. Download `WinRust.exe` from the [latest release](https://github.com/Lemxy/WinRust/releases/latest).
2. Run it as administrator.
3. Select the components you want to install and press the install button.

## Watch out for
The application is not code-signed, which may trigger SmartScreen warnings. It also modifies core Windows components, which could lead to instability if not properly managed. Users are advised to test it on a spare machine or VM first. The README does not mention licensing details, which may be a concern for some developers.
