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
        "---",
        "title: Categories",
        "---",
        "",
        "# Categories",
        "",
        "Featured repositories grouped by category.",
        "",
    ]
    for category in CATEGORIES:
        repos = by_category.get(category) or []
        if not repos:
            continue
        slug = _slugify(category)
        index_lines.append(f"- [{category}]({slug}.md) — {len(repos)} repos")

        lines = [
            "---",
            f"title: {category}",
            "---",
            "",
            f"# {category}",
            "",
        ]
        for e in sorted(
            repos, key=lambda x: (x.date_featured, x.stars_at_feature), reverse=True
        ):
            desc = f" — {e.description.strip()}" if e.description else ""
            lines.append(
                f"- [`{e.full_name}`](../{e.page}){desc} "
                f"(⭐ {e.stars_at_feature}, week of {e.date_featured})"
            )
        lines.extend(["", "[← All categories](index.md)", ""])
        if atomic_write_text_if_changed(cat_dir / f"{slug}.md", "\n".join(lines)):
            written += 1

    index_lines.append("")
    if atomic_write_text_if_changed(cat_dir / "index.md", "\n".join(index_lines)):
        written += 1
    return written


__all__ = ["write_category_pages"]
