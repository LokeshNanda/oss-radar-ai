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


def write_repo_page(
    repo: Repository,
    *,
    analysis_markdown: str,
    docs_dir: Path,
    category: str | None = None,
) -> bool:
    """Write a repository report page deterministically."""
    path = repo_markdown_path(repo, docs_dir=docs_dir)
    ensure_dir(path.parent)
    content = render_repo_page(repo, analysis_markdown, category=category)
    return atomic_write_text_if_changed(path, content)


def weekly_report_path(reference_date: date, *, docs_dir: Path) -> Path:
    """Return the path for a weekly report page."""
    return docs_dir / "reports" / f"{reference_date.isoformat()}.md"


def render_weekly_report_page(
    repos: Iterable[Repository],
    *,
    generated_on: date,
    docs_dir: Path,
) -> str:
    """Render a weekly report page with links to repo pages."""
    repo_list = list(repos)
    repo_list.sort(key=lambda r: (-r.stargazers_count, r.full_name))

    lines: List[str] = [
        "---",
        f"title: Week of {generated_on.isoformat()}",
        "---",
        "",
        f"# Week of {generated_on.isoformat()}",
        "",
        "AI-curated GitHub repositories with high-level insights of the top 10 repositories of the week.",
        "",
        f"_Generated on {generated_on.isoformat()}_",
        "",
        "## Repositories",
        "",
    ]

    for repo in repo_list:
        rel_path = repo_markdown_path(repo, docs_dir=docs_dir).relative_to(docs_dir)
        # Report lives in docs/reports/, so link to repos/ needs ../
        repo_link = "../" + rel_path.as_posix()
        desc = (repo.description or "").strip()
        suffix = f" — {desc}" if desc else ""
        lines.append(f"- [`{repo.full_name}`]({repo_link}){suffix}")

    lines.extend(["", "[← View past weeks](../archive.md)", ""])
    return "\n".join(lines)


def write_weekly_report_page(
    repos: Iterable[Repository],
    *,
    generated_on: date,
    docs_dir: Path,
) -> bool:
    """Write a weekly report page."""
    path = weekly_report_path(generated_on, docs_dir=docs_dir)
    ensure_dir(path.parent)
    content = render_weekly_report_page(
        repos, generated_on=generated_on, docs_dir=docs_dir
    )
    return atomic_write_text_if_changed(path, content)


def list_existing_reports(docs_dir: Path) -> List[date]:
    """List report dates from docs/reports/*.md, sorted newest first."""
    reports_dir = docs_dir / "reports"
    if not reports_dir.exists():
        return []
    dates: List[date] = []
    for p in reports_dir.glob("*.md"):
        stem = p.stem
        if len(stem) == 10 and stem[4] == "-" and stem[7] == "-":
            try:
                dates.append(date.fromisoformat(stem))
            except ValueError:
                continue
    dates.sort(reverse=True)
    return dates


def render_archive_page(docs_dir: Path) -> str:
    """Render the archive page listing all weekly reports."""
    report_dates = list_existing_reports(docs_dir)
    lines: List[str] = [
        "---",
        "title: Past Weeks",
        "---",
        "",
        "# Past Weeks",
        "",
        "Browse weekly reports by date.",
        "",
    ]
    for d in report_dates:
        rel = f"reports/{d.isoformat()}.md"
        lines.append(f"- [Week of {d.isoformat()}]({rel})")
    lines.extend(["", "[← Back to homepage](index.md)", ""])
    return "\n".join(lines)


def write_archive_page(docs_dir: Path) -> bool:
    """Write the archive page listing all weekly reports."""
    path = docs_dir / "archive.md"
    content = render_archive_page(docs_dir)
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

    lines.extend(["", "[View past weeks →](archive.md)", ""])
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
    "weekly_report_path",
    "render_weekly_report_page",
    "write_weekly_report_page",
    "list_existing_reports",
    "render_archive_page",
    "write_archive_page",
    "render_index_page",
    "write_index_page",
]

