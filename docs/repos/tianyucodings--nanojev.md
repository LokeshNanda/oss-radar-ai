---
title: TianyuCodings/NanoJev
source: https://github.com/TianyuCodings/NanoJev
stars: 1682
category: AI & Agents
---

# TianyuCodings/NanoJev

- **URL**: https://github.com/TianyuCodings/NanoJev
- **Stars**: 1682
- **Language**: Python
- **Category**: AI & Agents
- **Topics**: None

## What it does
NanoJev is a parallel decision model that processes states and questions to output complete probability distributions without the need for output-token decoding. It is designed to handle multiple tasks, specifically in gaming environments like ViZDoom, Maze, and Snake.

## Why it's interesting
NanoJev distinguishes itself by achieving high performance in decision-making tasks with a single model checkpoint across multiple games, demonstrating significant improvements over its predecessor, Jev, in terms of efficiency and success rates in various scenarios.

## How it works
The architecture utilizes a small backbone model (Qwen3-0.6B) that processes independent states and questions in parallel, returning distributions over candidate actions. It employs a shared scoring head for dynamic candidate selection and uses a softmax function for decision-making. The README does not provide detailed insights into the underlying algorithms or training methodologies beyond the mention of cross-entropy loss and specific learning rates.

## Get started in 5 minutes
1. Clone the repository: `git clone https://github.com/TianyuCodings/NanoJev.git`
2. Navigate into the directory: `cd NanoJev`
3. Install dependencies: `python -m pip install -r requirements-toy.txt huggingface_hub`
4. Download the model and dataset using the provided Python code snippets.
5. Start the inference service with the command provided in the README.

## Watch out for
The repository is relatively new (created in September 2026) and may lack extensive documentation or community support. Users should be cautious of potential bugs or incomplete features as the project matures. Additionally, there are no explicit licensing details mentioned in the README, which could be a concern for commercial use.
