---
title: JustAResearcher/gpu-unlock-ada
source: https://github.com/JustAResearcher/gpu-unlock-ada
stars: 3461
category: Developer Tools
---

# JustAResearcher/gpu-unlock-ada

- **URL**: https://github.com/JustAResearcher/gpu-unlock-ada
- **Stars**: 3461
- **Language**: C
- **Category**: Developer Tools
- **Topics**: None

## What it does
This repository provides a Linux kernel module that enables speed-select overrides for NVIDIA RTX 4090 and experimental RTX 4070 Ti SUPER GPUs, significantly increasing tensor throughput for FP16 and BF16 operations. It allows users to generate firmware locally to unlock additional performance capabilities of these GPUs.

## Why it's interesting
Unlike standard NVIDIA drivers, this tool allows for enhanced performance by overriding default settings, achieving up to 2× throughput for specific tensor operations. It is particularly relevant for developers and researchers working with high-performance computing and machine learning workloads who require maximum efficiency from their hardware.

## How it works
The module runs before the NVIDIA driver initializes, performing a PCIe Function Level Reset (FLR) and modifying the GPU's firmware settings. It requires specific kernel command line options to activate and supports various experimental targets, each needing an opt-in flag. The README details extensive performance benchmarks and the specific configurations needed for different GPU models, although it does not clarify the full range of potential compatibility with all Ada architecture GPUs.

## Get started in 5 minutes
To try it, clone the repository and build the module:
```sh
git clone https://github.com/JustAResearcher/gpu-unlock-ada.git
cd gpu-unlock-ada
make install
```
Then, configure your kernel command line with the appropriate PCI addresses for your GPU.

## Watch out for
This project is relatively new (created in October 2026) and may not be fully mature. Users should be cautious about potential stability issues, as the README notes that results can vary by card and configuration. The repository is licensed under GPL-2.0, and users should ensure they comply with this license when using or modifying the code.
