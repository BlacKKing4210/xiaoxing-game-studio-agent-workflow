---
name: game-system-delivery-pipeline
description: Turn an approved game-system brief into an implementation-ready package spanning design rules, data/configuration, UI behavior, art needs, QA evidence, and handoff. Use for system design documents, configuration tables, UI state packages, implementation planning, or acceptance preparation. Project facts and tool paths must come from formal project sources, not this Skill.
---

# Game System Delivery Pipeline

Build one coherent delivery package. Do not let design, numbers, UI, art, code, and QA drift into separate versions.

## Readiness Gate

Before production, require an approved objective, owner, formal sources, scope, non-goals, dependencies, allowed files, data ownership, acceptance criteria, and evidence plan. Mark the task NOT READY when a missing decision would force invention.

## Workflow

1. Reduce the system to one player-facing memory point and the smallest closed loop.
2. Define states, transitions, inputs, outcomes, failure paths, and interactions with existing systems.
3. Define data contracts and configuration ownership before choosing initial values.
4. Describe each UI state by decision, hierarchy, data source, interaction, edge cases, and QA checks. Use ui-design-priority for layout review.
5. List required art by runtime purpose, state, format, style source, and acceptance gate.
6. Map implementation changes to modules and shared-file risks without prescribing unauthorized architecture.
7. Build test cases for normal, boundary, empty, full, interrupted, failure, migration, and regression behavior.
8. Verify document and spreadsheet structure visually when those artifacts are delivered.
9. Remove temporary renders, inspect caches, duplicate exports, and unreferenced drafts.

## Delivery Contract

Report:

- objective and non-goals;
- formal source list and decisions still pending;
- player loop and state flow;
- data/config tables and owners;
- UI states and art requirements;
- implementation touch points and conflict risks;
- acceptance tests and observed evidence;
- cleanup and remaining risks.

Keep machine-specific software paths, project values, and current task status out of this Skill.
