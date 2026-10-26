---
title: oosexgang/hackios-xnu-kernel
source: https://github.com/oosexgang/hackios-xnu-kernel
stars: 1551
category: Other
---

# oosexgang/hackios-xnu-kernel

- **URL**: https://github.com/oosexgang/hackios-xnu-kernel
- **Stars**: 1551
- **Language**: C
- **Category**: Other
- **Topics**: None

## What it does
HakiOS allows users to run the open-source XNU kernel on Android devices with Qualcomm SoCs, specifically the POCO X5 Pro 5G, and boot the stock iOS 16.5 user space. It operates entirely in RAM without flashing the device, making it a research tool rather than a traditional ROM.

## Why it's interesting
This project stands out because it enables the execution of iOS user space on non-Apple hardware, leveraging a custom boot loader and drivers. It provides a unique approach to exploring iOS functionality on Android devices, which is not commonly available in existing solutions.

## How it works
The repository contains a patch for the XNU kernel, a custom boot loader, and necessary drivers for the supported device. The system is built from source using scripts provided in the repository, and it requires the user to fetch the iOS IPSW file from Apple's servers. The architecture involves loading the kernel and user space into RAM and utilizing the device's existing firmware and device tree for operation. There is uncertainty regarding the support for additional Qualcomm devices, as only the POCO X5 Pro is currently documented.

## Get started in 5 minutes
To quickly try HakiOS in QEMU, clone the repository, run `sysimage/fetch.sh` to download the iOS IPSW, and then execute `userland/build.sh` followed by `qemu/run-ios.sh` to start a session. For running on the POCO X5 Pro, follow the instructions in the README to pull firmware and load the system into RAM.

## Watch out for
The project is experimental and not fully mature; certain features like cellular connectivity and Bluetooth are still in progress. Additionally, it does not include any iOS binaries or firmware, and users must provide their own IPSW and device firmware. Licensing is compliant with the Apple Public Source License 2.0 for the kernel patch, but users should be aware of the legal implications of using proprietary iOS components.
