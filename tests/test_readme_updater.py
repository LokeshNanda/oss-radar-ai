"""Tests for README radar-section updating."""
from pathlib import Path

from open_source_radar_ai.catalog import CatalogEntry
from open_source_radar_ai.readme_updater import update_readme_radar_section


def entry(id, date="2026-07-20") -> CatalogEntry:
    return CatalogEntry(
        id=id,
        full_name=f"o/r{id}",
        html_url=f"https://github.com/o/r{id}",
        description="d",
        language=None,
        category="Other",
        stars_at_feature=10,
        date_featured=date,
        page=f"repos/o--r{id}.md",
    )


def test_replaces_between_markers(tmp_path: Path):
    readme = tmp_path / "README.md"
    readme.write_text(
        "intro\n<!-- RADAR:START -->\nold\n<!-- RADAR:END -->\noutro\n", encoding="utf-8"
    )
    changed = update_readme_radar_section(readme, [entry(1)], site_url="https://example.com/")
    assert changed
    text = readme.read_text(encoding="utf-8")
    assert "old" not in text and "o/r1" in text
    assert text.startswith("intro\n") and text.rstrip().endswith("outro")


def test_missing_markers_is_noop(tmp_path: Path):
    readme = tmp_path / "README.md"
    readme.write_text("no markers here\n", encoding="utf-8")
    assert update_readme_radar_section(readme, [entry(1)], site_url="https://x/") is False
