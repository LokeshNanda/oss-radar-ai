"""Fetching layer for trending GitHub repositories (Phase 2)."""

from __future__ import annotations

import os
import re
from typing import Iterable, List, Pattern, Set

from .config import AppConfig, load_config
from .github_client import GitHubClient, GitHubSearchParams, build_search_params
from .logging_utils import get_logger
from .models import Repository


LOGGER = get_logger(__name__)


# GitHub prohibits linking to game-cheat / malware-distribution content;
# featuring WilonityDev/WilonityLoader got this project's account flagged
# (2026-08). Repos whose name or description match these terms are skipped.
DEFAULT_BLOCKLIST_TERMS: tuple = (
    "aimbot",
    "wallhack",
    "triggerbot",
    "silent aim",
    "no recoil",
    "cheat lib",
    "cheat loader",
    "game cheat",
    "game hack",
    "hwid spoofer",
    "hwid cleaner",
    "hwid unban",
    "anti-cheat bypass",
    "anticheat bypass",
    "ac bypass",
    "eac bypass",
    "battleye bypass",
    "kernel spoof",
    "undetected injector",
)

# Topics are compared exactly (lowercase), not as substrings.
DEFAULT_BLOCKLIST_TOPICS: frozenset = frozenset(
    {"aimbot", "wallhack", "cheat", "cheats", "game-cheat", "game-hack", "hwid-spoofer"}
)


def _blocklist_patterns() -> List[Pattern[str]]:
    """Compile blocklist terms (defaults plus RADAR_BLOCKLIST_TERMS) to word-boundary regexes."""
    terms = list(DEFAULT_BLOCKLIST_TERMS)
    extra = os.getenv("RADAR_BLOCKLIST_TERMS", "")
    terms.extend(t.strip().lower() for t in extra.split(",") if t.strip())
    return [re.compile(r"\b" + re.escape(term) + r"\b") for term in terms]


def _blocked_repo_names() -> Set[str]:
    """Full names (owner/name, lowercase) from RADAR_BLOCKED_REPOS that must never be featured."""
    raw = os.getenv("RADAR_BLOCKED_REPOS", "")
    return {name.strip().lower() for name in raw.split(",") if name.strip()}


def is_blocked_repository(repo: Repository) -> bool:
    """Return True if the repository matches the content blocklist."""
    if repo.full_name.lower() in _blocked_repo_names():
        return True
    haystack = " ".join(
        [repo.full_name, repo.description or "", " ".join(repo.topics)]
    ).lower()
    if any(pattern.search(haystack) for pattern in _blocklist_patterns()):
        return True
    topics = {topic.lower() for topic in repo.topics}
    return bool(topics & DEFAULT_BLOCKLIST_TOPICS)


def filter_blocked_repositories(repos: Iterable[Repository]) -> List[Repository]:
    """Drop repositories matching the content blocklist, logging each skip."""
    result: List[Repository] = []
    for repo in repos:
        if is_blocked_repository(repo):
            LOGGER.warning(
                "Skipping %s: matches content blocklist (cheat/malware indicators).",
                repo.full_name,
            )
            continue
        result.append(repo)
    return result


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
    repositories = filter_blocked_repositories(repositories)

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


__all__ = [
    "fetch_trending_repositories",
    "fetch_trending_repositories_with_default_config",
    "filter_blocked_repositories",
    "is_blocked_repository",
]

