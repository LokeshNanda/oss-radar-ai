"""Deduplication layer to ensure idempotent processing (Phase 3)."""

from __future__ import annotations

from dataclasses import dataclass
import logging
import os
from pathlib import Path
from typing import Iterable, List, Set

from .io_utils import atomic_write_json_if_changed, read_json_file, ensure_dir
from .models import Repository


LOGGER = logging.getLogger(__name__)


@dataclass(frozen=True)
class DedupeState:
    """Represents processed repository IDs."""

    processed_repo_ids: Set[int]


def _default_state_path() -> Path:
    state_dir = Path(os.getenv("RADAR_STATE_DIR", ".radar_state"))
    return state_dir / "processed_repos.json"


def load_state(path: Path | None = None) -> DedupeState:
    """Load dedupe state from disk.

    Missing state files are treated as empty state.
    """
    resolved = path or _default_state_path()
    data = read_json_file(resolved)
    ids = data.get("processed_repo_ids") or []
    processed = {int(x) for x in ids}
    return DedupeState(processed_repo_ids=processed)


def filter_unprocessed(repos: Iterable[Repository], state: DedupeState) -> List[Repository]:
    """Filter out repositories that have already been processed."""
    repo_list = list(repos)
    result = [r for r in repo_list if r.id not in state.processed_repo_ids]
    LOGGER.info("Deduped %d -> %d repositories.", len(repo_list), len(result))
    return result


def update_state_with_processed(
    state: DedupeState,
    processed: Iterable[Repository],
) -> DedupeState:
    """Return a new state that includes the processed repositories."""
    updated = set(state.processed_repo_ids)
    for repo in processed:
        updated.add(repo.id)
    return DedupeState(processed_repo_ids=updated)


def save_state(state: DedupeState, path: Path | None = None) -> bool:
    """Persist dedupe state to disk deterministically.

    Returns:
        True if state was written/updated, False if no changes were needed.
    """
    resolved = path or _default_state_path()
    ensure_dir(resolved.parent)
    payload = {
        "processed_repo_ids": sorted(state.processed_repo_ids),
    }
    changed = atomic_write_json_if_changed(resolved, payload)
    if changed:
        LOGGER.info("Updated dedupe state at %s.", resolved.as_posix())
    else:
        LOGGER.info("Dedupe state unchanged at %s.", resolved.as_posix())
    return changed


__all__ = [
    "DedupeState",
    "load_state",
    "filter_unprocessed",
    "update_state_with_processed",
    "save_state",
]

