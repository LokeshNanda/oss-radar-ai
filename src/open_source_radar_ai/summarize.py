"""LLM summarization layer."""

from __future__ import annotations

import json
import logging

from .models import CATEGORIES, RepoAnalysis, Repository
from .openai_client import OpenAIClient, OpenAIConfig, load_openai_config
from .prompts import SYSTEM_PROMPT, build_repository_prompt


LOGGER = logging.getLogger(__name__)


class SummarizationError(RuntimeError):
    """Raised when summarization fails."""


def summarize_repository(
    repo: Repository,
    *,
    client: OpenAIClient,
    readme_excerpt: str | None = None,
) -> RepoAnalysis:
    """Generate a structured analysis (markdown + category) for a repository."""
    prompt = build_repository_prompt(repo, readme_excerpt=readme_excerpt)
    try:
        raw = client.chat_completion(
            system=SYSTEM_PROMPT,
            user=prompt,
            response_format={"type": "json_object"},
        )
    except Exception as exc:  # noqa: BLE001
        raise SummarizationError(f"Failed to summarize {repo.full_name}: {exc}") from exc

    try:
        data = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise SummarizationError(
            f"Non-JSON analysis for {repo.full_name}: {raw[:200]}"
        ) from exc

    markdown = data.get("analysis_markdown")
    if not isinstance(markdown, str) or not markdown.strip():
        raise SummarizationError(f"Empty analysis for {repo.full_name}.")

    category = data.get("category")
    if category not in CATEGORIES:
        LOGGER.warning(
            "Invalid category %r for %s; falling back to 'Other'.", category, repo.full_name
        )
        category = "Other"

    return RepoAnalysis(markdown=markdown.strip(), category=category)


def build_default_client() -> OpenAIClient:
    """Build a default OpenAI client from environment configuration."""
    cfg: OpenAIConfig = load_openai_config()
    return OpenAIClient(cfg)


__all__ = ["SummarizationError", "summarize_repository", "build_default_client"]
