---
name: create-context-and-worklog
description: >-
  Invoke ONLY via the explicit slash command /create-context-and-worklog. Writes a session
  worklog to git-ignored workspace.local/worklogs/ and a resume-context file to
  workspace.local/contexts/ for the gpu-llm-systems-lab project (two dated Markdown files,
  worklog-<date>.md + claude-context-<date>.md). Do NOT trigger this skill from natural-language
  requests, keyword matches, or as a proactive offer — even phrases like "write a worklog", "save
  a handoff", or "checkpoint the session" should NOT auto-invoke it. It runs only when the user
  explicitly types the /create-context-and-worklog command.
---

# Create context + worklog

Capture the current session into two durable Markdown files under `workspace.local/` so a fresh
Claude Code session (or the user, later) can resume without re-deriving everything. This is the
project's session-handoff format.

Run this skill **only** when the user explicitly types the `/create-context-and-worklog` slash
command. Do not invoke it from natural-language requests, keyword matches, or as a proactive
offer — if the user merely says "write a worklog" or "checkpoint this" without the slash command,
do the task directly rather than through this skill. This keeps the handoff a deliberate,
user-initiated action.

## Why two files, and how they differ

They serve different readers, so keep them distinct — don't let one become a copy of the other:

- **`worklog-<date>.md`** — a *backward-looking* record of **what happened this session**: what
  was done, why, the commits, what was deferred. It's the audit trail. A reviewer reads it to
  understand the session's changes.
- **`claude-context-<date>.md`** — a *forward-looking* **resume brief for a fresh session**:
  where things stand right now, how the repo is wired, the non-obvious gotchas that would
  otherwise bite, key decisions, and exactly what to do next. A new Claude reads *only this file*
  and should be able to continue correctly.

## Before writing: gather real facts, don't guess

The value of these files is that they're accurate, so verify against the live repo rather than
recalling from the conversation. Run:

```sh
git log --oneline -8               # recent commits (grab the exact HEAD short hash)
git status --short                 # is the tree clean? what's uncommitted?
git branch --show-current          # branch (usually main)
ls tasks/active tasks/backlog tasks/blocked   # current task-board state
```

If a Python project / test suite exists yet, capture its real state too (e.g.
`python -m pytest -q 2>&1 | tail -1`, `python -m ruff check .`) — never invent a test count. If
implementation hasn't started, say so plainly.

Pull the current phase/task status from the single sources of truth — `docs/roadmap.md` (phases)
and the `tasks/` board (`active/`, `backlog/`, `blocked/`, `completed/<year>/`) — not from
memory. Remember the division of labor: **Codex authors tasks, Claude executes them** (see
`CLAUDE.md` / `AGENTS.md`). If a task is blocked or an acceptance criterion is unmet, say so
plainly; an honest "T0001 in progress, Ruff still failing" is worth more than a rosy summary.

Also scan **`workspace.local/`** — the project's git-ignored local workspace — for artifacts a
prior session left behind, since they're invisible to a fresh session that only reads the tracked
repo. Look everywhere *except* this skill's own output dirs (`workspace.local/contexts/` and
`workspace.local/worklogs/` are the handoffs themselves, not incoming items):

```sh
find workspace.local -type f -not -path 'workspace.local/contexts/*' \
  -not -path 'workspace.local/worklogs/*' 2>/dev/null | head -50
```

The best-known such artifacts are agent-to-agent (a2a) messages under `workspace.local/a2a/` (per
`CLAUDE.md` / `AGENTS.md`: Markdown notes like `codex-<date>-*.md` / `claude-<date>-*.md`) — often
a new task Codex wants executed, or a review of completed work. Treat anything else there as in
scope too. Surface the relevant/unaddressed items in the context file's "NEXT" section (name the
file and its gist) so the resuming session knows they exist. Because the directory is git-ignored,
these files live nowhere else — if the handoff doesn't mention them, the next session won't know
they're there.

Use today's date (from the environment) for `<date>`, formatted `YYYYMMDD`, e.g.
`worklog-20260720.md`.

## Where the files go

