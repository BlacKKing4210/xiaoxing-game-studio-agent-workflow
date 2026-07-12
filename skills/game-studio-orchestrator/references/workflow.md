# Producer-Led Workflow

## 1. Requirement Intake

The producer may speak naturally. A clear request to build, start, replace, or continue is authorization to enter requirement intake. Record the request in a formal functional source before implementation when it changes product behavior.

Capture:

- goal and player-visible outcome;
- feature ID and priority;
- functional rules and numeric/configuration source;
- non-goals;
- responsible role owners;
- dependencies and shared files;
- preview and final acceptance.

Do not require the producer to fill redundant confirmation forms when the requested result and formal identity can be derived from approved sources.

## 2. Design Handoff

The design owner creates or updates the functional document and corresponding configuration source. The design package must resolve values that would otherwise force engineering to guess.

Engineering may begin framework work with development placeholders while art proceeds, provided final assets do not already exist and write scopes are separated.

## 3. Execution Contract

The accountable role owner creates a minimal contract and a short-lived execution task. The contract states one outcome, allowed files, sources, baselines, Skills, evidence, and close conditions.

## 4. First Receipt

The execution task remains read-only and reports:

- loaded contract and source versions;
- loaded project adapter and primary Skill;
- allowed write scope;
- baseline file hashes or equivalent version identifiers;
- shared-file conflicts and process state;
- READY, CONCERNS, or NOT READY.

The role owner independently checks the receipt and authorizes writes only when ready.

## 5. Production

Work stays inside the contract. A behavior failure stops QA before any repair. The owner classifies the failure and gives a narrow same-version repair authorization or versions the task when the objective, source, method, or baseline changes materially.

## 6. Preview

Deliver a playable or reviewable preview as soon as the smallest real chain is available. Use normal gameplay entry points. Test flags may accelerate setup but must remain off by default and may not call downstream acceptance callbacks directly.

## 7. Acceptance

The task maps each acceptance item to behavior, screenshot, asset, manifest, or deterministic evidence. Exit code zero, parse success, or file existence alone never proves player behavior.

## 8. Close And Continue

After owner acceptance, clean temporary outputs, archive the execution task, release locks, update the feature matrix, and select the next ready row by priority and feature ID.
