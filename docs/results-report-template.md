# <Study title>

## Executive finding

Write the main result in one or two sentences, including the workload and hardware conditions under which it holds.

## Research question

What was tested?

## Why it matters

Explain the practical systems or deployment decision affected by this result.

## Experimental setup

### Hardware

| Field | Value |
|---|---|
| Instance | — |
| GPU | — |
| GPU count | — |
| Interconnect | — |
| CPU | — |
| Host memory | — |

### Software

| Component | Version or commit |
|---|---|
| NVIDIA driver | — |
| CUDA | — |
| NCCL | — |
| PyTorch | — |
| Runtime | — |
| Repository | — |

### Model and workload

- Model:
- Revision:
- Precision:
- Prompt distribution:
- Output distribution:
- Concurrency:
- Parallelism:
- Warm-up:
- Repetitions:

## Correctness

Describe the reference, tolerance, quality metric, and pass criteria.

## Results

### Headline table

| Configuration | TTFT | ITL | Throughput | p99 | Peak memory | Quality |
|---|---:|---:|---:|---:|---:|---:|
| Baseline | — | — | — | — | — | — |
| Proposed | — | — | — | — | — | — |

### Key figure

Add the most decision-relevant graph.

### Profiler evidence

Add one timeline or kernel-level view that explains the result.

## Explanation

Separate:

- Measured observations
- Evidence-backed interpretation
- Remaining hypotheses

## Failed approaches

Document configurations or optimizations that did not work and why.

## Reproduction

```bash
# Exact command from a clean checkout
```

List required environment setup and expected output artifacts.

## Raw data

Link machine-readable results and the script that regenerates all tables and figures.

## Limitations

State hardware, model, workload, runtime, and statistical limitations.

## Practical recommendation

Explain when a practitioner should or should not use the tested approach.
