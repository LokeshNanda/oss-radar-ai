"""Smoke test: package imports and pipeline entry points exist."""
from open_source_radar_ai import pipeline, cli


def test_package_imports() -> None:
    assert callable(pipeline.run_pipeline)
    assert callable(cli.main_run)
