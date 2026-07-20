---
id: T0001
title: Bootstrap the Python project and local quality tooling
type: implementation
status: done
created: 2026-07-19
depends_on: []
related_issue: null
requires_approval: false
---

# Task T0001: Bootstrap the Python project and local quality tooling

## Outcome

A contributor can install the repository as a Python project, import the benchmark
package, and run one documented set of local quality checks.

## Context

Read before implementation:

- `README.md`, especially Repository layout and Planned command interface
- `docs/architecture.md`, especially Proposed implementation layout
- `docs/roadmap.md`, Phase 0
- `CONTRIBUTING.md`

The architecture explicitly recommends adding only the directories needed for a
working vertical slice. This task establishes tooling without creating placeholder
packages for later workstreams.

## In scope

- Add a `pyproject.toml` using a conventional build backend.
- Add an importable `benchmark` package with package metadata only.
- Configure pytest and Ruff in `pyproject.toml`.
- Add one smoke test proving that `benchmark` imports.
- Document local setup and quality-check commands.

## Out of scope

- PyTorch, CUDA, Triton, or inference-runtime dependencies
- Benchmark configuration and result models
- GPU or software inventory collection
- The benchmark runner or CLI
- CI workflows, containers, and GPU tests
- Empty `engines/`, `kernels/`, `distributed/`, or `serving/` trees

## Deliverables

- `pyproject.toml`
- `benchmark/__init__.py`
- `tests/test_package.py`
- A concise development setup section in `README.md` or `CONTRIBUTING.md`

## Design constraints

- Require Python 3.11 or newer.
- Keep runtime dependencies empty.
- Put pytest and Ruff in an explicit development dependency group or extra.
- Use a package version that clearly communicates bootstrap status.
- Do not add generated lockfiles unless the chosen workflow documents and verifies
  them in this task.

## Acceptance criteria

- [ ] A fresh development installation succeeds using the documented command.
- [ ] `python -c "import benchmark"` succeeds from outside the repository root.
- [ ] The test suite includes and passes an import smoke test.
- [ ] Ruff reports no violations in project Python files.
- [ ] No GPU stack or inference-runtime dependency is introduced.

## Validation

Record and run the exact equivalents selected by the implementation:

```bash
python -m pip install -e '<development-extra>'
python -c "import benchmark"
python -m pytest
python -m ruff check .
```

## Completion record

- Status: Implemented; awaiting Codex review (left in `active/`, not moved to `completed/`)
- Files changed:
  - `pyproject.toml` (new) — setuptools backend, `requires-python = ">=3.11"`, empty runtime
    `dependencies`, `dev` extra (`pytest>=8`, `ruff>=0.6`), bootstrap version `0.0.0`, pytest and
    Ruff config.
  - `benchmark/__init__.py` (new) — package metadata only (`__version__ = "0.0.0"`).
  - `tests/test_package.py` (new) — import smoke test.
  - `README.md` — added a "Development setup" section (install + quality-check commands).
- Commands run (in a fresh `.venv`, Python 3.13.13 which satisfies `>=3.11`):
  - `python3 -m venv .venv`
  - `.venv/bin/python -m pip install -e '.[dev]'`
  - `cd /tmp && .../.venv/bin/python -c "import benchmark"` -> `import ok 0.0.0`
  - `.venv/bin/python -m pytest -q` -> `1 passed`
  - `.venv/bin/python -m ruff check .` -> `All checks passed!`
- Evidence (acceptance criteria):
  - [x] Fresh editable install succeeds via the documented command.
  - [x] `python -c "import benchmark"` succeeds from outside the repository root (ran from `/tmp`).
  - [x] Test suite includes and passes the import smoke test (`1 passed`).
  - [x] Ruff reports no violations (`All checks passed!`).
  - [x] No GPU stack or inference-runtime dependency introduced (`dependencies = []`; `dev` extra
    is pytest + Ruff only; the only "NVIDIA"/"CUDA" strings are in the project description prose).
- Deviations from task: none. Chose setuptools as the build backend and a `[project.optional-dependencies]`
  `dev` extra (both conventional); no generated lockfile added, per the design constraint.
- Follow-up tasks: none newly required. T0002 (config model) and T0003 (result schema) already
  exist in `backlog/` and depend on this task.
