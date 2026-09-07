---
title: anthropics/commerce-agents
source: https://github.com/anthropics/commerce-agents
stars: 2320
category: AI & Agents
---

# anthropics/commerce-agents

- **URL**: https://github.com/anthropics/commerce-agents
- **Stars**: 2320
- **Language**: Python
- **Category**: AI & Agents
- **Topics**: None

## What it does
This repository provides a reference implementation for building shopping and merchant agents using Claude. It includes two types of agents: a shopping agent for customer interactions and a merchant agent for back-office operations, with examples across various sectors like retail and telecom.

## Why it's interesting
Unlike typical e-commerce solutions, this repository leverages Claude's capabilities to create intelligent agents that can handle complex interactions, such as cart management and inventory alerts, while ensuring compliance and approval processes are in place. The focus on fictional scenarios allows developers to experiment without real-world implications.

## How it works
The architecture is based on Python and Node.js, utilizing the Messages API and Claude Agent SDK. The agents are structured into distinct directories for shared components, shopping, and merchant functionalities. Each agent has defined skills and flows, with backend integrations that allow for customization based on the user's existing systems. The README outlines various ways to run the agents, including through a Messages API, an Agent SDK, or as Managed Agents, though specifics on deployment configurations for different platforms are not detailed.

## Get started in 5 minutes
1. Clone the repository: `git clone https://github.com/anthropics/commerce-agents.git`
2. Navigate into the directory: `cd commerce-agents`
3. Set up a Python virtual environment: `python3 -m venv .venv && source .venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Copy the example environment file and add your API key: `cp .env.example .env`
6. Run a demo vertical: `python scripts/run_demo.py retail`

## Watch out for
The repository is a reference implementation and is not actively maintained or open to contributions, which may limit its long-term viability. Additionally, while it provides a framework for building agents, developers will need to implement their own backend integrations and ensure compliance with business rules, as the examples do not include authentication or real transaction capabilities.
