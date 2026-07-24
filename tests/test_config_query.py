"""Tests for configurable search scope."""
from datetime import date

from open_source_radar_ai.config import AppConfig, GitHubConfig
from open_source_radar_ai.github_client import GitHubClient, GitHubSearchParams


def test_extra_query_appended():
    captured = {}

    class FakeSession:
        headers = {}

        def get(self, url, params=None, **kwargs):
            captured["params"] = params

            class R:
                status_code = 200

                @staticmethod
                def json():
                    return {"items": []}

            return R()

    cfg = AppConfig(
        github=GitHubConfig(
            token=None,
            api_base_url="https://api.github.com",
            per_page=10,
            days_back=7,
            extra_query="topic:rust language:rust",
        ),
        reference_date=date(2026, 7, 24),
    )
    client = GitHubClient(cfg)
    client._session = FakeSession()
    client.search_trending_repositories(
        GitHubSearchParams(created_since=date(2026, 7, 17), per_page=10)
    )
    assert captured["params"]["q"] == "created:>=2026-07-17 topic:rust language:rust"


def test_no_extra_query_unchanged():
    cfg = GitHubConfig(
        token=None, api_base_url="x", per_page=10, days_back=7, extra_query=""
    )
    assert cfg.extra_query == ""
