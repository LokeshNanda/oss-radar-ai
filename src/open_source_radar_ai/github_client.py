"""GitHub API client for Open Source Radar AI."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date, timedelta
import logging
from typing import Iterable, List, Optional

import requests

from .config import AppConfig, GitHubConfig
from .models import Repository


LOGGER = logging.getLogger(__name__)


class GitHubAPIError(RuntimeError):
    """Raised when the GitHub API returns an error response."""


@dataclass(frozen=True)
class GitHubSearchParams:
    """Parameters controlling the GitHub repository search."""

    created_since: date
    per_page: int


class GitHubClient:
    """Client wrapper around the GitHub REST API."""

    def __init__(self, config: AppConfig) -> None:
        self._config = config
        self._session = requests.Session()
        headers = {
            "Accept": "application/vnd.github+json",
            "User-Agent": "open-source-radar-ai",
        }
        token = config.github.token
        if token:
            headers["Authorization"] = f"Bearer {token}"
        self._session.headers.update(headers)

    @property
    def github_config(self) -> GitHubConfig:
        """Return the GitHub configuration."""
        return self._config.github

    def search_trending_repositories(self, params: GitHubSearchParams) -> List[Repository]:
        """Fetch trending repositories created since the given date.

        The function:
        - Queries the GitHub search API for repositories.
        - Sorts by stars descending.
        - Limits the number of returned repositories to ``params.per_page``.
        - Maps the results into ``Repository`` domain objects.
        """
        query = f"created:>={params.created_since.isoformat()}"
        if self.github_config.extra_query:
            query += f" {self.github_config.extra_query}"

        url = f"{self.github_config.api_base_url}/search/repositories"
        request_params = {
            "q": query,
            "sort": "stars",
            "order": "desc",
            "per_page": params.per_page,
        }

        LOGGER.info(
            "Requesting trending repositories from GitHub created since %s.",
            params.created_since.isoformat(),
        )

        response = self._session.get(url, params=request_params, timeout=30)
        if response.status_code >= 400:
            message = (
                "GitHub API request failed with status %s: %s"
                % (response.status_code, response.text)
            )
            LOGGER.error(message)
            raise GitHubAPIError(message)

        data = response.json()
        items = data.get("items") or []
        LOGGER.info("GitHub search returned %d repositories.", len(items))

        repositories: List[Repository] = [
            Repository.from_api_response(item) for item in items
        ]
        return repositories

    def get_repository_readme(self, full_name: str, *, max_chars: int = 16000) -> Optional[str]:
        """Fetch a repository's README as raw text; None on any failure."""
        url = f"{self.github_config.api_base_url}/repos/{full_name}/readme"
        try:
            response = self._session.get(
                url, headers={"Accept": "application/vnd.github.raw+json"}, timeout=30
            )
        except requests.RequestException as exc:
            LOGGER.warning("README fetch failed for %s: %s", full_name, exc)
            return None
        if response.status_code >= 400:
            LOGGER.info("No README for %s (status %d).", full_name, response.status_code)
            return None
        text = response.text.strip()
        if not text:
            return None
        return text[:max_chars]

    def get_repository_by_id(self, repo_id: int) -> Optional[Repository]:
        """Fetch a repository by numeric ID; None on any failure."""
        url = f"{self.github_config.api_base_url}/repositories/{repo_id}"
        try:
            response = self._session.get(url, timeout=30)
        except requests.RequestException as exc:
            LOGGER.warning("Repo fetch failed for id=%d: %s", repo_id, exc)
            return None
        if response.status_code >= 400:
            LOGGER.info("Repo id=%d unavailable (status %d).", repo_id, response.status_code)
            return None
        try:
            return Repository.from_api_response(response.json())
        except (KeyError, ValueError, TypeError) as exc:
            LOGGER.warning("Malformed repo payload for id=%d: %s", repo_id, exc)
            return None


def build_search_params(config: AppConfig) -> GitHubSearchParams:
    """Build ``GitHubSearchParams`` from the application configuration."""
    created_since = config.reference_date - timedelta(days=config.github.days_back)
    return GitHubSearchParams(
        created_since=created_since,
        per_page=config.github.per_page,
    )


__all__ = ["GitHubClient", "GitHubSearchParams", "GitHubAPIError", "build_search_params"]

