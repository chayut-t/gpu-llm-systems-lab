---
id: TXXXX
title: <Concise infrastructure outcome>
type: infrastructure
status: proposed
created: YYYY-MM-DD
depends_on: []
related_issue: null
requires_approval: true
---

# Task TXXXX: <Title>

## Outcome

State the infrastructure capability or state this task should produce.

## Context

List the experiment, project documents, existing resources, and constraints that
justify the change.

## In scope

- <Resource or configuration change>

## Out of scope

- <Related infrastructure change intentionally excluded>

## Target environment

- Provider and account scope:
- Region or availability zone:
- Instance type and count:
- GPU model, count, and expected topology:
- Storage and networking:
- Required images or software:

## Security and confidentiality

- Credential source and least-privilege boundary:
- Secret-handling requirements:
- Permitted data and model sources:
- Logging and redaction requirements:

Never place credentials, account identifiers, private hostnames, or confidential
data in the task file, command logs, or committed artifacts.

## Cost, duration, and approval

- Estimated hourly cost:
- Maximum total cost:
- Maximum lifetime:
- Approval required from:
- Approval evidence:

Do not create or modify paid external resources before approval is recorded.

## Procedure

### Preflight

- <Quota, credentials, configuration validation, and dry run>

### Provision or change

```bash
# Exact, idempotent commands or reference to a reviewed script
```

### Validate

- <Connectivity, topology, software, and workload smoke checks>

### Teardown or rollback

```bash
# Exact commands or reference to a reviewed script
```

State how to positively confirm that no billable or unintended resources remain.

## Failure and recovery plan

- Provisioning failure:
- Interrupted execution:
- Lost connectivity:
- Teardown failure and escalation:
- Artifact recovery:

## Acceptance criteria

- [ ] Target state is reproducible from reviewed commands or configuration.
- [ ] Access is least-privilege and secrets are absent from committed output.
- [ ] Cost and lifetime remain within the approved limits.
- [ ] Validation evidence is recorded.
- [ ] Rollback or teardown is tested or otherwise verified.
- [ ] Final resource and billing state is explicitly confirmed.

## Completion record

- Status: Not started
- Resources created or changed:
- Commands run:
- Validation evidence:
- Actual cost and duration:
- Teardown or final resource state:
- Deviations from task:
- Follow-up tasks:
