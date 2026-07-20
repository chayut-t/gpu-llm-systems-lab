---
id: T0002
title: Add a validated experiment configuration model
type: implementation
status: ready
created: 2026-07-19
depends_on: [T0001]
related_issue: null
requires_approval: false
---

# Task T0002: Add a validated experiment configuration model

## Outcome

The benchmark package can load, validate, and serialize a minimal runtime-agnostic
experiment configuration without hiding backend-specific options.

## Context

Read before implementation:

- `docs/architecture.md`, Backend contract and Workload model
- `docs/methodology.md`, sections 3 through 8
- `README.md`, Planned command interface
- Completed task `T0001`

This configuration is the input contract for later runners. It should encode only
fields required for the first vertical slice while permitting visible, namespaced
backend options.

## In scope

- Define a typed, versioned experiment configuration in `benchmark/config.py`.
- Represent model revision, tokenizer revision, engine, dtype, tensor-parallel size,
  input length, output length, concurrency, request count, warm-up count, repetition
  count, random seed, and backend-specific options.
- Load the configuration from JSON and serialize it deterministically to JSON.
- Reject missing required fields, unsupported schema versions, non-positive counts,
  and unknown top-level fields with actionable errors.
- Add focused unit tests and one documented example configuration.

## Out of scope

- YAML or command-line parsing
- Runtime-specific validation or imports
- Workload generation and benchmark execution
- Open-loop arrival processes and prompt-length distributions
- Environment inventory and result schemas
- Backward-compatibility migrations between schema versions

## Deliverables

- `benchmark/config.py`
- `tests/test_config.py`
- One small example JSON configuration in an appropriate documented location
- Documentation explaining the supported fields and validation command

## Design constraints

- The schema must contain an explicit version.
- Backend-specific options must remain visible rather than being silently ignored.
- Loading must not execute code or import an inference runtime.
- Prefer the smallest dependency set justified by the validation requirements.
- JSON output must be stable enough to hash as part of a future run identifier.

## Acceptance criteria

- [ ] A valid example configuration round-trips without semantic changes.
- [ ] Invalid versions, counts, and unknown top-level fields fail clearly.
- [ ] Backend-specific options survive a round trip unchanged.
- [ ] Tests cover valid input, each validation class, and deterministic output.
- [ ] All project quality checks from `T0001` pass.

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
