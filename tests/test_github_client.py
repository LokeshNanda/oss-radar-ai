"""Tests for GitHubClient README and by-id fetches."""
from datetime import date

from open_source_radar_ai.config import AppConfig, GitHubConfig
from open_source_radar_ai.github_client import GitHubClient


class FakeResponse:
    def __init__(self, status_code=200, text="", json_data=None):
        self.status_code = status_code
        self.text = text
        self._json = json_data or {}

    def json(self):
        return self._json


class FakeSession:
    def __init__(self, response):
        self.response = response
        self.headers = {}
        self.last_url = None

    def get(self, url, **kwargs):
        self.last_url = url
        return self.response


def make_client(response) -> GitHubClient:
    cfg = AppConfig(
        github=GitHubConfig(
            token=None,
            api_base_url="https://api.github.com",
            per_page=10,
            days_back=7,
        ),
        reference_date=date(2026, 7, 24),
    )
    client = GitHubClient(cfg)
    client._session = FakeSession(response)
    return client


def test_readme_returned_and_truncated():
    client = make_client(FakeResponse(200, text="x" * 20000))
    result = client.get_repository_readme("owner/repo", max_chars=100)
    assert result == "x" * 100


def test_readme_404_returns_none():
    client = make_client(FakeResponse(404, text="Not Found"))
    assert client.get_repository_readme("owner/repo") is None


def test_readme_empty_returns_none():
    client = make_client(FakeResponse(200, text="   "))
    assert client.get_repository_readme("owner/repo") is None


def test_get_repository_by_id():
    payload = {
        "id": 42,
        "name": "repo",
        "full_name": "owner/repo",
        "html_url": "https://github.com/owner/repo",
        "description": "d",
        "stargazers_count": 5,
        "language": "Python",
        "topics": [],
        "created_at": "2026-07-01T00:00:00Z",
        "updated_at": "2026-07-02T00:00:00Z",
        "owner": {"login": "owner"},
    }
    client = make_client(FakeResponse(200, json_data=payload))
    repo = client.get_repository_by_id(42)
    assert repo is not None and repo.stargazers_count == 5
