---
title: Arekejoker/qwen21-nsfw-pose-skill
source: https://github.com/Arekejoker/qwen21-nsfw-pose-skill
stars: 3264
category: AI & Agents
---

# Arekejoker/qwen21-nsfw-pose-skill

- **URL**: https://github.com/Arekejoker/qwen21-nsfw-pose-skill
- **Stars**: 3264
- **Language**: Python
- **Category**: AI & Agents
- **Topics**: agent-skill, comfyui, image-generation, openclaw, pose-control, qwen-image

## What it does
This repository provides a skill for generating NSFW images using the Qwen-Image 2.1 model, incorporating a library of 136 3D poses and a LoRA (Low-Rank Adaptation) model for enhanced image quality. It supports various modes for generating images based on text prompts, existing character images, or specific poses.

## Why it's interesting
The repository stands out due to its combination of NSFW content generation with precise pose control, allowing users to create highly customized images. The integration of a 3D pose library and the ability to replicate specific author examples adds a unique dimension to its functionality, which is not commonly found in similar projects.

## How it works
The skill is built on the ComfyUI framework and utilizes the Qwen-Image 2.1 model. It includes scripts for self-checking dependencies, generating images, and managing poses. Users can choose from four different operational modes to generate images based on their needs. The README details the installation process, hardware requirements, and specific commands for each mode. However, it does not clarify how the LoRA model is trained or its specific impact on image quality beyond general usage.

## Get started in 5 minutes
1. Install the dependencies as outlined in [install/setup.md](https://github.com/Arekejoker/qwen21-nsfw-pose-skill/install/setup.md).
2. Run the self-check script to ensure everything is set up correctly:
   ```bash
   python3 scripts/doctor.py
   ```
3. Generate an image using the author's example command:
   ```bash
   python3 scripts/qwen_pose_test.py --mode t2i --name author_case_shower --prompt "$(cat prompts/taws_v13_shower.txt)" --seed 80964 --steps 50 --cfg 2.5 --sampler er_sde --scheduler beta --width 1152 --height 1728 --lora "qwen2_1-femaledVaginus-nsfw-v1_3-fine_L22-31.safetensors" --lora-strength 1.0 --out outputs/author_case/shower.png
   ```

## Watch out for
The repository is relatively new, created in October 2026, and may still be evolving. Users should be cautious of the NSFW content and ensure compliance with relevant guidelines. The README mentions hardware requirements, recommending at least 12GB of NVIDIA GPU memory, which may limit accessibility for some users. Licensing is under Apache License 2.0, but third-party assets are not covered, which could pose legal considerations for redistribution.
