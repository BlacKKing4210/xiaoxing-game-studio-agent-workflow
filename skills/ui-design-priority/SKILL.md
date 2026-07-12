---
name: ui-design-priority
description: Prioritize, simplify, and review interface layouts before visual production or implementation. Use for UI mockups, game HUDs, menus, screen revisions, layout approval, information hierarchy, interaction-state design, or deciding what to remove. Project-specific rules, paths, values, and art direction must be supplied by a project profile or formal project documents.
---

# UI Design Priority

Make the current user decision obvious before styling the screen.

## Required Inputs

1. Identify the screen state and its single primary decision.
2. Read the task contract and any project-owned UI/art rules supplied by the caller.
3. Separate persistent state, contextual state, actions, and optional detail.
4. Stop and request owner clarification when layout authority, data ownership, or state behavior is missing.

## Workflow

1. List only the information needed to decide or act now.
2. Rank each item:
   - P0: required to act now.
   - P1: required consequence or context.
   - P2: useful on focus, selection, or detail view.
   - P3: decorative or removable.
3. Build the layout around P0 and P1. Hide, defer, or remove P2 and P3.
4. Define entry, exit, loading, empty, disabled, failure, success, and interrupted states.
5. Map every dynamic element to a data source or explicit unresolved dependency.
6. Use one component language for repeated controls and one visual hierarchy across adjacent states.
7. Check text fit, touch targets, contrast, keyboard/controller focus when relevant, and color-independent cues.
8. Produce the smallest layout that supports the approved behavior. Treat visual polish and final assets as separate gates unless the task explicitly combines them.

## Game UI Rules

- Preserve the gameplay field; treat HUD as an overlay rather than a dashboard.
- Prefer contextual controls over permanent controls.
- Use icons, portraits, grouping, position, and motion before explanatory prose.
- Keep one state image focused on one decision. Split materially different runtime states.
- Keep warnings visible but secondary unless they change the immediate decision.
- Do not invent resources, status values, controls, or systems to fill visual space.
- Do not treat generated placeholder letters or boxes as formal icons.

## Approval Output

For each screen or state, report:

- primary decision;
- P0-P3 hierarchy;
- layout regions and interaction flow;
- data sources and unresolved dependencies;
- supported states and QA checks;
- visual assets required now versus later;
- explicit removals and non-goals.

Do not write project-specific preferences back into this Skill. Put durable project rules in the project profile or formal art/UI documents.
