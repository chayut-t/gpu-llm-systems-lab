# Results

This directory contains small, publishable result artifacts.

```text
results/
├── raw/          # Machine-readable benchmark outputs
├── summarized/   # Derived tables
└── figures/      # Regenerable charts and compact profiler excerpts
```

## Rules

- Raw results are immutable.
- Every file must identify the producing repository commit.
- Derived outputs must be reproducible from raw data.
- Do not commit model weights, large traces, secrets, or confidential information.
- Large public artifacts should be stored externally with a stable reference and checksum.
- A published figure must have a script that regenerates it.
