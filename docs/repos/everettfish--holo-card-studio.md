---
title: EverettFish/holo-card-studio
source: https://github.com/EverettFish/holo-card-studio
stars: 1517
category: Developer Tools
---

# EverettFish/holo-card-studio

- **URL**: https://github.com/EverettFish/holo-card-studio
- **Stars**: 1517
- **Language**: Python
- **Category**: Developer Tools
- **Topics**: None

## What it does
Holo Card Studio allows users to create customizable 3D holographic cards based on textual descriptions or uploaded reference images. It generates a finished Blender project and an interactive Three.js webpage, preserving user-defined attributes like subject, style, and typography.

## Why it's interesting
This tool leverages Codex to automate the creation of visually appealing cards, which can be used for various purposes such as gaming, personal events, or team introductions. Its integration with Blender and Three.js provides a unique combination of 3D modeling and web interactivity, setting it apart from simpler graphic design tools.

## How it works
The application consists of a Python script that runs a pipeline to generate card assets. It uses layers for text, line art, subject, and background, which are combined to create a parallax effect. The generated assets include a Blender file (`card.blend`), a JSON configuration file, and a local web page for interaction. Users interact with Codex to specify card details, which the system processes to produce the final output. Uncertainty exists regarding the specific performance and limitations of the generated assets, as well as the extent of customization available in the Blender project.

## Get started in 5 minutes
1. Clone the repository: `git clone https://github.com/EverettFish/holo-card-studio`
2. Place the directory in Codex's skills directory: `~/.codex/skills/holo-card-studio/`
3. Ensure you have Python 3, Pillow, Node.js, and npm installed.
4. Run the pipeline with: `python scripts/run_pipeline.py --project <project-dir> --mode holographic`.
5. Use Codex to generate a card by providing a description or reference image.

## Watch out for
The repository is relatively new (created in September 2026), which may indicate that it is still in development or lacks extensive documentation. Users should be cautious about potential bugs or incomplete features. Additionally, the README does not specify the licensing terms, which could affect usage rights for generated content.
