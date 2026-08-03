---
title: sqliteai/waste
source: https://github.com/sqliteai/waste
stars: 1165
category: AI & Agents
---

# sqliteai/waste

- **URL**: https://github.com/sqliteai/waste
- **Stars**: 1165
- **Language**: C
- **Category**: AI & Agents
- **Topics**: None

## What it does
WASTE is an embeddable inference engine for running the Kimi K3 model, which has 2.78 trillion parameters, on consumer hardware by streaming model weights directly from NVMe storage. It allows for inference without requiring extensive RAM by caching only a portion of the model in memory.

## Why it's interesting
WASTE is designed to run large models like Kimi K3 locally, making it accessible for users with standard consumer hardware, unlike many alternatives that require cloud resources or extensive hardware setups. Its unique approach of streaming weights from disk rather than loading them entirely into RAM sets it apart from typical inference engines.

## How it works
WASTE operates by keeping the shared part of the model in RAM while streaming selected experts from disk as needed. It uses a lookahead router to predict which experts will be required, optimizing read times and minimizing latency. The README details that the model uses 3-bit residual vector quantization for experts and maintains a bounded expert cache to improve efficiency. However, the README does not specify the exact algorithms or techniques used for the lookahead routing, leaving some uncertainty in the implementation details.

## Get started in 5 minutes
1. Clone the repository: `git clone https://github.com/sqliteai/waste`
2. Navigate into the directory: `cd waste`
3. Build the engine: `make`
4. Run the model-free test suite: `make check`
5. Follow the instructions in the README to download and convert the Kimi K3 model weights.

## Watch out for
The project is still evolving, and the format and API are not yet frozen, which may lead to instability. Users should be aware that the performance measurements are experimental and tied to specific hardware configurations. Additionally, while the project is open-source under the Apache 2.0 license, there may be significant storage requirements (about 1 TB for the model) and a recommended minimum of 64 GB of RAM for optimal performance.
