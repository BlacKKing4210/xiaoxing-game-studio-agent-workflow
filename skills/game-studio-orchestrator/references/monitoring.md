# Monitoring And Token Economy

## Current-Batch Monitoring

Inspect only active tasks, necessary dependencies, listed locks, and their latest responsible receipts. Paused or deferred work is checked only when its trigger arrives or its files unexpectedly change.

Report immediately when:

- a task writes before its first receipt or owner authorization;
- the write scope or baseline drifts;
- two writers touch a shared file;
- a candidate, placeholder, or not-runtime asset enters release paths;
- task state disagrees with files or processes;
- a milestone is overdue with no valid long-running work;
- completion evidence or cleanup is missing.

## Quiet Success

Healthy unchanged checks stay silent. Notify for exceptions, decisions, playable previews, or completion.

## Token Economy

- Read scope and latest receipts first.
- Use indexes, hashes, manifests, and changed-file metadata.
- Load full contracts or documents only for changed or disputed sections.
- Batch mechanical checks.
- Expand only failed items.
- Do not repeat unchanged status prose.

Token savings never weaken final quality, write gates, QA, or real behavior evidence.
