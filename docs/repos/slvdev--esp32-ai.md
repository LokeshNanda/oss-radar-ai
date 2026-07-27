---
title: slvDev/esp32-ai
source: https://github.com/slvDev/esp32-ai
stars: 1436
category: AI & Agents
---

# slvDev/esp32-ai

- **URL**: https://github.com/slvDev/esp32-ai
- **Stars**: 1436
- **Language**: Python
- **Category**: AI & Agents
- **Topics**: None

## What it does
This repository implements a 28.9 million parameter language model that generates text on an ESP32-S3 microcontroller. It operates entirely on the device without server connectivity, producing output at approximately 9 tokens per second.

## Why it's interesting
This project is notable for successfully fitting a large language model onto a microcontroller with limited resources, using a novel approach called Per-Layer Embeddings to store most of the model in flash memory rather than RAM. This allows it to operate with a significantly larger model size compared to previous attempts on similar hardware.

## How it works
The architecture leverages the ESP32-S3's 512KB SRAM for the model's core processing while storing the majority of the parameters (25 million) in flash memory. It retrieves only the necessary rows from the embedding table as needed, which minimizes memory usage. The model was trained on the TinyStories dataset, focusing on generating coherent short stories, but it does not support complex tasks like answering questions or writing code. Uncertainty exists regarding the completeness of the implementation details, as the README does not provide exhaustive information on the training process or specific limitations of the model.

## Get started in 5 minutes
To run the model, follow the instructions in the `firmware/esp32_llm/README.md` for firmware installation, wiring, and flashing steps. The source code for training and experiments can be found in the `src/` and `experiments/` directories.

## Watch out for
The repository is relatively new, created in July 2026, and may contain bugs or incomplete features, as indicated by the author's note about a bug in parameter accounting. Additionally, the README does not specify a license, which could pose legal concerns for use in projects.
