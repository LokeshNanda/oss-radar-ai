# Contributing

Thanks for your interest in improving Open Source Radar AI!

## Development setup

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -e ".[dev]"

# run the tests
python -m pytest tests -q

# preview the site
mkdocs serve
```

Running the full pipeline locally needs an `OPENAI_API_KEY` (copy `.env.example` to `.env`), but most changes can be developed and tested without one — the test suite uses fakes for all external APIs.

## Code expectations

- **Deterministic writes** — generate files through `io_utils.atomic_write_text_if_changed` / `atomic_write_json_if_changed` so reruns produce no diff noise.
- **Graceful degradation** — external failures (GitHub API, LLM) must log and skip, never crash the pipeline.
- **Typed and logged** — follow the existing style: type hints, module-level `LOGGER`, focused modules.
- **Tests with every change** — add or extend a test in `tests/` mirroring the module you touched. Fake external services; don't call real APIs in tests.
- **`mkdocs build --strict` must pass** for any change that affects generated pages.

## Good first contributions

- **Feed enhancements** — e.g. per-category RSS feeds, or an Atom feed alongside RSS.
- **New provider docs** — verify the radar against another OpenAI-compatible provider and document the exact env vars in `docs/run-your-own.md`.
- **Report polish** — better weekly-report layout, richer star-velocity display, category emojis.

## Pull requests

Keep PRs small and focused (one feature or fix per PR). Describe what changed and why; include test output in the description.
