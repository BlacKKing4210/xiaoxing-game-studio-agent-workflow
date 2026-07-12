# Game Studio Agent Workflow

A producer-led, evidence-driven workflow for running a small game studio with Codex agents.

It turns natural-language production requests into scoped design, engineering, art, QA, and handoff work while keeping one accountable producer, short-lived execution tasks, explicit write ownership, playable evidence, and a feature-level progress matrix.

> Community project. Not an official OpenAI product.

## What It Solves

- Long approval chains before anything appears in the game.
- Role agents that create work and then stop monitoring it.
- Parallel agents editing the same runtime files.
- Placeholder art surviving after final assets exist.
- Status dashboards that track documents instead of complete features.
- Stuck conversations with no lossless replacement path.
- Repeated context loading and unnecessary token use.

## Operating Model

1. **One producer front door** accepts natural-language requests and owns priority.
2. **Long-lived role owners** cover design, engineering, art, and producer operations.
3. **Short-lived execution tasks** perform production; role owners define contracts and accept results.
4. **A read-only receipt precedes writes** so sources, scope, Skills, locks, and baselines are known.
5. **Playable proof is the default milestone**. Art and engineering work in parallel when safe.
6. **The progress workbook tracks complete features**, not isolated documents or assets.
7. **Stuck tasks are replaced losslessly** with a read-only handoff before the old task is archived.

## Key Rules

- A feature is represented by its functional specification plus its numeric/configuration source, or by a producer directive that has been filed into a formal source.
- Nine dimensions are tracked per feature: design document, numeric table, code, scene, UI, icon/image, scene integration, image integration, and UI integration.
- Not-applicable dimensions display `Not needed` and are excluded from averages.
- Work advances by priority, then by ascending feature ID. Only dependencies, shared locks, or safety blockers may change that order.
- Existing final assets must be used. Temporary visual assets are allowed only when the required final asset does not exist; all placeholders are marked for replacement.
- A contract being ready does not mean an execution task is ready. The task must submit its own read-only receipt before its owner authorizes writes.

## Repository Layout

```text
.codex-plugin/                 Codex plugin manifest
skills/                        Installable workflow Skills
templates/project/             Project bootstrap templates
templates/automation/          Monitoring and workbook refresh prompt
templates/progress/            Feature progress workbook
examples/                      Sanitized example contracts
scripts/                       Bootstrap and validation tools
```

## Quick Start

```powershell
git clone https://github.com/xiaoxingwang986-cyber/game-studio-agent-workflow.git
cd game-studio-agent-workflow
./scripts/init-project.ps1 -ProjectRoot "D:\Games\MyGame" -ProjectName "My Game" -Engine Godot
```

Then open the game project in Codex and say:

```text
You are the producer. Load the project workflow, take over the current files, and continue the highest-priority ready feature.
```

The generated `AGENTS.md` routes that request to the project handoff and scope files.

## Codex Plugin

The repository root is a Codex plugin. Add the cloned folder as a local plugin in Codex to use:

- `game-studio-orchestrator`
- `game-pm-execution-ops`

The plugin is optional. The templates can be used independently.

## Documentation

- [Workflow](skills/game-studio-orchestrator/references/workflow.md)
- [Role and task lifecycle](skills/game-studio-orchestrator/references/role-lifecycle.md)
- [Gates and evidence](skills/game-studio-orchestrator/references/gates-and-evidence.md)
- [Art and engineering parallelism](skills/game-studio-orchestrator/references/art-engineering.md)
- [Feature progress matrix](skills/game-studio-orchestrator/references/progress-matrix.md)
- [Monitoring and token economy](skills/game-studio-orchestrator/references/monitoring.md)

## Privacy

This repository contains no production game assets, character data, project paths, thread IDs, hashes, private prompts, or game-specific balancing values. Use the Profile and active scope templates for project-local facts.

## License

MIT. See [LICENSE](LICENSE).
