---
name: godot-feature-slice-implementation
description: Implement and verify a narrowly scoped, approved feature in an existing Godot project. Use when translating an implementation-ready task contract into GDScript, scene, resource, or structured-data changes with baseline checks, shared-file ownership, real behavior evidence, regression testing, and temporary-file cleanup.
---

# Godot Feature Slice Implementation

Implement one approved behavior slice without redesigning the project around it.

## Required Contract

Require the caller to provide:

- project root, Godot version or executable, and stable launch method;
- approved feature source and acceptance criteria;
- allowed and forbidden files;
- shared-file owner and starting hashes or another stable baseline;
- required player-visible behavior evidence and regression cases;
- temporary-output location and cleanup rule.

Return `NOT READY` when a required contract item is missing, formal sources conflict, a shared file has another writer, the baseline drifted, or the requested behavior requires an unapproved design decision.

## Start Gate

1. Read the task contract and relevant current files before proposing edits.
2. Confirm the project root is the authorized runtime project.
3. Verify the supplied baseline and inspect current conventions, loaders, signals, data contracts, and tests.
4. Map every acceptance item to an observable execution path. A file, field, or node merely existing is not behavior evidence.
5. Report `READY`, `CONCERNS`, or `NOT READY`, including files, conflicts, test paths, and non-goals. Do not write before `READY`.

## Implementation

- Keep the edit set within the approved slice and existing ownership boundaries.
- Prefer current data-driven contracts and helpers over parallel fallback logic or hardcoded feature branches.
- Patch shared scripts narrowly; never replace a whole shared file with a stale copy.
- Keep debug and acceptance modes explicitly disabled by default and separate from normal play.
- Apply resource precedence before creating placeholders: use an available complete matching real asset first; if the contract allows development preview, use a mechanically valid unreviewed real asset second; create a placeholder only when no matching real asset exists.
- Keep rejected and non-runtime assets out of runtime. Treat an explicitly authorized `dev_preview_ready` asset as a separate, isolated, replaceable state, never as formal art.
- Mark placeholders as development-only, record their replacement target, and replace them immediately when a matching real asset becomes available. Never show a reduced placeholder as the asset preview when the full resource already exists.
- Stop on baseline drift, scope expansion, hidden design work, or a second writer touching a shared file.

## Verification

1. Parse every changed structured-data file and verify cross-references.
2. Run the current Godot project using the supplied stable command and inspect script errors.
3. Run normal mode separately and prove it has no test preset, automatic acceptance flow, test-only state, or test-log pollution.
4. Run any explicit test entry separately, verify it is disabled by default, and exercise the real gameplay entry path for each acceptance item. Do not fake success by directly invoking a downstream callback when the behavior depends on signals, collisions, timers, UI input, or scene flow.
5. Run named regressions for adjacent sealed behavior and shared data contracts.
6. Scan forbidden fields, deprecated state, accidental runtime assets, and out-of-scope file changes.
7. Recalculate the final hashes of every allowed modified file and shared file. Confirm no unauthorized file changed; stop if the baseline changes during a long test or before handoff.
8. Remove task drivers, screenshots, caches, temporary user data, duplicate exports, and empty directories after evidence is recorded.

## Completion Evidence

Report starting and final hashes for every allowed modified file and shared file, the authorized changed-file list, confirmation that unauthorized files did not change, acceptance-to-evidence mapping, normal-mode behavior, test-mode behavior, regressions, remaining risks, shared-file impact, and cleanup result. Treat a successful engine exit as smoke evidence only, never as proof that the feature works.
