"""Tests for the trends page."""
from pathlib import Path

from open_source_radar_ai.catalog import CatalogEntry
from open_source_radar_ai.trends import write_trends_page


def entry(id, date, category="Other", language="Python") -> CatalogEntry:
    return CatalogEntry(
        id=id,
        full_name=f"o/r{id}",
        html_url="u",
        description=None,
        language=language,
        category=category,
        stars_at_feature=1,
        date_featured=date,
        page=f"repos/o--r{id}.md",
    )


def test_trends_page_contents(tmp_path: Path):
    docs = tmp_path / "docs"
    entries = [
        entry(1, "2026-07-20", "AI & Agents", "Python"),
        entry(2, "2026-07-13", "AI & Agents", "Rust"),
        entry(3, "2026-06-01", "Security", "Python"),
    ]
    assert write_trends_page(entries, docs_dir=docs)
    text = (docs / "trends.md").read_text(encoding="utf-8")
    assert "3 repositories featured" in text
    assert "| AI & Agents |" in text
    assert "2026-07" in text and "2026-06" in text
    assert "Python" in text and "Rust" in text
