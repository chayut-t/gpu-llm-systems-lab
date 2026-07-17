# Hardware Matrix

## Purpose

Performance conclusions are conditional on hardware generation, memory system, interconnect, and software support. This document defines the expected emphasis for each likely environment.

## Candidate AWS environments

| Instance family | Representative GPU | Typical research emphasis |
|---|---|---|
| `p4d` / `p4de` | A100 | BF16, INT8/INT4, NVSwitch scaling, bandwidth-bound kernels |
| `p5` | H100 | Native FP8, Transformer Engine, high-throughput TensorRT-LLM |
| `p5e` / `p5en` | H200-class configurations | Larger HBM capacity, long context, high-bandwidth multi-GPU serving |
| `g6` | L4 | Cost-aware serving, memory constraints, quantization, lower-power inference |

Exact instance specifications must be captured at run time rather than inferred from the family name.

## A100 emphasis

Good questions:

- When does weight-only INT4 improve decode throughput?
- Which fused memory-bound operators benefit most from reduced HBM traffic?
- How well does tensor parallelism scale across the node?
- How much communication can be hidden during prefill?
- Where do small decode GEMMs lose efficiency?

Avoid:

- Native FP8 speed claims
- Generalizing one-node NVSwitch results to multi-node networking
- Assuming memory savings imply latency savings

## H100/H200 emphasis

Good questions:

- Native FP8 versus BF16 by workload regime
- Transformer Engine integration
- Tensor Memory Accelerator and newer kernel strategies where applicable
- Larger-context serving enabled by HBM capacity
- TensorRT-LLM performance across attention and GEMM paths
- Communication overlap at higher compute throughput

Be careful that faster compute can make communication and scheduling more visible.

## L4 emphasis

Good questions:

- Quantization under memory pressure
- Small- and medium-model serving
- Latency at modest concurrency
- Throughput per dollar
- Throughput per watt where measurement is reliable
- PCIe-only or limited-interconnect scaling
- Runtime overhead relative to GPU compute

Do not compare L4 and datacenter accelerators using only peak throughput. Include cost, power, model size, latency target, and deployment constraints.

## Cross-hardware comparison rules

A cross-hardware study must answer one of two clearly different questions:

### Equal-workload comparison

Run the same model, precision, workload, and quality target.

This measures absolute behavior but may not use each device optimally.

### Best-valid-configuration comparison

Tune each device independently while preserving the application-level objective and quality target.

This measures deployment potential but introduces more configuration differences.

Do not mix these interpretations in one chart.

## Required topology capture

For every multi-GPU run, record:

- GPU count
- Peer-access matrix
- NVLink/NVSwitch availability
- PCIe topology
- NUMA placement
- NCCL topology output where appropriate
- Container and host networking
- EFA or other network adapter for multi-node runs

Hardware names alone are insufficient.
