# Contributing

Contributions are welcome when they improve correctness, reproducibility, measurement quality, or systems understanding.

## Before opening a pull request

For a substantial experiment or architectural change, open an issue first and describe:

- Research question
- Motivation
- Proposed implementation
- Correctness plan
- Benchmark plan
- Expected profiler evidence
- Hardware requirements

## Pull-request requirements

A pull request should include, as applicable:

- Focused scope
- Tests
- Type hints for Python code
- Clear error handling
- Reproduction commands
- Environment details
- Raw or representative result artifacts
- Statistical treatment
- Correctness evidence
- Profiler evidence for performance claims
- Documentation updates
- Limitations

## Performance claims

Do not claim a speedup using:

- A single timing sample
- Different workloads
- Different quality targets
- Different model revisions
- Incomplete warm-up
- Debug-enabled baseline only
- Unexplained synchronization
- Profiler-instrumented results compared with non-profiled results
- Selective reporting of favorable shapes

State the baseline, workload, hardware, software stack, repetitions, and uncertainty.

## Kernel contributions

CUDA and Triton contributions should include:

- Reference implementation
- Correctness tests
- Shape and dtype coverage
- Numerical tolerance rationale
- Benchmark across representative regimes
- Alignment and contiguity assumptions
- Bounds handling
- Race-condition analysis
- Profiler evidence when performance is the motivation

## Data and confidentiality

Use only public models, datasets, and algorithms.

Do not submit:

- Employer code or internal design
- Private traces or logs
- Credentials
- Customer data
- Proprietary model weights
- Confidential benchmark results
- Infrastructure identifiers that should remain private

## Style

The project will add automated formatting and linting when implementation begins. Until then:

- Prefer small, readable modules
- Document non-obvious performance assumptions
- Avoid abstraction that hides critical behavior
- Keep backend-specific options visible
- Separate measurement from interpretation

## Commit messages

Use concise imperative messages, for example:

```text
Add runtime metadata schema
Implement Triton RMSNorm reference
Document NCCL overlap methodology
```
