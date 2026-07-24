"""Trends page generation from the catalog."""

from __future__ import annotations

from collections import Counter
from pathlib import Path
from typing import Iterable, List

from .catalog import CatalogEntry
from .io_utils import atomic_write_text_if_changed, ensure_dir
from .models import CATEGORIES


MAX_MONTHS = 6
MAX_LANGUAGES = 10


def write_trends_page(entries: Iterable[CatalogEntry], *, docs_dir: Path) -> bool:
    """Write docs/trends.md with category-by-month and language tables."""
    entry_list = list(entries)
    total = len(entry_list)

    months = sorted({e.date_featured[:7] for e in entry_list}, reverse=True)[:MAX_MONTHS]
    cat_month = Counter((e.category, e.date_featured[:7]) for e in entry_list)
    languages = Counter(e.language for e in entry_list if e.language)

    lines: List[str] = [
        "---",
        "title: Trends",
        "---",
        "",
        "# 📊 Trends",
        "",
        f"**{total} repositories featured** on the radar so far.",
        "",
        "## Categories over time",
        "",
    ]

    if months:
        lines.append("| Category | " + " | ".join(months) + " |")
        lines.append("| --- | " + " | ".join("---" for _ in months) + " |")
        for category in CATEGORIES:
            counts = [cat_month.get((category, month), 0) for month in months]
            if not any(counts):
                continue
            lines.append(
                f"| {category} | " + " | ".join(str(c) for c in counts) + " |"
            )
    else:
        lines.append("_No data yet._")

    lines.extend(["", "## Top languages", ""])
    if languages:
        lines.append("| Language | Repos | Share |")
        lines.append("| --- | --- | --- |")
        for language, count in languages.most_common(MAX_LANGUAGES):
            share = round(100 * count / total)
            lines.append(f"| {language} | {count} | {share}% |")
    else:
        lines.append("_No language data yet._")

    lines.append("")
    ensure_dir(docs_dir)
    return atomic_write_text_if_changed(docs_dir / "trends.md", "\n".join(lines))


__all__ = ["write_trends_page"]
