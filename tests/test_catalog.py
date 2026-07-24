"""Tests for the repository catalog."""
from pathlib import Path

from open_source_radar_ai.catalog import (
    CatalogEntry,
    load_catalog,
    save_catalog,
    upsert_entries,
)


def entry(id=1, date="2026-07-20", stars=10, category="Other") -> CatalogEntry:
    return CatalogEntry(
        id=id,
        full_name=f"o/r{id}",
        html_url=f"https://github.com/o/r{id}",
        description="d",
        language="Python",
        category=category,
        stars_at_feature=stars,
        date_featured=date,
        page=f"repos/o--r{id}.md",
    )


def test_roundtrip(tmp_path: Path):
    path = tmp_path / "catalog.json"
    save_catalog([entry(1), entry(2)], path=path)
    loaded = load_catalog(path=path)
    assert sorted(e.id for e in loaded) == [1, 2]
    assert entry(1) in loaded


def test_load_missing_returns_empty(tmp_path: Path):
    assert load_catalog(path=tmp_path / "nope.json") == []


def test_upsert_dedupes_and_sorts():
    old = [entry(1, date="2026-07-13", stars=5)]
    new = [entry(1, date="2026-07-13", stars=7), entry(2, date="2026-07-20", stars=1)]
    merged = upsert_entries(old, new)
    assert len(merged) == 2
    assert merged[0].id == 2  # newest date first
    assert merged[1].stars_at_feature == 7  # new wins