Write each file into its dedicated git-ignored directory under `workspace.local/` (create the
directory if it doesn't exist):

- **`workspace.local/worklogs/worklog-<date>.md`** — the backward-looking session record.
- **`workspace.local/contexts/claude-context-<date>.md`** — the forward-looking resume brief.

Both live under `workspace.local/`, the project's local workspace, so they stay local and never
enter the public history — that's deliberate. Do **not** put the handoff files under `docs/`,
`tasks/`, or anywhere tracked unless the user explicitly asks to commit a handoff.

Never write cluster/queue/registry/account/host identifiers or absolute private paths into these
files — the same infrastructure non-disclosure rule that governs tracked files applies here too
(real infra detail lives only in the git-ignored `docs/infrastructure.local.md` and
`CLAUDE.local.md`).

## Handling an existing file for today

If `workspace.local/worklogs/worklog-<date>.md` (or the context file) already exists, do **not**
overwrite it and do **not** silently make a new name. Read it, then **append a new timestamped
section** so the day's notes accumulate in one file:

```markdown

---

## Update — <HH:MM local>

<the new session's content>
```

Add the same kind of appended section to the context file, but note that the context file is a
*current-state* document: the appended section should read as "here's the updated state now,"
superseding earlier sections rather than just adding history. Briefly say at the top of the new
section that it supersedes the earlier state.

## worklog-<date>.md structure

Fill sections that apply; drop ones that don't (don't pad). Keep it terse and concrete — commit
hashes, file paths, task IDs, exact counts.

```markdown
# Worklog — <date>

Project: `gpu-llm-systems-lab` (reproducible GPU LLM inference benchmarking lab).
Branch `<branch>`, HEAD `<short-hash>`, <clean|N files uncommitted>, <task/test state>.

## Summary of the session

<2-4 sentences: what this session accomplished and why.>

## <Task / workstream> — <status, e.g. "T0001 done" or "review close-out">

- <bulleted specifics: what was built/changed, with file paths, task IDs, and commit hashes>

## Repo hygiene / infra (this session)

<gitignore, infra note, tooling, plan/status edits — only if relevant>

## Not done / deferred

- <items intentionally left, with the reason (blocker, later phase, needs GPU, needs approval)>

## Next

<what the next session should pick up; point at the context file>
```

## claude-context-<date>.md structure

This is the more important file — a new session relies on it. Lead with a one-line "read this
first" framing.

```markdown
# Resume context for a new Claude Code session — <date>

Read this first if you're picking up work on `gpu-llm-systems-lab`. It tells you where things
stand, how the repo is wired, the non-obvious gotchas, and exactly what to do next.

## What this project is

<2-3 sentences: the reproducible GPU LLM inference lab; Codex authors tasks, Claude executes.>

## Current state (authoritative)

- Branch `<branch>`, HEAD `<short-hash>`, <tree state>, <task-board / test state>.
- <which roadmap phase; which tasks are active/ready/blocked/done; cite task IDs>

## Repo layout that already exists

<the directories/modules that exist now, one line each, so the reader doesn't re-discover them>

## How to work in this repo

<the real commands that currently exist (task workflow; pytest/ruff once bootstrapped) — copy
the ones in CLAUDE.md / README so they don't drift. Note the Codex-authors / Claude-executes
division and that the active task file is the controlling scope.>

## Non-obvious gotchas (will bite you otherwise)

<numbered list: stay within the active task's scope; don't weaken acceptance criteria; record
discoveries as follow-up tasks not scope creep; no infra identifiers in tracked files; read
docs/infrastructure.local.md (and the private CLAUDE.local.md) before GPU work; profiler runs
perturb headline numbers; and any new one learned this session.>

## NEXT: <the next task or phase>

<a concrete, ordered plan for what to do next, with pointers to the exact task file, roadmap
section, and source docs. Enough that a fresh session can start immediately.>
```

## After writing

Tell the user the two paths (`workspace.local/worklogs/…` and `workspace.local/contexts/…`), that
they're git-ignored (local-only, not committed), and one line on how they were verified (the
git/task facts you pulled). If you appended to an existing file rather than creating a new one,
say so.
