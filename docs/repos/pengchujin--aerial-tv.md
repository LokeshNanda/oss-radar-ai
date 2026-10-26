---
title: pengchujin/aerial-tv
source: https://github.com/pengchujin/aerial-tv
stars: 5757
category: Other
---

# pengchujin/aerial-tv

- **URL**: https://github.com/pengchujin/aerial-tv
- **Stars**: 5757
- **Language**: Kotlin
- **Category**: Other
- **Topics**: None

## What it does
Aerial is an open-source Android TV launcher designed to provide a clean desktop experience for Chinese market TVs, such as those from Xiaomi and TCL. It mimics the design of Apple TV's interface, eliminating ads and unwanted recommendations, and allows users to organize their apps and customize their home screen.

## Why it's interesting
Unlike typical Android TV interfaces that often include ads and promotional content, Aerial focuses on user customization and a clean aesthetic. It also supports a wide range of devices, including various brands and models, which is not common among similar launchers.

## How it works
Aerial operates by utilizing an accessibility service to maintain its presence as the default launcher, even when the system attempts to switch back to the original interface. It requires ADB debugging to be enabled on the TV for installation and can be installed via command line or through an agent application. The README provides detailed instructions for various TV brands and models, but it is unclear how well it performs on unsupported devices or older models without ADB access.

## Get started in 5 minutes
1. Enable ADB debugging on your TV (instructions vary by brand).
2. Use the command: `curl -fsSL https://aerial.qust.me/install.sh | KEEP_ADB=1 TV=<your-TV-IP> bash` to install Aerial.
3. Follow the prompts to set it as your default launcher.

## Watch out for
The project is relatively new, created in October 2026, and may still have bugs or incomplete features. Users should be cautious about compatibility with older devices or those that do not support ADB. The licensing is under MIT, which is permissive, but users should be aware of the potential for reliance on third-party services for features like wallpapers and screensavers.
