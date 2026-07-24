"""Tests for markdown generation."""
from datetime import datetime, timezone
from pathlib import Path

from open_source_radar_ai.generator import render_repo_page
from open_source_radar_ai.models import Repository


def make_repo() -> Repository:
    now = datetime(2026, 7, 20, tzinfo=timezone.utc)
    return Repository(
        id=1,
        name="r",
        full_name="o/r",
        html_url="https://github.com/o/r",
        description="d",
        stargazers_count=10,
        language="Go",
        topics=[],
        created_at=now,
        updated_at=now,
        owner_login="o",
    )


def test_render_repo_page_with_category():
    page = render_repo_page(make_repo(), "## What it does\nx", category="Developer Tools")
    assert "category: Developer Tools" in page
    assert "- **Category**: Developer Tools" in page


def test_render_repo_page_without_category_unchanged():
    page = render_repo_page(make_repo(), "body")
    assert "category:" not in page


def test_archive_groups_by_month(tmp_path: Path):
    from open_source_radar_ai.generator import render_archive_page

    reports = tmp_path / "reports"
    reports.mkdir(parents=True)
    for d in ("2026-07-20", "2026-07-13", "2026-06-01"):
        (reports / f"{d}.md").write_text("x", encoding="utf-8")
    text = render_archive_page(tmp_path)
    assert "## July 2026" in text and "## June 2026" in text
    assert text.index("## July 2026") < text.index("## June 2026")


def test_social_draft_in_weekly_report():
    from datetime import date

    from open_source_radar_ai.generator import render_weekly_report_page

    page = render_weekly_report_page(
        [make_repo()],
        generated_on=date(2026, 7, 20),
        docs_dir=Path("docs"),
        site_url="https://example.com/",
    )
    assert '??? note "📣 Share this week\'s radar"' in page
    assert "https://example.com/reports/2026-07-20/" in page
