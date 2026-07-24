"""Tests for the backfill CLI."""
import json
from pathlib import Path

import open_source_radar_ai.backfill as backfill_mod
from open_source_radar_ai.catalog import load_catalog

PAGE = """---
title: o/r1
source: https://github.com/o/r1
stars: 42
---

# o/r1

- **URL**: https://github.com/o/r1
- **Stars**: 42

## Executive Summary
Old analysis text.
"""

REPORT = """---
title: Week of 2026-03-02
---
- [`o/r1`](../repos/o--r1.md) — something
"""


def setup_docs(tmp_path: Path) -> Path:
    docs = tmp_path / "docs"
    (docs / "repos").mkdir(parents=True)
    (docs / "reports").mkdir(parents=True)
    (docs / "repos" / "o--r1.md").write_text(PAGE, encoding="utf-8")
    (docs / "reports" / "2026-03-02.md").write_text(REPORT, encoding="utf-8")
    return docs


class FakeLLM:
    def chat_completion(self, *, system, user, response_format=None):
        return json.dumps({"category": "Developer Tools"})


def test_backfill_populates_catalog_and_frontmatter(tmp_path: Path, monkeypatch):
    docs = setup_docs(tmp_path)
    monkeypatch.setenv("RADAR_STATE_DIR", str(tmp_path / "state"))
    monkeypatch.setattr(backfill_mod, "build_default_client", lambda: FakeLLM())
    count = backfill_mod.run_backfill(docs, categorize=True)
    assert count == 1
    entries = load_catalog(path=tmp_path / "state" / "catalog.json")
    assert entries[0].full_name == "o/r1"
    assert entries[0].category == "Developer Tools"
    assert entries[0].date_featured == "2026-03-02"
    assert "category: Developer Tools" in (docs / "repos" / "o--r1.md").read_text(
        encoding="utf-8"
    )


def test_backfill_skips_pages_already_in_catalog(tmp_path: Path, monkeypatch):
    docs = setup_docs(tmp_path)
    monkeypatch.setenv("RADAR_STATE_DIR", str(tmp_path / "state"))
    monkeypatch.setattr(backfill_mod, "build_default_client", lambda: FakeLLM())
    assert backfill_mod.run_backfill(docs, categorize=True) == 1
    assert backfill_mod.run_backfill(docs, categorize=True) == 0
