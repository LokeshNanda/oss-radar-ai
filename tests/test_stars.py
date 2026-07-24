"""Tests for star history tracking."""
from datetime import date, datetime, timezone
from pathlib import Path

from open_source_radar_ai.models import Repository
from open_source_radar_ai.stars import (
    compute_risers,
    load_star_history,
    record_snapshot,
    save_star_history,
)


def make_repo(i=1, stars=100) -> Repository:
    now = datetime(2026, 7, 14, tzinfo=timezone.utc)
    return Repository(
        id=i,
        name=f"r{i}",
        full_name=f"o/r{i}",
        html_url=f"https://github.com/o/r{i}",
        description=None,
        stargazers_count=stars,
        language=None,
        topics=[],
        created_at=now,
        updated_at=now,
        owner_login="o",
    )


def test_record_and_roundtrip(tmp_path: Path):
    history = {}
    record_snapshot(history, make_repo(1, 100), date(2026, 7, 20))
    record_snapshot(history, make_repo(1, 150), date(2026, 7, 27))
    path = tmp_path / "star_history.json"
    save_star_history(history, path=path)
    loaded = load_star_history(path=path)
    assert loaded["1"]["snapshots"] == {"2026-07-20": 100, "2026-07-27": 150}


def test_compute_risers_orders_by_delta():
    history = {
        "1": {"full_name": "o/r1", "html_url": "u1", "snapshots": {"2026-07-20": 100, "2026-07-27": 150}},
        "2": {"full_name": "o/r2", "html_url": "u2", "snapshots": {"2026-07-20": 100, "2026-07-27": 300}},
        "3": {"full_name": "o/r3", "html_url": "u3", "snapshots": {"2026-07-20": 100}},
        "4": {"full_name": "o/r4", "html_url": "u4", "snapshots": {"2026-07-20": 100, "2026-07-27": 90}},
    }
    risers = compute_risers(history, limit=5)
    assert [r["full_name"] for r in risers] == ["o/r2", "o/r1"]
    assert risers[0]["delta"] == 200
