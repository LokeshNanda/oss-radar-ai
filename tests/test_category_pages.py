"""Tests for category index pages."""
from pathlib import Path

from open_source_radar_ai.catalog import CatalogEntry
from open_source_radar_ai.category_pages import write_category_pages


def entry(id, category) -> CatalogEntry:
    return CatalogEntry(
        id=id,
        full_name=f"o/r{id}",
        html_url=f"https://github.com/o/r{id}",
        description="d",
        language="Python",
        category=category,
        stars_at_feature=10,
        date_featured="2026-07-20",
        page=f"repos/o--r{id}.md",
    )


def test_writes_index_and_category_pages(tmp_path: Path):
    docs = tmp_path / "docs"
    written = write_category_pages(
        [entry(1, "AI & Agents"), entry(2, "Security")], docs_dir=docs
    )
    assert written == 3  # index + 2 categories
    index = (docs / "categories" / "index.md").read_text(encoding="utf-8")
    assert "AI & Agents" in index and "Security" in index
    ai = (docs / "categories" / "ai-agents.md").read_text(encoding="utf-8")
    assert "[`o/r1`](../repos/o--r1.md)" in ai


def test_empty_catalog_writes_only_index(tmp_path: Path):
    assert write_category_pages([], docs_dir=tmp_path / "docs") == 1
