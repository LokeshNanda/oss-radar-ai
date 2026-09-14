---
title: crwdla/tokentab
source: https://github.com/crwdla/tokentab
stars: 973
category: Developer Tools
---

# crwdla/tokentab

- **URL**: https://github.com/crwdla/tokentab
- **Stars**: 973
- **Language**: Python
- **Category**: Developer Tools
- **Topics**: ai, ai-token-monitor, claude-code, token-optimization, token-usage

## What it does
`tokentab` is a command-line interface (CLI) tool that reads session logs from Claude Code, Codex, and Gemini CLI to calculate token usage and associated costs, organized by model, project, and day. It operates entirely locally, requiring no external accounts or API keys.

## Why it's interesting
Unlike many token monitoring tools that rely on external APIs or cloud services, `tokentab` processes data locally, ensuring privacy and control over usage metrics. It also provides a straightforward way to visualize token usage and costs through a web dashboard without needing additional frameworks.

## How it works
The tool reads log files from specific directories for each supported tool and calculates token usage based on the logs. It uses a hand-maintained pricing table for cost calculations, ensuring that it does not require network access for pricing. The architecture allows for easy extension by adding new providers through a defined interface. However, the README mentions that the integration for the Cursor tool is not fully implemented, which introduces some uncertainty about its current capabilities.

## Get started in 5 minutes
1. Clone the repository: `git clone https://github.com/crwdla/tokentab`
2. Navigate to the directory: `cd tokentab`
3. Install the package: `pip install .`
4. Run the CLI: `python cli.py`

## Watch out for
The project is relatively new, created in September 2026, which may imply limited community support or maturity. Additionally, the pricing data is manually maintained, so users should be aware of potential inaccuracies if the pricing table is not updated. The tool is licensed under MIT, allowing for broad usage but users should ensure compliance with any dependencies.
