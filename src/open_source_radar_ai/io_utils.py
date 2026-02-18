"""File I/O utilities with idempotent, atomic writes."""

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any, Dict


def ensure_dir(path: Path) -> None:
    """Ensure a directory exists (idempotent)."""
    path.mkdir(parents=True, exist_ok=True)


def read_text_if_exists(path: Path) -> str | None:
    """Read text if the file exists, otherwise return None."""
    if not path.exists():
        return None
    return path.read_text(encoding="utf-8")


def atomic_write_text_if_changed(path: Path, content: str) -> bool:
    """Atomically write a file only if content differs.

    Returns:
        True if the file was written/updated, False if no change was needed.
    """
    existing = read_text_if_exists(path)
    if existing == content:
        return False

    ensure_dir(path.parent)
    tmp_path = path.with_suffix(path.suffix + ".tmp")
    tmp_path.write_text(content, encoding="utf-8")
    os.replace(tmp_path, path)
    return True


def read_json_file(path: Path) -> Dict[str, Any]:
    """Read a JSON object from disk.

    Returns an empty dict if the file does not exist.
    """
    raw = read_text_if_exists(path)
    if raw is None:
        return {}
    return json.loads(raw)


def atomic_write_json_if_changed(path: Path, obj: Dict[str, Any]) -> bool:
    """Write JSON to disk deterministically, only if changed.

    JSON formatting is stable to reduce noisy diffs.
    """
    content = json.dumps(obj, indent=2, sort_keys=True) + "\n"
    return atomic_write_text_if_changed(path, content)


__all__ = [
    "ensure_dir",
    "read_text_if_exists",
    "atomic_write_text_if_changed",
    "read_json_file",
    "atomic_write_json_if_changed",
]

