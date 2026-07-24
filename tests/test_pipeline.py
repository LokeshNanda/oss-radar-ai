"""End-to-end pipeline test with fakes."""
import json
from datetime import datetime, timezone
from pathlib import Path

import open_source_radar_ai.pipeline as pipeline_mod
from open_source_radar_ai.catalog import load_catalog
from open_source_radar_ai.models import RepoAnalysis, Repository


def make_repo(i: int) -> Repository:
    now = datetime(2026, 7, 20, tzinfo=timezone.utc)
    return Repository(
        id=i,
        name=f"r{i}",
        full_name=f"o/r{i}",
        html_url=f"https://github.com/o/r{i}",
        description="d",
        stargazers_count=100 - i,
        language="Python",
        topics=[],
        created_at=now,
        updated_at=now,
        owner_login="o",
    )


def test_pipeline_writes_pages_and_catalog(tmp_path: Path, monkeypatch):
    docs = tmp_path / "docs"
    state = tmp_path / "state"
    monkeypatch.setenv("RADAR_DOCS_DIR", str(docs))
    monkeypatch.setenv("RADAR_STATE_DIR", str(state))
    monkeypatch.setenv("RADAR_REFERENCE_DATE", "2026-07-20")
    readme = tmp_path / "README.md"
    readme.write_text("<!-- RADAR:START -->\n<!-- RADAR:END -->\n", encoding="utf-8")
    monkeypatch.setenv("RADAR_README_PATH", str(readme))

    monkeypatch.setattr(
        pipeline_mod,
        "fetch_trending_repositories",
        lambda cfg, *, exclude_ids=None, client=None: [make_repo(1), make_repo(2)],
    )
    monkeypatch.setattr(pipeline_mod, "build_default_client", lambda: object())
    monkeypatch.setattr(
        pipeline_mod,
        "summarize_repository",
        lambda repo, *, client, readme_excerpt=None: RepoAnalysis(
            markdown="## What it does\nx", category="Developer Tools"
        ),
    )

    class FakeGitHubClient:
        def __init__(self, cfg):
            pass

        def get_repository_readme(self, full_name, *, max_chars=16000):
            return "readme text"

        def get_repository_by_id(self, repo_id):
            return None

    monkeypatch.setattr(pipeline_mod, "GitHubClient", FakeGitHubClient)

    result = pipeline_mod.run_pipeline()
    assert result.summarized == 2
    assert (docs / "repos" / "o--r1.md").exists()
    assert "category: Developer Tools" in (docs / "repos" / "o--r1.md").read_text(
        encoding="utf-8"
    )
    entries = load_catalog(path=state / "catalog.json")
    assert {e.id for e in entries} == {1, 2}
    ids = json.loads((state / "processed_repos.json").read_text())["processed_repo_ids"]
    assert ids == [1, 2]
    assert "o/r1" in readme.read_text(encoding="utf-8")
