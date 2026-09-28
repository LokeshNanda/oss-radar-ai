---
title: Contrastive-LM/CLM
source: https://github.com/Contrastive-LM/CLM
stars: 2110
category: AI & Agents
---

# Contrastive-LM/CLM

- **URL**: https://github.com/Contrastive-LM/CLM
- **Stars**: 2110
- **Language**: Python
- **Category**: AI & Agents
- **Topics**: None

## What it does
Contrastive-LM (CLM) is a Python library that implements Contrastive Language Models, specifically the CLM-8B model. It is designed for fast and generalizable decision-making by connecting states and actions through a contrastive learning objective.

## Why it's interesting
CLM claims to achieve state-of-the-art performance on agentic coding benchmarks while operating with significantly lower latency compared to alternatives like Jev. It utilizes a unique architecture that disaggregates state and action embeddings, allowing for efficient training and serving.

## How it works
CLM employs a two-stage training process: it first pre-trains on a large dataset of question-answer pairs, then mid-trains on synthetic hard negatives, and finally post-trains on agentic trajectories. The architecture consists of a frozen LLM backbone with a trainable projection head. The model uses a bidirectional InfoNCE loss for training, optimizing the alignment of state and action embeddings. However, the README does not provide detailed information on the specific implementation of the model or its performance metrics beyond what is stated.

## Get started in 5 minutes
1. Install the package using `pip install contrastive-lm`.
2. Serve the model by running `clm-serve` after setting up the encoder with `vllm serve Qwen/Qwen3-8B`.
3. Use the provided Python client to interact with the model and ask typed questions about states.

## Watch out for
The repository is relatively new (created in September 2026) and lacks extensive documentation and community support, which may affect its maturity. Additionally, there are no clear indications of security practices or potential vulnerabilities in the README. The code is licensed under the Apache 2.0 License, which is permissive but does not guarantee support or updates.
