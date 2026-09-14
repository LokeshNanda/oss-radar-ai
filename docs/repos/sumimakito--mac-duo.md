---
title: sumimakito/Mac-Duo
source: https://github.com/sumimakito/Mac-Duo
stars: 823
category: Other
---

# sumimakito/Mac-Duo

- **URL**: https://github.com/sumimakito/Mac-Duo
- **Stars**: 823
- **Language**: Swift
- **Category**: Other
- **Topics**: flip, iphone, iphoneduo, mac, macos, menubar, menubar-app, menubarapp

## What it does
Mac Duo adds a visual effect to MacBooks that simulates the iPhone Duo effect when the lid is closed, causing the screen content to tilt, blur, and fade. It provides controls in the menu bar for adjusting the effect's perspective and rendering.

## Why it's interesting
This application uniquely leverages GPU rendering and real-time screen capture to create a visually appealing effect that is not commonly found in other macOS applications. It specifically targets MacBooks with a lid angle sensor, providing a tailored experience that enhances the device's aesthetics.

## How it works
The app uses Metal for GPU rendering to apply perspective, blur, and dimming effects. It captures the screen content in real-time using ScreenCaptureKit. The README notes that the effect is limited to MacBooks with a compatible built-in lid angle sensor, and it does not work with external displays or when macOS is in sleep mode. Uncertainties include the specifics of the rendering process and how it interacts with different macOS versions beyond the stated requirements.

## Get started in 5 minutes
To try Mac Duo, download the DMG or ZIP from the releases section, install it, and grant Screen Recording permission when prompted. Ensure you have macOS 14 or later and a compatible MacBook.

## Watch out for
The app is limited to MacBooks with a built-in lid angle sensor, and it may not function as expected on unsupported models. Additionally, the effect stops when macOS sleeps, and clicks pass through to underlying applications. The project is licensed under the Apache License 2.0.
