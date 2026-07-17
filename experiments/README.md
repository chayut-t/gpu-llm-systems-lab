# Experiment Registry

Each experiment should have a stable identifier and a dedicated directory once implementation begins.

Suggested layout:

```text
experiments/
└── 20260101-runtime-baseline/
    ├── README.md
    ├── config/
    ├── scripts/
    ├── analysis/
    └── artifacts.md
```

Do not commit large profiler traces, model weights, or duplicated raw outputs directly to Git. Record stable external artifact locations and checksums when needed.

## Experiment index

| ID | Question | Hardware | Status | Report |
|---|---|---|---:|---|
| — | — | — | Planned | — |
