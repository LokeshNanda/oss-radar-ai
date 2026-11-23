---
title: sybil-solutions/inference-optimisation-skill
source: https://github.com/sybil-solutions/inference-optimisation-skill
stars: 2080
category: AI & Agents
---

# sybil-solutions/inference-optimisation-skill

- **URL**: https://github.com/sybil-solutions/inference-optimisation-skill
- **Stars**: 2080
- **Language**: Python
- **Category**: AI & Agents
- **Topics**: agent-skill, benchmarking, claude-code, inference, llm, speculative-decoding

## What it does
This repository provides an agent skill for optimizing the speed of local large language model (LLM) servers across various hardware configurations and quantization methods. It focuses on improving metrics such as decoding speed, speculative decoding, prefill performance, KV cache size, and startup time.

## Why it's interesting
Unlike typical optimization tools that may simply provide flags or settings, this skill employs a systematic approach to measure and log performance improvements through a rigorous hill-climbing methodology. It emphasizes theoretical ceilings and controlled experiments to ensure that optimizations are meaningful and reproducible.

## How it works
The skill operates by first calculating theoretical performance ceilings based on hardware specifications. It then systematically modifies one variable at a time, measuring the impact against interleaved control runs. The results are logged, and only configurations that meet strict acceptance criteria are published. The skill includes scripts for benchmarking and ceiling calculations, and it can be integrated with various agents that support `SKILL.md`-style skills. The README does not specify any limitations on the types of models it can optimize beyond those mentioned.

## Get started in 5 minutes
1. Clone the repository: `git clone https://github.com/sybil-solutions/inference-optimisation-skill`
2. Create the skills directory: `mkdir -p ~/.claude/skills`
3. Copy the skill: `cp -r inference-optimisation-skill/skills/inference-optimisation ~/.claude/skills/`
4. Run a benchmark using the provided scripts: `python3 skills/inference-optimisation/scripts/bench.py run configs/base.json --long 131072`

## Watch out for
The repository is relatively new, created in November 2026, which may imply that it is still evolving and could have undiscovered issues. The README does not mention any specific security concerns or licensing issues beyond the MIT license. Users should be cautious about the experimental nature of the optimizations and the need for thorough testing in their specific environments.
