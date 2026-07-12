# Exception Receipt

```yaml
state: READY | CONCERNS | NOT_READY
task_or_role: <id or name>
observed: <current evidence>
expected: <contract or scope rule>
evidence:
  - <receipt, file, hash, process, or behavior proof>
impact: <what cannot safely continue>
recommended_producer_decision: <smallest useful decision>
```

For a healthy unchanged check, emit no report. For completion, include acceptance coverage, final baselines, regression, cleanup, process state, and lock release.
