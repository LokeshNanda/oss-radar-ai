"""Tests for the fetching layer's content blocklist."""
from datetime import date, datetime, timezone

from open_source_radar_ai.config import AppConfig, GitHubConfig
from open_source_radar_ai.fetch import (
    fetch_trending_repositories,
    filter_blocked_repositories,
    is_blocked_repository,
)
from open_source_radar_ai.models import Repository


def make_repo(
    repo_id: int = 1,
    full_name: str = "owner/repo",
    description: str | None = None,
    topics: tuple = (),
    stars: int = 100,
) -> Repository:
    now = datetime(2026, 8, 3, tzinfo=timezone.utc)
    owner, _, name = full_name.partition("/")
    return Repository(
        id=repo_id,
        name=name,
        full_name=full_name,
        html_url=f"https://github.com/{full_name}",
        description=description,
        stargazers_count=stars,
        language=None,
        topics=list(topics),
        created_at=now,
        updated_at=now,
        owner_login=owner,
    )


def make_config() -> AppConfig:
    return AppConfig(
        github=GitHubConfig(
            token=None,
            api_base_url="https://api.github.com",
            per_page=10,
            days_back=7,
        ),
        reference_date=date(2026, 8, 3),
    )


class FakeClient:
    def __init__(self, repos):
        self._repos = repos

    def search_trending_repositories(self, params):
        return list(self._repos)


def test_blocks_cheat_description():
    repo = make_repo(
        full_name="WilonityDev/WilonityLoader",
        description=(
            "Wilonity Loader – cheat lib w/ spoofer, driver bypass, undetected "
            "injector for 20+ games. Kernel spoof, HWID cleaner, AC bypass. "
            "ESP, aimbot, wallhack, triggerbot."
        ),
        topics=("game", "hack"),
    )
    assert is_blocked_repository(repo)


def test_blocks_by_topic():
    repo = make_repo(description="A modding toolkit", topics=("aimbot",))
    assert is_blocked_repository(repo)


def test_allows_normal_repo():
    repo = make_repo(description="An open-source, agentic-first CRM.")
    assert not is_blocked_repository(repo)


def test_allows_cheatsheet_repos():
    repo = make_repo(
        full_name="owner/awesome-cheatsheets",
        description="A collection of cheatsheets for developers",
    )
    assert not is_blocked_repository(repo)


def test_word_boundary_avoids_substring_false_positive():
    # "mac bypass" must not match the "ac bypass" term.
    repo = make_repo(description="Utility to bypass mac bypass quirks on macOS")
    assert not is_blocked_repository(repo)


def test_env_blocked_repos(monkeypatch):
    monkeypatch.setenv("RADAR_BLOCKED_REPOS", "bad/actor, Other/Repo")
    assert is_blocked_repository(make_repo(full_name="Bad/Actor"))
    assert not is_blocked_repository(make_repo(full_name="good/actor"))


def test_env_extra_terms(monkeypatch):
    monkeypatch.setenv("RADAR_BLOCKLIST_TERMS", "cryptostealer")
    repo = make_repo(description="A cryptostealer toolkit")
    assert is_blocked_repository(repo)


def test_filter_logs_and_drops(caplog):
    blocked = make_repo(repo_id=2, full_name="x/cheats", description="aimbot for CS2")
    kept = make_repo(repo_id=3, full_name="x/ok", description="A web framework")
    result = filter_blocked_repositories([blocked, kept])
    assert result == [kept]


def test_fetch_applies_blocklist():
    blocked = make_repo(repo_id=2, full_name="x/loader", description="undetected injector")
    kept = make_repo(repo_id=3, full_name="x/ok", description="A web framework")
    client = FakeClient([blocked, kept])
    result = fetch_trending_repositories(make_config(), client=client)
    assert [r.id for r in result] == [3]
