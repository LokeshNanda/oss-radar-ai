"""Configuration loading for Open Source Radar AI.

Configuration is sourced from environment variables, with optional support
for a local ``.env`` file in development environments.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
import logging
import os
from pathlib import Path
from typing import Optional

try:
    from dotenv import load_dotenv  # type: ignore[import]
except ModuleNotFoundError:  # pragma: no cover
    load_dotenv = None


LOGGER = logging.getLogger(__name__)


def load_dotenv_if_present() -> None:
    """Load environment variables from a local .env file if present.

    This function is safe and idempotent; calling it multiple times has
    no side effects beyond environment variable loading.
    """
    env_path = Path(".env")
    if env_path.exists():
        if load_dotenv is None:
            LOGGER.warning(
                "python-dotenv is not installed; .env file will not be loaded."
            )
            return
        load_dotenv(dotenv_path=env_path)
        LOGGER.debug("Loaded environment variables from .env file.")
    else:
        LOGGER.debug(".env file not found; relying on process environment.")


@dataclass(frozen=True)
class GitHubConfig:
    """Configuration for GitHub API access."""

    token: Optional[str]
    api_base_url: str
    per_page: int
    days_back: int


@dataclass(frozen=True)
class AppConfig:
    """Top-level application configuration."""

    github: GitHubConfig
    reference_date: date


def _load_github_token() -> Optional[str]:
    """Load and log the GitHub token if present."""
    token = os.getenv("GITHUB_TOKEN")
    if token:
        LOGGER.debug("Using GitHub token from environment.")
    else:
        LOGGER.warning(
            "GITHUB_TOKEN is not set; GitHub API requests will be unauthenticated "
            "and may be heavily rate limited."
        )
    return token


def _load_int_env(name: str, default: int, *, min_value: int) -> int:
    """Load an integer environment variable with validation and logging."""
    raw = os.getenv(name, str(default))
    try:
        value = int(raw)
        if value < min_value:
            raise ValueError(f"{name} must be >= {min_value}")
        return value
    except ValueError:
        LOGGER.warning("Invalid %s=%s; falling back to %d.", name, raw, default)
        return default


def _load_reference_date() -> date:
    """Load the reference date used for computing the search window."""
    reference_date_raw = os.getenv("RADAR_REFERENCE_DATE")
    if not reference_date_raw:
        return date.today()

    try:
        return date.fromisoformat(reference_date_raw)
    except ValueError:
        LOGGER.warning(
            "Invalid RADAR_REFERENCE_DATE=%s; expected YYYY-MM-DD. "
            "Falling back to today's date.",
            reference_date_raw,
        )
        return date.today()


def load_config() -> AppConfig:
    """Load application configuration from environment variables.

    Environment variables:
    - GITHUB_TOKEN: optional GitHub personal access token.
    - GITHUB_API_BASE_URL: override for GitHub API base URL.
    - GITHUB_PER_PAGE: number of repositories per page (default: 10).
    - GITHUB_DAYS_BACK: lookback window in days (default: 7).
    - RADAR_REFERENCE_DATE: reference date in YYYY-MM-DD format used to
      compute the created-since cutoff. If omitted, today's UTC date is used.

    Returns:
        An ``AppConfig`` instance populated from the environment.
    """
    load_dotenv_if_present()

    token = _load_github_token()
    api_base_url = os.getenv("GITHUB_API_BASE_URL", "https://api.github.com")
    per_page = _load_int_env("GITHUB_PER_PAGE", 10, min_value=1)
    days_back = _load_int_env("GITHUB_DAYS_BACK", 7, min_value=1)
    reference = _load_reference_date()

    github_cfg = GitHubConfig(
        token=token,
        api_base_url=api_base_url.rstrip("/"),
        per_page=per_page,
        days_back=days_back,
    )

    return AppConfig(github=github_cfg, reference_date=reference)


__all__ = ["AppConfig", "GitHubConfig", "load_config", "load_dotenv_if_present"]

