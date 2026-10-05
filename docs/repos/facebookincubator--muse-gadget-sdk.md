---
title: facebookincubator/muse-gadget-sdk
source: https://github.com/facebookincubator/muse-gadget-sdk
stars: 1327
category: Developer Tools
---

# facebookincubator/muse-gadget-sdk

- **URL**: https://github.com/facebookincubator/muse-gadget-sdk
- **Stars**: 1327
- **Language**: C
- **Category**: Developer Tools
- **Topics**: None

## What it does
Muse Gadget SDK is an open-source software development kit that allows developers to create custom gadgets using off-the-shelf hardware like ESP32 boards and Raspberry Pi. It provides the necessary SDKs and firmware to connect these devices to the Muse platform, enabling interaction with various displays, buttons, sensors, and actuators.

## Why it's interesting
Unlike many other IoT SDKs, Muse Gadget SDK is specifically designed for hobbyists and developers who want to tinker with hardware and software integration. It emphasizes a DIY approach, allowing users to build their own devices and customize their functionality, which is appealing for those interested in hands-on experimentation.

## How it works
The SDK consists of two main components: the ESP32 Device SDK and the Linux Device SDK. The ESP32 SDK allows users to connect ESP32 boards to Muse, while the Linux SDK enables Raspberry Pi or Linux boxes to function as Muse gadgets. Each SDK has its own `README.md` for setup instructions and an `AGENTS.md` for coding agents. Users must obtain an SDK token to pair their gadgets with the Muse app on iOS and Android, which requires enabling Developer mode in the app.

## Get started in 5 minutes
1. Obtain an SDK token from the Muse settings page.
2. Choose either the ESP32 or Linux SDK and follow the setup instructions in the respective `README.md` file.
3. Flash your device and pair it with the Muse app by enabling Developer mode and looking for devices prefixed with "MuseGadget".

## Watch out for
The repository is relatively new, created in October 2026, which may indicate that it is still in active development and could have unresolved issues or incomplete features. Additionally, the README includes a disclaimer about potential risks, such as bricking devices or voiding warranties, which users should consider before proceeding. The licensing is under the Apache License 2.0, but there are third-party components with different licenses that users should review.
