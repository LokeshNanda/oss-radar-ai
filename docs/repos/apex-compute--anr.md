---
title: apex-compute/ANR
source: https://github.com/apex-compute/ANR
stars: 2383
category: AI & Agents
---

# apex-compute/ANR

- **URL**: https://github.com/apex-compute/ANR
- **Stars**: 2383
- **Language**: C++
- **Category**: AI & Agents
- **Topics**: None

## What it does
Apex Neural Rendering (ANR) provides tools for frame generation, super resolution, and ray reconstruction for video games using neural rendering techniques. It includes a recording tool (`nr-record`) that captures frame generation inputs for comparison against other technologies like NVIDIA DLSS and FSR.

## Why it's interesting
ANR aims to enhance gaming visuals through advanced neural rendering methods, specifically targeting performance improvements in frame generation and upscaling. Its ability to record and compare outputs from different rendering technologies allows developers and users to evaluate performance and quality in a structured manner.

## How it works
The repository includes several components: ANR FG for frame generation, ANR SR for super resolution, and ANR RR for ray reconstruction, although the latter two are still in beta. The `nr-record` tool captures inputs from games using D3D12 or Vulkan APIs, allowing users to replay and compare outputs from different frame generation methods. Installation involves downloading packages from the Releases section and running specific installation scripts for Windows or Linux. The build process utilizes Bazel, with specific commands provided for different components.

## Get started in 5 minutes
1. Download the `anr-fg-full` or `anr-fg-addon` package from the [Releases](https://github.com/apex-compute/ANR/releases) section.
2. Close your game and run the installer with the folder of the game's `.exe`:
   - For Windows: `install.cmd`
   - For Linux: `sh install.sh "<folder>"`
3. Set the game's launch options as instructed and enable frame generation in the game settings.

## Watch out for
The project is in beta for several features, and the source code for some components is still marked as "coming soon." There are specific GPU requirements, primarily NVIDIA and AMD cards, and it relies on external tools like OptiScaler and ffmpeg. Licensing for OptiScaler is GPL-3.0, which may affect how ANR can be used in proprietary projects.
