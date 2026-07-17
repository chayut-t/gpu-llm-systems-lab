# Benchmark Methodology

## Purpose

This document defines the minimum standard for any performance claim published in this repository.

The methodology is designed to prevent common errors:

- Comparing unmatched workloads
- Measuring warm-up instead of steady state
- Reporting throughput while hiding tail latency
- Attributing speedup to the wrong subsystem
- Ignoring correctness or accuracy loss
- Treating a single run as representative
- Publishing hardware-specific behavior as a universal conclusion

## 1. Define the question before running the benchmark

Every experiment begins with a falsifiable question.

Good:

> Does fusing residual addition and RMSNorm reduce decode latency for small token batches by eliminating HBM round trips?

Weak:

> Is the Triton kernel faster?

The research log must state:

- Observation
- Hypothesis
- Proposed change
- Expected effect
- Metrics that would confirm or reject the hypothesis

## 2. Capture the environment

Record at minimum:

### Hardware

- Cloud provider and instance type
- GPU model and count
- GPU memory
- GPU power limit
- GPU clocks if fixed
- Interconnect: PCIe, NVLink, NVSwitch, or other
- CPU model and socket count
- Host memory
- Local and network storage
- NUMA topology when relevant

### Software

- Operating system
- Container image digest
- NVIDIA driver
- CUDA toolkit
- cuDNN
- NCCL
- Python
- PyTorch
- Triton
- vLLM
- SGLang
- TensorRT-LLM
- Model Optimizer
- Git commit for this repository
- Git commit or package version for each runtime under test

Store environment details alongside every raw result.

## 3. Pin model and data revisions

Record:

- Model repository
- Exact model revision or commit
- Tokenizer revision
- Configuration
- Quantization method
- Calibration dataset and revision
- Evaluation dataset and revision
- Prompt-generation method
- Random seed

Do not use a moving `main` revision for a published result.

## 4. Define the workload precisely

Specify:

- Prompt-length distribution
- Output-length distribution
- Arrival process
- Concurrency
- Request count
- Batch policy
- Maximum sequence length
- Prefix reuse
- Sampling parameters
- Stop conditions
- Tensor-parallel degree
- Pipeline- or expert-parallel degree
- Cache state
- Streaming behavior

For synthetic workloads, publish the generator and seed.

For trace-based workloads, publish the trace when licensing permits or provide a statistically equivalent generator.

## 5. Separate prefill and decode

Report prefill and decode separately whenever possible.

### Prefill metrics

- TTFT
- Prompt tokens/s
- Attention and GEMM time
- Peak memory
- Communication time
- CPU/tokenization overhead

### Decode metrics

- ITL
- Generated tokens/s
- KV-cache bandwidth pressure
- Small-GEMM behavior
- Scheduler overhead
- Communication on the critical path

A configuration may be best for prefill and poor for decode. Avoid collapsing the two regimes into one unexplained number.

## 6. Warm-up policy

Warm-up must cover:

- Model loading
- CUDA context creation
- Kernel compilation
- Graph capture
- Memory-pool stabilization
- Runtime autotuning
- Representative sequence lengths
- Representative batch sizes

Do not include compilation or one-time initialization in steady-state latency unless cold-start behavior is the explicit research question.

Document the exact warm-up count and conditions.

## 7. Measurement windows and repetitions

For each configuration:

- Run enough requests to reach stable behavior
- Repeat the complete run independently
- Record every repetition
- Report central tendency and dispersion
- Prefer confidence intervals or bootstrap intervals
- Investigate outliers rather than silently deleting them

A reasonable initial policy is at least five independent repetitions, adjusted upward when variance is high.

## 8. Synchronization and timing

Use the correct timing mechanism for the scope:

- End-to-end wall time for user-visible latency
- CUDA events for isolated GPU regions
- Nsight Systems for cross-thread and CPU/GPU timelines
- Nsight Compute for kernel-level metrics

