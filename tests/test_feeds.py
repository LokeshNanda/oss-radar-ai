"""Tests for RSS and JSON feeds."""
import json
import xml.etree.ElementTree as ET
from pathlib import Path

from open_source_radar_ai.catalog import CatalogEntry
from open_source_radar_ai.feeds import write_feeds


def entry(id, date) -> CatalogEntry:
    return CatalogEntry(
        id=id,
        full_name=f"o/r{id}",
        html_url=f"https://github.com/o/r{id}",
        description="d & co",
        language="Python",
        category="Other",
        stars_at_feature=10,
        date_featured=date,
        page=f"repos/o--r{id}.md",
    )


def test_writes_valid_rss_and_json(tmp_path: Path):
    docs = tmp_path / "docs"
    entries = [entry(1, "2026-07-20"), entry(2, "2026-07-20"), entry(3, "2026-07-13")]
    write_feeds(entries, docs_dir=docs, site_url="https://example.com/")
    tree = ET.parse(docs / "feed.xml")  # raises if malformed
    items = tree.getroot().findall("./channel/item")
    assert len(items) == 2
    assert items[0].find("link").text == "https://example.com/reports/2026-07-20/"
    latest = json.loads((docs / "api" / "latest.json").read_text(encoding="utf-8"))
    assert latest["generated_on"] == "2026-07-20"
    assert len(latest["repos"]) == 2
    catalog = json.loads((docs / "api" / "catalog.json").read_text(encoding="utf-8"))
    assert len(catalog["repos"]) == 3


def test_empty_catalog_writes_empty_feed(tmp_path: Path):
    docs = tmp_path / "docs"
    write_feeds([], docs_dir=docs, site_url="https://example.com/")
    assert (docs / "feed.xml").exists()
