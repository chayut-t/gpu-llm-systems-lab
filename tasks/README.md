# Task Workflow

This directory contains small, reviewable units of work for humans and coding
agents. A task is an execution contract: it defines one outcome, its boundaries,
the evidence required to accept it, and the state needed to continue later.

Stable project design belongs in `docs/`. Research investigations belong in
`experiments/`, and publishable measurements belong in `results/`. Task files
coordinate that work without duplicating those records.

## Layout

```text
tasks/
├── README.md
├── templates/
│   ├── implementation.md
│   ├── research.md
│   ├── experiment.md
│   └── infrastructure.md
├── backlog/
├── active/
├── blocked/
└── completed/
    └── <year>/
```

Directories represent lifecycle state, not work type:

- `backlog/`: ordered candidates that are not currently being executed
- `active/`: the one selected task, either ready or in progress
- `blocked/`: tasks that cannot proceed until a recorded condition changes
- `completed/<year>/`: accepted tasks retained as project history

`active/` should normally contain exactly one task. A task waiting on external
access, approval, or infrastructure moves to `blocked/` before another task is
selected.

## Task identifiers and filenames

Use monotonically increasing identifiers and descriptive filenames:

```text
T0001-bootstrap-python-project.md
T0002-add-experiment-configuration.md
```

The identifier never changes when the file moves between lifecycle directories.
Use one of these task types unless a new reusable template is justified:

- `implementation`: code, tests, documentation, or repository configuration
- `research`: evidence gathering intended to answer a question or enable a decision
- `experiment`: a controlled measurement that tests a hypothesis
- `infrastructure`: provisioning or changing external compute and supporting systems

## Required task contract

Every task must state:

1. The outcome, phrased as one observable result
2. Context and authoritative project references
3. Work that is explicitly in and out of scope
4. Concrete deliverables
5. Acceptance criteria and validation evidence
6. Constraints, dependencies, and approval requirements
7. Completion notes recording changes, commands, evidence, and follow-ups

If a task has several independently useful outcomes, split it before execution.
Discoveries do not silently expand scope; record them as follow-up tasks.

## Lifecycle

1. Create a task from the appropriate template in `backlog/` with status `proposed`.
2. Refine it until its dependencies and acceptance criteria are unambiguous; set
   status to `ready`.
3. Move the highest-priority ready task to `active/`.
4. Set status to `in_progress` only when execution starts.
5. If it cannot continue, record the blocking condition, set status to `blocked`,
   and move it to `blocked/`.
6. After all acceptance criteria pass, fill in the completion record, set status
   to `done`, and move it to `completed/<year>/`.

Moving a task to `completed/` means its stated outcome was accepted. It does not
mean every follow-up idea was implemented.

## Using an agent

Give the agent the task file as its controlling scope. A suitable prompt is:

```text
Implement tasks/active/<task-file>.md.

Read every referenced document first. Stay within the stated scope, run all
acceptance checks, and update the completion record. Record newly discovered work
as follow-up recommendations rather than implementing it. Do not commit changes.
```

The agent must preserve unrelated working-tree changes and must not weaken an
acceptance criterion merely to make a task pass.

## Research and experiment records

A research task records the question, source standard, synthesis deliverable, and
decision it enables. Long-lived technical conclusions should be incorporated into
the appropriate document or experiment record instead of existing only in the task.

An experiment task should reference a stable directory under `experiments/` and
follow `docs/research-log-template.md`. Raw results go in `results/raw/`, derived
outputs in `results/summarized/`, and figures in `results/figures/`. Large profiler
artifacts remain external and are referenced by stable location and checksum.

## GPU and external infrastructure safeguards

Tasks that provision resources or run paid experiments must include:

- exact provider, region, instance type, GPU count, and expected topology
- estimated hourly cost, maximum cost, and maximum duration
- an explicit approval gate before provisioning or starting an expensive run
- an idempotent run identifier and exact commands
- credential and secret-handling constraints
- artifact download and checksum verification
- teardown steps and positive confirmation that billable resources are gone
- recovery steps for interruption, partial failure, and artifact upload failure

Separate preparation, approval, execution, artifact collection, and teardown in the
task. Preparing a run does not authorize provisioning or spending money.
