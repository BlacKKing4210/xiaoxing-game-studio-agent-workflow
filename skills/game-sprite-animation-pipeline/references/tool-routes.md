# Tool Routes For AI Game Sequence Frames

Use this reference when comparing tools or giving GitHub-oriented recommendations.

## Sprite-Sheet-Diffusion

Best fit: closest research project to "game character sprite sheet generation".

Role:
- Generate game character motion frames from reference and pose/control data.
- Supports action-folder style outputs such as run, jump, melee, dead in its examples.

Use when:
- The user explicitly wants a sprite-sheet-specific GitHub project.
- The user can tolerate standalone Python setup and downloading weights.

Warn:
- Not a ComfyUI node.
- Requires model weights and a directory structure with character/motions/ground_truth/poses.
- Not magic one-image-to-all-actions; pose sequences still matter.

## ComfyUI Route

Best fit: practical route for Autumn/ComfyUI users.

Suggested components:
- ComfyUI-AnimateDiff-Evolved: animation generation.
- ComfyUI-VideoHelperSuite: load videos, load image sequences, split/compose frame batches.
- comfyui_controlnet_aux: OpenPose/DWPose/Lineart/Depth preprocessors.
- ComfyUI_IPAdapter_plus: lock character identity from reference art.
- Advanced-ControlNet: optional timing/mask/control refinements.

Use when:
- The user already works inside ComfyUI.
- The user wants to use a side-view character image and export sequence frames.

Typical flow:
Reference side-view -> pose/control sequence -> IPAdapter identity lock -> AnimateDiff frames/video -> VideoHelperSuite split -> cleanup -> spritesheet.

## Pose-Driven Video Route

Best fit: natural large actions.

Projects:
- MusePose: pose-driven image-to-video framework.
- MimicMotion: high-quality human motion video generation with pose guidance.
- Moore-AnimateAnyone: underlying AnimateAnyone-style implementation used or referenced by related work.

Use when:
- The user has or can create an action video.
- The action needs natural motion like run, fall, attack, death.

Warn:
- Output tends to be video-like, not immediately game-ready.
- Side-view game style, transparent background, and weapon consistency require cleanup.

## Keyframe Interpolation Route

Best fit: short controllable actions.

Projects/tools:
- ToonCrafter: cartoon/image interpolation between keyframes.
- DynamiCrafter or ComfyUI-DynamiCrafterWrapper: ComfyUI integration for image animation/interpolation.
- RIFE/FILM: frame interpolation, useful after keyframes already exist.

Use when:
- The user can generate or draw start/end/key poses.
- The action is attack, hurt, death, turn, skill wind-up, or recovery.

Warn:
- Interpolation does not invent a robust walk cycle from nothing.
- Keyframes must already have consistent character design and camera.

## Rigging Route

Best fit: production animation when non-AI tools are allowed.

Tools:
- Spine
- DragonBones
- Unity 2D Animation
- Godot 2D skeleton

Use when:
- The user can use animation software.
- The priority is stable loops and reusable animation controls.

Warn:
- This is not AI-only.
- AI helps create separated body parts and style concepts, not complete rigged animation.

## Post Processing

Always include cleanup steps for game assets:

- split video to PNG frames
- remove background or use transparent generation if reliable
- crop to fixed canvas
- align foot baseline
- normalize character scale
- remove duplicate loop closing frame
- create spritesheet metadata: frame width, height, fps, action name, frame count

## 4x2 Independent-Cell Method

Use this method when generating a direct image-model walk cycle and the user needs a GIF preview.

Prompt requirements:
- exactly 8 frames
- 4 columns by 2 rows
- one complete character per cell
- large transparent padding around each character
- no overlap between neighboring cells
- no grid, numbers, or labels
- same side-view camera, scale, lighting, and outfit in every cell
- foot baseline aligned inside each cell

Why:
- Warping one standing image fails because it produces wobble, not gait.
- Tight horizontal strips often overlap characters, causing residual feet/backpacks/limbs after slicing.
- Independent cells are easier to crop, baseline-align, and convert to GIF.

Cutting workflow:
1. Copy the generated source sheet to the output folder.
2. Split into 4x2 cells.
3. Remove light checker or flat background to alpha if needed.
4. Crop each cell to visible content with the same output frame size.
5. Bottom-align or foot-baseline-align all frames.
6. Export individual PNG frames.
7. Create a GIF preview with a neutral matte/checker background for reliable display.
8. Create a transparent spritesheet for game import.

Quality gate:
- Reject if any frame contains fragments from adjacent cells.
- Reject if the character is mostly standing and only shifted or warped.
- Reject if frames do not show contact/down/passing/up/opposite-contact phases.
- Reject if hands do not counter-swing or accessories are frozen when the body moves.
