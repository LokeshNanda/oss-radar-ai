"""GitHub API client for Open Source Radar AI."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date, timedelta
import logging
from typing import Iterable, List

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


def build_search_params(config: AppConfig) -> GitHubSearchParams:
    """Build ``GitHubSearchParams`` from the application configuration."""
    created_since = config.reference_date - timedelta(days=config.github.days_back)
    return GitHubSearchParams(
        created_since=created_since,
        per_page=config.github.per_page,
    )


__all__ = ["GitHubClient", "GitHubSearchParams", "GitHubAPIError", "build_search_params"]

