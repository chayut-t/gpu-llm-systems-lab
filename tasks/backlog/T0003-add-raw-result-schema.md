---
id: T0003
title: Add the versioned raw benchmark result schema
type: implementation
status: ready
created: 2026-07-19
depends_on: [T0001, T0002]
related_issue: null
requires_approval: false
---

# Task T0003: Add the versioned raw benchmark result schema

## Outcome

The benchmark package can validate and serialize a versioned raw-result envelope
that preserves provenance, per-request measurements, correctness, and failures.

## Context

Read before implementation:

- `docs/architecture.md`, Result model
- `docs/methodology.md`, sections 9, 12, and 14
- `results/README.md`
- Completed tasks `T0001` and `T0002`

The schema is a storage contract, not a metrics collector. Later inventory and
runner tasks will populate it.

## In scope

- Define typed, versioned raw-result models in `benchmark/schemas.py`.
- Represent run identity and UTC timestamp, repository commit, environment metadata,
  the complete experiment configuration, per-request metrics, aggregate metrics,
  correctness results, artifact references, runtime logs, and failure information.
- Serialize deterministically to JSON without losing per-request data.
- Validate structural invariants and reject unknown top-level fields.
- Add unit tests and one minimal example raw-result file.

## Out of scope

- Collecting hardware or software metadata
- Computing aggregate statistics
- Running workloads or profilers
- Defining engine-specific metric vocabularies
- Enforcing immutability through an external object store
- Result migrations, databases, dashboards, and plotting

## Deliverables

- `benchmark/schemas.py`
- `tests/test_schemas.py`
- One small example raw result under `results/raw/` or a test fixture directory,
  clearly marked as synthetic rather than a published performance result
- Documentation of schema versioning and artifact references

## Design constraints

- The result must embed or losslessly include the exact experiment configuration.
- Per-request records must remain first-class; aggregates cannot replace them.
- Failed and partially completed runs must be representable.
- Artifact references must support a stable location, checksum, media type, tool
  version, and capture command without embedding large profiler files.
- Timestamps must be timezone-aware UTC values.
- Floating-point values must reject non-finite JSON values unless a field explicitly
  defines another representation.

## Acceptance criteria

- [ ] A successful synthetic run round-trips without semantic changes.
- [ ] A failed or partial run can retain failure details and available measurements.
- [ ] Multiple per-request records remain intact and ordered.
- [ ] Invalid versions, timestamps, non-finite values, and structural contradictions
  fail with actionable errors.
- [ ] JSON serialization is deterministic.
- [ ] All project quality checks pass.

## Validation

```bash
python -m pytest
python -m ruff check .
# Add the exact example-validation command during implementation.
```

## Completion record

- Status: Not started
- Files changed:
- Commands run:
- Evidence:
- Deviations from task:
- Follow-up tasks:
