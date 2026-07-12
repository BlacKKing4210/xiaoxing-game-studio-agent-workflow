# Contributing

Contributions should improve the generic workflow without embedding private project facts.

## Rules

1. Keep project names, absolute paths, task IDs, hashes, credentials, and production assets out of the repository.
2. Put reusable behavior in Skills or templates; keep engine-specific details in adapters.
3. Add a concrete acceptance example for workflow changes.
4. Preserve the single accountable producer model and explicit write ownership.
5. Run the validation scripts before opening a pull request.

## Validation

```powershell
./scripts/validate-repository.ps1
```
