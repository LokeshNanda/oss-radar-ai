# Open Source Radar AI

AI-powered GitHub Open Source Radar that automatically discovers trending repositories and generates architect-level technical insights using LLMs. Built with Python, MkDocs, and GitHub Actions.

---

## 🎯 Goal

Build a fully automated system that:

- Fetches trending repositories from GitHub
- Generates structured architect-level analysis using LLMs
- Publishes Markdown summaries
- Deploys automatically via GitHub Actions
- Hosts as a static site using MkDocs + GitHub Pages

---

## 🏗 Architecture Overview

GitHub API → Python Pipeline → LLM Summarization → Markdown Generation → MkDocs Build → GitHub Pages Deployment

---

## 🧠 Design Principles

- Modular architecture
- Idempotent runs
- No hardcoded secrets
- Deterministic file generation
- Extensible to multiple LLM providers
- Production-ready automation

---

## 🚀 Local Development

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
