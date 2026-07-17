# Research Log: <Experiment title>

- **Experiment ID:** `<YYYYMMDD-short-name>`
- **Owner:** `<name>`
- **Status:** Proposed | Running | Completed | Inconclusive | Abandoned
- **Date:** `<YYYY-MM-DD>`
- **Repository commit:** `<sha>`
- **Related issue/PR:** `<link>`

## Question

State one falsifiable research question.

## Observation

What behavior motivated this experiment? Include the exact benchmark configuration and result.

## Hypothesis

Describe the proposed mechanism. Distinguish measured facts from inference.

## Proposed change

What code, configuration, scheduling policy, or hardware setting will change?

## Expected impact

| Metric | Expected direction | Reason |
|---|---:|---|
| TTFT | — | — |
| ITL | — | — |
| Throughput | — | — |
| Peak memory | — | — |
| Accuracy | — | — |

## Verification plan

### Controlled variables

- Model:
- Model revision:
- Hardware:
- Runtime:
- Precision:
- Workload:
- Seed:
- Warm-up:
- Repetitions:

### Measurements

- Headline metrics:
- Profiler:
- Correctness gate:
- Statistical method:

### Acceptance or rejection criteria

Define the result that would support or reject the hypothesis before running the experiment.

## Implementation notes

Record important design decisions, especially memory layout, synchronization, dispatch, and numerical behavior.

## Results

### Summary

One paragraph describing what happened.

### Headline measurements

| Configuration | Metric 1 | Metric 2 | Metric 3 |
|---|---:|---:|---:|
| Baseline | — | — | — |
| Proposed | — | — | — |

### Profiler evidence

Link the relevant Nsight Systems timeline, Nsight Compute report, trace, or parsed metrics.

## Interpretation

Explain the result using measured evidence.

## Limitations

What does this experiment not establish?

## Decision

- [ ] Adopt the change
- [ ] Reject the change
- [ ] Run a follow-up experiment
- [ ] Inconclusive

## Follow-up

List the next highest-value experiment.
