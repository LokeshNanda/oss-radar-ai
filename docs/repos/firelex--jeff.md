---
title: firelex/jeff
source: https://github.com/firelex/jeff
stars: 1380
category: AI & Agents
---

# firelex/jeff

- **URL**: https://github.com/firelex/jeff
- **Stars**: 1380
- **Language**: Python
- **Category**: AI & Agents
- **Topics**: None

## What it does
Jeff is a decision-making model that operates in milliseconds, designed to provide calibrated probabilities for various options in any domain. It utilizes a base model (0.8B parameters) and allows for the integration of swappable LoRA adapters to enhance its decision-making capabilities.

## Why it's interesting
Jeff stands out by combining a lightweight model with the ability to make quick decisions, significantly outperforming larger models like Qwen3.8-27B in terms of speed and accuracy for specific tasks. Its architecture allows for the use of specialized adapters, which can be trained for particular decision-making tasks, making it versatile across different applications.

## How it works
Jeff functions as a classifier that takes a description of a situation and a list of options, returning probabilities for each option based on a single forward pass. It employs a base model with additional LoRA adapters that can be swapped in and out depending on the task. The README provides detailed performance metrics comparing Jeff with larger models, showing improved accuracy and speed. However, it does not specify the exact architecture or training methods used for the base model or adapters, leaving some uncertainty in those areas.

## Get started in 5 minutes
To quickly set up Jeff, clone the repository and run the following commands:
```bash
git clone https://github.com/firelex/jeff && cd jeff
uv sync --no-default-groups --extra lora
uv run --no-default-groups hf download mstrasser/Jeff-Qwen3.5-0.8B --revision v1.2 --local-dir Jeff-Qwen3.5-0.8B-v1.2
for name in guard tools ground; do
  uv run --no-default-groups hf download mstrasser/Jeff-Qwen3.5-0.8B-$name --local-dir adapters/$name
done
JEFF_CHECKPOINT=Jeff-Qwen3.5-0.8B-v1.2 JEFF_ADAPTERS=adapters PORT=8765 \
  uv run --no-default-groups --extra lora jeff-serve
```

## Watch out for
The repository is relatively new, created in September 2026, and while it has garnered a significant number of stars (1380), it may still be in a community preview phase. Users should be cautious of potential bugs or incomplete features, especially since the README mentions a stable long-term-support version (v1.3) is forthcoming. Additionally, licensing details are not explicitly mentioned in the README, which may be a concern for some users.
