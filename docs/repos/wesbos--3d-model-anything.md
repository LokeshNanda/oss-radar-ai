---
title: wesbos/3d-model-anything
source: https://github.com/wesbos/3d-model-anything
stars: 2012
category: Web & Frontend
---

# wesbos/3d-model-anything

- **URL**: https://github.com/wesbos/3d-model-anything
- **Stars**: 2012
- **Language**: Swift
- **Category**: Web & Frontend
- **Topics**: None

## What it does
This repository provides tools to capture room geometry and photographs using an iPhone with LiDAR, reconstructing them into editable Three.js scenes. It includes an iPhone app, a Three.js viewer, and an AI coding agent to assist in the modeling process.

## Why it's interesting
Unlike typical 3D modeling tools, this project focuses on an iterative reconstruction workflow that allows users to create detailed models of interior spaces rather than relying on a one-click solution. The integration of AI to assist in the modeling process is a notable feature that sets it apart from conventional 3D modeling applications.

## How it works
The architecture consists of an iPhone app for capturing room data, which exports this data for processing. The skill for converting scans to Three.js scenes is located in `.agents/skills/scan-to-threejs/SKILL.md`. Users can run a local viewer using Node.js to explore the reconstructed models. The README mentions that Python 3 is required for some helper scripts, and additional libraries like Pillow and NumPy may be needed for certain functionalities. However, the specifics of the AI agent's implementation and its capabilities are not detailed, leaving some uncertainty about its full functionality.

## Get started in 5 minutes
1. Ensure you have Node.js 22.12+ installed.
2. Clone the repository and navigate to it.
3. Run `npm ci` to install dependencies.
4. Start the development server with `npm run dev` and open http://localhost:5188 in your browser.

## Watch out for
The project is in an early stage, as indicated by its creation date in October 2026, and it currently only includes a demo of an office space. The app is not yet available on the App Store, and users should be cautious about privacy since captures should remain private before publishing. Licensing is under MIT for the source code, but asset terms apply separately, which may limit usage of included textures and images.
