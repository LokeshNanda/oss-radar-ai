"""Markdown generation for repository reports (Phase 5)."""

from __future__ import annotations

import re
from datetime import date
from pathlib import Path
from typing import Iterable, List

from .io_utils import atomic_write_text_if_changed, ensure_dir
from .models import Repository


def _slugify(value: str) -> str:
    slug = value.lower().strip()
    slug = re.sub(r"[^a-z0-9]+", "-", slug)
    slug = re.sub(r"-{2,}", "-", slug).strip("-")
    return slug or "repo"


def repo_markdown_path(repo: Repository, *, docs_dir: Path) -> Path:
    """Return the deterministic path for a repository markdown page."""
    owner, name = repo.full_name.split("/", 1)
    filename = f"{_slugify(owner)}--{_slugify(name)}.md"
    return docs_dir / "repos" / filename


def render_repo_page(repo: Repository, analysis_markdown: str) -> str:
    """Render a repository report page."""
    frontmatter = (
        "---\n"
        f"title: {repo.full_name}\n"
        f"source: {repo.html_url}\n"
        f"stars: {repo.stargazers_count}\n"
        "---\n\n"
    )
    header = f"# {repo.full_name}\n\n"
    meta = (
        f"- **URL**: {repo.html_url}\n"
        f"- **Stars**: {repo.stargazers_count}\n"
        f"- **Language**: {repo.language or 'Unknown'}\n"
        f"- **Topics**: {', '.join(repo.topics) if repo.topics else 'None'}\n\n"
    )
    body = analysis_markdown.strip() + "\n"
    return frontmatter + header + meta + body


def write_repo_page(
    repo: Repository,
    *,
    analysis_markdown: str,
    docs_dir: Path,
) -> bool:
    """Write a repository report page deterministically."""
    path = repo_markdown_path(repo, docs_dir=docs_dir)
    ensure_dir(path.parent)
    content = render_repo_page(repo, analysis_markdown)
    return atomic_write_text_if_changed(path, content)


def render_index_page(
    repos: Iterable[Repository],
    *,
    generated_on: date,
    docs_dir: Path,
) -> str:
    """Render the docs homepage with links to repo pages."""
    repo_list = list(repos)
    repo_list.sort(key=lambda r: (-r.stargazers_count, r.full_name))

    lines: List[str] = [
        "---",
        "title: Open Source Weekly Radar AI",
        "---",
        "",
        "# Open Source Weekly Radar AI",
        "",
        "AI-curated GitHub repositories with high-level insights of the top 10 repositories of the week.",
        "",
        f"_Generated on {generated_on.isoformat()}_",
        "",
        "## Latest repositories",
        "",
    ]

    for repo in repo_list:
        rel_path = repo_markdown_path(repo, docs_dir=docs_dir).relative_to(docs_dir)
        desc = (repo.description or "").strip()
        suffix = f" — {desc}" if desc else ""
        lines.append(f"- [`{repo.full_name}`]({rel_path.as_posix()}){suffix}")

    lines.append("")
    return "\n".join(lines)


def write_index_page(
    repos: Iterable[Repository],
    *,
    generated_on: date,
    docs_dir: Path,
) -> bool:
    """Write docs index page only if it changed."""
    path = docs_dir / "index.md"
    content = render_index_page(repos, generated_on=generated_on, docs_dir=docs_dir)
    return atomic_write_text_if_changed(path, content)


__all__ = [
    "repo_markdown_path",
    "render_repo_page",
    "write_repo_page",
    "render_index_page",
    "write_index_page",
]

