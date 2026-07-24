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
