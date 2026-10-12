---
title: mhtsec/ARTEX
source: https://github.com/mhtsec/ARTEX
stars: 3490
category: Security
---

# mhtsec/ARTEX

- **URL**: https://github.com/mhtsec/ARTEX
- **Stars**: 3490
- **Language**: Go
- **Category**: Security
- **Topics**: None

## What it does
ARTEX is an AI-driven penetration testing system designed for automated security assessments. It integrates a Go backend with a Next.js frontend, allowing users to manage tasks, assets, and findings through a web interface.

## Why it's interesting
ARTEX stands out due to its dual-graph architecture, which separates asset management from exploration processes, enabling a more organized approach to penetration testing. Additionally, it supports LLM (Large Language Model) integration for enhanced decision-making during assessments, which is not commonly found in traditional tools.

## How it works
The system operates on a dual-graph model: an Asset Graph for managing assets and an Exploration Graph for tracking the testing process. The backend is built in Go and uses PostgreSQL for data storage. The architecture includes components for task management, agent execution, and real-time data processing, with agents capable of sharing insights across tasks. The README does not specify how the AI models are trained or the exact algorithms used for decision-making, leaving some uncertainty in this area.

## Get started in 5 minutes
To quickly set up ARTEX, clone the repository and run the installation script:
```bash
git clone https://github.com/mhtsec/ARTEX.git
cd ARTEX
./install.sh
```
This script will guide you through setting up the necessary Docker containers and configurations.

## Watch out for
The project is licensed under the GNU Affero General Public License v3.0, which requires any derivative works to also be open-sourced. Users must adhere to strict usage guidelines, prohibiting any real-world testing on live systems. Additionally, the original Docker image source is no longer available, which may affect deployment if the self-maintained image fails.
