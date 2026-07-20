# AGENTS.md

Guidance for Codex and other coding agents working in this repository.

## What this is

**GPU LLM Systems Lab** — a reproducible, profiler-driven laboratory for understanding and
optimizing LLM inference across NVIDIA GPU architectures. See `README.md` for the research
question and `docs/` for the authoritative design (`architecture.md`, `methodology.md`,
`hardware-matrix.md`, `profiling-guide.md`, `roadmap.md`).

## Division of labor: Codex authors tasks, Claude executes them

This project uses a two-agent workflow:

- **Codex (you) is the task author / planner.** Codex creates and refines task files under
  `tasks/`, reviews completed work, and decides what to do next. When you create a task, follow
  `tasks/README.md` and the templates in `tasks/templates/`: state one observable outcome,
  in/out of scope, deliverables, acceptance criteria, and validation. Put new tasks in
  `tasks/backlog/` as `proposed`, refine to `ready`, and promote the selected one to
  `tasks/active/` (normally exactly one active task).
- **Claude Code is the task executor.** Claude implements `tasks/active/<file>.md` within its
  stated scope, runs the acceptance checks, and fills in the completion record. Claude records
  newly discovered work as follow-up tasks rather than expanding scope.

When you hand a task to Claude, the task file *is* the contract — make its scope and acceptance
criteria unambiguous before promoting it to `active/`.

## Agent-to-agent communication

`workspace.local/` is the local workspace directory for this project. Use it for temporary
working material, notes, and coordination artifacts that should remain local. The directory is
git-ignored; do not commit its contents or treat anything in it as a reproducible project output.

Use `workspace.local/a2a/` specifically for local Markdown messages between agents.

- Codex messages must be named
  `workspace.local/a2a/codex-<date>-<descriptive-name>.md`.
- Claude Code messages must be named
  `workspace.local/a2a/claude-<date>-<descriptive-name>.md`.

Use ISO dates (`YYYY-MM-DD`) and a concise descriptive filename component. When picking up work,
read the most recent context file first (see below) and check `workspace.local/a2a/` for pending
messages.

## Session handoff files

Two more `workspace.local/` subdirectories hold session-handoff files (written by Claude Code's
`/create-context-and-worklog` skill; also git-ignored):

- `workspace.local/worklogs/worklog-<YYYYMMDD>.md` — backward-looking record of what a session did.
- `workspace.local/contexts/claude-context-<YYYYMMDD>.md` — forward-looking resume brief for the
  next session.

## GPU / infrastructure

GPU experiments run on remote compute, not this laptop. Infra-specific details (cluster, queues,
pods, FSx paths) live only in the git-ignored `docs/infrastructure.local.md` and
`CLAUDE.local.md` — never in committed files, tasks, or prose. Tasks that provision resources or
run paid experiments must follow the safeguards in `tasks/README.md` (approval gate, cost/time
ceilings, teardown confirmation).
