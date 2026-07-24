"""Fetching layer for trending GitHub repositories (Phase 2)."""

from __future__ import annotations

from typing import Iterable, List, Set

from .config import AppConfig, load_config
from .github_client import GitHubClient, GitHubSearchParams, build_search_params
from .logging_utils import get_logger
from .models import Repository


LOGGER = get_logger(__name__)


def fetch_trending_repositories(
    config: AppConfig,
    *,
    exclude_ids: Iterable[int] | None = None,
    client: GitHubClient | None = None,
) -> List[Repository]:
    """Fetch trending repositories from GitHub.

    Args:
        config: Loaded application configuration.
        exclude_ids: Optional iterable of repository IDs that should be
            excluded from the result set. This parameter allows higher
            layers to enforce idempotency and deduplication.

    Returns:
        A list of ``Repository`` instances sorted by star count descending.
    """
    client = client or GitHubClient(config)
    search_params: GitHubSearchParams = build_search_params(config)

    excluded: Set[int] = set(exclude_ids or [])
    repositories = client.search_trending_repositories(search_params)

    if excluded:
        filtered = [repo for repo in repositories if repo.id not in excluded]
        LOGGER.info(
            "Filtered %d repositories based on exclude_ids; %d remain.",
            len(repositories) - len(filtered),
            len(filtered),
        )
        repositories = filtered
    else:
        LOGGER.info("No exclude_ids provided; returning all %d repositories.", len(repositories))

    # Ensure deterministic ordering by stargazers count and then id.
    repositories.sort(key=lambda r: (-r.stargazers_count, r.id))
    return repositories


def fetch_trending_repositories_with_default_config(
    *,
    exclude_ids: Iterable[int] | None = None,
) -> List[Repository]:
    """Convenience wrapper that loads configuration and fetches repositories.

    This function is idempotent with respect to side effects; it only reads
    configuration and the GitHub API and does not mutate local state.
    """
    config = load_config()
    return fetch_trending_repositories(config, exclude_ids=exclude_ids)


__all__ = ["fetch_trending_repositories", "fetch_trending_repositories_with_default_config"]

