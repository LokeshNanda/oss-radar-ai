"""One-time backfill of historical repo pages into the catalog."""

from __future__ import annotations

import json
import logging
from pathlib import Path
import re
from typing import Dict, List, Optional

from .catalog import CatalogEntry, load_catalog, save_catalog, upsert_entries
from .io_utils import atomic_write_text_if_changed
from .models import CATEGORIES
from .summarize import build_default_client


LOGGER = logging.getLogger(__name__)

FALLBACK_DATE = "2026-01-01"

CATEGORY_PROMPT = """Classify this GitHub repository into exactly one category.
Categories: {categories}
Repository: {full_name}
Existing analysis (may be truncated):
{excerpt}

Respond with JSON: {{"category": "<one of the categories>"}}"""


def parse_repo_page(path: Path) -> Optional[Dict[str, object]]:
    """Parse a docs/repos/*.md page's frontmatter; None if malformed."""
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return None
    match = re.match(r"^---\n(.*?)\n---\n", text, flags=re.DOTALL)
    if not match:
        return None
    fields: Dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" in line:
            key, _, value = line.partition(":")
            fields[key.strip()] = value.strip()
    if "title" not in fields or "source" not in fields:
        return None
    try:
        stars = int(fields.get("stars", "0"))
    except ValueError:
        stars = 0
    return {
        "full_name": fields["title"],
        "source": fields["source"],
        "stars": stars,
        "category": fields.get("category"),
        "body": text[match.end():],
        "raw": text,
    }


def build_report_date_map(docs_dir: Path) -> Dict[str, str]:
    """Map repo page filename -> earliest weekly report date that links it."""
    mapping: Dict[str, str] = {}
    reports_dir = docs_dir / "reports"
    if not reports_dir.exists():
        return mapping
    for report in sorted(reports_dir.glob("*.md")):
        report_date = report.stem
        for match in re.finditer(r"\(\.\./repos/([^)]+\.md)\)", report.read_text(encoding="utf-8")):
            mapping.setdefault(match.group(1), report_date)
    return mapping


def _categorize(client, full_name: str, body: str) -> str:
    prompt = CATEGORY_PROMPT.format(
        categories=", ".join(CATEGORIES), full_name=full_name, excerpt=body[:2000]
    )
    try:
        raw = client.chat_completion(
            system="You classify GitHub repositories.",
            user=prompt,
            response_format={"type": "json_object"},
        )
        category = json.loads(raw).get("category")
    except Exception as exc:  # noqa: BLE001
        LOGGER.warning("Categorization failed for %s: %s", full_name, exc)
        return "Other"
    return category if category in CATEGORIES else "Other"


def _write_category_frontmatter(path: Path, raw: str, category: str) -> None:
    if re.search(r"^category: ", raw, flags=re.MULTILINE):
        updated = re.sub(
            r"^category: .*$", f"category: {category}", raw, count=1, flags=re.MULTILINE
        )
    else:
        updated = raw.replace("\n---\n", f"\ncategory: {category}\n---\n", 1)
    atomic_write_text_if_changed(path, updated)


def run_backfill(docs_dir: Path, *, categorize: bool) -> int:
    """Add historical repo pages missing from the catalog; returns count added."""
    existing = load_catalog()
    by_name = {e.full_name: e for e in existing}
    next_id = min([e.id for e in existing if e.id < 0], default=0) - 1

    date_map = build_report_date_map(docs_dir)
    client = build_default_client() if categorize else None

    new_entries: List[CatalogEntry] = []
    for page_path in sorted((docs_dir / "repos").glob("*.md")):
        parsed = parse_repo_page(page_path)
        if parsed is None:
            LOGGER.warning("Skipping malformed page %s", page_path.name)
            continue
        full_name = str(parsed["full_name"])
        known = by_name.get(full_name)
        if known is not None:
            # Re-categorize entries stuck at "Other" when an LLM is available.
            if client is not None and known.category == "Other":
                category = _categorize(client, full_name, str(parsed["body"]))
                if category != "Other":
                    _write_category_frontmatter(page_path, str(parsed["raw"]), category)
                    new_entries.append(
                        CatalogEntry(
                            id=known.id,
                            full_name=known.full_name,
                            html_url=known.html_url,
                            description=known.description,
                            language=known.language,
                            category=category,
                            stars_at_feature=known.stars_at_feature,
                            date_featured=known.date_featured,
                            page=known.page,
                        )
                    )
            continue

        category = parsed["category"]
        if category not in CATEGORIES:
            category = (
                _categorize(client, full_name, str(parsed["body"])) if client else "Other"
            )
        _write_category_frontmatter(page_path, str(parsed["raw"]), str(category))

        new_entries.append(
            CatalogEntry(
                id=next_id,
                full_name=full_name,
                html_url=str(parsed["source"]),
                description=None,
                language=None,
                category=str(category),
                stars_at_feature=int(parsed["stars"]),  # type: ignore[arg-type]
                date_featured=date_map.get(page_path.name, FALLBACK_DATE),
                page=f"repos/{page_path.name}",
            )
        )
        next_id -= 1

    if new_entries:
        save_catalog(upsert_entries(existing, new_entries))
    LOGGER.info("Backfilled %d repository pages into the catalog.", len(new_entries))
    return len(new_entries)


__all__ = ["parse_repo_page", "build_report_date_map", "run_backfill"]
