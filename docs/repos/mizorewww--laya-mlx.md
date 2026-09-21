---
title: mizorewww/laya-mlx
source: https://github.com/mizorewww/laya-mlx
stars: 2418
category: AI & Agents
---

# mizorewww/laya-mlx

- **URL**: https://github.com/mizorewww/laya-mlx
- **Stars**: 2418
- **Language**: Python
- **Category**: AI & Agents
- **Topics**: apple-silicon, decision-model, inference, laya, local-ai, machine-learning, mlx, modernbert, system-one, typed-decisions

## What it does
Laya-MLX is a native MLX runtime designed for executing typed decision models on Apple Silicon, achieving median response times of 7–14 ms for short decisions. It operates entirely locally without relying on PyTorch, Transformers, or cloud APIs.

## Why it's interesting
This repository focuses on typed decision-making, providing a unique approach to inference that avoids token-by-token decoding, which is common in many AI models. The performance metrics are specifically optimized for Apple Silicon, making it a tailored solution for developers working in that ecosystem.

## How it works
Laya-MLX utilizes a bidirectional encoder to process state and typed questions, producing probabilities for various decision types (choice, score, and noul). It supports multiple checkpoints, including a multilingual model, and employs Hugging Face's Rust tokenizer for efficient tokenization. The architecture is built around the MLX framework, and it is noted that the implementation is an independent port, not an official release from Convai Innovations.

## Get started in 5 minutes
1. Install the package: `pip install laya-mlx`
2. Load a model and make a prediction:
   ```python
   import laya_mlx as laya
   agent = laya.load("aac6fef/laya-mlx")
   result = agent.predict("I was billed twice. Please refund the duplicate.", {
       "department": {
           "type": "choice",
           "instructions": "Who should handle this?",
           "criteria": ["billing", "technical", "sales"],
       }
   })
   print(result["answers"]["department"])
   ```
3. For a terminal demo, run: `pip install 'laya-mlx[demo]'` followed by `laya-snake`.

## Watch out for
The repository is relatively new (created in September 2026), which may imply limited community support or maturity. It is specifically designed for macOS 14+ and Python 3.11+, which may restrict its usability on other platforms. The licensing is under Apache-2.0, and users should verify compliance with any dependencies or adaptations from upstream repositories.
