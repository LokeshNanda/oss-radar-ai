"""Top-level package for Open Source Radar AI.

This package provides tools to fetch and analyze trending open-source
repositories from GitHub and generate architect-level insights.
"""

from importlib.metadata import version, PackageNotFoundError


def get_version() -> str:
    """Return the installed package version.

    Falls back to ``"0.0.0"`` if the package metadata cannot be found.
    """
    try:
        return version("open-source-radar-ai")
    except PackageNotFoundError:
        return "0.0.0"


__all__ = ["get_version"]

