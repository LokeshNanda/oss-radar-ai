"""OpenAI client and configuration (Phase 4)."""

from __future__ import annotations

from dataclasses import dataclass
import json
import logging
import os
import random
import time
from typing import Any, Dict, List, Optional

import requests

from .config import load_dotenv_if_present


LOGGER = logging.getLogger(__name__)


class OpenAIAPIError(RuntimeError):
    """Raised when the OpenAI API returns an error response."""


@dataclass(frozen=True)
class OpenAIConfig:
    """Configuration required for OpenAI API access."""

    api_key: str
    base_url: str
    model: str
    temperature: float
    max_tokens: int
    timeout_seconds: int
    max_retries: int


def _load_float_env(name: str, default: float) -> float:
    raw = os.getenv(name, str(default))
    try:
        return float(raw)
    except ValueError:
        LOGGER.warning("Invalid %s=%s; using %s.", name, raw, default)
        return default


def _load_int_env(name: str, default: int) -> int:
    raw = os.getenv(name, str(default))
    try:
        return int(raw)
    except ValueError:
        LOGGER.warning("Invalid %s=%s; using %d.", name, raw, default)
        return default


def load_openai_config() -> OpenAIConfig:
    """Load OpenAI configuration from environment variables.

    Required:
    - OPENAI_API_KEY

    Optional:
    - OPENAI_BASE_URL (default: https://api.openai.com)
    - OPENAI_MODEL (default: gpt-4o-mini)
    - OPENAI_TEMPERATURE (default: 0.2)
    - OPENAI_MAX_TOKENS (default: 900)
    - OPENAI_TIMEOUT_SECONDS (default: 45)
    - OPENAI_MAX_RETRIES (default: 5)
    """
    load_dotenv_if_present()

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise OpenAIAPIError("OPENAI_API_KEY is not set.")

    base_url = os.getenv("OPENAI_BASE_URL", "https://api.openai.com").rstrip("/")
    model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

    temperature = _load_float_env("OPENAI_TEMPERATURE", 0.2)
    max_tokens = _load_int_env("OPENAI_MAX_TOKENS", 1400)
    timeout_seconds = _load_int_env("OPENAI_TIMEOUT_SECONDS", 45)
    max_retries = _load_int_env("OPENAI_MAX_RETRIES", 5)

    return OpenAIConfig(
        api_key=api_key,
        base_url=base_url,
        model=model,
        temperature=temperature,
        max_tokens=max_tokens,
        timeout_seconds=timeout_seconds,
        max_retries=max_retries,
    )


def _should_retry(status_code: int) -> bool:
    return status_code == 429 or 500 <= status_code <= 599


def _sleep_backoff(attempt: int) -> None:
    base = min(2 ** attempt, 30)
    jitter = random.uniform(0.0, 0.25 * base)
    time.sleep(base + jitter)


class OpenAIClient:
    """Minimal OpenAI Chat Completions client with retries."""

    def __init__(self, config: OpenAIConfig) -> None:
        self._config = config
        self._session = requests.Session()
        self._session.headers.update(
            {
                "Authorization": f"Bearer {config.api_key}",
                "Content-Type": "application/json",
            }
        )

    def chat_completion(
        self,
        *,
        system: str,
        user: str,
        response_format: Optional[Dict[str, Any]] = None,
    ) -> str:
        """Create a chat completion and return the assistant content."""
        url = f"{self._config.base_url}/v1/chat/completions"
        payload: Dict[str, Any] = {
            "model": self._config.model,
            "temperature": self._config.temperature,
            "max_tokens": self._config.max_tokens,
            "messages": [
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
        }
        if response_format is not None:
            payload["response_format"] = response_format

        last_error: Optional[str] = None
        for attempt in range(self._config.max_retries + 1):
            try:
                resp = self._session.post(
                    url, data=json.dumps(payload), timeout=self._config.timeout_seconds
                )
            except requests.RequestException as exc:
                last_error = str(exc)
                LOGGER.warning("OpenAI request error (attempt %d): %s", attempt + 1, exc)
                _sleep_backoff(attempt)
                continue

            if resp.status_code >= 400:
                last_error = f"status={resp.status_code} body={resp.text}"
                if _should_retry(resp.status_code) and attempt < self._config.max_retries:
                    LOGGER.warning(
                        "OpenAI error (attempt %d): %s", attempt + 1, last_error
                    )
                    _sleep_backoff(attempt)
                    continue
                raise OpenAIAPIError(f"OpenAI API request failed: {last_error}")

            data = resp.json()
            choices: List[Dict[str, Any]] = data.get("choices") or []
            if not choices:
                raise OpenAIAPIError("OpenAI API response missing choices.")
            message = (choices[0].get("message") or {}).get("content")
            if not isinstance(message, str) or not message.strip():
                raise OpenAIAPIError("OpenAI API response missing message content.")
            return message.strip()

        raise OpenAIAPIError(f"OpenAI API request failed after retries: {last_error}")


__all__ = ["OpenAIClient", "OpenAIConfig", "OpenAIAPIError", "load_openai_config"]

