---
name: game-studio-orchestrator
description: Set up, operate, resume, or audit a producer-led multi-agent game studio workflow. Use for new or existing Godot, Unity, Unreal, web, or document-first game projects that need role ownership, short-lived execution tasks, Skills, write locks, evidence gates, playable previews, monitoring, lossless stuck-task replacement, handoff, or feature-level progress tracking.
---

# Game Studio Orchestrator

Run the project as a small accountable studio. Optimize for visible game progress without weakening source control, write ownership, evidence, or cleanup.

## Start Or Resume

1. Locate the project root, engine, stage, Profile, workflow, active scope, PM handoff, and feature progress workbook.
2. Stay read-only until the formal sources are readable and the current accountable producer is known.
3. If this is a new project, instantiate the repository templates and create the initial feature matrix.
4. If this is a resumed project, continue from current receipts and file baselines. Do not replay completed work or copy old chats.
5. Keep exactly one accountable producer. Role owners and execution operators are not additional producers.

Read [workflow.md](references/workflow.md) for the full operating sequence.

## Roles

- **Producer/PM**: priority, cross-role ordering, shared write windows, final status, and producer communication.
- **Design owner**: functional rules, numeric/config contracts, non-goals, and design acceptance.
- **Engineering owner**: technical contracts, shared-file ownership, implementation slices, and runtime acceptance.
- **Art owner**: art contracts, final-quality assets, visual direction, and handoff boundaries.
- **PM execution operator**: read-only monitoring, evidence collection, workbook refresh, and exception reporting.
- **Execution tasks**: short-lived production workers with one contract, one primary Skill, one write scope, and a close condition.

Role owners may create, authorize, retry, and archive execution tasks in their domain. They must notify the producer after creation or material state changes.

## Work Selection

Use the feature progress workbook as the advancement queue:

1. Higher priority first.
2. Same priority: ascending feature ID.
3. Completed features last.
4. Skip only for an unmet dependency, shared write conflict, or safety blocker; record the reason.

A complete feature row is backed by a functional document plus a numeric/configuration source, or by a producer directive filed into a formal source.

Read [progress-matrix.md](references/progress-matrix.md) when creating or refreshing the workbook.

## Task Gate

Every production task requires:

1. goal, scope, non-goals, accountable owner, dependencies, allowed files, source baselines, acceptance, evidence, cleanup, and close conditions;
2. a project-context adapter and one primary domain Skill;
3. a first read-only receipt proving the task loaded its contract, Skills, sources, write scope, locks, and baselines;
4. independent owner review and explicit write authorization;
5. a completion receipt mapping acceptance items to behavior or asset evidence.

Contract readiness is not execution readiness. Missing Skills, ambiguous sources, or conflicting baselines make the task not ready.

Read [gates-and-evidence.md](references/gates-and-evidence.md) for gate states and evidence rules.

## Fast Visible Progress

- Design hands implementation-ready boundaries directly to engineering.
- Art and engineering proceed in parallel when write scopes do not conflict.
- If final art exists, use the complete final asset.
- If final art does not exist, engineering may use a clearly marked development placeholder.
- UI may use temporary visuals. Non-UI art should target final quality from first production.
- Once an asset passes minimum mechanical checks, place it in a development preview unless the producer explicitly requests an art review first.
- A preview is not a release. Preserve `dev_only`, `not_runtime`, and `replace_before_release` markers.

Read [art-engineering.md](references/art-engineering.md) for the parallel delivery model.

## Monitoring And Replacement

- Monitor only the current assigned batch on a short interval.
- Refresh the feature workbook on a slower interval or on explicit producer request.
- Normal checks remain quiet. Report exceptions, playable previews, decisions, and completion.
- Detect real stalls using missing outputs, absent tool/process activity, stale receipts, and file progress, not only a task's UI status.
- For a stuck long-lived role or execution task, create a read-only candidate, verify handoff, switch ownership, then archive the old task. Never allow two writers during replacement.

Read [role-lifecycle.md](references/role-lifecycle.md) and [monitoring.md](references/monitoring.md).

## Source And Token Discipline

- Project facts live in the Profile, contract, active scope, formal documents, and configuration tables, not in generic Skills.
- Unchanged sources are verified by index and hash instead of repeatedly loaded in full.
- Expand only anomalies and changed requirements.
- Prefer manifests, tables, and deterministic checks over narrative repetition.
- Quality, gates, QA, and real behavior evidence are never reduced to save tokens.

## Close

Before closing a task:

1. verify authorized files only;
2. map acceptance to real evidence;
3. run scoped regression;
4. confirm no candidate or placeholder leaked into release paths;
5. remove task-local caches, logs, screenshots, mirrors, and temporary files;
6. return shared locks;
7. archive the execution task;
8. select the next ready feature from the progress workbook.
