---
title: robbietilton/Compositor
source: https://github.com/robbietilton/Compositor
stars: 4039
category: Developer Tools
---

# robbietilton/Compositor

- **URL**: https://github.com/robbietilton/Compositor
- **Stars**: 4039
- **Language**: Swift
- **Category**: Developer Tools
- **Topics**: None

## What it does
Compositor is an open-source image editing application designed as a free alternative to Adobe Photoshop, specifically for macOS. It offers a range of features including layers, selections, painting tools, adjustments, and filters, all aimed at providing a familiar workflow for users accustomed to Photoshop.

## Why it's interesting
Unlike GIMP, which many users find less intuitive, Compositor aims to replicate the Photoshop experience while being completely free and open source. This focus on user familiarity and a comprehensive feature set makes it a compelling option for those looking for a cost-effective image editing solution.

## How it works
Compositor is built using Swift and requires macOS 26 and Xcode 26 to build from source. The application structure includes features like layers with blend modes, non-destructive transformations, various selection tools, and a range of painting and adjustment options. The README provides a script for releasing the application, which involves notarization and packaging, but does not detail the internal architecture or specific libraries used.

## Get started in 5 minutes
To try Compositor, clone the repository, open `Compositor.xcodeproj` in Xcode, and run the **Compositor** scheme. Ensure you have macOS 26 and Xcode 26 installed.

## Watch out for
The repository is relatively new, created in September 2026, which may imply that it is still in development and could have bugs or incomplete features. Additionally, users need to manage external notarization credentials and a Developer ID Application certificate for building releases, which may complicate the setup process.
