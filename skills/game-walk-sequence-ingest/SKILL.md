---
name: game-walk-sequence-ingest
description: Convert character action video or frame sources into normalized transparent game animation sequences, previews, manifests, and runtime-ready configuration. Use for walk, idle, attack, hurt, death, or similar 2D action-frame ingestion. Requires a caller-supplied project profile or task contract for naming, canvas, baseline, archive, registry, and runtime integration rules.
---

# Game Walk Sequence Ingest

Treat extraction, visual approval, formal archival, and runtime integration as separate gates.

## Inputs

Require:

- source video or frame set;
- confirmed character identity and action name;
- canvas, scale, center, foot baseline, facing, FPS, loop rule, and frame-count target;
- formal archive and runtime naming rules;
- runtime registry/data contract when integration is authorized.

Do not infer project paths, character identity, or engine files from examples.

## Workflow

1. Probe frame count, FPS, duration, dimensions, background, duplicate cycles, and action boundaries.
2. Produce a source-timing contact sheet or short preview. Keep this output outside formal/runtime directories until approved.
3. Identify one complete action range before sampling any output frames. For looping actions, use one clean cycle between equivalent poses or contacts. For non-looping actions, use one complete passage from preparation through recovery.
4. Record the selected start frame/time, end frame/time, duration, and selection reason. Omit a duplicate closing frame for loops.
5. Sample the target frame count only inside that selected action range and preserve chronological order. Never distribute target frames across the whole source clip merely to reach a requested count.
6. Remove the background, clean edge spill, preserve effects, and normalize all frames to one supplied canvas and baseline.
7. Verify frame-to-frame scale, center, facing, foot stability, transparent margins, chronological motion, and loop continuity.
8. Produce numbered PNGs plus exactly the requested user-facing previews. Add a manifest when more than one output class exists.
9. After visual approval, archive the sequence with official identity and action naming.
10. Only after explicit program authorization, update the project registry and engine loader using the project-owned data contract. Do not assume particular engine scripts.
11. Run path/reference checks and an engine smoke test when runtime integration occurred.

## Cycle Gate

Do not extract a game sequence until the complete action range is identified.

Require each preview manifest to record:

- `action_range_start_frame` and `action_range_end_frame`;
- `action_range_start_seconds`, `action_range_end_seconds`, and `action_range_duration_seconds`;
- `action_range_kind`: `loop_cycle` or `complete_non_looping_action`;
- `sampling_scope`: `selected_action_range_only`;
- source frame indices in strictly increasing order.

For walk and other cyclic motion, verify the same foot/contact phase at both boundaries and remove the duplicate closing pose. If a clean cycle cannot be identified confidently, stop and request review instead of sampling the whole video.

## Preview, Classification, and Scale

- Default user-facing review to two previews: normalized game timing and the selected source-action timing. Keep diagnostic variants out of the review surface unless requested.
- Classify the action from the character's primary body motion. Secondary motion from clothing, carried objects, weapons, or effects must not override the body action.
- Use the character body as the scale anchor. Do not shrink the character merely because a carried object, weapon arc, or effect expands the full alpha bounds.
- Record actual frame durations and total playback time for reviewed previews, not only a speed multiplier.

## Task-Local Tools

Keep source paths, batch IDs, reviewed frame ranges, current output paths, and one-off rebuild scripts with the task output. Do not bundle them into this Skill. Promote a script into the Skill only after it is parameterized, free of project or batch data, repeatedly validated, and still materially improves reliability.

## Stop Conditions

Stop before frame extraction when the complete action range is missing or uncertain. Stop before formal ingest when identity is uncertain, the action does not fit the supplied canvas, the loop has visible discontinuity, chronological motion appears reversed, style differs from approved same-use assets, or integration requires an unapproved shared-file change.

## Completion Evidence

Report source, selected action range and duration, boundary poses or contacts, sampled source-frame indices, frame count, FPS, loop behavior, dimensions, baseline variance, output paths, visual approval, registry changes, runtime test, risks, and temporary-file cleanup.
