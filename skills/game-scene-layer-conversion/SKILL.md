---
name: game-scene-layer-conversion
description: Safely consolidate approved multi-layer 2D game scenes into fewer non-runtime or runtime-ready layers while preserving transparency, independent X-axis loops, protected subjects, crop and output-slot evidence, and visual acceptance. Use when reducing scene-layer count, baking compatible background layers, preparing loopable parallax art, or separating art conversion from engine integration.
---

# Game Scene Layer Conversion

Convert only an already-approved scene package. Treat this as an art-production workflow, not permission to redesign a scene or integrate it into an engine.

## Start gate

Require a task contract containing all of the following before creating an output:

- approved source files and their authoritative layer order;
- a layer inventory: visual role, transparency, scroll behavior, repeat behavior, and whether it contains a protected subject or interaction;
- the requested reduction goal, target output slots, required format, color/alpha expectations, and acceptance owner;
- named workspace and explicit classification for every output: `NOT_RUNTIME` or `RUNTIME_CANDIDATE`;
- a preservation map that states which layers may be baked together and why their movement, looping, and depth behavior remain compatible.

Stop and ask for clarification if any source is unapproved, layer order or alpha state is unknown, a protected subject would be baked, independent movement requirements conflict, the target crop is unspecified, or runtime integration is requested without a separate engineering handoff.

## Protect the scene before reducing layers

Keep gameplay-meaningful or visually identifiable material independent unless the task contract explicitly says it is decorative and safe to bake. This includes playable characters, enemies, pickups, hazards, doors, interactive props, event objects, collision/readability markers, and unique landmarks needed for orientation.

Do not merge layers solely because they overlap. Bake only a group that shares all relevant properties: depth/scroll relationship, repeat behavior, visibility conditions, blend treatment, and output crop. If a layer needs a different X-axis speed or must remain editable, it is not compatible with that bake group.

Record a preservation map before conversion and a conversion map afterward. For each output slot, show its source layers, order, protected-subject exclusions, crop bounds, intended loop behavior, alpha treatment, and classification. Keep those records with the task artifact, not inside this generic Skill.

## Convert safely

1. Work on copies in a task-local workspace. Preserve the approved source untouched.
2. Normalize source interpretation before compositing: pixel dimensions, color representation, alpha presence, and intended layer order. Do not silently flatten transparency.
3. Use normal source-over compositing unless the approved source explicitly specifies another blend operation. Preserve the declared order.
4. Treat alpha representation as a pipeline constraint. When filtering, resampling, transforming, or compositing semi-transparent pixels, use a toolchain whose alpha behavior is known. Premultiply before operations that require premultiplied color, then unpremultiply only when the target format/workflow requires straight alpha. Never mix assumptions. Inspect translucent edges over more than one matte color.
5. Crop only to the approved output slot. Do not trim transparent margins, shift anchors, or invent fill content unless the task contract authorizes it. Record every intentional crop, padding, or fill decision in the output evidence.
6. Export the smallest useful set of outputs. Label each artifact `NOT_RUNTIME` until a separate, explicit engine handoff accepts it; a `RUNTIME_CANDIDATE` is still not an engine-integrated asset.

Read [references/method-basis.md](references/method-basis.md) when selecting a compositor, validating alpha behavior, or interpreting loop seams.

## Verify loops and composition

Run checks on every output layer that is intended to repeat along the X axis:

- duplicate the layer along the X axis and inspect both joins at the intended crop and scale;
- inspect it at the expected scroll direction and at multiple offsets, including a join centered in view;
- test each independently scrolling layer alone, then in the full composite; never infer independent-loop safety from a flattened preview;
- inspect transparency over light, dark, and a contrasting matte for fringes, halos, dark edges, or unexpected opaque pixels;
- compare the approved source composite with the reduced-layer composite at the same view. Confirm protected subjects, depth cues, and readable gameplay space remain intact.

Mechanical checks (dimensions, alpha presence, seam-difference metrics, or pixel comparisons) are diagnostic evidence only. They cannot replace human visual acceptance. The named visual owner must inspect the moving, composited result and accept or reject it.

## Handoff and cleanup

Deliver the preservation/conversion map, output files, crop and slot evidence, alpha/loop QA evidence, visual acceptance result, and any known limitations. Keep source and output classifications unambiguous.

Do not edit scenes, import settings, code, registries, or runtime asset folders in this workflow. Hand engine integration to a separate task with its own ownership, target locations, acceptance criteria, and rollback plan.

Delete temporary previews, intermediate exports, comparison mattes, caches, and failed attempts after evidence is captured. Retain only task-required deliverables and explicitly approved QA evidence. Report whether cleanup is complete.

## Completion status

Report `ARCHIVABLE` only when the task contract is satisfied, the visual owner has accepted the result, all output classifications are clear, required evidence is present, and temporary files are removed. Report `REVISION_REQUIRED` for a failed visual, alpha, crop, slot, or loop check. Report `BLOCKED` for missing approval, contradictory movement requirements, missing source information, or an attempted runtime handoff outside scope.
