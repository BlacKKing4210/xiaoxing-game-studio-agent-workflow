---
name: game-sprite-animation-pipeline
description: Plan AI-driven game character sequence-frame animation and sprite-sheet workflows. Use when the user asks about generating 2D game protagonist/enemy animation frames, sprite sheets, walking/idle/combat/death actions, seamless loops, ComfyUI animation pipelines, pose-controlled animation, Sprite-Sheet-Diffusion, AnimateDiff, ToonCrafter, or frame cleanup for game-ready assets.
---

# Game Sprite Animation Pipeline

## Core Judgment

Treat "one image -> all game animations" as an unstable promise. Prefer workflows that separate:

1. character identity locking
2. action or pose control
3. frame generation
4. loop and cleanup validation
5. sprite-sheet packaging

If the user only has AI tools, do not recommend Spine/DragonBones as the main production path unless they ask for rigging. Mention them only as a non-AI production alternative.

## Route Selection

Choose one route based on the user's constraints:

- **ComfyUI practical route**: Use for users already on ComfyUI/Autumn/AI drawing workflows. Recommend AnimateDiff-Evolved + VideoHelperSuite + controlnet_aux + IPAdapter_plus. This is the default practical route.
- **Sprite-Sheet-Diffusion route**: Use when the user wants the closest research project for game sprite sheets. Explain that it needs its own Python environment, model weights, reference frames, and pose sequences; it is not a simple ComfyUI node.
- **Pose-video route**: Use for natural larger motion such as running, attacking, falling, or death. Mention MusePose, MimicMotion, or AnimateAnyone-style projects.
- **Keyframe interpolation route**: Use for short actions with clear start/end frames such as attack, hit, death, turn, or skill anticipation. Mention ToonCrafter, DynamiCrafter wrappers, RIFE, or FILM.
- **2D rigging route**: Use only when the user can use non-AI animation tools. AI supplies separated parts, then Spine/Unity/Godot rigs animate.

For tool/project details, read `references/tool-routes.md` when the user asks for GitHub projects, installation, or tool comparisons.

## Recommended AI-Only Workflow

Use this when the user provides a side-view protagonist and wants idle/walk/combat/death sequence frames:

1. Create a clean left-facing character standard image: full body, neutral pose, simple background, no crop, readable silhouette.
2. Prepare pose/control sequences per action. Use OpenPose/DWPose, lineart, depth, or simple silhouette guides. Do not rely on text prompts alone for walk/attack timing.
3. Lock identity with IPAdapter/reference image/LoRA where available.
4. Generate short clips or frame batches per action.
5. Export or split to PNG frames.
6. Normalize canvas size, foot baseline, character scale, and direction.
7. Fix loop actions by checking first/last frame continuity; usually omit the duplicated final frame in the final sheet.
8. Package as individual PNG sequence plus a spritesheet.

## Sprite Sheet Generation Rule

For image-generation models, prefer **4x2 independent-cell generation** for an 8-frame walk cycle, not a tight horizontal strip. Prompt for exactly 8 separate full-body frames arranged in 4 columns by 2 rows, with generous transparent padding inside each equal-size cell and no overlap between cells. Then cut each cell into a frame and build the GIF/spritesheet.

Use this rule because two common failures were observed:

1. Warping a single standing pose only makes the character wobble; it does not create real walking because the legs, arms, weight, and contact poses never change correctly.
2. A tight horizontal 8-frame strip can draw a correct walk cycle but place characters too close together, so cutting by equal widths creates residual backpacks, feet, or limb fragments from neighboring frames.

For walk-cycle prompts, explicitly require:

- stable foot baseline in every cell
- clear alternating leg contact and passing poses
- arm counter-swing opposite the legs
- subtle backpack bounce with body weight
- hair, sash, cloak, and loose accessories following through slightly
- no duplicated standing poses
- no overlap between cells

## Action Specs

Suggest these starter specs unless the project has its own animation bible:

- idle: 8 frames, looping
- walk: 8 frames, looping
- run: 8 frames, looping
- attack: 6-10 frames, non-looping
- hurt: 3-4 frames, non-looping
- dodge: 6-8 frames, non-looping or short recover
- death: 8-12 frames, non-looping

For loops, require matching phase and foot contact between the first and last usable frame. If a generation tool creates a repeated closing frame, remove it from the sheet to avoid a pause.

## Prompting And Controls

When drafting prompts or workflows:

- State the view direction explicitly, e.g. "left-facing side-view game character".
- Keep camera, scale, lighting, and background fixed.
- Ask for clean silhouette and full body.
- Avoid uncontrolled words like "dynamic camera", "different angle", "cinematic cut", or "turnaround" unless the action needs them.
- Separate weapon, hair, cloak, backpack, and long accessories in critique notes because they drift most often.
- Prefer pose images, skeleton frames, lineart, or silhouette controls over text-only prompts.

## Quality Checks

Before calling an output game-ready, check:

- character face, outfit, weapon, and color consistency across frames
- no angle flip or unwanted camera zoom
- feet do not slide in idle/walk/run unless intended
- canvas is stable and centered
- action readable at game resolution
- first/last usable loop frames connect without a hitch
- transparent background or flat chroma background is clean
- spritesheet frame order and frame dimensions are documented

## Failure Modes

Warn the user early when relevant:

- A single reference image rarely preserves identity across all actions without reference conditioning.
- Text-only "seamless walking animation" prompts often produce foot sliding and inconsistent anatomy.
- "Stand pose plus deformation" outputs are not acceptable for walk cycles; they read as wobbling, not walking.
- Tight sprite strips can be unusable even when poses look good if adjacent frames overlap and contaminate the cut frames.
- AI video tools output video, not game-ready transparent sprite sheets; cleanup is part of the pipeline.
- Sprite-Sheet-Diffusion is promising but heavy: Python environment, model weights, and pose/ground-truth folder structure are required.
- Flux can design characters well, but SD/AnimateDiff-style pipelines may be more practical for batch animation frames.
