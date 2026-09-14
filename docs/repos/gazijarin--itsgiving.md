---
title: gazijarin/itsgiving
source: https://github.com/gazijarin/itsgiving
stars: 829
category: Other
---

# gazijarin/itsgiving

- **URL**: https://github.com/gazijarin/itsgiving
- **Stars**: 829
- **Language**: Python
- **Category**: Other
- **Topics**: None

## What it does
This repository provides a Python application that uses facial recognition to overlay memes based on user expressions during video calls. It supports a virtual camera feature, allowing users to integrate it with popular meeting platforms like Zoom and Teams.

## Why it's interesting
Unlike typical video filters, this application personalizes meme reactions based on individual facial expressions, utilizing MediaPipe for real-time facial landmark detection and calibration to each user's neutral expression. This adaptive approach aims to enhance user engagement in meetings with humor and creativity.

## How it works
The application leverages MediaPipe to detect facial landmarks and expressions, measuring deviations from a user's neutral state to trigger specific meme overlays. It includes two main scripts: `its_giving.py` for a fixed threshold version and `its_giving_v2.py`, which calibrates to the user's unique facial metrics. The setup involves creating a virtual camera using OBS Studio or similar tools, and the application requires specific versions of dependencies to function correctly, particularly MediaPipe and OpenCV.

## Get started in 5 minutes
1. Clone the repository.
2. Set up a Python virtual environment:
   ```bash
   python3.12 -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the calibration:
   ```bash
   python its_giving_v2.py --calibrate
   ```
5. Start the application:
   ```bash
   python its_giving_v2.py
   ```
6. Select the virtual camera in your meeting application.

## Watch out for
The repository is relatively new (created in September 2026) and may lack extensive documentation or community support. Users should be cautious about the dependency management, as specific versions are required to avoid compatibility issues. Additionally, the README advises against unpinning dependencies due to conflicts between MediaPipe and OpenCV versions. There is no explicit licensing information provided in the README.
