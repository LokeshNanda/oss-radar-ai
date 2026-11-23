---
title: AFK-surf/xnulinux
source: https://github.com/AFK-surf/xnulinux
stars: 1326
category: Developer Tools
---

# AFK-surf/xnulinux

- **URL**: https://github.com/AFK-surf/xnulinux
- **Stars**: 1326
- **Language**: Objective-C++
- **Category**: Developer Tools
- **Topics**: None

## What it does
`xnulinux` allows users to run macOS userspace applications on an unmodified arm64 Linux kernel by loading the macOS XNU kernel as a loadable kernel module. It facilitates the execution of macOS processes alongside Linux processes without a hypervisor, leveraging Linux for resources like memory and networking.

## Why it's interesting
This project stands out because it enables native execution of macOS applications directly on Linux hardware, which is uncommon compared to traditional virtualization or emulation solutions. It achieves this by integrating the macOS kernel into the Linux environment, allowing for a seamless experience between the two operating systems.

## How it works
The architecture involves loading the XNU kernel (`xnu.ko`) into the Linux kernel, which communicates with it through a foreign kernel interface (`fki.ko`). XNU directly manages CPUs and memory while relying on Linux for I/O operations and other system resources. The setup requires an arm64 Linux host with specific configurations, and it has been tested on platforms like NVIDIA DGX Spark and Apple Silicon Macs. However, details on performance metrics or limitations in certain scenarios are not fully outlined in the README.

## Get started in 5 minutes
1. Ensure you have an arm64 Linux host with at least 16 GB of RAM.
2. Follow the build instructions in the README, starting with `scripts/vm-xnu-build.sh` to set up the toolchain and build XNU.
3. Create a macOS VM disk using `scripts/mk-macvm-disk.sh` on a Mac.
4. Boot the hosted system using `scripts/xnulinux-boot.sh` on the Linux host.

## Watch out for
The project is still in development, with certain limitations such as slower memory access compared to native VMs and the need for specific hardware configurations. Licensing is also complex, as it involves multiple licenses (APSL-2.0, GPL-2.0) for different components, which may affect redistribution or usage in proprietary projects. Additionally, the README notes that the GPU bridge is not fully functional yet, limiting graphical performance.
