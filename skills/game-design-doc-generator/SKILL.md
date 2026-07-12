---
name: game-design-doc-generator
description: Generate and verify implementation-ready game design artifacts such as DOCX specifications, configuration workbooks, diagrams, UI requirement briefs, and art requirement lists from an approved system brief. Use when the requested output is a formal document package rather than only design reasoning. Project rules and values must be supplied by formal sources.
---

# Game Design Doc Generator

Generate artifacts from one approved source of truth. Use game-system-delivery-pipeline first when the system itself is not yet implementation-ready.

## Required Inputs

- approved objective, scope, non-goals, owner, and acceptance criteria;
- project formal sources and output locations;
- required artifact list;
- engine/runtime terminology when implementation diagrams are needed;
- unresolved items explicitly marked pending.

## Workflow

1. Read references/gdd-package-spec.md and the caller-supplied project sources.
2. Build one compact content model for rules, states, data, UI, art, implementation, and QA.
3. Generate only the artifacts requested by the task contract.
4. Keep document text, spreadsheet fields, diagrams, UI requirements, and art requirements consistent with the same content model.
5. Use documents for DOCX work and render every final DOCX for visual QA.
6. Use spreadsheets for workbooks and verify formulas, references, sheet names, text fit, and visual layout.
7. Use editable diagrams or regenerable source when flowcharts are required.
8. Label assumptions and unresolved decisions; do not promote them to formal rules.
9. Remove temporary renders, inspect caches, duplicate exports, and unused drafts.

## Quality Gate

- A programmer can identify states, data sources, events, edge cases, and allowed changes.
- A numerical designer can identify tunable fields, ownership, and initial-value rationale.
- A UI or art executor can identify runtime purpose, priority, state, format, and references.
- QA can derive normal, boundary, empty, full, interrupted, failure, and regression checks.
- All delivered artifacts agree with each other and with the formal source.

Do not write project-specific corrections directly into this Skill. Submit reusable method changes through the repeated-validation and lead-owner review process.
