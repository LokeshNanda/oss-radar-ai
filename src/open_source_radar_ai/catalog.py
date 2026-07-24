"""Persistent catalog of all featured repositories."""

from __future__ import annotations

from dataclasses import asdict, dataclass
import os
from pathlib import Path
from typing import Iterable, List, Optional

from .io_utils import atomic_write_json_if_changed, ensure_dir, read_json_file


@dataclass(frozen=True)
class CatalogEntry:
    """One featured repository in the site catalog."""

    id: int
    full_name: str
    html_url: str
    description: Optional[str]
    language: Optional[str]
    category: str
    stars_at_feature: int
    date_featured: str
    page: str


def _default_path() -> Path:
    return Path(os.getenv("RADAR_STATE_DIR", ".radar_state")) / "catalog.json"


def load_catalog(path: Path | None = None) -> List[CatalogEntry]:
    """Load the catalog; missing file means empty catalog."""
    data = read_json_file(path or _default_path())
    return [CatalogEntry(**item) for item in data.get("repos") or []]


def save_catalog(entries: Iterable[CatalogEntry], path: Path | None = None) -> bool:
    """Persist the catalog deterministically (sorted newest first)."""
    resolved = path or _default_path()
    ensure_dir(resolved.parent)
    ordered = sorted(
        entries, key=lambda e: (e.date_featured, e.stars_at_feature), reverse=True
    )
    return atomic_write_json_if_changed(resolved, {"repos": [asdict(e) for e in ordered]})


def upsert_entries(
    existing: Iterable[CatalogEntry], new: Iterable[CatalogEntry]
) -> List[CatalogEntry]:
    """Merge entries by repo id; new entries win. Sorted newest first."""
    merged = {e.id: e for e in existing}
    for e in new:
        merged[e.id] = e
    return sorted(
        merged.values(), key=lambda e: (e.date_featured, e.stars_at_feature), reverse=True
    )


__all__ = ["CatalogEntry", "load_catalog", "save_catalog", "upsert_entries"]
