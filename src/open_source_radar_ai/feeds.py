"""RSS and JSON feed generation from the catalog."""

from __future__ import annotations

from collections import defaultdict
from dataclasses import asdict
from datetime import datetime, timezone
from email.utils import format_datetime
from pathlib import Path
from typing import Dict, Iterable, List
from xml.sax.saxutils import escape

from .catalog import CatalogEntry
from .io_utils import atomic_write_json_if_changed, atomic_write_text_if_changed, ensure_dir


MAX_RSS_ITEMS = 12

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


def _rss_item(week: str, repos: List[CatalogEntry], *, site_url: str) -> str:
    link = f"{site_url}reports/{week}/"
    bullet_list = "".join(
        f"<li>{escape(e.full_name)}{' — ' + escape(e.description) if e.description else ''}</li>"
        for e in sorted(repos, key=lambda r: -r.stars_at_feature)
    )
    year, month, day = (int(part) for part in week.split("-"))
    pub_date = format_datetime(datetime(year, month, day, tzinfo=timezone.utc))
    return (
        "<item>\n"
        f"<title>Open Source Radar — Week of {week}</title>\n"
        f"<link>{link}</link>\n"
        f"<guid>{link}</guid>\n"
        f"<pubDate>{pub_date}</pubDate>\n"
        f"<description>{escape(f'<ul>{bullet_list}</ul>')}</description>\n"
        "</item>"
    )


def write_feeds(
    entries: Iterable[CatalogEntry], *, docs_dir: Path, site_url: str
) -> None:
    """Write docs/feed.xml, docs/api/latest.json and docs/api/catalog.json."""
    entry_list = list(entries)
    by_week: Dict[str, List[CatalogEntry]] = defaultdict(list)
    for e in entry_list:
        by_week[e.date_featured].append(e)
    weeks = sorted(by_week, reverse=True)

    items = "\n".join(
        _rss_item(week, by_week[week], site_url=site_url) for week in weeks[:MAX_RSS_ITEMS]
    )
    ensure_dir(docs_dir)
    atomic_write_text_if_changed(
        docs_dir / "feed.xml", RSS_TEMPLATE.format(site_url=site_url, items=items)
    )

    api_dir = docs_dir / "api"
    ensure_dir(api_dir)
    latest_week = weeks[0] if weeks else None
    latest_repos = (
        sorted(by_week[latest_week], key=lambda r: -r.stars_at_feature)
        if latest_week
        else []
    )
    atomic_write_json_if_changed(
        api_dir / "latest.json",
        {"generated_on": latest_week, "repos": [asdict(e) for e in latest_repos]},
    )
    atomic_write_json_if_changed(
        api_dir / "catalog.json", {"repos": [asdict(e) for e in entry_list]}
    )


__all__ = ["write_feeds"]
