"""Command-line interface for Open Source Radar AI."""

from __future__ import annotations

import sys
from typing import Iterable

from .config import load_config
from .fetch import fetch_trending_repositories
from .logging_utils import configure_logging, get_logger


LOGGER = get_logger(__name__)


def main_fetch(argv: Iterable[str] | None = None) -> int:
    """Entry point for the ``radar-fetch`` console script."""
    _ = list(argv or [])
    configure_logging()

    try:
        config = load_config()
        repositories = fetch_trending_repositories(config)
    except Exception as exc:  # noqa: BLE001
        LOGGER.exception("Fetch failed: %s", exc)
        return 1

    LOGGER.info("Fetched %d trending repositories successfully.", len(repositories))
    return 0


def main_run(argv: Iterable[str] | None = None) -> int:
    """Entry point for the ``radar-run`` console script."""
    _ = list(argv or [])
    configure_logging()

    try:
        from .pipeline import run_pipeline

        result = run_pipeline(load_config())
    except Exception as exc:  # noqa: BLE001
        LOGGER.exception("Pipeline run failed: %s", exc)
        return 1

    LOGGER.info("Pipeline complete: %s", result)
    return 0


if __name__ == "__main__":  # pragma: no cover
    sys.exit(main_fetch())

