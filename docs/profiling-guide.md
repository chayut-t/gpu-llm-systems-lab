# Profiling Guide

## Profiling philosophy

Start with a question, not a profiler.

Bad workflow:

1. Capture a huge trace
2. Search for something unusual
3. Invent an explanation

Preferred workflow:

1. Observe a performance regime
2. Form a hypothesis
3. Select the minimum evidence needed
4. Profile a representative run
5. Confirm or reject the hypothesis
6. Re-run headline benchmarks without profiler overhead

## Tool selection

| Question | Primary tool |
|---|---|
| Where is end-to-end time spent? | Nsight Systems |
| Are CPU gaps or synchronizations limiting execution? | Nsight Systems |
| Which kernels dominate? | Nsight Systems, runtime trace |
| Why is one kernel slow? | Nsight Compute |
| Is a kernel bandwidth- or compute-limited? | Nsight Compute |
| Is PyTorch dispatch or graph breaking important? | PyTorch Profiler, compilation logs |
| Is communication scaling poorly? | NCCL Tests, Nsight Systems |
| Is the scheduler creating queueing or bubbles? | Runtime telemetry plus Nsight Systems |

## Nsight Systems workflow

Use Nsight Systems to inspect:

- CPU launch cadence
- CUDA API calls
- Kernel sequence
- Synchronization
- Memory copies
- NCCL collectives
- Stream concurrency
- GPU idle intervals
- Graph capture and replay
- Request-level annotations

### Capture narrowly

Prefer a short, representative steady-state interval over model startup plus thousands of requests.

Use NVTX ranges to mark:

- Request
- Prefill
- Decode step
- Scheduler iteration
- Collective
- KV-cache operation
- Backend-specific phases

### Questions to answer

- Is the GPU continuously busy?
- Are kernels separated by CPU gaps?
- Are collectives serialized with compute?
- Are memory copies on the critical path?
- Does decode show many small launches?
- Does continuous batching create efficient work or scheduler overhead?
- Is tail latency associated with queueing, synchronization, or long kernels?

## Nsight Compute workflow

Profile selected kernels, not the entire application.

Start with:

- Kernel duration
- Achieved occupancy
- SM throughput
- DRAM throughput
- L2 behavior
- Warp stall reasons
- Register count
- Shared-memory use
- Launch dimensions
- Instruction mix

### Roofline reasoning

Classify the kernel using arithmetic intensity and achieved throughput.

Potential outcomes:

- Bandwidth-bound: reduce bytes moved, improve coalescing, fuse operations
- Compute-bound: improve instruction efficiency, tensor-core use, or algorithm
- Latency-bound: increase parallelism or reduce dependencies
- Launch-bound: fuse work or capture graphs
- Occupancy-limited: reduce registers/shared memory or change mapping

Do not equate low occupancy with poor performance automatically. Some efficient kernels intentionally trade occupancy for instruction or data-reuse advantages.

## Kernel comparison protocol

For each implementation:

- Same inputs
- Same outputs
- Same dtype
- Same correctness tolerance
- Same device
- Warmed-up code
- Multiple shapes
- Multiple repetitions
- Distribution, not only minimum latency

Report:

- Median latency
- Tail or dispersion
- Effective bandwidth where meaningful
- Estimated bytes moved
- Achieved bandwidth
- Registers/thread
- Occupancy
- Numerical error

## Distributed profiling

Separate:

- Collective duration
- Time overlapped with useful compute
- Time still exposed on the critical path

A shorter collective is not the only path to speedup. Better scheduling may hide the same collective.

For NCCL:

- Measure isolated collective behavior with NCCL Tests
- Compare isolated bandwidth to application behavior
- Inspect message size
- Inspect topology
- Inspect stream placement
- Inspect dependencies before and after the collective

## Profiling artifacts

Store reports outside Git when they are too large, but keep:

- Capture command
- Tool version
- Target process
- Time window
- Configuration
- Exported summary
- Screenshot or small excerpt used in the report
- Stable artifact location

Never publish traces containing confidential paths, hostnames, tokens, model inputs, or employer data.

## Common mistakes

- Profiling cold start when claiming steady-state performance
- Profiling a different shape from the headline result
- Leaving debug logging enabled
- Comparing one profiled run to one unprofiled run
- Treating utilization as a sufficient explanation
- Ignoring CPU and scheduler behavior
- Assuming the longest kernel is the best optimization target
- Measuring a microkernel improvement that does not affect end-to-end latency
