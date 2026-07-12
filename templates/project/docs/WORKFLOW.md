# {{PROJECT_NAME}} Production Workflow

Version: WORKFLOW-1

## Authority

- One accountable producer owns priority, shared-file ordering, and final status.
- Design, engineering, and art owners are long-lived role entrances.
- Role owners define contracts, monitor their tasks, and accept results.
- Production is performed by short-lived execution tasks.
- The PM execution operator monitors and refreshes status but cannot make producer decisions.

## Requirement Intake

Natural-language producer requests are valid intake. File behavior-changing requests into a functional source and corresponding configuration source before implementation when required. Do not ask for redundant confirmation when the requested outcome and identity are clear from approved sources.

## Work Order

Use `PM/feature_progress.xlsx` as the advancement queue. Higher priority goes first. Same priority uses ascending feature ID. Completed features are last. Skip only for dependencies, shared locks, or safety blockers and record the reason.

## Execution Task Gate

Every task has one objective, one accountable owner, one primary Skill, one isolated write scope, source baselines, acceptance evidence, cleanup, and close conditions.

The task first submits a read-only receipt. The owner independently reviews it and explicitly authorizes writes. Contract READY is not task READY.

## Runtime And Asset Rules

- Final assets already available must be used completely.
- Missing assets may use explicit development placeholders.
- UI may use temporary visuals; non-UI art targets final quality from first production.
- Candidate and not-runtime assets cannot be read by release/runtime code.
- Mechanical art checks may hand directly to a development preview unless the producer requests art review.

## Evidence

Real player-visible behavior is preferred. Exit code zero, parsing, file existence, or direct callback tests cannot replace a real behavior requirement.

## Monitoring

Monitor the current batch on a short interval. Refresh the workbook on a slower interval. Healthy checks remain quiet. Report exceptions, decisions, playable previews, and completion.

## Stuck Task Replacement

Inspect files, processes, outputs, and locks. Start a read-only replacement candidate, verify handoff, switch the unique task/role identity, then archive the old task. Never permit dual writers.

## Completion

Verify acceptance, regression, authorized files, placeholder/runtime boundaries, temporary cleanup, process exit, lock release, task archive, workbook update, and selection of the next feature.
