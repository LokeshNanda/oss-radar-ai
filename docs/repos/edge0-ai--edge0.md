---
title: Edge0-AI/Edge0
source: https://github.com/Edge0-AI/Edge0
stars: 1652
category: AI & Agents
---

# Edge0-AI/Edge0

- **URL**: https://github.com/Edge0-AI/Edge0
- **Stars**: 1652
- **Language**: Python
- **Category**: AI & Agents
- **Topics**: None

## What it does
`edge0` is an open-source streaming mixture of experts (MoE) inference framework designed for efficient model serving. It supports two model tiers (`edge0-35b` and `edge0-8b`), which include pre-trained checkpoints and trained adapters for optimized performance.

## Why it's interesting
This framework offers a unique combination of SSD expert offload, Recover-LoRA, and prerouter routing prediction, which enhances inference speed and reduces memory usage compared to traditional models. Its backend isolation allows for future extensibility to other platforms beyond Apple Silicon, which is currently the only supported hardware.

## How it works
The architecture is built around a core logic that is independent of the backend, allowing for easy integration of new backends (e.g., CUDA). The framework uses a trained prerouter to predict expert routing, which improves throughput by overlapping expert loading with the forward pass. The model and its adapters are organized in a single directory, simplifying the loading process. However, the README does not specify how the framework handles different types of input data or the specifics of the training process for the models.

## Get started in 5 minutes
1. Install Python 3.10+ and create a virtual environment:
   ```bash
   python3.12 -m venv .venv && .venv/bin/pip install -e '.[dev,fetch]'
   ```
2. Download a model using the provided scripts:
   ```bash
   .venv/bin/python scripts/fetch_models.py --tier edge0-35b --target-dir models
   ```
3. Set the environment variable for the model:
   ```bash
   export EDGE0_35B_MODEL=$PWD/models/edge0-35b
   ```
4. Run a quick demo:
   ```bash
   edge0 demo edge0-35b
   ```

## Watch out for
The framework currently only supports macOS with Apple Silicon for its MLX backend, with a CUDA backend planned for the future. The README does not provide extensive documentation on potential limitations or known issues, and users should be aware of the memory requirements (~2.9 GB for `edge0-35b`). Additionally, the lack of topics and description in the repository may indicate that it is still in a relatively early stage of development.
