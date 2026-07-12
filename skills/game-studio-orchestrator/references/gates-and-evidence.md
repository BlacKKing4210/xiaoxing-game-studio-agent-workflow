# Gates And Evidence

## Three States

- `READY`: sources, Skills, scope, baselines, locks, and acceptance are sufficient for the next authorized action.
- `CONCERNS`: a recoverable mismatch or incomplete proof exists; unsafe continuation is paused.
- `NOT READY`: a required source, Skill, identity, dependency, baseline, or authorization is absent or conflicting.

Add a lifecycle or runtime qualifier when useful, such as `READ_ONLY`, `AUTHORIZED`, `DEV_PREVIEW`, `NOT_RUNTIME`, `FORMAL_RUNTIME`, `COMPLETE`, or `ARCHIVED`.

## Evidence Hierarchy

Prefer, in order:

1. normal player-visible behavior through the real business path;
2. scoped accelerated behavior that preserves the real path;
3. deterministic file, manifest, schema, or pixel evidence;
4. static inspection;
5. process exit status.

Lower evidence cannot replace higher evidence when the acceptance item is player behavior.

## Baselines

Use hashes, commit IDs, asset manifests, or explicit versions. A status-only scope update should not invalidate unrelated work; changes to objectives, write scopes, owners, contracts, locked inputs, shared files, or acceptance do.

## Shared Files

Every shared runtime file has one writer at a time. Parallel tasks may proceed only with disjoint write scopes or explicit sequencing. A lock is released after acceptance, cleanup, and archive.

## Temporary Boundaries

Profiles, caches, logs, screenshots, test mirrors, render outputs, and QA evidence live in a task-local temporary root. Snapshot formal editor/user directories before and after runtime QA when contamination is possible.
