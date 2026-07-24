"""Prompt templates for LLM summarization."""

from __future__ import annotations

from .models import CATEGORIES, Repository


SYSTEM_PROMPT = """You write sharp, honest breakdowns of GitHub repositories for busy developers.
Be concrete and specific. No marketing tone, no hype, no filler.
When the README does not support a claim, say what is uncertain instead of guessing."""


def build_repository_prompt(repo: Repository, readme_excerpt: str | None = None) -> str:
    """Build a structured prompt for a repository analysis."""
    topics = ", ".join(repo.topics) if repo.topics else "None"
    description = repo.description or "No description provided."
    language = repo.language or "Unknown"
    categories = ", ".join(f'"{c}"' for c in CATEGORIES)

    readme_block = ""
    if readme_excerpt:
        readme_block = f"""
README (may be truncated):
<readme>
{readme_excerpt}
</readme>
"""

    return f"""Analyze this GitHub repository for a developer audience.

Repository metadata:
- Name: {repo.full_name}
- URL: {repo.html_url}
- Description: {description}
- Primary language: {language}
- Topics: {topics}
- Stars: {repo.stargazers_count}
- Created at: {repo.created_at.date().isoformat()}
{readme_block}
Respond with a single JSON object with exactly these keys:
- "category": one of [{categories}]
- "analysis_markdown": a markdown string using these headings exactly:

## What it does
(2-3 sentences, concrete)

## Why it's interesting
(what makes it different from the obvious alternatives)

## How it works
(architecture/approach, grounded in the README; note uncertainty where it exists)

## Get started in 5 minutes
(the shortest realistic path to trying it, from the README)

## Watch out for
(maturity, gaps, caveats, licensing or security concerns)

Constraints:
- Ground every claim in the metadata or README; never invent features.
- Prefer specific, testable statements over vague ones.
"""


__all__ = ["SYSTEM_PROMPT", "build_repository_prompt"]