Avoid adding unnecessary global synchronization that changes runtime behavior.

State where synchronization occurs.

## 9. Metrics

### Latency

- TTFT
- ITL
- End-to-end latency
- p50
- p95
- p99
- Maximum observed latency when useful

### Throughput

- Requests/s
- Prompt tokens/s
- Generated tokens/s
- Total tokens/s

### Resource use

- Peak allocated memory
- Peak reserved memory
- KV-cache memory
- GPU utilization
- SM occupancy
- HBM bandwidth
- Power and energy where available
- CPU utilization
- Host-to-device traffic

### Distributed behavior

- Collective latency
- Algorithm bandwidth
- Bus bandwidth
- Exposed communication time
- Hidden communication time
- Scaling efficiency

### Quality

- Perplexity
- Task accuracy
- Output agreement
- Numerical error
- Application-specific quality metric

## 10. Scaling efficiency

For `N` GPUs:

```text
scaling_efficiency(N) = throughput(N) / (N × throughput(1))
```

State whether the denominator uses the same workload, global batch, per-GPU batch, latency target, and memory constraints.

Strong scaling and weak scaling must not be mixed.

## 11. Fair comparisons

A fair comparison requires:

- Same model and revision
- Same input and output distribution
- Same quality target
- Same request completion criteria
- Equivalent batching opportunity
- Equivalent precision or explicit quality tradeoff
- Equivalent cache state
- Comparable memory limits
- Similar warm-up state

Runtime-specific optimizations are allowed, but they must be disclosed.

## 12. Correctness gates

A performance result is invalid until correctness passes.

Kernel tests should include:

- Reference comparison
- Representative and adversarial shapes
- Multiple dtypes
- Tolerance justification
- NaN and infinity behavior
- Non-contiguous inputs where supported
- Boundary sizes
- Determinism expectations

Quantized-model studies should include a quality gate chosen before measuring speed.

## 13. Profiling requirements

A major optimization claim should include at least one of:

- Nsight Systems timeline
- Nsight Compute kernel report
- PyTorch Profiler trace
- Runtime-native trace
- NCCL performance data

Profiler collection can perturb performance. Use profiling runs to explain behavior and non-profiled runs for headline numbers unless the overhead is proven negligible.

## 14. Raw results and provenance

Raw results must be:

- Machine-readable
- Immutable after publication
- Linked to a Git commit
- Associated with one configuration
- Rich enough to regenerate all summary tables and figures

Suggested fields:

```json
{
  "run_id": "uuid",
  "timestamp_utc": "ISO-8601",
  "git_commit": "sha",
  "hardware": {},
  "software": {},
  "model": {},
  "workload": {},
  "runtime": {},
  "metrics": {},
  "correctness": {},
  "artifacts": {}
}
```

Derived tables and figures belong in `results/summarized/` and `results/figures/`.

## 15. Interpretation standard

Separate:

1. **Measurement** — directly observed
2. **Inference** — explanation supported by evidence
3. **Hypothesis** — plausible but unverified
4. **Limitation** — what the experiment cannot establish

Avoid causal language when only correlation was measured.

## 16. Negative results

Publish a negative result when:

- The hypothesis was reasonable
- The experiment was fair
- Correctness passed
- The profiler explains why the optimization failed
- The result changes future engineering decisions

A polished null result is more credible than an unexplained speedup.

## 17. Reproduction checklist

Before publishing:

- [ ] Clean-checkout command works
- [ ] Environment is pinned
- [ ] Model and dataset revisions are pinned
- [ ] Warm-up is documented
- [ ] Repetitions are sufficient
- [ ] Tail latency is reported
- [ ] Correctness passed
- [ ] Raw results are committed or archived
- [ ] Figures regenerate from scripts
- [ ] Profiler evidence supports the explanation
- [ ] Limitations are explicit
- [ ] No employer-confidential material is present
