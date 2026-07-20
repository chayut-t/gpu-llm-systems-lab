"""Smoke test proving the benchmark package imports and exposes metadata."""

import benchmark


def test_benchmark_imports() -> None:
    assert benchmark.__version__ == "0.0.0"
