---
id: TXXXX
title: <Concise experimental outcome>
type: experiment
status: proposed
created: YYYY-MM-DD
depends_on: []
related_issue: null
related_experiment: experiments/<stable-experiment-id>/
requires_approval: true
---

# Task TXXXX: <Title>

## Outcome

State the experimental conclusion or bounded dataset this task should produce.

## Research question and hypothesis

- Question:
- Observation:
- Hypothesis:
- Expected effect:
- Rejection criterion:

Use `docs/research-log-template.md` for the durable experiment record.

## Context

List prior tasks, baselines, project documents, and relevant profiler evidence.

## In scope

- <Configurations and comparisons to run>

## Out of scope

- <Nearby workload, runtime, or hardware intentionally excluded>

## Experimental design

### Hardware and software

- Provider, region, and instance type:
- GPU model, count, memory, and interconnect:
- Container or environment revision:
- Driver, CUDA, NCCL, framework, and runtime versions:
- Repository commit:

### Model and workload

- Model and tokenizer revisions:
- Input and output distributions:
- Arrival process or concurrency:
- Precision and parallelism:
- Warm-up policy:
- Measurement window and repetitions:
- Random seed:

### Controls and correctness gate

- Controlled variables:
- Reference implementation or baseline:
- Correctness or quality metric:
- Acceptance tolerance:
- Conditions that invalidate the run:

### Measurements and profiling

- Headline metrics:
- Tail and uncertainty reporting:
- Profiling mode and representative configuration:
- Evidence required to support the interpretation:

## Infrastructure budget and approval

- Estimated hourly cost:
- Maximum total cost:
- Maximum duration:
- Run identifier:
- Approval required from:
- Approval evidence:

Preparation and dry runs may proceed without spending approval. Do not provision or
start a paid run until the approval evidence is recorded.

## Execution and artifact plan

1. Validate configuration and correctness on the cheapest suitable environment.
2. Capture the environment and topology before measurement.
3. Execute the exact recorded commands with an idempotent run identifier.
4. Write raw results under `results/raw/`.
5. Write derived outputs under `results/summarized/` and `results/figures/`.
6. Store large profiler artifacts externally; record stable references and checksums.
7. Download and verify all required artifacts before teardown.
8. Tear down resources and confirm no billable resources remain.

## Failure and recovery plan

- Interrupted run:
- Partial or invalid measurements:
- Artifact upload failure:
- Teardown failure and escalation:

## Acceptance criteria

- [ ] Correctness or quality gates pass before performance results are accepted.
- [ ] All repetitions and invalid runs are retained or accounted for.
- [ ] Raw results are machine-readable and linked to the producing commit.
- [ ] Headline results are measured without profiler overhead.
- [ ] Profiler evidence uses a matching representative configuration.
- [ ] Measurement, inference, hypothesis, and limitation are separated.
- [ ] Required artifacts are verified and billable resources are confirmed removed.

## Completion record

- Status: Not started
- Run identifiers:
- Commands run:
- Result and experiment paths:
- External artifacts and checksums:
- Cost and duration:
- Teardown confirmation:
- Conclusion:
- Limitations:
- Follow-up tasks:
