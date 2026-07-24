# Popularity Roadmap Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Implement all phases of `specs/2026-07-24-popularity-roadmap-design.md`: discoverability quick wins, README-aware categorized LLM analysis with star tracking, zero-manual distribution (RSS/JSON/social cards/auto-README), the fork-your-own-radar template, and stickiness pages (trends, hall of fame).

**Architecture:** Extend the existing modular pipeline (`fetch → dedupe → summarize → generate`) with: a persistent **catalog** (`.radar_state/catalog.json`) that becomes the single data source for category pages, JSON feeds, trends and hall-of-fame; README-aware structured LLM output (JSON mode → `RepoAnalysis(markdown, category)`); and a **star history** state file for weekly deltas. All writes stay deterministic via `io_utils.atomic_write_text_if_changed`.

**Tech Stack:** Python 3.11, requests, MkDocs Material, GitHub Actions, OpenAI-compatible Chat Completions API, pytest (new dev dependency).

## Global Constraints

- Python >= 3.11 (`pyproject.toml`).
- All file generation must be deterministic and idempotent — always write through `io_utils.atomic_write_text_if_changed` / `atomic_write_json_if_changed`.
- No secrets in code; all config via env vars (document new ones in `.env.example`).
- README fetch or LLM failures must degrade gracefully (skip repo / metadata-only), never crash the pipeline.
- `mkdocs build --strict` must pass after every docs-affecting task.
- Site URL: `https://lokeshnanda.github.io/oss-radar-ai/`. Repo: `https://github.com/LokeshNanda/oss-radar-ai`.
- Plans/specs live in top-level `plans/` and `specs/` (NOT under `docs/` — that's the published site).
- Tests run with `python -m pytest tests -q`.
- Commit after every task; do not push unless the user asks.

---

# PHASE 0 — Discoverability quick wins

### Task 1: MIT LICENSE + pytest scaffolding

**Files:**
- Create: `LICENSE`
- Modify: `pyproject.toml`
- Create: `tests/test_smoke.py`

**Interfaces:**
- Produces: `[project.optional-dependencies] dev = ["pytest"]`; a `tests/` directory all later tasks add to.

- [ ] **Step 1: Create LICENSE** — standard MIT license text, `Copyright (c) 2026 Lokesh Nanda`.

- [ ] **Step 2: Add dev extra and license metadata to pyproject.toml**

```toml
[project]
name = "open-source-radar-ai"
version = "0.2.0"
description = "AI-powered GitHub Open Source Radar"
requires-python = ">=3.11"
license = { file = "LICENSE" }
dependencies = [
    "requests",
    "python-dotenv",
    "mkdocs",
    "mkdocs-material",
]

[project.optional-dependencies]
dev = ["pytest"]
```
(keep existing `[project.scripts]`, build-system, setuptools sections unchanged)

- [ ] **Step 3: Smoke test**

```python
"""Smoke test: package imports and pipeline entry points exist."""
from open_source_radar_ai import pipeline, cli


def test_package_imports() -> None:
    assert callable(pipeline.run_pipeline)
    assert callable(cli.main_run)
```

- [ ] **Step 4: Install and run** — `pip install -e ".[dev]"` then `python -m pytest tests -q` → 1 passed.

- [ ] **Step 5: Commit** — `git add LICENSE pyproject.toml tests/ && git commit -m "chore: add MIT license and pytest scaffolding"`

### Task 2: MkDocs SEO + theme upgrade

**Files:**
- Modify: `mkdocs.yml` (full replacement below)

- [ ] **Step 1: Replace mkdocs.yml**

```yaml
site_name: Open Source Radar AI
site_description: AI-curated GitHub trending repositories with developer-focused insights, updated weekly.
site_url: https://lokeshnanda.github.io/oss-radar-ai/
repo_url: https://github.com/LokeshNanda/oss-radar-ai
repo_name: LokeshNanda/oss-radar-ai

theme:
  name: material
  palette:
    - media: "(prefers-color-scheme: light)"
      scheme: default
      primary: indigo
      toggle:
        icon: material/weather-night
        name: Switch to dark mode
    - media: "(prefers-color-scheme: dark)"
      scheme: slate
      primary: indigo
      toggle:
        icon: material/weather-sunny
        name: Switch to light mode
  features:
    - navigation.instant
    - navigation.tracking
    - navigation.top
    - search.suggest
    - toc.follow

plugins:
  - search

markdown_extensions:
  - admonition
  - pymdownx.details
  - attr_list

nav:
  - Home: index.md
  - Past weeks: archive.md
```

- [ ] **Step 2: Verify** — `mkdocs build --strict` passes; `site/sitemap.xml` contains absolute `https://lokeshnanda.github.io/oss-radar-ai/` URLs.

- [ ] **Step 3: Commit** — `git commit -m "feat: mkdocs SEO metadata, dark mode, sitemap"`

### Task 3: README overhaul

**Files:**
- Modify: `README.md` (full replacement)

- [ ] **Step 1: Write new README** with: one-line pitch; live-site link + badges (workflow status `…/actions/workflows/trending.yml/badge.svg`, MIT license shield, "Live site" shield); a `## 📡 This week's radar` section wrapped in `<!-- RADAR:START -->` / `<!-- RADAR:END -->` markers (seeded with the current week's top-10 list from `docs/index.md`, so Phase 2 automation has markers to replace); "How it works" mermaid flowchart (GitHub API → dedupe → LLM analysis → MkDocs → Pages); features list; "Run your own radar" teaser linking to the (Phase 3) guide; local development section (venv, `pip install -e ".[dev]"`, `radar-run`, env vars table); links to ROADMAP.md and spec.

- [ ] **Step 2: Verify** markers present exactly once each: `grep -c "RADAR:START" README.md` → 1.

- [ ] **Step 3: Commit** — `git commit -m "docs: README overhaul with badges, radar section markers, how-it-works"`

### Task 4: GitHub repo metadata (topics + homepage)

**Files:** none (GitHub API / settings change)

- [ ] **Step 1:** If a `GITHUB_TOKEN` with repo scope is available in `.env`, run:
  - `PATCH /repos/LokeshNanda/oss-radar-ai` body `{"homepage": "https://lokeshnanda.github.io/oss-radar-ai/"}`
  - `PUT /repos/LokeshNanda/oss-radar-ai/topics` body `{"names": ["github-trending","llm","ai","open-source","mkdocs","github-actions","developer-tools","trending-repositories"]}`

- [ ] **Step 2:** Verify via `GET /repos/LokeshNanda/oss-radar-ai` (homepage + topics populated). If no token available, output the exact manual steps (Settings → About → website + topics) in the final report instead.

---

# PHASE 1 — Content quality

### Task 5: README fetching in GitHubClient

**Files:**
- Modify: `src/open_source_radar_ai/github_client.py`
- Test: `tests/test_github_client.py`

**Interfaces:**
- Produces: `GitHubClient.get_repository_readme(full_name: str, *, max_chars: int = 16000) -> str | None` (None on any failure/404/empty; truncated to max_chars). `GitHubClient.get_repository_by_id(repo_id: int) -> Repository | None` (used by Task 10).
- Produces: `fetch_trending_repositories(config, *, exclude_ids=None, client: GitHubClient | None = None)` — optional shared client.

- [ ] **Step 1: Write failing tests** (fake session pattern used by all client tests)

```python
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
        github=GitHubConfig(token=None, api_base_url="https://api.github.com", per_page=10, days_back=7),
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
        "id": 42, "name": "repo", "full_name": "owner/repo",
        "html_url": "https://github.com/owner/repo", "description": "d",
        "stargazers_count": 5, "language": "Python", "topics": [],
        "created_at": "2026-07-01T00:00:00Z", "updated_at": "2026-07-02T00:00:00Z",
        "owner": {"login": "owner"},
    }
    client = make_client(FakeResponse(200, json_data=payload))
    repo = client.get_repository_by_id(42)
    assert repo is not None and repo.stargazers_count == 5
```

- [ ] **Step 2: Run to verify failure** — `python -m pytest tests/test_github_client.py -q` → AttributeError.

- [ ] **Step 3: Implement** in `github_client.py` (add `Optional` import):

```python
    def get_repository_readme(self, full_name: str, *, max_chars: int = 16000) -> Optional[str]:
        """Fetch a repository's README as raw text; None on any failure."""
        url = f"{self.github_config.api_base_url}/repos/{full_name}/readme"
        try:
            response = self._session.get(
                url, headers={"Accept": "application/vnd.github.raw+json"}, timeout=30
            )
        except requests.RequestException as exc:
            LOGGER.warning("README fetch failed for %s: %s", full_name, exc)
            return None
        if response.status_code >= 400:
            LOGGER.info("No README for %s (status %d).", full_name, response.status_code)
            return None
        text = response.text.strip()
        if not text:
            return None
        return text[:max_chars]

    def get_repository_by_id(self, repo_id: int) -> Optional[Repository]:
        """Fetch a repository by numeric ID; None on any failure."""
        url = f"{self.github_config.api_base_url}/repositories/{repo_id}"
        try:
            response = self._session.get(url, timeout=30)
        except requests.RequestException as exc:
            LOGGER.warning("Repo fetch failed for id=%d: %s", repo_id, exc)
            return None
        if response.status_code >= 400:
            LOGGER.info("Repo id=%d unavailable (status %d).", repo_id, response.status_code)
            return None
        try:
            return Repository.from_api_response(response.json())
        except (KeyError, ValueError, TypeError) as exc:
            LOGGER.warning("Malformed repo payload for id=%d: %s", repo_id, exc)
            return None
```

Also modify `fetch.py:fetch_trending_repositories` signature to `(config, *, exclude_ids=None, client: GitHubClient | None = None)` and use `client = client or GitHubClient(config)`.

- [ ] **Step 4: Run tests** — all pass.
- [ ] **Step 5: Commit** — `git commit -m "feat: fetch repo READMEs and repos by id from GitHub API"`

### Task 6: Structured README-aware analysis (RepoAnalysis + JSON mode)

**Files:**
- Modify: `src/open_source_radar_ai/models.py`, `prompts.py`, `openai_client.py`, `summarize.py`
- Test: `tests/test_summarize.py`

**Interfaces:**
- Produces: `models.CATEGORIES: tuple[str, ...]` = `("AI & Agents", "Developer Tools", "Web & Frontend", "Data & Analytics", "Infrastructure & DevOps", "Security", "Languages & Runtimes", "Other")`.
- Produces: `models.RepoAnalysis` frozen dataclass with `markdown: str`, `category: str`.
- Produces: `summarize_repository(repo, *, client, readme_excerpt: str | None = None) -> RepoAnalysis`.
- Produces: `OpenAIClient.chat_completion(*, system, user, response_format: dict | None = None) -> str`.

- [ ] **Step 1: Failing tests**

```python
"""Tests for structured summarization."""
import json
import pytest
from datetime import datetime, timezone
from open_source_radar_ai.models import Repository, RepoAnalysis, CATEGORIES
from open_source_radar_ai.summarize import SummarizationError, summarize_repository


def make_repo() -> Repository:
    now = datetime(2026, 7, 20, tzinfo=timezone.utc)
    return Repository(
        id=1, name="r", full_name="o/r", html_url="https://github.com/o/r",
        description="desc", stargazers_count=100, language="Rust", topics=["cli"],
        created_at=now, updated_at=now, owner_login="o",
    )


class FakeLLM:
    def __init__(self, content):
        self.content = content
        self.last_user = None

    def chat_completion(self, *, system, user, response_format=None):
        self.last_user = user
        return self.content


def test_returns_analysis_with_valid_category():
    payload = json.dumps({"category": "Developer Tools", "analysis_markdown": "## What it does\nStuff."})
    result = summarize_repository(make_repo(), client=FakeLLM(payload))
    assert isinstance(result, RepoAnalysis)
    assert result.category == "Developer Tools"
    assert "What it does" in result.markdown


def test_invalid_category_falls_back_to_other():
    payload = json.dumps({"category": "Bananas", "analysis_markdown": "## What it does\nStuff."})
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
```

- [ ] **Step 2: Verify failure** — ImportError on `RepoAnalysis`.

- [ ] **Step 3: Implement.**

`models.py` — append:

```python
CATEGORIES: tuple = (
    "AI & Agents",
    "Developer Tools",
    "Web & Frontend",
    "Data & Analytics",
    "Infrastructure & DevOps",
    "Security",
    "Languages & Runtimes",
    "Other",
)


@dataclass(frozen=True)
class RepoAnalysis:
    """Structured LLM analysis of a repository."""

    markdown: str
    category: str
```

`prompts.py` — full replacement:

```python
"""Prompt templates for LLM summarization."""

from __future__ import annotations

from .models import CATEGORIES, Repository


SYSTEM_PROMPT = """You write sharp, honest breakdowns of GitHub repositories for busy developers.
Be concrete and specific. No marketing tone, no hype, no filler.
When the README does not support a claim, say what is uncertain instead of guessing."""


def build_repository_prompt(repo: Repository, readme_excerpt: str | None = None) -> str:
    """Build a structured prompt for a repository analysis."""
    topics = ", ".join(repo.topics) if repo.topics else "None"
    description = repo.description or "No description provided."
    language = repo.language or "Unknown"
    categories = ", ".join(f'"{c}"' for c in CATEGORIES)

    readme_block = ""
    if readme_excerpt:
        readme_block = f"""
README (may be truncated):
<readme>
{readme_excerpt}
</readme>
"""

    return f"""Analyze this GitHub repository for a developer audience.

Repository metadata:
- Name: {repo.full_name}
- URL: {repo.html_url}
- Description: {description}
- Primary language: {language}
- Topics: {topics}
- Stars: {repo.stargazers_count}
- Created at: {repo.created_at.date().isoformat()}
{readme_block}
Respond with a single JSON object with exactly these keys:
- "category": one of [{categories}]
- "analysis_markdown": a markdown string using these headings exactly:

## What it does
(2-3 sentences, concrete)

## Why it's interesting
(what makes it different from the obvious alternatives)

## How it works
(architecture/approach, grounded in the README; note uncertainty where it exists)

## Get started in 5 minutes
(the shortest realistic path to trying it, from the README)

## Watch out for
(maturity, gaps, caveats, licensing or security concerns)

Constraints:
- Ground every claim in the metadata or README; never invent features.
- Prefer specific, testable statements over vague ones.
"""


__all__ = ["SYSTEM_PROMPT", "build_repository_prompt"]
```

`openai_client.py` — change `chat_completion` signature to `def chat_completion(self, *, system: str, user: str, response_format: Optional[Dict[str, Any]] = None) -> str:` and after building `payload`, add:

```python
        if response_format is not None:
            payload["response_format"] = response_format
```

Also bump default `OPENAI_MAX_TOKENS` fallback from `900` to `1400` (README-aware analyses are longer).

`summarize.py` — full replacement:

```python
"""LLM summarization layer."""

from __future__ import annotations

import json
import logging

from .models import CATEGORIES, RepoAnalysis, Repository
from .openai_client import OpenAIClient, OpenAIConfig, load_openai_config
from .prompts import SYSTEM_PROMPT, build_repository_prompt


LOGGER = logging.getLogger(__name__)


class SummarizationError(RuntimeError):
    """Raised when summarization fails."""


def summarize_repository(
    repo: Repository,
    *,
    client: OpenAIClient,
    readme_excerpt: str | None = None,
) -> RepoAnalysis:
    """Generate a structured analysis (markdown + category) for a repository."""
    prompt = build_repository_prompt(repo, readme_excerpt=readme_excerpt)
    try:
        raw = client.chat_completion(
            system=SYSTEM_PROMPT,
            user=prompt,
            response_format={"type": "json_object"},
        )
    except Exception as exc:  # noqa: BLE001
        raise SummarizationError(f"Failed to summarize {repo.full_name}: {exc}") from exc

    try:
        data = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise SummarizationError(
            f"Non-JSON analysis for {repo.full_name}: {raw[:200]}"
        ) from exc

    markdown = data.get("analysis_markdown")
    if not isinstance(markdown, str) or not markdown.strip():
        raise SummarizationError(f"Empty analysis for {repo.full_name}.")

    category = data.get("category")
    if category not in CATEGORIES:
        LOGGER.warning(
            "Invalid category %r for %s; falling back to 'Other'.", category, repo.full_name
        )
        category = "Other"

    return RepoAnalysis(markdown=markdown.strip(), category=category)


def build_default_client() -> OpenAIClient:
    """Build a default OpenAI client from environment configuration."""
    cfg: OpenAIConfig = load_openai_config()
    return OpenAIClient(cfg)


__all__ = ["SummarizationError", "summarize_repository", "build_default_client"]
```

- [ ] **Step 4: Run tests** — all pass (note: `pipeline.py` still passes `analysis` as str; it breaks type-wise but isn't executed by tests — fixed in Task 8).
- [ ] **Step 5: Commit** — `git commit -m "feat: README-aware structured analysis with category (JSON mode)"`

### Task 7: Catalog state module

**Files:**
- Create: `src/open_source_radar_ai/catalog.py`
- Test: `tests/test_catalog.py`

**Interfaces:**
- Produces: `CatalogEntry` frozen dataclass: `id: int, full_name: str, html_url: str, description: str | None, language: str | None, category: str, stars_at_feature: int, date_featured: str (ISO), page: str (docs-relative posix, e.g. "repos/o--r.md")`.
- Produces: `load_catalog(path=None) -> list[CatalogEntry]`, `save_catalog(entries, path=None) -> bool`, `upsert_entries(existing, new) -> list[CatalogEntry]` (dedupe by id, new wins; sorted by `date_featured` desc then stars desc).
- State file: `.radar_state/catalog.json` → `{"repos": [entry-dicts]}` (respects `RADAR_STATE_DIR`).

- [ ] **Step 1: Failing tests**

```python
"""Tests for the repository catalog."""
from pathlib import Path
from open_source_radar_ai.catalog import CatalogEntry, load_catalog, save_catalog, upsert_entries


def entry(id=1, date="2026-07-20", stars=10, category="Other") -> CatalogEntry:
    return CatalogEntry(
        id=id, full_name=f"o/r{id}", html_url=f"https://github.com/o/r{id}",
        description="d", language="Python", category=category,
        stars_at_feature=stars, date_featured=date, page=f"repos/o--r{id}.md",
    )


def test_roundtrip(tmp_path: Path):
    path = tmp_path / "catalog.json"
    save_catalog([entry(1), entry(2)], path=path)
    loaded = load_catalog(path=path)
    assert [e.id for e in loaded] == [1, 2]
    assert loaded[0] == entry(1)


def test_load_missing_returns_empty(tmp_path: Path):
    assert load_catalog(path=tmp_path / "nope.json") == []


def test_upsert_dedupes_and_sorts():
    old = [entry(1, date="2026-07-13", stars=5)]
    new = [entry(1, date="2026-07-13", stars=7), entry(2, date="2026-07-20", stars=1)]
    merged = upsert_entries(old, new)
    assert len(merged) == 2
    assert merged[0].id == 2  # newest date first
    assert merged[1].stars_at_feature == 7  # new wins
```

- [ ] **Step 2: Verify failure** — ModuleNotFoundError.

- [ ] **Step 3: Implement `catalog.py`**

```python
"""Persistent catalog of all featured repositories."""

from __future__ import annotations

from dataclasses import asdict, dataclass
import os
from pathlib import Path
from typing import Iterable, List, Optional

from .io_utils import atomic_write_json_if_changed, ensure_dir, read_json_file


@dataclass(frozen=True)
class CatalogEntry:
    """One featured repository in the site catalog."""

    id: int
    full_name: str
    html_url: str
    description: Optional[str]
    language: Optional[str]
    category: str
    stars_at_feature: int
    date_featured: str
    page: str


def _default_path() -> Path:
    return Path(os.getenv("RADAR_STATE_DIR", ".radar_state")) / "catalog.json"


def load_catalog(path: Path | None = None) -> List[CatalogEntry]:
    """Load the catalog; missing file means empty catalog."""
    data = read_json_file(path or _default_path())
    return [CatalogEntry(**item) for item in data.get("repos") or []]


def save_catalog(entries: Iterable[CatalogEntry], path: Path | None = None) -> bool:
    """Persist the catalog deterministically (sorted newest first)."""
    resolved = path or _default_path()
    ensure_dir(resolved.parent)
    ordered = sorted(entries, key=lambda e: (e.date_featured, e.stars_at_feature), reverse=True)
    return atomic_write_json_if_changed(resolved, {"repos": [asdict(e) for e in ordered]})


def upsert_entries(
    existing: Iterable[CatalogEntry], new: Iterable[CatalogEntry]
) -> List[CatalogEntry]:
    """Merge entries by repo id; new entries win. Sorted newest first."""
    merged = {e.id: e for e in existing}
    for e in new:
        merged[e.id] = e
    return sorted(merged.values(), key=lambda e: (e.date_featured, e.stars_at_feature), reverse=True)


__all__ = ["CatalogEntry", "load_catalog", "save_catalog", "upsert_entries"]
```

- [ ] **Step 4: Run tests** — pass.
- [ ] **Step 5: Commit** — `git commit -m "feat: persistent catalog of featured repositories"`

### Task 8: Pipeline integration (README → analysis → category on pages → catalog)

**Files:**
- Modify: `src/open_source_radar_ai/pipeline.py`, `generator.py` (`render_repo_page`/`write_repo_page`)
- Test: `tests/test_generator.py`, `tests/test_pipeline.py`

**Interfaces:**
- Consumes: Task 5 `get_repository_readme` + `fetch(client=...)`, Task 6 `RepoAnalysis`, Task 7 catalog API.
- Produces: `render_repo_page(repo, analysis_markdown, *, category: str | None = None)` — frontmatter gains `category:` line and meta gains `- **Category**:` when provided. `write_repo_page(repo, *, analysis_markdown, docs_dir, category=None)`.
- Produces: pipeline env `RADAR_README_MAX_CHARS` (default 16000).

- [ ] **Step 1: Failing tests**

`tests/test_generator.py`:

```python
"""Tests for markdown generation."""
from datetime import datetime, timezone
from open_source_radar_ai.generator import render_repo_page
from open_source_radar_ai.models import Repository


def make_repo() -> Repository:
    now = datetime(2026, 7, 20, tzinfo=timezone.utc)
    return Repository(
        id=1, name="r", full_name="o/r", html_url="https://github.com/o/r",
        description="d", stargazers_count=10, language="Go", topics=[],
        created_at=now, updated_at=now, owner_login="o",
    )


def test_render_repo_page_with_category():
    page = render_repo_page(make_repo(), "## What it does\nx", category="Developer Tools")
    assert "category: Developer Tools" in page
    assert "- **Category**: Developer Tools" in page


def test_render_repo_page_without_category_unchanged():
    page = render_repo_page(make_repo(), "body")
    assert "category:" not in page
```

`tests/test_pipeline.py` (monkeypatch everything external; run into tmp dirs):

```python
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
        id=i, name=f"r{i}", full_name=f"o/r{i}", html_url=f"https://github.com/o/r{i}",
        description="d", stargazers_count=100 - i, language="Python", topics=[],
        created_at=now, updated_at=now, owner_login="o",
    )


def test_pipeline_writes_pages_and_catalog(tmp_path: Path, monkeypatch):
    docs = tmp_path / "docs"
    state = tmp_path / "state"
    monkeypatch.setenv("RADAR_DOCS_DIR", str(docs))
    monkeypatch.setenv("RADAR_STATE_DIR", str(state))
    monkeypatch.setenv("RADAR_REFERENCE_DATE", "2026-07-20")

    monkeypatch.setattr(
        pipeline_mod, "fetch_trending_repositories",
        lambda cfg, *, exclude_ids=None, client=None: [make_repo(1), make_repo(2)],
    )
    monkeypatch.setattr(pipeline_mod, "build_default_client", lambda: object())
    monkeypatch.setattr(
        pipeline_mod, "summarize_repository",
        lambda repo, *, client, readme_excerpt=None: RepoAnalysis(
            markdown="## What it does\nx", category="Developer Tools"
        ),
    )

    class FakeGitHubClient:
        def __init__(self, cfg):
            pass

        def get_repository_readme(self, full_name, *, max_chars=16000):
            return "readme text"

    monkeypatch.setattr(pipeline_mod, "GitHubClient", FakeGitHubClient)

    result = pipeline_mod.run_pipeline()
    assert result.summarized == 2
    assert (docs / "repos" / "o--r1.md").exists()
    assert "category: Developer Tools" in (docs / "repos" / "o--r1.md").read_text(encoding="utf-8")
    entries = load_catalog(path=state / "catalog.json")
    assert {e.id for e in entries} == {1, 2}
    ids = json.loads((state / "processed_repos.json").read_text())["processed_repo_ids"]
    assert ids == [1, 2]
```

- [ ] **Step 2: Verify failure.**

- [ ] **Step 3: Implement.**

`generator.py` — new `render_repo_page`:

```python
def render_repo_page(
    repo: Repository, analysis_markdown: str, *, category: str | None = None
) -> str:
    """Render a repository report page."""
    category_fm = f"category: {category}\n" if category else ""
    frontmatter = (
        "---\n"
        f"title: {repo.full_name}\n"
        f"source: {repo.html_url}\n"
        f"stars: {repo.stargazers_count}\n"
        f"{category_fm}"
        "---\n\n"
    )
    header = f"# {repo.full_name}\n\n"
    category_line = f"- **Category**: {category}\n" if category else ""
    meta = (
        f"- **URL**: {repo.html_url}\n"
        f"- **Stars**: {repo.stargazers_count}\n"
        f"- **Language**: {repo.language or 'Unknown'}\n"
        f"{category_line}"
        f"- **Topics**: {', '.join(repo.topics) if repo.topics else 'None'}\n\n"
    )
    body = analysis_markdown.strip() + "\n"
    return frontmatter + header + meta + body
```

`write_repo_page` gains `category: str | None = None` and forwards it.

`pipeline.py` — inside `run_pipeline`: import `GitHubClient` from `.github_client`, `CatalogEntry/load_catalog/save_catalog/upsert_entries` from `.catalog`. Build `gh_client = GitHubClient(cfg)` once, pass to `fetch_trending_repositories(cfg, exclude_ids=..., client=gh_client)`. Per repo:

```python
    readme_max = int(os.getenv("RADAR_README_MAX_CHARS", "16000"))
    new_entries: List[CatalogEntry] = []
    for repo in repos:
        readme_excerpt = gh_client.get_repository_readme(repo.full_name, max_chars=readme_max)
        try:
            analysis = summarize_repository(repo, client=client, readme_excerpt=readme_excerpt)
        except SummarizationError as exc:
            LOGGER.error("%s", exc)
            continue
        if write_repo_page(
            repo, analysis_markdown=analysis.markdown, docs_dir=docs_dir, category=analysis.category
        ):
            pages_written += 1
        summarized.append(repo)
        page_rel = repo_markdown_path(repo, docs_dir=docs_dir).relative_to(docs_dir).as_posix()
        new_entries.append(
            CatalogEntry(
                id=repo.id, full_name=repo.full_name, html_url=repo.html_url,
                description=repo.description, language=repo.language,
                category=analysis.category, stars_at_feature=repo.stargazers_count,
                date_featured=cfg.reference_date.isoformat(), page=page_rel,
            )
        )
```

After the loop (before dedupe-state save): `save_catalog(upsert_entries(load_catalog(), new_entries))`. Import `repo_markdown_path` from `.generator`.

- [ ] **Step 4: Run full suite** — `python -m pytest tests -q` all pass; `mkdocs build --strict` passes.
- [ ] **Step 5: Commit** — `git commit -m "feat: wire README-aware analysis, categories and catalog into pipeline"`

### Task 9: Category index pages

**Files:**
- Create: `src/open_source_radar_ai/category_pages.py`
- Modify: `src/open_source_radar_ai/pipeline.py` (call it), `mkdocs.yml` (nav)
- Test: `tests/test_category_pages.py`

**Interfaces:**
- Consumes: `catalog.CatalogEntry`, `generator._slugify`.
- Produces: `write_category_pages(entries: list[CatalogEntry], *, docs_dir: Path) -> int` (pages written). Writes `docs/categories/index.md` (counts per category) and `docs/categories/<slug>.md` per non-empty category (each repo: link to `../{entry.page}`, description, stars, week featured).

- [ ] **Step 1: Failing test**

```python
"""Tests for category index pages."""
from pathlib import Path
from open_source_radar_ai.catalog import CatalogEntry
from open_source_radar_ai.category_pages import write_category_pages


def entry(id, category) -> CatalogEntry:
    return CatalogEntry(
        id=id, full_name=f"o/r{id}", html_url=f"https://github.com/o/r{id}",
        description="d", language="Python", category=category,
        stars_at_feature=10, date_featured="2026-07-20", page=f"repos/o--r{id}.md",
    )


def test_writes_index_and_category_pages(tmp_path: Path):
    docs = tmp_path / "docs"
    written = write_category_pages([entry(1, "AI & Agents"), entry(2, "Security")], docs_dir=docs)
    assert written == 3  # index + 2 categories
    index = (docs / "categories" / "index.md").read_text(encoding="utf-8")
    assert "AI & Agents" in index and "Security" in index
    ai = (docs / "categories" / "ai-agents.md").read_text(encoding="utf-8")
    assert "[`o/r1`](../repos/o--r1.md)" in ai


def test_empty_catalog_writes_only_index(tmp_path: Path):
    assert write_category_pages([], docs_dir=tmp_path / "docs") == 1
```

- [ ] **Step 2: Verify failure.**

- [ ] **Step 3: Implement `category_pages.py`**

```python
"""Category index page generation."""

from __future__ import annotations

from collections import defaultdict
from pathlib import Path
from typing import Dict, Iterable, List

from .catalog import CatalogEntry
from .generator import _slugify
from .io_utils import atomic_write_text_if_changed, ensure_dir
from .models import CATEGORIES


def write_category_pages(entries: Iterable[CatalogEntry], *, docs_dir: Path) -> int:
    """Write categories/index.md plus one page per non-empty category."""
    by_category: Dict[str, List[CatalogEntry]] = defaultdict(list)
    for entry in entries:
        by_category[entry.category].append(entry)

    cat_dir = docs_dir / "categories"
    ensure_dir(cat_dir)
    written = 0

    index_lines = [
        "---", "title: Categories", "---", "",
        "# Categories", "",
        "Featured repositories grouped by category.", "",
    ]
    for category in CATEGORIES:
        repos = by_category.get(category) or []
        if not repos:
            continue
        slug = _slugify(category)
        index_lines.append(f"- [{category}]({slug}.md) — {len(repos)} repos")

        lines = [
            "---", f"title: {category}", "---", "",
            f"# {category}", "",
        ]
        for e in sorted(repos, key=lambda x: (x.date_featured, x.stars_at_feature), reverse=True):
            desc = f" — {e.description.strip()}" if e.description else ""
            lines.append(
                f"- [`{e.full_name}`](../{e.page}){desc} (⭐ {e.stars_at_feature}, week of {e.date_featured})"
            )
        lines.extend(["", "[← All categories](index.md)", ""])
        if atomic_write_text_if_changed(cat_dir / f"{slug}.md", "\n".join(lines)):
            written += 1

    index_lines.append("")
    if atomic_write_text_if_changed(cat_dir / "index.md", "\n".join(index_lines)):
        written += 1
    return written


__all__ = ["write_category_pages"]
```

Pipeline: after saving catalog, `write_category_pages(full_catalog, docs_dir=docs_dir)` (where `full_catalog` is the upserted list). mkdocs.yml nav gains `- Categories: categories/index.md` after Home.

- [ ] **Step 4: Run tests + `mkdocs build --strict`** (needs `docs/categories/index.md` to exist for nav — run a minimal generation or create via pipeline test artifacts; simplest: run `python -c "from open_source_radar_ai.category_pages import write_category_pages; from open_source_radar_ai.catalog import load_catalog; from pathlib import Path; write_category_pages(load_catalog(), docs_dir=Path('docs'))"`).
- [ ] **Step 5: Commit** — `git commit -m "feat: per-category index pages"`

### Task 10: Star history + weekly velocity/risers

**Files:**
- Create: `src/open_source_radar_ai/stars.py`
- Modify: `src/open_source_radar_ai/pipeline.py`, `generator.py` (weekly report)
- Test: `tests/test_stars.py`

**Interfaces:**
- Consumes: `GitHubClient.get_repository_by_id` (Task 5), catalog (ordering for refresh priority).
- Produces (in `stars.py`): `load_star_history(path=None) -> dict`, `save_star_history(history, path=None) -> bool` (file `.radar_state/star_history.json`, shape `{"<id>": {"full_name": str, "html_url": str, "snapshots": {"YYYY-MM-DD": int}}}`); `record_snapshot(history, repo, on_date: date) -> None` (mutates dict); `compute_risers(history, *, limit=5) -> list[dict]` — for entries with >= 2 snapshots, delta = latest - previous snapshot value, returns `[{"full_name", "html_url", "delta", "stars"}]` sorted by delta desc, positive deltas only.
- Produces: `render_weekly_report_page(..., risers: list[dict] | None = None)` — appends a `## 📈 Biggest risers` section when risers non-empty; repo lines gain `⭐ N (≈M/day)` where `M = round(stars / max(1, (generated_on - created_at.date()).days), 1)`.
- Env: `RADAR_STAR_REFRESH_LIMIT` (default 50) — max previously-tracked repos re-fetched per run, most recently featured first.

- [ ] **Step 1: Failing tests**

```python
"""Tests for star history tracking."""
from datetime import date, datetime, timezone
from pathlib import Path
from open_source_radar_ai.models import Repository
from open_source_radar_ai.stars import (
    compute_risers, load_star_history, record_snapshot, save_star_history,
)


def make_repo(i=1, stars=100) -> Repository:
    now = datetime(2026, 7, 14, tzinfo=timezone.utc)
    return Repository(
        id=i, name=f"r{i}", full_name=f"o/r{i}", html_url=f"https://github.com/o/r{i}",
        description=None, stargazers_count=stars, language=None, topics=[],
        created_at=now, updated_at=now, owner_login="o",
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
```

- [ ] **Step 2: Verify failure.**

- [ ] **Step 3: Implement `stars.py`**

```python
"""Star-count history tracking for featured repositories."""

from __future__ import annotations

from datetime import date
import os
from pathlib import Path
from typing import Any, Dict, List

from .io_utils import atomic_write_json_if_changed, ensure_dir, read_json_file
from .models import Repository


def _default_path() -> Path:
    return Path(os.getenv("RADAR_STATE_DIR", ".radar_state")) / "star_history.json"


def load_star_history(path: Path | None = None) -> Dict[str, Any]:
    """Load star history; missing file means empty history."""
    return read_json_file(path or _default_path())


def save_star_history(history: Dict[str, Any], path: Path | None = None) -> bool:
    """Persist star history deterministically."""
    resolved = path or _default_path()
    ensure_dir(resolved.parent)
    return atomic_write_json_if_changed(resolved, history)


def record_snapshot(history: Dict[str, Any], repo: Repository, on_date: date) -> None:
    """Record a star-count snapshot for a repository (mutates history)."""
    key = str(repo.id)
    entry = history.setdefault(
        key, {"full_name": repo.full_name, "html_url": repo.html_url, "snapshots": {}}
    )
    entry["full_name"] = repo.full_name
    entry["html_url"] = repo.html_url
    entry["snapshots"][on_date.isoformat()] = repo.stargazers_count


def compute_risers(history: Dict[str, Any], *, limit: int = 5) -> List[Dict[str, Any]]:
    """Top repositories by star gain between their two most recent snapshots."""
    risers: List[Dict[str, Any]] = []
    for entry in history.values():
        snapshots = entry.get("snapshots") or {}
        if len(snapshots) < 2:
            continue
        dates = sorted(snapshots)
        delta = snapshots[dates[-1]] - snapshots[dates[-2]]
        if delta <= 0:
            continue
        risers.append(
            {
                "full_name": entry["full_name"],
                "html_url": entry["html_url"],
                "delta": delta,
                "stars": snapshots[dates[-1]],
            }
        )
    risers.sort(key=lambda r: -r["delta"])
    return risers[:limit]


__all__ = ["load_star_history", "save_star_history", "record_snapshot", "compute_risers"]
```

`generator.py` — `render_weekly_report_page` and `write_weekly_report_page` gain `risers: list | None = None`. Repo line becomes:

```python
    for repo in repo_list:
        rel_path = repo_markdown_path(repo, docs_dir=docs_dir).relative_to(docs_dir)
        repo_link = "../" + rel_path.as_posix()
        desc = (repo.description or "").strip()
        suffix = f" — {desc}" if desc else ""
        age_days = max(1, (generated_on - repo.created_at.date()).days)
        velocity = round(repo.stargazers_count / age_days, 1)
        lines.append(
            f"- [`{repo.full_name}`]({repo_link}){suffix} (⭐ {repo.stargazers_count}, ≈{velocity}/day)"
        )
```

and before the footer:

```python
    if risers:
        lines.extend(["", "## 📈 Biggest risers", "", "Previously featured repos still gaining stars:", ""])
        for r in risers:
            lines.append(f"- [`{r['full_name']}`]({r['html_url']}) — +{r['delta']} stars (now ⭐ {r['stars']})")
```

`pipeline.py` — after summarization loop:

```python
    history = load_star_history()
    for repo in summarized:
        record_snapshot(history, repo, cfg.reference_date)
    refresh_limit = int(os.getenv("RADAR_STAR_REFRESH_LIMIT", "50"))
    current_ids = {repo.id for repo in summarized}
    tracked_ids = [
        e.id for e in full_catalog if e.id not in current_ids
    ][:refresh_limit]
    for repo_id in tracked_ids:
        refreshed = gh_client.get_repository_by_id(repo_id)
        if refreshed is not None:
            record_snapshot(history, refreshed, cfg.reference_date)
    save_star_history(history)
    risers = compute_risers(history)
```

Pass `risers=risers` into `write_weekly_report_page`. (`full_catalog` is sorted newest-featured first from Task 8.)

- [ ] **Step 4: Run full suite** — pass.
- [ ] **Step 5: Commit** — `git commit -m "feat: star history tracking, velocity and biggest-risers in weekly report"`

### Task 11: Backfill CLI (`radar-backfill`)

**Files:**
- Create: `src/open_source_radar_ai/backfill.py`
- Modify: `pyproject.toml` (script entry), `src/open_source_radar_ai/cli.py`
- Test: `tests/test_backfill.py`

**Interfaces:**
- Produces: `parse_repo_page(path: Path) -> dict | None` — parses frontmatter (`title`, `source`, `stars`, optional `category`) from a `docs/repos/*.md` page; returns None if malformed.
- Produces: `build_report_date_map(docs_dir: Path) -> dict[str, str]` — scans `docs/reports/*.md` for `(../repos/<file>.md)` links → `{page_filename: report_date}`.
- Produces: `run_backfill(docs_dir: Path, *, categorize: bool) -> int` — populates catalog entries for pages missing from catalog (`date_featured` from report map, fallback `"2026-01-01"`; `id` = negative sequential ids `-1, -2, ...` for pages whose numeric GitHub id is unknown — catalog upsert keys on id so negatives never collide with real ones); when `categorize=True`, asks the LLM for category-only JSON per page (prompt: metadata + first 2000 chars of existing analysis; response `{"category": ...}`), else `"Other"`. Rewrites each page's frontmatter to include the category.
- CLI: `radar-backfill` → `main_backfill(argv)`; flag `--no-llm` sets `categorize=False`.

- [ ] **Step 1: Failing tests** (fixture page + report in tmp docs dir; fake LLM client monkeypatched into `backfill.build_default_client`; asserts catalog populated, category written back into frontmatter, report-date mapping used)

```python
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
    assert "category: Developer Tools" in (docs / "repos" / "o--r1.md").read_text(encoding="utf-8")


def test_backfill_skips_pages_already_in_catalog(tmp_path: Path, monkeypatch):
    docs = setup_docs(tmp_path)
    monkeypatch.setenv("RADAR_STATE_DIR", str(tmp_path / "state"))
    monkeypatch.setattr(backfill_mod, "build_default_client", lambda: FakeLLM())
    assert backfill_mod.run_backfill(docs, categorize=True) == 1
    assert backfill_mod.run_backfill(docs, categorize=True) == 0
```

- [ ] **Step 2: Verify failure.**

- [ ] **Step 3: Implement `backfill.py`** — frontmatter parse via simple `---` block splitting and `key: value` lines; catalog match by `full_name` (existing entries) to decide skip; negative ids assigned as `-(index+1)` offset below current min; category prompt:

```python
CATEGORY_PROMPT = """Classify this GitHub repository into exactly one category.
Categories: {categories}
Repository: {full_name}
Existing analysis (may be truncated):
{excerpt}

Respond with JSON: {{"category": "<one of the categories>"}}"""
```

`main_backfill` in `cli.py` mirrors `main_run` (configure logging, parse `--no-llm`, call `run_backfill(Path(os.getenv("RADAR_DOCS_DIR", "docs")), categorize=...)`, log count, return 0/1). Add `radar-backfill = "open_source_radar_ai.cli:main_backfill"` to `[project.scripts]`; `pip install -e ".[dev]"` to refresh entry points.

- [ ] **Step 4: Run tests** — pass.
- [ ] **Step 5: Run the real backfill** — requires `OPENAI_API_KEY` in `.env`; run `radar-backfill` (cost ≈ $0.05 for ~230 pages with gpt-4o-mini). If no key available locally, run `radar-backfill --no-llm` so pages/catalog gain dates now and categories default to Other (re-runnable later). Then regenerate category pages (same command as Task 9 Step 4) and `mkdocs build --strict`.
- [ ] **Step 6: Commit** — `git commit -m "feat: radar-backfill CLI to catalog and categorize historical pages"`

---

# PHASE 2 — Zero-manual distribution

### Task 12: RSS + JSON feeds

**Files:**
- Create: `src/open_source_radar_ai/feeds.py`
- Modify: `src/open_source_radar_ai/pipeline.py`, `generator.py` (index page footer), `README.md` (feed links)
- Test: `tests/test_feeds.py`

**Interfaces:**
- Consumes: catalog entries; `list_existing_reports(docs_dir)`.
- Produces: `write_feeds(entries: list[CatalogEntry], *, docs_dir: Path, site_url: str) -> None` writing:
  - `docs/feed.xml` — RSS 2.0; one `<item>` per distinct `date_featured` week (up to 12 newest): title `Open Source Radar — Week of <date>`, link `{site_url}reports/<date>/`, guid = link, description = HTML-escaped `<li>` list of that week's `full_name — description`. `pubDate` in RFC 822 (`email.utils.format_datetime(datetime(y,m,d, tzinfo=timezone.utc))`). No build timestamps (determinism).
  - `docs/api/latest.json` — `{"generated_on": <newest date>, "repos": [entry dicts for newest week]}`.
  - `docs/api/catalog.json` — `{"repos": [all entry dicts]}`.
- Env: `RADAR_SITE_URL` (default `https://lokeshnanda.github.io/oss-radar-ai/`), read in pipeline.

- [ ] **Step 1: Failing tests**

```python
"""Tests for RSS and JSON feeds."""
import json
import xml.etree.ElementTree as ET
from pathlib import Path
from open_source_radar_ai.catalog import CatalogEntry
from open_source_radar_ai.feeds import write_feeds


def entry(id, date) -> CatalogEntry:
    return CatalogEntry(
        id=id, full_name=f"o/r{id}", html_url=f"https://github.com/o/r{id}",
        description="d & co", language="Python", category="Other",
        stars_at_feature=10, date_featured=date, page=f"repos/o--r{id}.md",
    )


def test_writes_valid_rss_and_json(tmp_path: Path):
    docs = tmp_path / "docs"
    entries = [entry(1, "2026-07-20"), entry(2, "2026-07-20"), entry(3, "2026-07-13")]
    write_feeds(entries, docs_dir=docs, site_url="https://example.com/")
    tree = ET.parse(docs / "feed.xml")  # raises if malformed
    items = tree.getroot().findall("./channel/item")
    assert len(items) == 2
    assert items[0].find("link").text == "https://example.com/reports/2026-07-20/"
    latest = json.loads((docs / "api" / "latest.json").read_text(encoding="utf-8"))
    assert latest["generated_on"] == "2026-07-20"
    assert len(latest["repos"]) == 2
    catalog = json.loads((docs / "api" / "catalog.json").read_text(encoding="utf-8"))
    assert len(catalog["repos"]) == 3


def test_empty_catalog_writes_empty_feed(tmp_path: Path):
    docs = tmp_path / "docs"
    write_feeds([], docs_dir=docs, site_url="https://example.com/")
    assert (docs / "feed.xml").exists()
```

- [ ] **Step 2: Verify failure.**

- [ ] **Step 3: Implement `feeds.py`** — group entries by `date_featured` desc; build XML with `xml.sax.saxutils.escape` for text nodes; write via `atomic_write_text_if_changed`; JSON via `atomic_write_json_if_changed` with `asdict(entry)`. RSS skeleton:

```python
RSS_TEMPLATE = """<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
<channel>
<title>Open Source Radar AI</title>
<link>{site_url}</link>
<description>AI-curated GitHub trending repositories, updated weekly.</description>
{items}
</channel>
</rss>
"""
```

Pipeline: after category pages, `write_feeds(full_catalog, docs_dir=docs_dir, site_url=os.getenv("RADAR_SITE_URL", "https://lokeshnanda.github.io/oss-radar-ai/"))`. Index page (`render_index_page`): add line `[Subscribe via RSS](feed.xml){:target="_blank"} · [JSON API](api/latest.json)` before the archive link. README: add RSS/JSON badges-or-links line under the badges.

- [ ] **Step 4: Run tests + `mkdocs build --strict`** (docs/feed.xml + docs/api/*.json are copied verbatim by mkdocs — regenerate via a one-off `python -c` run against the real catalog so the committed site has them).
- [ ] **Step 5: Commit** — `git commit -m "feat: RSS feed and JSON API endpoints"`

### Task 13: Social cards (OG images) in CI

**Files:**
- Modify: `mkdocs.yml`, `.github/workflows/trending.yml`

- [ ] **Step 1:** Add to `mkdocs.yml` plugins:

```yaml
plugins:
  - search
  - social:
      enabled: !ENV [CI, false]
```

- [ ] **Step 2:** In `trending.yml` install step, add imaging deps:

```yaml
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          sudo apt-get update && sudo apt-get install -y libcairo2-dev libfreetype6-dev libffi-dev libjpeg-dev libpng-dev libz-dev pngquant
          pip install -e .
          pip install "mkdocs-material[imaging]"
```

- [ ] **Step 3: Verify locally** — `mkdocs build --strict` still passes with plugin disabled (CI env var unset locally).
- [ ] **Step 4: Commit** — `git commit -m "feat: social card OG images in CI builds"`

### Task 14: Auto-updating repo README radar section

**Files:**
- Create: `src/open_source_radar_ai/readme_updater.py`
- Modify: `src/open_source_radar_ai/pipeline.py`, `.github/workflows/trending.yml` (`git add README.md`)
- Test: `tests/test_readme_updater.py`

**Interfaces:**
- Produces: `render_radar_section(entries: list[CatalogEntry], *, site_url: str) -> str` — markdown list of the newest week's repos with links to GitHub + site page.
- Produces: `update_readme_radar_section(readme_path: Path, entries, *, site_url) -> bool` — replaces content between `<!-- RADAR:START -->` and `<!-- RADAR:END -->`; returns False (no-op, warn) if markers missing.

- [ ] **Step 1: Failing tests**

```python
"""Tests for README radar-section updating."""
from pathlib import Path
from open_source_radar_ai.catalog import CatalogEntry
from open_source_radar_ai.readme_updater import update_readme_radar_section


def entry(id, date="2026-07-20") -> CatalogEntry:
    return CatalogEntry(
        id=id, full_name=f"o/r{id}", html_url=f"https://github.com/o/r{id}",
        description="d", language=None, category="Other",
        stars_at_feature=10, date_featured=date, page=f"repos/o--r{id}.md",
    )


def test_replaces_between_markers(tmp_path: Path):
    readme = tmp_path / "README.md"
    readme.write_text("intro\n<!-- RADAR:START -->\nold\n<!-- RADAR:END -->\noutro\n", encoding="utf-8")
    changed = update_readme_radar_section(readme, [entry(1)], site_url="https://example.com/")
    assert changed
    text = readme.read_text(encoding="utf-8")
    assert "old" not in text and "o/r1" in text
    assert text.startswith("intro\n") and text.rstrip().endswith("outro")


def test_missing_markers_is_noop(tmp_path: Path):
    readme = tmp_path / "README.md"
    readme.write_text("no markers here\n", encoding="utf-8")
    assert update_readme_radar_section(readme, [entry(1)], site_url="https://x/") is False
```

- [ ] **Step 2: Verify failure.**
- [ ] **Step 3: Implement** — regex `re.sub(r"(<!-- RADAR:START -->).*?(<!-- RADAR:END -->)", ..., flags=re.DOTALL)`; section content = `_Week of <date>_` + list `- [full_name](html_url) — description ([analysis](site_url + page-as-url))` where page URL = `site_url + entry.page.removesuffix('.md') + '/'`. Pipeline calls it with `Path("README.md")` (env `RADAR_README_PATH` override for tests) after feeds. Workflow commit step: `git add docs .radar_state README.md`.
- [ ] **Step 4: Run tests; run pipeline-level README update against real README via `python -c` with real catalog; verify README section populated.**
- [ ] **Step 5: Commit** — `git commit -m "feat: auto-update README radar section each run"`

### Task 15: Copy-paste social draft in weekly reports

**Files:**
- Modify: `src/open_source_radar_ai/generator.py`
- Test: extend `tests/test_generator.py`

**Interfaces:**
- Produces: `render_social_draft(repos, *, generated_on, site_url) -> str` — a `??? note "📣 Share this week's radar"` collapsible block (pymdownx.details, enabled in Task 2) containing a ready-to-post text: hook line, top-3 repos with star counts, site link. Appended to weekly report by `render_weekly_report_page` (new keyword `site_url: str | None = None`; block only added when provided).

- [ ] **Step 1: Failing test**

```python
def test_social_draft_in_weekly_report():
    from datetime import date
    from open_source_radar_ai.generator import render_weekly_report_page
    page = render_weekly_report_page(
        [make_repo()], generated_on=date(2026, 7, 20),
        docs_dir=Path("docs"), site_url="https://example.com/",
    )
    assert '??? note "📣 Share this week\'s radar"' in page
    assert "https://example.com/reports/2026-07-20/" in page
```

(add `from pathlib import Path` to the test module)

- [ ] **Step 2: Verify failure.**
- [ ] **Step 3: Implement** — draft body (indented 4 spaces inside the `???` block, in a fenced code block so it's copyable):

```
    ```text
    This week's most interesting new GitHub repos:

    1. o/r1 (⭐ 1200) — <description>
    2. ...
    3. ...

    Full AI-generated breakdowns of all 10:
    https://.../reports/2026-07-20/
    #opensource #github #developers
    ```
```

Pipeline passes `site_url` through `write_weekly_report_page`.

- [ ] **Step 4: Run full suite + `mkdocs build --strict`.**
- [ ] **Step 5: Commit** — `git commit -m "feat: copy-paste social draft in weekly reports"`

---

# PHASE 3 — Fork-your-own-radar template

### Task 16: Config-driven radar scope

**Files:**
- Modify: `src/open_source_radar_ai/config.py`, `github_client.py`, `mkdocs.yml`, `.env.example`
- Test: `tests/test_config_query.py`

**Interfaces:**
- Produces: `GitHubConfig.extra_query: str` (env `RADAR_SEARCH_QUERY`, default `""`) — appended to the search query: `created:>=<date> <extra_query>`.
- Produces: mkdocs.yml `site_name: !ENV [RADAR_SITE_NAME, "Open Source Radar AI"]` and `site_description: !ENV [RADAR_SITE_DESCRIPTION, "AI-curated GitHub trending repositories with developer-focused insights, updated weekly."]`.

- [ ] **Step 1: Failing test**

```python
"""Tests for configurable search scope."""
from datetime import date
from open_source_radar_ai.config import AppConfig, GitHubConfig
from open_source_radar_ai.github_client import GitHubClient, GitHubSearchParams


def test_extra_query_appended(monkeypatch):
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
            token=None, api_base_url="https://api.github.com",
            per_page=10, days_back=7, extra_query="topic:rust language:rust",
        ),
        reference_date=date(2026, 7, 24),
    )
    client = GitHubClient(cfg)
    client._session = FakeSession()
    client.search_trending_repositories(GitHubSearchParams(created_since=date(2026, 7, 17), per_page=10))
    assert captured["params"]["q"] == "created:>=2026-07-17 topic:rust language:rust"


def test_no_extra_query_unchanged():
    cfg = GitHubConfig(token=None, api_base_url="x", per_page=10, days_back=7, extra_query="")
    assert cfg.extra_query == ""
```

- [ ] **Step 2: Verify failure** (dataclass has no `extra_query`).
- [ ] **Step 3: Implement** — add `extra_query: str` field to `GitHubConfig`; `load_config` reads `os.getenv("RADAR_SEARCH_QUERY", "").strip()`; `search_trending_repositories` builds `query = f"created:>={...}"` then `if self.github_config.extra_query: query += f" {self.github_config.extra_query}"`. Update `.env.example` with `RADAR_SEARCH_QUERY=`, `RADAR_SITE_NAME=`, `RADAR_SITE_DESCRIPTION=`, `RADAR_SITE_URL=`, `RADAR_STAR_REFRESH_LIMIT=50`, `RADAR_README_MAX_CHARS=16000`. Update mkdocs.yml `site_name`/`site_description` to `!ENV` form. Note: any other `AppConfig(...)/GitHubConfig(...)` constructions in existing tests need `extra_query=""` added.
- [ ] **Step 4: Run full suite + `mkdocs build --strict`.**
- [ ] **Step 5: Commit** — `git commit -m "feat: configurable search scope and site identity for forks"`

### Task 17: LLM provider base_url normalization

**Files:**
- Modify: `src/open_source_radar_ai/openai_client.py`, `.env.example`
- Test: `tests/test_openai_client.py`

**Interfaces:**
- Produces: `chat_completion` URL building tolerates base URLs that already end in `/v1` (OpenRouter `https://openrouter.ai/api/v1`, Groq `https://api.groq.com/openai/v1`, Ollama `http://localhost:11434/v1`): use `base + "/chat/completions"` if base ends with `/v1`, else `base + "/v1/chat/completions"`.

- [ ] **Step 1: Failing test**

```python
"""Tests for OpenAI-compatible endpoint URL building."""
from open_source_radar_ai.openai_client import build_chat_completions_url


def test_default_openai_base():
    assert build_chat_completions_url("https://api.openai.com") == "https://api.openai.com/v1/chat/completions"


def test_base_already_has_v1():
    assert build_chat_completions_url("https://openrouter.ai/api/v1") == "https://openrouter.ai/api/v1/chat/completions"
```

- [ ] **Step 2: Verify failure.**
- [ ] **Step 3: Implement**

```python
def build_chat_completions_url(base_url: str) -> str:
    """Build the chat-completions endpoint for OpenAI-compatible providers."""
    base = base_url.rstrip("/")
    if base.endswith("/v1"):
        return f"{base}/chat/completions"
    return f"{base}/v1/chat/completions"
```

Use it in `chat_completion`. `.env.example` gains commented provider examples (OpenRouter/Groq/Ollama base URLs + model names).

- [ ] **Step 4: Run suite.**
- [ ] **Step 5: Commit** — `git commit -m "feat: support OpenAI-compatible providers (OpenRouter, Groq, Ollama)"`

### Task 18: Run-your-own guide + CONTRIBUTING

**Files:**
- Create: `docs/run-your-own.md`, `CONTRIBUTING.md`
- Modify: `mkdocs.yml` (nav), `README.md` (link the guide)

- [ ] **Step 1: Write `docs/run-your-own.md`** — "Deploy your own radar in ~10 minutes": fork → add `OPENAI_API_KEY` secret → enable Pages (GitHub Actions source) → optionally set `RADAR_SEARCH_QUERY` / `RADAR_SITE_NAME` / `RADAR_SITE_URL` as repository variables and reference them in the workflow env block (include the exact `env:` YAML snippet) → run `workflow_dispatch`. Include niche-radar examples (`topic:rust`, `topic:ai language:python`, `topic:security`). Include cost note (≈$0.05/week with gpt-4o-mini) and free-provider option via Task 17 env vars.
- [ ] **Step 2: Write `CONTRIBUTING.md`** — dev setup (`pip install -e ".[dev]"`, `python -m pytest tests -q`, `mkdocs serve`), code style expectations (typed, logged, deterministic writes), where to add tests, small-PR guidance, and 3 suggested starter contributions (new category heuristics, feed enhancements, new provider docs).
- [ ] **Step 3:** Nav gains `- Run your own: run-your-own.md`. README "Run your own radar" section links to the published guide URL. `mkdocs build --strict` passes.
- [ ] **Step 4: Commit** — `git commit -m "docs: run-your-own guide and CONTRIBUTING"`

---

# PHASE 4 — Stickiness

### Task 19: Trends page

**Files:**
- Create: `src/open_source_radar_ai/trends.py`
- Modify: `src/open_source_radar_ai/pipeline.py`, `mkdocs.yml` (nav)
- Test: `tests/test_trends.py`

**Interfaces:**
- Consumes: catalog entries.
- Produces: `write_trends_page(entries, *, docs_dir: Path) -> bool` → `docs/trends.md` with: total featured count; markdown table categories × last 6 months (`date_featured[:7]` buckets, newest column first); top-10 language table with counts and percentage.

- [ ] **Step 1: Failing test**

```python
"""Tests for the trends page."""
from pathlib import Path
from open_source_radar_ai.catalog import CatalogEntry
from open_source_radar_ai.trends import write_trends_page


def entry(id, date, category="Other", language="Python") -> CatalogEntry:
    return CatalogEntry(
        id=id, full_name=f"o/r{id}", html_url="u", description=None,
        language=language, category=category, stars_at_feature=1,
        date_featured=date, page=f"repos/o--r{id}.md",
    )


def test_trends_page_contents(tmp_path: Path):
    docs = tmp_path / "docs"
    entries = [
        entry(1, "2026-07-20", "AI & Agents", "Python"),
        entry(2, "2026-07-13", "AI & Agents", "Rust"),
        entry(3, "2026-06-01", "Security", "Python"),
    ]
    assert write_trends_page(entries, docs_dir=docs)
    text = (docs / "trends.md").read_text(encoding="utf-8")
    assert "3 repositories featured" in text
    assert "| AI & Agents |" in text
    assert "2026-07" in text and "2026-06" in text
    assert "Python" in text and "Rust" in text
```

- [ ] **Step 2: Verify failure.**
- [ ] **Step 3: Implement** — `Counter` over `(category, month)` and `language`; build tables with fixed category row order (`CATEGORIES`), months = sorted distinct `date_featured[:7]` desc, capped at 6; percentages via `round(100*count/total)`. Pipeline calls after category pages; nav gains `- Trends: trends.md`; generate real `docs/trends.md` from real catalog before mkdocs build (same `python -c` pattern as Task 9).
- [ ] **Step 4: Run suite + `mkdocs build --strict`.**
- [ ] **Step 5: Commit** — `git commit -m "feat: trends page (categories and languages over time)"`

### Task 20: Hall of fame

**Files:**
- Create: `src/open_source_radar_ai/hall_of_fame.py`
- Modify: `src/open_source_radar_ai/pipeline.py`, `mkdocs.yml` (nav)
- Test: `tests/test_hall_of_fame.py`

**Interfaces:**
- Consumes: star history (Task 10).
- Produces: `write_hall_of_fame(history: dict, *, docs_dir: Path) -> bool` → `docs/hall-of-fame.md` with two tables: **All-time top 20** (latest snapshot stars desc: rank, repo link, stars, first-seen date) and **Recent risers** (reuse `stars.compute_risers(history, limit=10)`).

- [ ] **Step 1: Failing test**

```python
"""Tests for the hall of fame page."""
from pathlib import Path
from open_source_radar_ai.hall_of_fame import write_hall_of_fame


def test_hall_of_fame(tmp_path: Path):
    docs = tmp_path / "docs"
    history = {
        "1": {"full_name": "o/big", "html_url": "u1", "snapshots": {"2026-07-13": 5000, "2026-07-20": 6000}},
        "2": {"full_name": "o/small", "html_url": "u2", "snapshots": {"2026-07-20": 10}},
    }
    assert write_hall_of_fame(history, docs_dir=docs)
    text = (docs / "hall-of-fame.md").read_text(encoding="utf-8")
    assert text.index("o/big") < text.index("o/small")
    assert "+1000" in text  # riser delta
```

- [ ] **Step 2: Verify failure.**
- [ ] **Step 3: Implement** — latest snapshot = `snapshots[max(snapshots)]`, first seen = `min(snapshots)`; markdown tables; pipeline calls after trends with loaded history; nav gains `- Hall of fame: hall-of-fame.md`; generate the real page via `python -c` before build.
- [ ] **Step 4: Run suite + `mkdocs build --strict`.**
- [ ] **Step 5: Commit** — `git commit -m "feat: hall of fame page from star history"`

### Task 21: Archive improvements

**Files:**
- Modify: `src/open_source_radar_ai/generator.py` (`render_archive_page`)
- Test: extend `tests/test_generator.py`

**Interfaces:**
- Produces: archive grouped by month (`## 2026-07` headings, newest first) with report links under each; keeps existing function signature.

- [ ] **Step 1: Failing test**

```python
def test_archive_groups_by_month(tmp_path: Path):
    from open_source_radar_ai.generator import render_archive_page
    reports = tmp_path / "reports"
    reports.mkdir(parents=True)
    for d in ("2026-07-20", "2026-07-13", "2026-06-01"):
        (reports / f"{d}.md").write_text("x", encoding="utf-8")
    text = render_archive_page(tmp_path)
    assert "## July 2026" in text and "## June 2026" in text
    assert text.index("## July 2026") < text.index("## June 2026")
```

- [ ] **Step 2: Verify failure.**
- [ ] **Step 3: Implement** — group `list_existing_reports` dates by `(year, month)`; heading via `date(y, m, 1).strftime("%B %Y")`; regenerate real `docs/archive.md` via `python -c "from open_source_radar_ai.generator import write_archive_page; from pathlib import Path; write_archive_page(Path('docs'))"`.
- [ ] **Step 4: Run suite + `mkdocs build --strict`.**
- [ ] **Step 5: Commit** — `git commit -m "feat: archive grouped by month"`

### Task 22: Final verification + roadmap checkboxes

- [ ] **Step 1:** `python -m pytest tests -q` — all green.
- [ ] **Step 2:** `mkdocs build --strict` — passes.
- [ ] **Step 3:** Full offline pipeline dry-run into a scratch dir: set `RADAR_DOCS_DIR`/`RADAR_STATE_DIR` to scratch copies and monkeypatch-free run is impossible without API keys — instead run the pipeline test suite plus a `python -c` invocation of each generator against real catalog/history to confirm real-site artifacts (categories, trends, hall-of-fame, feeds, README section) are current and committed.
- [ ] **Step 4:** Tick all boxes in `ROADMAP.md`, update `ARCHITECTURE.md` with the new modules (catalog, stars, feeds, category_pages, trends, hall_of_fame, readme_updater, backfill).
- [ ] **Step 5:** Commit — `git commit -m "docs: mark roadmap phases complete, refresh architecture"`. Report to user; ask before pushing (workflow bot also pushes to main — pull --rebase first).

## Self-review notes

- Spec coverage: Phase 0 → Tasks 1–4; Phase 1 → Tasks 5–11; Phase 2 → Tasks 12–15; Phase 3 → Tasks 16–18 (base_url support existed; Task 17 fixes real-provider compatibility); Phase 4 → Tasks 19–21; verification → Task 22. Spec's "tag filtering" is satisfied by category pages + search (Material tags plugin dropped as redundant — YAGNI).
- Type consistency: `RepoAnalysis(markdown, category)` used in Tasks 6/8; `CatalogEntry` field set identical in Tasks 7/9/12/14/19; `compute_risers` dict keys consistent in Tasks 10/20.
- Ordering hazard: Task 6 leaves `pipeline.py` passing `RepoAnalysis` where `str` expected until Task 8 — tests don't exercise that path; acceptable within the same phase.
