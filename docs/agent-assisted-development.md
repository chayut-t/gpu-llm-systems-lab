# Agent-Assisted Development Policy

## Purpose

AI coding agents can accelerate implementation, but this repository is intended to demonstrate genuine systems understanding. The policy below preserves both productivity and technical credibility.

## Appropriate uses

Agents may be used aggressively for:

- Repository scaffolding
- Build-system setup
- Dockerfiles
- CI configuration
- Boilerplate backend adapters
- Test generation
- Python bindings
- Benchmark plumbing
- Data-schema implementation
- Plotting scripts
- Documentation editing
- Repetitive refactoring
- Static analysis and style cleanup

## Human-owned work

The project owner must personally understand and own:

- Research questions
- Performance hypotheses
- Experimental controls
- Correctness criteria
- Kernel decomposition
- Memory-access reasoning
- Parallelization strategy
- Profiler interpretation
- Optimization decisions
- Statistical interpretation
- Final technical claims

An agent-generated explanation is not evidence.

## Required design record

Each meaningful optimization should include:

1. **Observation**  
   What was measured?

2. **Hypothesis**  
   What mechanism could explain the observation?

3. **Proposed change**  
   What specific implementation or configuration will change?

4. **Expected effect**  
   Which metrics should move, by what direction, and why?

5. **Verification plan**  
   Which benchmark and profiler evidence will test the hypothesis?

6. **Result**  
   What happened?

7. **Interpretation**  
   Why was the hypothesis supported or rejected?

8. **Next step**  
   What experiment follows?

Use `docs/research-log-template.md`.

## Review protocol for agent-generated code

Before merging:

- Read every changed line
- Run correctness tests
- Run static checks
- Inspect generated dependencies
- Check error handling
- Verify resource cleanup
- Validate synchronization assumptions
- Confirm measurements are not perturbed
- Compare with a trusted reference
- Remove claims not supported by evidence

For CUDA and Triton code, additionally verify:

- Bounds checks
- Alignment assumptions
- Race conditions
- Dtype conversion
- Accumulation precision
- Launch dimensions
- Device synchronization
- Shape dispatch
- Numerical tolerance

## Experiment orchestration safeguards

An autonomous experiment agent must have:

- Explicit budget limits
- Allowed instance types
- Maximum duration
- Maximum concurrency
- Human approval for expensive runs
- Idempotent run identifiers
- Immutable raw results
- Full command logging
- Failure recovery
- Secret isolation
- No access to confidential employer resources

## Disclosure

It is not necessary to annotate every line written with agent assistance. The repository should instead make authorship quality visible through:

- Rigorous design notes
- Correctness tests
- Reproducible measurements
- Profiler-backed explanations
- Clear limitations
- Ability to explain every important decision

During interviews or technical discussions, be direct about where agents accelerated implementation and where the core reasoning was personally performed.
