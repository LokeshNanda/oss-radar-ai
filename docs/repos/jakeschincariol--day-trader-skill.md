---
title: Jakeschincariol/day-trader-skill
source: https://github.com/Jakeschincariol/day-trader-skill
stars: 1849
category: Developer Tools
---

# Jakeschincariol/day-trader-skill

- **URL**: https://github.com/Jakeschincariol/day-trader-skill
- **Stars**: 1849
- **Language**: Python
- **Category**: Developer Tools
- **Topics**: backtesting, claude, claude-skills, day-trading, stock-market

## What it does
This repository provides 11 Python-based skills for day trading, enabling users to scan charts, track news, time entries and exits, and simulate outcomes before executing trades. It utilizes public data sources like Yahoo Finance and SEC filings to inform trading decisions.

## Why it's interesting
Unlike many trading tools that require API keys or subscriptions, this package is free and open-source, operating entirely on public data. It emphasizes user control by requiring explicit approval for trades, which is a significant safety feature in automated trading environments.

## How it works
The skills are organized into a workflow where each command feeds into the next, from scanning charts to managing risk and executing trades. Users can run Python scripts for each skill, which interact with public data endpoints. The architecture relies on standard library Python, and the skills are designed to be modular, allowing users to customize their trading strategies. However, the README does not clarify how the skills handle real-time data or the specifics of their performance metrics beyond simulations.

## Get started in 5 minutes
To get started, clone the repository and copy the desired skill folders into your Claude skills directory:
```bash
git clone https://github.com/Jakeschincariol/day-trader-skill.git
cp -r day-trader-skill/trader-* ~/.claude/skills/
```
Ensure you have Python 3.8 or newer, and configure your `trader/config.json` with your name and email for SEC tools.

## Watch out for
The repository is relatively new (created in October 2026), so it may lack extensive community support or documentation. Users should be cautious about relying on the Time Machine simulations, as they are based on historical data and do not predict future performance. Additionally, the software does not provide financial advice, and users are warned about the risks of day trading. The license is MIT, allowing for modification and redistribution.
