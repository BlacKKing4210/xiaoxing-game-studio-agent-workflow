---
name: game-unit-sideview-production
description: Produce and validate game-ready transparent side-view character or monster units from approved source art. Use for side-view unit generation, chroma-key cleanup, canvas normalization, baseline alignment, same-use style checks, formal naming, or runtime sideview preparation. Project style anchors and numeric specifications must come from a caller-supplied profile.
---

# Game Unit Sideview Production

Use the project profile as the source of truth for style references, canvas, baseline, scale, facing, naming, archive, and runtime destinations.

## Workflow

1. Confirm source identity and approved same-use style references.
2. Produce one sample before any batch. Compare silhouette, head/body ratio, line treatment, material density, lighting, view angle, and transparent margins.
3. Stop the batch when style or identity differs from the approved reference.
4. Remove chroma or background without damaging outlines and effects.
5. Normalize with scripts/normalize_sideview.py using values supplied by the project profile.
6. Inspect alpha bounds, subject height, center, foot baseline, edge spill, clipping, and canvas size.
7. Keep formal art approval separate from runtime integration. Do not mark generated output formal without the project art owner.
8. Update registries and runtime paths only when the task contract authorizes them.
9. Delete intermediate masks, failed generations, duplicate exports, and temporary scripts unless an explicitly named rejected-art archive is required.

## Completion Evidence

Report identity, source and reference hashes, supplied geometry values, measured alpha bounds, facing, formal/runtime status, registry changes, visual QA, engine QA when applicable, and cleanup.
