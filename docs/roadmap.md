# Technical Roadmap

## Objective

Build a public, reproducible body of work demonstrating practical expertise in GPU kernels, inference runtimes, quantization, distributed systems, profiling, and serving architecture.

The roadmap is organized around completed technical artifacts rather than time spent. The suggested weeks are pacing guidance, not deadlines.

## Success criteria

By the end of the initial program, the repository should contain:

- A stable benchmark harness
- At least one profiler-backed runtime comparison
- One useful operator implemented in Triton and CUDA
- One quantization speed-versus-accuracy study
- One multi-GPU scaling and communication-overlap study
- A polished technical report
- At least one credible upstream issue or pull request

## Phase 0 — Repository and measurement foundations

### Deliverables

- Repository conventions
- Environment capture
- Result schema
- Hardware inventory script
- Benchmark configuration format
- Research log template
- Correctness policy
- Warm-up and repetition policy

### Exit criteria

A trivial benchmark can be run twice from a clean environment and produce comparable, machine-readable output with all required metadata.

---

## Phase 1 — Runtime benchmark harness

### Engines

- PyTorch eager
- `torch.compile`
- vLLM
- SGLang
- TensorRT-LLM

### Models

Start with one or two public dense models in the 7B–14B range. Select models with broad runtime support and stable public checkpoints. Add MoE only after the dense-model harness is reliable.

### Workload dimensions

- Input lengths: 128, 1K, 4K, 16K
- Output lengths: 32, 256, 1K
- Concurrency: 1, 4, 16, 64, saturation
- Tensor parallelism: 1, 2, 4, 8
- Static vs continuous batching
- BF16, INT8, INT4, and supported FP8
- Warm and cold model state where relevant
- Prefix reuse enabled and disabled where supported

### Metrics

- TTFT
- ITL
- End-to-end latency
- Requests/s
- Prompt tokens/s
- Generated tokens/s
- Total tokens/s
- p50/p95/p99
- Peak allocated and reserved memory
- GPU utilization
- Power and energy where available
- Scaling efficiency
- Accuracy or perplexity impact

### Required analysis

Do not stop at a throughput table. For each important result, identify the dominant regime:

- Kernel-launch-bound
- Compute-bound
- HBM-bandwidth-bound
- KV-cache-bandwidth-bound
- Communication-bound
- Scheduler- or queueing-bound
- CPU/tokenizer-bound
- Memory-capacity-bound

### Exit criteria

One end-to-end report comparing at least three engines on one GPU configuration, with reproducible commands, profiler evidence, and uncertainty estimates.

---

## Phase 2 — Profiling and bottleneck report

### Tools

- Nsight Systems
- Nsight Compute
- PyTorch Profiler
- Runtime-native metrics
- NCCL debug and tracing facilities where needed

### Deliverables

- System-wide timeline
- Kernel inventory
- CPU/GPU synchronization analysis
- Memory-allocation analysis
- Critical-path description
- Ranked optimization opportunities

### Exit criteria

A reader can see how the measured bottleneck was inferred from evidence rather than intuition.

---

## Phase 3 — Triton fused kernel

### Recommended operator

**Fused residual + RMSNorm + optional activation quantization**

Inputs:

- Hidden state
- Residual
- RMSNorm weights

Outputs:

- Updated residual
- Normalized activation
- Optional quantized activation and scale

### Why this operator

- Primarily memory-bandwidth-bound
- Multiple reads and writes can be fused
- Small enough to complete rigorously
- Directly relevant to LLM inference
- Exercises vectorized loads, reductions, fusion, and numerical stability

### Comparisons

- PyTorch reference
- `torch.compile`
- Triton
- Existing framework or runtime implementation where accessible

### Measurements

- Latency
- Achieved bandwidth
- Estimated bytes moved
- Occupancy
- Register pressure
- Warp organization
- Numerical error
- Sensitivity to token count, hidden size, and dtype

### Exit criteria

Correctness tests across representative shapes and a profiler-backed explanation of where speedup comes from—or why no speedup was achieved.

---

## Phase 4 — CUDA and CUTLASS/CuTe implementation

Implement the same operator in CUDA, using CUTLASS/CuTe when appropriate.

### Focus areas

- Coalesced and vectorized memory access
- Reduction strategy
- Thread-block and warp mapping
- Register use
- Shared-memory use
- Launch configuration
- Numerical stability
- Dispatch across shape regimes

### Exit criteria

A fair comparison among PyTorch, compiled PyTorch, Triton, and CUDA. The report must explain implementation tradeoffs, not merely identify the fastest version.

---

## Phase 5 — Quantization crossover study

### Research question

**When does quantization actually accelerate inference on a specific GPU and workload?**

### Methods

- BF16 baseline
- INT8 activation-and-weight
- Weight-only INT8
- Weight-only INT4
- SmoothQuant-style activation smoothing
- Native FP8 on supported hardware
- Multiple group sizes
- Multiple calibration-set sizes

### Report for every method

