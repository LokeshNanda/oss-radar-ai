---
title: TheoLeeCJ/SemIf
source: https://github.com/TheoLeeCJ/SemIf
stars: 2783
category: AI & Agents
---

# TheoLeeCJ/SemIf

- **URL**: https://github.com/TheoLeeCJ/SemIf
- **Stars**: 2783
- **Language**: Python
- **Category**: AI & Agents
- **Topics**: None

## What it does
SemIf is a project that implements semantic decision-making using open models, specifically designed to run on consumer-grade GPUs like the RTX 3090. It allows for direct scoring of typed options based on runtime-defined criteria, bypassing the need for traditional text generation.

## Why it's interesting
Unlike closed services like Jev from TypeSafe, SemIf is an independent project that provides a similar interface pattern using open models. It emphasizes speed and efficiency by directly reading option probabilities without generating extraneous text, making it a potentially faster alternative for decision-making tasks.

## How it works
SemIf processes unstructured state and runtime criteria through a 4B model to produce typed option probabilities in a single forward pass. The architecture allows for shared-state awareness, meaning it can reuse the same state across multiple decisions, which enhances performance. The README does not specify the exact model training details or the full range of supported models beyond those mentioned (Qwen3.5-4B, MiniCPM5 2B, etc.), leaving some uncertainty about the complete capabilities.

## Get started in 5 minutes
To quickly try SemIf, set up a Python virtual environment and install the necessary dependencies:
```bash
python -m venv .venv
. .venv/bin/activate
pip install -e '.[test]'
```
Then, run the example command:
```bash
CUDA_VISIBLE_DEVICES=0 semif-score --mode direct --model Qwen/Qwen3.5-4B --input examples/decisions.jsonl --output results.jsonl
```

## Watch out for
The project is relatively new (created in September 2026) and may not have extensive community support or documentation. Additionally, while it claims to be independent, it references other proprietary systems, which may raise concerns about compatibility or performance expectations. The licensing is under MIT, but users should verify the licensing of any third-party models used.
