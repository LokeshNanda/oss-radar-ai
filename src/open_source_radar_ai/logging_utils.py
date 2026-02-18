"""Logging configuration utilities for Open Source Radar AI."""

from __future__ import annotations

import logging
import os
from typing import Optional


def configure_logging(level: Optional[str] = None) -> None:
    """Configure application-wide logging.

    The log level can be controlled by the ``RADAR_LOG_LEVEL`` environment
    variable (e.g., ``DEBUG``, ``INFO``, ``WARNING``, ``ERROR``). If both the
    argument and environment variable are omitted, ``INFO`` is used.
    """
    env_level = os.getenv("RADAR_LOG_LEVEL", "").upper()
    resolved_level = level or env_level or "INFO"

    numeric_level = getattr(logging, resolved_level, logging.INFO)

    logging.basicConfig(
        level=numeric_level,
        format="%(asctime)s [%(levelname)s] %(name)s - %(message)s",
    )


def get_logger(name: str) -> logging.Logger:
    """Return a module-level logger instance."""
    return logging.getLogger(name)


__all__ = ["configure_logging", "get_logger"]

