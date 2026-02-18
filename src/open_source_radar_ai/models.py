"""Domain models used by Open Source Radar AI."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Any, Dict, List, Optional


@dataclass(frozen=True)
class Repository:
    """Representation of a GitHub repository relevant for analysis."""

    id: int
    name: str
    full_name: str
    html_url: str
    description: Optional[str]
    stargazers_count: int
    language: Optional[str]
    topics: List[str]
    created_at: datetime
    updated_at: datetime
    owner_login: str

    @staticmethod
    def from_api_response(payload: Dict[str, Any]) -> "Repository":
        """Create a ``Repository`` instance from GitHub API JSON."""
        created_at = datetime.fromisoformat(payload["created_at"].replace("Z", "+00:00"))
        updated_at = datetime.fromisoformat(payload["updated_at"].replace("Z", "+00:00"))
        owner = payload.get("owner") or {}

        topics: List[str] = payload.get("topics") or []

        return Repository(
            id=int(payload["id"]),
            name=str(payload["name"]),
            full_name=str(payload["full_name"]),
            html_url=str(payload["html_url"]),
            description=payload.get("description"),
            stargazers_count=int(payload.get("stargazers_count", 0)),
            language=payload.get("language"),
            topics=list(topics),
            created_at=created_at,
            updated_at=updated_at,
            owner_login=str(owner.get("login", "")),
        )


__all__ = ["Repository"]

