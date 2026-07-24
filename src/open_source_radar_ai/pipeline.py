"""Orchestration pipeline for Open Source Radar AI."""

from __future__ import annotations

from dataclasses import dataclass
import logging
import os
from pathlib import Path
from typing import List

from .catalog import CatalogEntry, load_catalog, save_catalog, upsert_entries
from .config import AppConfig, load_config
from .dedupe import load_state, save_state, update_state_with_processed
from .fetch import fetch_trending_repositories
from .generator import (
    repo_markdown_path,
    write_archive_page,
    write_index_page,
    write_repo_page,
    write_weekly_report_page,
)
from .github_client import GitHubClient
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
    gh_client = GitHubClient(cfg)
    repos = fetch_trending_repositories(
        cfg, exclude_ids=state.processed_repo_ids, client=gh_client
    )
    fetched_count = len(repos)

    limit = _max_repos_per_run()
    repos = repos[:limit]

    client = build_default_client()
    summarized: List[Repository] = []
    pages_written = 0

    readme_max = int(os.getenv("RADAR_README_MAX_CHARS", "16000"))
    new_entries: List[CatalogEntry] = []
    for repo in repos:
        readme_excerpt = gh_client.get_repository_readme(
            repo.full_name, max_chars=readme_max
        )
        try:
            analysis = summarize_repository(
                repo, client=client, readme_excerpt=readme_excerpt
            )
        except SummarizationError as exc:
            LOGGER.error("%s", exc)
            continue

        if write_repo_page(
            repo,
            analysis_markdown=analysis.markdown,
            docs_dir=docs_dir,
            category=analysis.category,
        ):
            pages_written += 1
        summarized.append(repo)
        page_rel = repo_markdown_path(repo, docs_dir=docs_dir).relative_to(docs_dir).as_posix()
        new_entries.append(
            CatalogEntry(
                id=repo.id,
                full_name=repo.full_name,
                html_url=repo.html_url,
                description=repo.description,
                language=repo.language,
                category=analysis.category,
                stars_at_feature=repo.stargazers_count,
                date_featured=cfg.reference_date.isoformat(),
                page=page_rel,
            )
        )

    full_catalog = upsert_entries(load_catalog(), new_entries)
    save_catalog(full_catalog)

    index_written = False
    if summarized:
        write_weekly_report_page(
            summarized, generated_on=cfg.reference_date, docs_dir=docs_dir
        )
        index_written = write_index_page(
            summarized, generated_on=cfg.reference_date, docs_dir=docs_dir
        )

    write_archive_page(docs_dir)

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

