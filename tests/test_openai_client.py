"""Tests for OpenAI-compatible endpoint URL building."""
from open_source_radar_ai.openai_client import build_chat_completions_url


def test_default_openai_base():
    assert (
        build_chat_completions_url("https://api.openai.com")
        == "https://api.openai.com/v1/chat/completions"
    )


def test_base_already_has_v1():
    assert (
        build_chat_completions_url("https://openrouter.ai/api/v1")
        == "https://openrouter.ai/api/v1/chat/completions"
    )
