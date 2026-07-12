---
name: game-looping-scene-layer-production
description: Plan, produce, or reconstruct contract-defined 2D horizontal looping scene layers from approved briefs and references while protecting independent objects, preserving alpha and visual continuity, and keeping outputs outside runtime. Use for new or rebuilt background, ground, road, far, mid, or other independently scrolling scene layers; do not use to merely consolidate approved layers or integrate assets into an engine.
---

# Looping Scene Layer Production

Create a new source package only from a complete task contract. Keep this workflow separate from approved-layer conversion and from runtime integration.

## Start gate

Require a task-local, formally approved contract with all of the following:

- visual brief, approved style reference(s), and their allowed use;
- source inventory, provenance or license/permission record, and a source hash manifest;
- declared layer inventory. Each layer must state role, draw order, repeat axis, independent scroll behavior, alpha expectation, crop or safe-area needs, and output classification;
- an object allow/exclude matrix that classifies every visible object as `protected`, `independent`, or `environmental`. State whether baking is allowed for each row;
- output contract: task-local directory, file format, color and alpha requirements, hash algorithm, required evidence, acceptance owner, and initial `NOT_RUNTIME` classification;
- declared horizontal and vertical native crops, expected moving views, anchor/alignment lines needed for compositing, and the intended human visual review.

Treat playable characters, enemies, buildings, vehicles, barricades, pickups, event objects, text, unique landmarks, collision/readability markers, and any uncertain object as `protected` or `independent` by default. Bake one only when the matrix explicitly permits it. If an excluded object appears in a reference and removal is prohibited or unclear, stop as `BLOCKED`; never silently delete it or weaken the matrix.

Stop as `BLOCKED` if approval, source provenance, layer contract, object matrix, alpha/crop needs, loop behavior, or output classification is missing or contradictory. Stop if asked to write to an engine, code, registry, runtime asset directory, or formal source. Create no outputs before this gate passes.

## Plan before producing

Create a preservation/production map in the task directory before creating imagery. For each declared layer, record:

- inputs and their hashes; visual role; allowed and excluded objects; intended draw order and movement;
- native bounds, horizontal repeat behavior, alpha and color treatment, alignment anchors, and required crops;
- chosen method: hand drawing, controlled local editing, or a generative tool; and
- output filename, output hash, `NOT_RUNTIME` classification, evidence locations, and acceptance status.

Do not write a fixed layer count into the workflow. Accept any layer structure declared by the contract, such as a background/road pair or a far/mid/ground arrangement.

When the contract permits a master-first method, plan one complete native-size looping master image before any layer separation. The master must establish the final composition, horizon, ground edge, lighting, color, protected-object exclusions, crop behavior, and horizontal seam. Treat the approved master pixels as the source of truth for later extraction; do not independently regenerate layers after master approval.

## Choose an allowed production method

Use hand drawing or controlled local editing when it best preserves the approved visual anchor. Use a generative tool only when the contract permits it and its license, access terms, input rights, output use, and reproducibility notes are recorded in the task evidence.

Use generation to create or reconstruct image content, not to conceal an incomplete contract. Preserve the style anchor and intended use; do not mix unrelated references or quietly substitute an unapproved style.

Achieve low visual noise through composition, shape hierarchy, restrained contrast, and controlled material detail. Do not use global or regional blur, broad feathering, geometric patches, repeated technical overlays, or procedural texture as a substitute for finished scene art. Reject visible repair boundaries, indiscriminate loss of focus, or marks that read as technical annotation rather than scene material.

## Produce safely

1. Work only in the contract's independent task directory. Preserve approved inputs unchanged.
2. Establish the full composition and layer relationship before separating or rebuilding layers. When master-first is contracted, finish and visually approve one complete horizontally looping master first, then extract the declared layers from those approved pixels. Keep shared horizon, ground edge, lighting direction, color temperature, contact relationship, and declared anchors coherent across layers.
3. Keep every protected or independent object out of loop layers unless explicitly allowed. Do not convert an uncertain object into environmental decoration.
4. Build each horizontally repeating layer as an independent loop. Do not rely on another layer to cover its seam.
5. Preserve declared transparency. Use an alpha-aware pipeline for painting, transforms, filtering, and export; inspect translucent edges rather than flattening them.
6. Export only the declared files at their native dimensions. Do not trim transparent margins, shift anchors, add unstated padding, or invent fill content without a contract amendment.
7. Keep every deliverable `NOT_RUNTIME`. A request to make it usable at runtime requires a separate task, owner, destination, and acceptance gate.

Do not call independently generated layers a split master. If extraction from the approved master cannot satisfy alpha, occlusion, protected-object, or independent-loop requirements without repainting, stop and amend the contract rather than silently regenerating divergent layers.

## QA and human acceptance

For each output layer, retain evidence that it passes all applicable checks:

- repeat the layer as `A|A|A`, inspect both joins, and inspect multiple horizontal offsets including a centered join;
- observe each moving layer alone and in the declared composite at its own scroll behavior;
- inspect native horizontal and vertical crops, including the declared safe areas, for seams, cut objects, discontinuous ground, anchor drift, or loss of readability;
- inspect alpha on light, dark, and contrasting mattes for halos, fringes, or accidental opacity;
- verify color, alignment, and contact coherence between layers;
- compare the output against the approved visual anchor and confirm the object matrix: excluded and independent objects are absent from baked layers; and
- record source/output hashes, production map, repeat/crop/alpha/object-exclusion evidence, tool provenance, and cleanup result.

Dimensions, hashes, seam metrics, and pixel comparisons are diagnostics only. The named visual owner must visually inspect the animated composite and native crops, then explicitly accept or reject the package. No mechanical result can substitute for that review.

## Revisions, handoff, and status

Allow same-baseline revisions only when the approved inputs, object matrix, output contract, and task directory are unchanged. Update the preservation/production map and rerun every affected QA check.

Stop writing and request a new task contract when approved sources, style anchor, layer structure, object permissions, native crops, output destination/classification, or acceptance owner changes. Do not silently carry an old output into a new baseline.

Delete temporary prompts, previews, intermediates, comparison mattes, caches, and failed exports after required evidence is retained. Keep only task-required deliverables and explicitly approved evidence.

Report one of these states:

- `READY`: start gate passed; provide the planned production and QA path. This is not visual acceptance.
- `REVISION_REQUIRED`: a produced package fails a loop, crop, alpha, object, provenance, style, or visual review check; keep it out of runtime.
- `BLOCKED`: a required input, permission, matrix decision, contract field, or separate runtime handoff is missing, contradictory, or out of scope.

Use `APPROVE_CANDIDATE` only after all contracted evidence is present and the visual owner has not yet performed the final acceptance. Never claim final approval on the owner's behalf.
