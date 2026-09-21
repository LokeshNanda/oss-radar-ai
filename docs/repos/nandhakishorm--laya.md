---
title: NandhaKishorM/laya
source: https://github.com/NandhaKishorM/laya
stars: 6911
category: AI & Agents
---

# NandhaKishorM/laya

- **URL**: https://github.com/NandhaKishorM/laya
- **Stars**: 6911
- **Language**: Python
- **Category**: AI & Agents
- **Topics**: None

## What it does
Laya is a multilingual, non-autoregressive decision engine that evaluates typed questions over various states (like text or JSON documents) in a single forward pass, achieving response times around 33 ms. It utilizes reinforcement learning against strictly proper scoring rules and includes a router that selects the optimal model checkpoint based on the input language and script.

## Why it's interesting
Laya differentiates itself by offering a routing mechanism that automatically detects the language and script of the input, allowing it to leverage different model checkpoints for improved accuracy and speed. This is particularly useful for applications requiring multilingual support without the overhead of text generation or parsing.

## How it works
Laya consists of three checkpoints: `laya` for English, `laya-multilingual` for over 100 languages, and `laya-typed-decisions` for specific workflows. The router intelligently selects the appropriate model based on the input's characteristics, which is measured in milliseconds before any forward pass. The README does not provide detailed architectural diagrams or code structure, leaving some uncertainty about the internal workings beyond the routing mechanism and model loading.

## Get started in 5 minutes
To get started, install the package using `pip install laya`. Then, import Laya and create a `Router` instance to preload the models for optimal performance. An example code snippet is provided in the README for routing a state and defining typed questions.

## Watch out for
The repository lacks a detailed description and specific topics, which may hinder discoverability. Additionally, the README mentions performance benchmarks but does not clarify the maturity of the project or its community support. The license is Apache 2.0, which is permissive, but users should verify compliance with any dependencies.
