---
title: HybridRobotics/supermimic
source: https://github.com/HybridRobotics/supermimic
stars: 1644
category: AI & Agents
---

# HybridRobotics/supermimic

- **URL**: https://github.com/HybridRobotics/supermimic
- **Stars**: 1644
- **Language**: Python
- **Category**: AI & Agents
- **Topics**: None

## What it does
SuperMimic is a system designed for humanoid whole-body motion tracking using a differentiable world model. It allows users to train a motion tracker and policy for various tasks related to humanoid motion.

## Why it's interesting
SuperMimic differentiates itself by integrating a differentiable world model, which may enhance the training and adaptability of humanoid motion tracking compared to traditional methods. The project also builds on existing frameworks like mjlab, which suggests a focus on leveraging established research in robotics.

## How it works
The system requires the installation of the uv tool and cloning of both the SuperMimic and mjlab repositories. Users can train the model using specific task IDs and can playback trained models. The README does not provide detailed information on the underlying architecture or algorithms used in the differentiable world model, leaving some uncertainty about its implementation specifics.

## Get started in 5 minutes
1. Install uv using the provided command.
2. Clone the repositories as siblings:
   ```bash
   mkdir supermimic_ws && cd supermimic_ws
   git clone git@github.com:HybridRobotics/supermimic.git
   git clone git@github.com:HybridRobotics/mjlab_research.git
   cd supermimic
   ```
3. Train a model with:
   ```bash
   CUDA_VISIBLE_DEVICES=<GPU_ID> uv run src/supermimic/scripts/train.py <TASK_ID> --runner.run_name <description>
   ```

## Watch out for
The repository is relatively new, created in November 2026, which may imply limited community support or maturity. Users should also be aware of potential gaps in documentation, particularly regarding the architecture of the differentiable world model. The project is licensed under the Apache License 2.0, which is permissive but requires attribution.
