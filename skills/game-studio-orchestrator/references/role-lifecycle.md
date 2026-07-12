# Role And Task Lifecycle

## Long-Lived Role Owners

Keep producer, design owner, engineering owner, art owner, and PM execution operator visible for the life of the project. They own contracts, boundaries, monitoring, and acceptance rather than bulk production.

Each role owner maintains:

- active task IDs;
- last verified progress time;
- next check time;
- expected milestone;
- write scopes and shared locks;
- timeout and replacement action.

## Short-Lived Execution Tasks

Create a task for one production objective. Same-version repairs remain in the task. Close and version the task when the objective, formal source, locked baseline, critical method, or write scope changes.

Archive completed tasks. Do not delete evidence required for traceability.

## Lossless Replacement

1. Detect a real stall through receipts, file progress, and process/tool activity.
2. Freeze new writes and determine current outputs, processes, and locks.
3. Create a replacement candidate in read-only mode.
4. Load the handoff package and verify current baselines.
5. Switch the unique role/task identity only after the candidate is READY.
6. Archive the old task and update routing.

At no point may both old and replacement tasks write the same scope.

## Cold Producer Takeover

A new producer conversation can be activated by a short natural-language takeover phrase. It reads the file-based handoff package, proves the current workflow version, roles, active tasks, blockers, and state, then replaces the old producer identity. Only one active producer is allowed.
