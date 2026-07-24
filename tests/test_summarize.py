"""Tests for structured summarization."""
import json
from datetime import datetime, timezone

import pytest

from open_source_radar_ai.models import CATEGORIES, RepoAnalysis, Repository
from open_source_radar_ai.summarize import SummarizationError, summarize_repository


def make_repo() -> Repository:
    now = datetime(2026, 7, 20, tzinfo=timezone.utc)
    return Repository(
        id=1,
        name="r",
        full_name="o/r",
        html_url="https://github.com/o/r",
        description="desc",
        stargazers_count=100,
        language="Rust",
        topics=["cli"],
        created_at=now,
        updated_at=now,
        owner_login="o",
    )


class FakeLLM:
    def __init__(self, content):
        self.content = content
        self.last_user = None

    def chat_completion(self, *, system, user, response_format=None):
        self.last_user = user
        return self.content


def test_returns_analysis_with_valid_category():
    payload = json.dumps(
        {"category": "Developer Tools", "analysis_markdown": "## What it does\nStuff."}
    )
    result = summarize_repository(make_repo(), client=FakeLLM(payload))
    assert isinstance(result, RepoAnalysis)
    assert result.category == "Developer Tools"
    assert "What it does" in result.markdown


def test_invalid_category_falls_back_to_other():
    payload = json.dumps(
        {"category": "Bananas", "analysis_markdown": "## What it does\nStuff."}
    )
    assert summarize_repository(make_repo(), client=FakeLLM(payload)).category == "Other"


def test_malformed_json_raises():
    with pytest.raises(SummarizationError):
        summarize_repository(make_repo(), client=FakeLLM("not json"))


def test_readme_excerpt_included_in_prompt():
    payload = json.dumps({"category": "Other", "analysis_markdown": "## What it does\nx"})
    llm = FakeLLM(payload)
    summarize_repository(make_repo(), client=llm, readme_excerpt="UNIQUE_README_MARKER")
    assert "UNIQUE_README_MARKER" in llm.last_user


def test_categories_are_fixed_set():
    assert "Other" in CATEGORIES and len(CATEGORIES) == 8
