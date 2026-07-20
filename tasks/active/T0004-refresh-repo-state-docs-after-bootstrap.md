---
id: T0004
title: Refresh repository-state and two-agent workflow documentation
type: implementation
status: ready
created: 2026-07-20
depends_on: [T0001]
related_issue: null
requires_approval: false
---

# Task T0004: Refresh repository-state and two-agent workflow documentation

## Outcome

Repository instructions consistently describe both the bootstrapped Python project and the
two-agent authority boundary: Codex may author/refine tasks, write its own A2A messages, and
promote a selected task from `backlog/` to `active/`; Claude performs implementation and every
later task lifecycle transition.

## Context

Read before implementation:

- Completed task `tasks/completed/2026/T0001-bootstrap-python-project.md`
- Codex review `workspace.local/a2a/codex-2026-07-20-t0001-review.md` (the three non-blocking
  observations recorded there are the source of this task)
- `CLAUDE.md`, especially the "What this is" state description
- `AGENTS.md`, especially the division of labor and task handoff protocol
- `README.md`, especially "Repository layout" and "Development setup"
- `pyproject.toml`

T0001 added an importable `benchmark` package, `pyproject.toml`, and `tests/`, plus the `tasks/`
workflow. Codex explicitly deferred these documentation refreshes out of T0001 to avoid
retroactively expanding that task; this task captures them.

The operator clarified on 2026-07-20 that promoting a ready task from `tasks/backlog/` to
`tasks/active/` is an allowed Codex planning action. This is the only task lifecycle move Codex
may perform. Claude remains responsible for setting execution/completion status and moving tasks
from `active/` to `blocked/` or `completed/<year>/`.

## In scope

- Update `CLAUDE.md` so the repository-state text describes the completed bootstrap (importable
  package, packaging config, tests) instead of "no implementation code exists," and identifies
  T0002 and T0003 as planned follow-on work.
- Align `AGENTS.md` and `CLAUDE.md` on the exact two-agent authority boundary:
  - Codex may author and refine task files, write its own A2A messages, select the next task, and
    promote that task from `tasks/backlog/` to `tasks/active/`.
  - Codex does not implement tasks or edit code, project documentation, configuration, results,
    or another agent's A2A messages.
  - Claude performs implementation and all subsequent task state/lifecycle changes, including
    `ready` to `in_progress`, `active/` to `blocked/`, and accepted work to
    `completed/<year>/` with status `done`.
  - Remove or qualify absolute statements such as "Codex performs no task lifecycle moves" and
    "Claude is the only agent that touches the repo" so they do not contradict the permitted
    `backlog/` to `active/` promotion.
- Update the `README.md` "Repository layout" tree to include `pyproject.toml`, `benchmark/`,
  `tests/`, and the `tasks/` workflow, and stop describing `benchmark/` as not yet added while
  keeping still-planned implementation directories clearly marked as planned.
- Remove or de-couple the lifecycle-dependent task path in the `pyproject.toml` comment: refer to
  task ID `T0001` without embedding its current lifecycle directory (it now lives under
  `tasks/completed/2026/`).

## Out of scope

- Any change to `benchmark/`, `tests/`, or the packaging behavior established by T0001
- New runtime or development dependencies
- The config model (T0002) and result schema (T0003)
- Broader documentation rewrites beyond the state/layout accuracy fixes above
- Giving Codex authority to implement tasks, edit ordinary project files, mark work complete,
  move active tasks to `blocked/` or `completed/`, or edit Claude's A2A messages

## Deliverables

- Edited `AGENTS.md`
- Edited `CLAUDE.md`
- Edited `README.md`
- Edited `pyproject.toml` comment

## Design constraints

- Documentation only plus one code comment; no behavior change.
- Do not reintroduce infrastructure identifiers into committed files.
- Keep the distinction between the now-existing `benchmark` package and still-planned
  implementation directories explicit.
- State the Codex `backlog/` to `active/` exception narrowly and identically in both agent
  instruction files; do not weaken Claude's ownership of execution and closure.

## Acceptance criteria

- [ ] `AGENTS.md` and `CLAUDE.md` both state that Codex may promote a selected ready task from
  `tasks/backlog/` to `tasks/active/` as a planning action.
- [ ] Both files state that Claude owns implementation plus every lifecycle/status change after
  activation, including blocking and completion.
- [ ] Neither file contains an unqualified statement that Codex performs no lifecycle moves or
  that Claude is the only agent that ever changes any repository file.
- [ ] No committed file states that the repository has no implementation code.
- [ ] `README.md` repository layout lists `pyproject.toml`, `benchmark/`, `tests/`, and `tasks/`,
  and no longer says `benchmark/` will be added later.
- [ ] `pyproject.toml` contains no reference to a lifecycle-specific task directory path.
- [ ] All T0001 quality checks still pass (`python -m pytest`, `python -m ruff check .`).

## Validation

```bash
python -m pytest
python -m ruff check .
rg -n "no .*implementation code" CLAUDE.md
rg -n "tasks/active/T0001" pyproject.toml
rg -n "no task lifecycle moves|only agent that (changes|touches) the repo" AGENTS.md CLAUDE.md
```

The three `rg` commands above should return no matches. Manually compare the authority boundary
in `AGENTS.md` and `CLAUDE.md` to ensure the same exception and restrictions appear in both.

## Completion record

- Status: Not started
- Files changed:
- Commands run:
- Evidence:
- Deviations from task:
- Follow-up tasks:
