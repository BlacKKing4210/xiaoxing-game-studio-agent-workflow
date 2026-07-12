---
name: replace-with-project-context
description: Load and enforce the formal context for REPLACE_WITH_PROJECT. Use before any design, engineering, art, UI, QA, documentation, or asset task in this project so generic domain Skills receive the current Profile, contract, sources, scope, baselines, and gates.
---

# Project Context Adapter

Keep project facts here or in the formal Profile, never in generic domain Skills.

## Start

1. Read `REPLACE_WITH_PROJECT_PROFILE_PATH`.
2. Read the current task contract.
3. Resolve formal functional and numeric/configuration sources through the Profile.
4. Check goal, scope, non-goals, owner, dependencies, allowed files, shared locks, baselines, acceptance, evidence, and required Skills.
5. Return `READY`, `CONCERNS`, or `NOT READY` before loading the domain Skill.

## Boundaries

- Do not infer project paths, identities, values, or asset rules from the generic Skill.
- Do not accept old chat text as a current source when formal files exist.
- Do not write before the execution task's first read-only receipt is independently accepted.
- Stop on source, contract, Skill, baseline, lock, or acceptance conflict.

## Handoff

After this adapter returns READY, load the task's primary domain Skill and any required tool Skills. Pass only task-relevant project facts.
