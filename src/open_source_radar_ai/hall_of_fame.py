"""Hall of fame page generation from star history."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List

from .io_utils import atomic_write_text_if_changed, ensure_dir
from .stars import compute_risers


TOP_LIMIT = 20
RISER_LIMIT = 10


def write_hall_of_fame(history: Dict[str, Any], *, docs_dir: Path) -> bool:
    """Write docs/hall-of-fame.md: all-time top repos and recent risers."""
    ranked = []
    for entry in history.values():
        snapshots = entry.get("snapshots") or {}
        if not snapshots:
            continue
        latest = max(snapshots)
        ranked.append(
            {
                "full_name": entry["full_name"],
                "html_url": entry["html_url"],
                "stars": snapshots[latest],
                "first_seen": min(snapshots),
            }
        )
    ranked.sort(key=lambda r: -r["stars"])

    lines: List[str] = [
        "---",
        "title: Hall of fame",
        "---",
        "",
        "# 🏆 Hall of fame",
        "",
        "## All-time top repositories",
        "",
    ]
    if ranked:
        lines.append("| # | Repository | Stars | First featured |")
        lines.append("| --- | --- | --- | --- |")
        for rank, r in enumerate(ranked[:TOP_LIMIT], start=1):
            lines.append(
                f"| {rank} | [`{r['full_name']}`]({r['html_url']}) | "
                f"⭐ {r['stars']} | {r['first_seen']} |"
            )
    else:
        lines.append("_No star history yet — check back after the next weekly run._")

    risers = compute_risers(history, limit=RISER_LIMIT)
    lines.extend(["", "## 📈 Recent risers", ""])
    if risers:
        lines.append("| Repository | Gained | Now |")
        lines.append("| --- | --- | --- |")
        for r in risers:
            lines.append(
                f"| [`{r['full_name']}`]({r['html_url']}) | +{r['delta']} | ⭐ {r['stars']} |"
            )
    else:
        lines.append("_Risers appear once repositories have at least two weekly snapshots._")

    lines.append("")
    ensure_dir(docs_dir)
    return atomic_write_text_if_changed(docs_dir / "hall-of-fame.md", "\n".join(lines))


__all__ = ["write_hall_of_fame"]