- Weight memory
- KV-cache memory
- Accuracy or perplexity
- TTFT
- Decode latency
- Throughput
- Quantize/dequantize cost
- Kernel mix
- Crossover concurrency or batch size
- Shape regimes where the method regresses

### Hardware-specific cautions

- A100: emphasize BF16, INT8, and INT4. Do not claim native FP8 acceleration.
- H100/H200: evaluate native FP8 where the runtime and kernels support it.
- L4: emphasize memory-constrained serving, lower-power inference, and smaller deployment configurations.

### Exit criteria

A report whose primary conclusion is supported by both end-to-end measurements and kernel-level evidence. A well-explained negative result is acceptable.

---

## Phase 6 — Multi-GPU communication

### Operations

- All-reduce
- Reduce-scatter
- All-gather
- All-to-all
- Point-to-point transfer where relevant

### Experiments

- 2, 4, and 8 GPUs
- Small and large message sizes
- Prefill and decode separately
- Different tensor-parallel degrees
- Communication without overlap
- Communication with overlap
- Separate compute and communication streams
- Topology-aware comparisons

### Metrics

- Algorithm bandwidth
- Bus bandwidth
- Collective latency
- Exposed communication time
- Hidden communication time
- Scaling efficiency
- GPU idle gaps
- Critical-path impact

### Exit criteria

A result that explains why overlap helps one regime but not another.

---

## Phase 7 — Distributed transformer or MoE benchmark

Build a focused inference benchmark supporting:

- Tensor parallelism
- Expert parallelism
- Asynchronous collectives
- Communication/computation overlap
- Dense or MoE layers
- Prefill and decode measurement

MoE should be added only when the dense benchmark is stable enough that all-to-all behavior can be isolated and explained.

### Exit criteria

A reproducible scaling study with a topology-aware interpretation.

---

## Phase 8 — Stretch: disaggregated serving

### Architecture

- Request router
- Prefill worker pool
- Decode worker pool
- KV-cache transfer
- Queue-length telemetry
- Static and dynamic worker allocation
- Workload simulator

### Configurations

- Colocated workers
- 4 prefill + 4 decode
- 2 prefill + 6 decode
- Dynamic reassignment

### Workloads

- Chat: moderate prompt, long output
- Retrieval: long prompt, short output
- Code generation: long prompt, long output
- Steady arrivals
- Bursty arrivals

### Questions

- When does disaggregation improve utilization?
- When does KV transfer erase the benefit?
- Which prefill/decode split minimizes tail latency?
- How robust is a static split to workload drift?
- Can queue-aware reassignment outperform a fixed policy?

### Exit criteria

A report separating scheduling benefit from data-transfer overhead.

---

## Phase 9 — Agentic performance engineer

Build an agent that operates a controlled experiment loop.

### Candidate tools

- `run_benchmark`
- `profile_with_nsys`
- `profile_kernel_with_ncu`
- `run_nccl_test`
- `compare_accuracy`
- `inspect_gpu_memory`
- `query_previous_results`
- `propose_next_experiment`

### Required safeguards

- Explicit experiment budget
- Human approval before expensive runs
- Idempotent execution
- Structured result storage
- Reproducible tool arguments
- Failure recovery
- No access to employer-confidential systems or data
- Clear separation between observation and inference

### Exit criteria

The agent can identify a bottleneck, propose a falsifiable hypothesis, execute an approved experiment, and produce a traceable report.

---

## Upstream contribution

Target projects may include:

- TensorRT-LLM
- NVIDIA Model Optimizer
- CUTLASS
- NVIDIA Dynamo
- Transformer Engine
- NCCL Tests
- vLLM or SGLang when the contribution is relevant to the study

Start narrow:

- Reproducible performance bug
- Missing regression test
- Incorrect benchmark behavior
- Profiling or observability improvement
- Documentation of confusing performance behavior
- Hardware-specific correctness issue
- Small kernel or dispatch improvement

Reference accepted contributions prominently in the README.

---

## Suggested 16-week sequence

| Weeks | Deliverable |
|---:|---|
| 1–2 | Measurement contract, environment capture, benchmark harness, BF16 baselines |
| 3–4 | Nsight profiling and bottleneck report |
| 5–7 | Triton fused kernel |
| 8–9 | CUDA or CUTLASS/CuTe implementation |
| 10–11 | Quantization crossover study |
| 12–13 | Tensor-parallel and NCCL scaling analysis |
| 14 | Communication overlap |
| 15 | Technical report, figures, and reproducibility pass |
| 16 | Upstream issue or pull request |

## Priority order

Given prior experience in PTQ, long-context inference, sparse attention, and TensorRT-LLM:

1. Serving benchmark and profiler analysis
2. Fused Triton/CUDA inference kernel
3. Multi-GPU communication-overlap study
4. Quantization speed-versus-accuracy investigation
5. Upstream TensorRT-LLM or Model Optimizer contribution

Avoid spending the opening months on generic CUDA tutorials, training a language model from scratch, a standard RAG application, or an isolated agent demo. Those projects do not provide the same signal for inference-systems roles.
