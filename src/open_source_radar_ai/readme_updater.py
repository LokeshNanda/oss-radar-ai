"""Auto-update the repository README's radar section."""

from __future__ import annotations

import logging
from pathlib import Path
import re
from typing import Iterable, List

from .catalog import CatalogEntry
from .io_utils import atomic_write_text_if_changed


LOGGER = logging.getLogger(__name__)

START_MARKER = "<!-- RADAR:START -->"
END_MARKER = "<!-- RADAR:END -->"


def _page_url(entry: CatalogEntry, site_url: str) -> str:
    return site_url + entry.page.removesuffix(".md") + "/"


def render_radar_section(entries: List[CatalogEntry], *, site_url: str) -> str:
    """Render the newest week's repositories as a markdown list."""
    if not entries:
        return "_No repositories featured yet._"
    latest_week = max(e.date_featured for e in entries)
    weekly = sorted(
        (e for e in entries if e.date_featured == latest_week),
        key=lambda e: -e.stars_at_feature,
    )
    lines = [f"_Week of {latest_week}_", ""]
    for e in weekly:
        desc = f" — {e.description.strip()}" if e.description else ""
        lines.append(
            f"- [`{e.full_name}`]({e.html_url}){desc} ([analysis]({_page_url(e, site_url)}))"
        )
    return "\n".join(lines)


def update_readme_radar_section(
    readme_path: Path, entries: Iterable[CatalogEntry], *, site_url: str
) -> bool:
    """Replace the radar section between markers; False if markers missing."""
    if not readme_path.exists():
        LOGGER.warning("README not found at %s; skipping radar section update.", readme_path)
        return False
    text = readme_path.read_text(encoding="utf-8")
    if START_MARKER not in text or END_MARKER not in text:
        LOGGER.warning("Radar markers missing in %s; skipping update.", readme_path)
        return False
    section = render_radar_section(list(entries), site_url=site_url)
    updated = re.sub(
        re.escape(START_MARKER) + r".*?" + re.escape(END_MARKER),
        f"{START_MARKER}\n{section}\n{END_MARKER}",
        text,
        count=1,
        flags=re.DOTALL,
    )
    return atomic_write_text_if_changed(readme_path, updated)


__all__ = ["render_radar_section", "update_readme_radar_section"]
