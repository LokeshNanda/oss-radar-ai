---
title: nullmoth/nvidia-macos-driver
source: https://github.com/nullmoth/nvidia-macos-driver
stars: 2673
category: Developer Tools
---

# nullmoth/nvidia-macos-driver

- **URL**: https://github.com/nullmoth/nvidia-macos-driver
- **Stars**: 2673
- **Language**: Rust
- **Category**: Developer Tools
- **Topics**: None

## What it does
This repository provides a Metal driver for NVIDIA GeForce RTX graphics cards on Intel Macs running macOS 15 Sequoia. It supports a range of NVIDIA GPUs and implements both display and Metal interfaces, allowing for enhanced graphics performance on compatible systems.

## Why it's interesting
Unlike standard macOS drivers, this project specifically targets NVIDIA's Turing and later architectures, enabling their use on macOS systems where official support is lacking. It also integrates with OpenCore, a popular bootloader for running macOS on non-Apple hardware, which is not commonly addressed by other drivers.

## How it works
The driver architecture includes a Metal driver plugin that translates Apple AIR to SPIR-V, which is then processed by a Vulkan back end (NVK) and kernel extensions (kexts) that interface with the GPU. The README details the installation paths for various components and outlines the necessary configurations for OpenCore, including specific NVRAM settings and boot arguments. However, the README does not specify the extent of testing across all supported GPUs, leaving some uncertainty about compatibility beyond the tested RTX 5060.

## Get started in 5 minutes
To quickly try the driver, download the prebuilt package from the Releases section, extract it, verify the SHA256 checksums, and run the installation script. Ensure to allow the necessary kernel extensions in System Settings after installation and reboot your system.

## Watch out for
The driver is still in development and may not work on every PC, as noted in the README. Users should be cautious about compatibility with their specific hardware configurations and ensure they follow the detailed installation instructions. The licensing restricts commercial use, allowing only personal, educational, and non-profit applications.
