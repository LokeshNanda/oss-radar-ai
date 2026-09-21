---
title: jarrodwatts/jev-trader
source: https://github.com/jarrodwatts/jev-trader
stars: 1685
category: AI & Agents
---

# jarrodwatts/jev-trader

- **URL**: https://github.com/jarrodwatts/jev-trader
- **Stars**: 1685
- **Language**: TypeScript
- **Category**: AI & Agents
- **Topics**: None

## What it does
The `jev-trader` repository implements an AI-driven trading bot that makes buy or sell decisions on the Kuru MON-USDC order book approximately every 300 milliseconds. It places limit orders based on the AI model's predictions, aiming to earn the spread instead of paying it.

## Why it's interesting
This project stands out due to its integration of a TypeSafe AI model that operates in real-time, making decisions within the constraints of blockchain transaction blocks. The bot's architecture allows for dry runs without real financial risk, enabling developers to test and refine their strategies without capital exposure.

## How it works
The bot operates by reading the order book and making decisions based on a model that predicts market movements. It uses two RPC calls per decision cycle: one for reading the order book and another for sending the transaction. The bot's architecture includes components for handling blockchain interactions, model inference, and event streaming. The README does not specify the exact nature of the AI model's training or performance metrics, leaving some uncertainty about its effectiveness compared to other trading strategies.

## Get started in 5 minutes
1. Copy the example environment file: `cp .env.example .env`
2. Install dependencies using Bun: `bun install`
3. Start the application: `bun run start`
4. Optionally, set `MODEL=jev` and `TYPESAFE_AI_API_KEY` for real model usage.

## Watch out for
The repository is relatively new, created in September 2026, which may imply limited community support and potential bugs. Additionally, the README does not mention licensing, which is crucial for understanding usage rights. Security concerns may arise from handling private keys and interacting with live trading environments.
