"""Star-count history tracking for featured repositories."""

from __future__ import annotations

from datetime import date
import os
from pathlib import Path
from typing import Any, Dict, List

from .io_utils import atomic_write_json_if_changed, ensure_dir, read_json_file
from .models import Repository


def _default_path() -> Path:
    return Path(os.getenv("RADAR_STATE_DIR", ".radar_state")) / "star_history.json"


def load_star_history(path: Path | None = None) -> Dict[str, Any]:
    """Load star history; missing file means empty history."""
    return read_json_file(path or _default_path())


def save_star_history(history: Dict[str, Any], path: Path | None = None) -> bool:
    """Persist star history deterministically."""
    resolved = path or _default_path()
    ensure_dir(resolved.parent)
    return atomic_write_json_if_changed(resolved, history)


def record_snapshot(history: Dict[str, Any], repo: Repository, on_date: date) -> None:
    """Record a star-count snapshot for a repository (mutates history)."""
    key = str(repo.id)
    entry = history.setdefault(
        key, {"full_name": repo.full_name, "html_url": repo.html_url, "snapshots": {}}
    )
    entry["full_name"] = repo.full_name
    entry["html_url"] = repo.html_url
    entry["snapshots"][on_date.isoformat()] = repo.stargazers_count


def compute_risers(history: Dict[str, Any], *, limit: int = 5) -> List[Dict[str, Any]]:
    """Top repositories by star gain between their two most recent snapshots."""
    risers: List[Dict[str, Any]] = []
    for entry in history.values():
        snapshots = entry.get("snapshots") or {}
        if len(snapshots) < 2:
            continue
        dates = sorted(snapshots)
        delta = snapshots[dates[-1]] - snapshots[dates[-2]]
        if delta <= 0:
            continue
        risers.append(
            {
                "full_name": entry["full_name"],
                "html_url": entry["html_url"],
                "delta": delta,
                "stars": snapshots[dates[-1]],
            }
        )
    risers.sort(key=lambda r: -r["delta"])
    return risers[:limit]


__all__ = ["load_star_history", "save_star_history", "record_snapshot", "compute_risers"]
