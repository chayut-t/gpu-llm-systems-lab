# CLAUDE.md

Guidance for Claude Code working in this repository.

## What this is

**GPU LLM Systems Lab** — a reproducible, profiler-driven laboratory for understanding and
optimizing LLM inference across NVIDIA GPU architectures (A100 / H100 / H200 / L4). The guiding
principle: a performance result is useful only when it is reproducible, correctly measured, and
explained by the underlying hardware and software behavior.

- `README.md` — research question, planned experiments, repository layout, reproducibility
  contract.
- `docs/` — authoritative design: `architecture.md`, `methodology.md` (the measurement
  standard), `hardware-matrix.md`, `profiling-guide.md`, `roadmap.md` (16-week / phased plan),
  `agent-assisted-development.md`, plus report/research-log templates.
- `tasks/` — the file-based task system (see below).
- `experiments/`, `results/` — investigation records and publishable artifacts (scaffolding
  only so far).

No implementation code exists yet — the first vertical slice (Python package, config model,
result schema) is defined in `tasks/`. Don't assume a module or command beyond what's tracked;
verify first.

## Division of labor: Codex authors tasks, Claude executes them

This project uses a two-agent workflow:

- **Codex is the task author / planner** — it creates and refines task files under `tasks/`
  (see `AGENTS.md`), reviews completed work, and decides what comes next.
- **Claude Code (you) is the task executor.** Your controlling scope is
  `tasks/active/<file>.md`. Read every document it references first, stay strictly within its
  stated scope, run all acceptance checks, and fill in the completion record. Record newly
  discovered work as **follow-up task recommendations** rather than implementing it. Do not
  weaken an acceptance criterion just to make a task pass. Do not commit changes unless asked.

See `tasks/README.md` for the full lifecycle (`backlog/` → `active/` → `blocked/` →
`completed/<year>/`), the task contract, and the GPU/infra safeguards. `active/` normally holds
exactly one task.

## Agent-to-agent communication

`workspace.local/` is the local workspace directory for this project — temporary working
material, notes, and coordination artifacts that should remain local. It is git-ignored; do not
commit its contents or treat anything in it as a reproducible project output.

Use `workspace.local/a2a/` for local Markdown messages between agents:

- Codex messages: `workspace.local/a2a/codex-<date>-<descriptive-name>.md`.
- Claude Code messages: `workspace.local/a2a/claude-<date>-<descriptive-name>.md`.

Use ISO dates (`YYYY-MM-DD`). Session-handoff files live in two more git-ignored subdirectories,
written by the `/create-context-and-worklog` skill:

- `workspace.local/worklogs/worklog-<YYYYMMDD>.md` — backward-looking record of a session's work.
- `workspace.local/contexts/claude-context-<YYYYMMDD>.md` — forward-looking resume brief; read
  the most recent one first when resuming, and check `workspace.local/a2a/` for pending messages.

## Things worth keeping in mind

- **Reproducibility is the product.** Every published result must record hardware, software
  versions, model/tokenizer revisions, workload, warm-up, repetitions, and uncertainty
  (`README.md` reproducibility contract, `docs/methodology.md`).
- **Separate measurement from interpretation.** Keep measured facts, evidence-backed inference,
  and hypotheses distinct; an agent-generated explanation is not evidence
  (`docs/agent-assisted-development.md`).
- **Profiler runs perturb performance.** Use profiling runs to explain behavior and non-profiled
  runs for headline numbers (`docs/methodology.md` sec 13).
- **Public-only inputs.** Use only public models, datasets, and algorithms; no
  employer-confidential code, data, or infrastructure identifiers in committed files.

## GPU / infrastructure

GPU experiments run on remote compute, not this laptop. **Before launching or driving any GPU
run, read `docs/infrastructure.local.md`** — it holds the target cluster/queues (multi-queue,
one per GPU architecture), launch commands, and gotchas, along with the relevant cluster skill
and config-directory conventions. Those infra files are git-ignored so cluster/queue/pod details
stay out of the public repo — never put them in committed files or prose. CPU-only work
(aggregation, plotting, tests, analysis) runs locally. See `CLAUDE.local.md` for the private
pointers.
