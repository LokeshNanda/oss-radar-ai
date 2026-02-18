"""LLM summarization layer (Phase 4)."""

from __future__ import annotations

import logging

from .models import Repository
from .openai_client import OpenAIClient, OpenAIConfig, load_openai_config
from .prompts import SYSTEM_PROMPT, build_repository_prompt


LOGGER = logging.getLogger(__name__)


class SummarizationError(RuntimeError):
    """Raised when summarization fails."""


def summarize_repository(repo: Repository, *, client: OpenAIClient) -> str:
    """Generate a structured markdown analysis for a repository."""
    prompt = build_repository_prompt(repo)
    try:
        return client.chat_completion(system=SYSTEM_PROMPT, user=prompt)
    except Exception as exc:  # noqa: BLE001
        raise SummarizationError(f"Failed to summarize {repo.full_name}: {exc}") from exc


def build_default_client() -> OpenAIClient:
    """Build a default OpenAI client from environment configuration."""
    cfg: OpenAIConfig = load_openai_config()
    return OpenAIClient(cfg)


__all__ = ["SummarizationError", "summarize_repository", "build_default_client"]

