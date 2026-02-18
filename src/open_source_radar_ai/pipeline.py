"""Orchestration pipeline for Open Source Radar AI."""

from __future__ import annotations

from dataclasses import dataclass
import logging
import os
from pathlib import Path
from typing import List

from .config import AppConfig, load_config
from .dedupe import load_state, save_state, update_state_with_processed
from .fetch import fetch_trending_repositories
from .generator import write_index_page, write_repo_page
from .models import Repository
from .summarize import SummarizationError, build_default_client, summarize_repository


LOGGER = logging.getLogger(__name__)


@dataclass(frozen=True)
class PipelineResult:
    """Result details for a pipeline run."""

    fetched: int
    new_repos: int
    summarized: int
    pages_written: int
    index_written: bool


def _docs_dir() -> Path:
    return Path(os.getenv("RADAR_DOCS_DIR", "docs"))


def _max_repos_per_run() -> int:
    raw = os.getenv("RADAR_MAX_REPOS_PER_RUN", "10")
    try:
        value = int(raw)
        return value if value > 0 else 10
    except ValueError:
        return 10


def run_pipeline(config: AppConfig | None = None) -> PipelineResult:
    """Run the fetch -> dedupe -> summarize -> generate pipeline."""
    cfg = config or load_config()
    docs_dir = _docs_dir()

    state = load_state()
    repos = fetch_trending_repositories(cfg, exclude_ids=state.processed_repo_ids)
    fetched_count = len(repos)

    limit = _max_repos_per_run()
    repos = repos[:limit]

    client = build_default_client()
    summarized: List[Repository] = []
    pages_written = 0

    for repo in repos:
        try:
            analysis = summarize_repository(repo, client=client)
        except SummarizationError as exc:
            LOGGER.error("%s", exc)
            continue

        if write_repo_page(repo, analysis_markdown=analysis, docs_dir=docs_dir):
            pages_written += 1
        summarized.append(repo)

    index_written = False
    if summarized:
        index_written = write_index_page(
            summarized, generated_on=cfg.reference_date, docs_dir=docs_dir
        )

    new_state = update_state_with_processed(state, summarized)
    save_state(new_state)

    return PipelineResult(
        fetched=fetched_count,
        new_repos=len(repos),
        summarized=len(summarized),
        pages_written=pages_written,
        index_written=index_written,
    )


__all__ = ["PipelineResult", "run_pipeline"]

