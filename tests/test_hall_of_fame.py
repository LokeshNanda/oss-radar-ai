"""Tests for the hall of fame page."""
from pathlib import Path

from open_source_radar_ai.hall_of_fame import write_hall_of_fame


def test_hall_of_fame(tmp_path: Path):
    docs = tmp_path / "docs"
    history = {
        "1": {
            "full_name": "o/big",
            "html_url": "u1",
            "snapshots": {"2026-07-13": 5000, "2026-07-20": 6000},
        },
        "2": {"full_name": "o/small", "html_url": "u2", "snapshots": {"2026-07-20": 10}},
    }
    assert write_hall_of_fame(history, docs_dir=docs)
    text = (docs / "hall-of-fame.md").read_text(encoding="utf-8")
    assert text.index("o/big") < text.index("o/small")
    assert "+1000" in text  # riser delta
