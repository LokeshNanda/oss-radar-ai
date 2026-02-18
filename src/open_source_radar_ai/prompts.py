"""Prompt templates for LLM summarization."""

from __future__ import annotations

from .models import Repository


SYSTEM_PROMPT = """You are a senior software architect.
Write analytical, specific, no-hype technical insights.
Use concise language and avoid marketing tone."""


def build_repository_prompt(repo: Repository) -> str:
    """Build a structured prompt for a repository analysis."""
    topics = ", ".join(repo.topics) if repo.topics else "None"
    description = repo.description or "No description provided."
    language = repo.language or "Unknown"

    return f"""Analyze this GitHub repository and produce a structured markdown report.

Repository metadata:
- Name: {repo.full_name}
- URL: {repo.html_url}
- Description: {description}
- Primary language: {language}
- Topics: {topics}
- Stars: {repo.stargazers_count}
- Created at: {repo.created_at.date().isoformat()}
- Updated at: {repo.updated_at.date().isoformat()}

Output requirements (markdown, use these headings exactly):
## Executive Summary
(exactly 3 lines)

## Problem it solves

## Target audience

## Why it is trending

## Architecture insights

## Enterprise relevance

## Suggested experiments

Constraints:
- Be honest about uncertainty; do not invent facts not implied by the metadata.
- Prefer concrete, testable statements over vague claims.
"""


__all__ = ["SYSTEM_PROMPT", "build_repository_prompt"]

