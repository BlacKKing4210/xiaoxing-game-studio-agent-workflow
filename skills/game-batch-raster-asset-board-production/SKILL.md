---
name: game-batch-raster-asset-board-production
description: Produce a coherent batch of raster game assets through one whole-set visual approval board, then split and normalize only the approved pixels into individual transparent files. Use for item icons, props, pickups, inventory art, or other same-use asset sets where batch style consistency and cross-item distinction should be approved before final file preparation.
---

# Batch Raster Asset Board Production

Use one review surface to settle the whole set before spending work on individual delivery files. Treat candidate versus formal as an approval and location distinction, not a quality distinction: generate final-quality art from the start.

## Start gate

Require a formal contract that declares:

- the complete asset inventory and each item's visual identity;
- approved same-use style references;
- board layout, minimum review resolution, labels outside asset cells, and background/key-color rules;
- per-file names, dimensions, alpha, safe area, occupancy, and small-display targets;
- candidate, formal archive, and runtime destinations;
- acceptance owner, evidence, prohibited content, and NOT_RUNTIME status.

Stop if the set, style source, board layout, split geometry, or final file contract is missing or contradictory.

## Whole-set board first

1. Create one high-resolution board containing every contracted asset exactly once.
2. Keep each asset isolated inside a fixed cell with generous separation. Put labels, cell guides, and review notes outside the art; they must never enter split pixels.
3. Show the full set at one consistent scale language. Use larger contract-defined cells only where a different final aspect ratio requires them.
4. Review the board for style coherence, silhouette hierarchy, palette, outline, detail density, lighting, and cross-item distinction.
5. Reject or revise the board as a whole when repeated style drift affects the set. Allow targeted cell revisions only when the board's style language remains unchanged.
6. Do not create formal individual files before the visual owner approves the board.

The review board is not a low-quality placeholder. Its cells must contain the intended final art. Do not regenerate approved cells merely to call them final.

### Treat the board as the approval surface, not necessarily one model call

For a batch of distinct assets, prefer one final-quality generation per asset or other contract-defined isolated generation units when the image tool cannot reliably place many identities into exact cells. Keep those isolated outputs task-local and unapproved, then assemble their unchanged subject pixels deterministically into the fixed whole-set board before visual review.

- Do not present, archive, or hand off isolated generation outputs as approved individual assets.
- Use deterministic placement, scaling, padding, and flat-background normalization only; do not repaint subjects while assembling the board.
- Submit one complete board for whole-set visual approval. Freeze only the approved board hash and cell map.
- After approval, create delivery files by splitting the approved board, not by bypassing it with the pre-board isolated outputs.
- Remove pre-board sources after board-to-split traceability and required evidence are complete.

If a single free-layout generation repeatedly violates fixed cells, stop repeating it. Switch to isolated generation plus deterministic board assembly under a new method version when the contract permits; otherwise escalate the method conflict.

## Split approved pixels

After written board approval:

1. Freeze the approved board hash and cell map.
2. Extract each cell without repainting or generative reinterpretation.
3. Remove only the declared flat background/key color with an alpha-aware method.
4. Normalize canvas size, padding, alignment, safe area, and occupancy using deterministic transforms. Do not stretch subjects or crop visible pixels.
5. Preserve approved pixels except for background removal, alpha-edge cleanup, and contract-defined scaling/placement.
6. Produce contact sheets or small-size previews from the split files, not from separate regenerated art.

If the board resolution cannot yield the contracted final files without upscaling damage or ambiguity, stop before approval and rebuild the board at adequate resolution.

## QA

Verify both the whole set and every split file:

- board inventory, cell identity, board hash, cell rectangles, and extraction traceability;
- exact file name, dimensions, color mode, alpha extrema, transparent corners, non-transparent bbox, safe area, occupancy, and SHA256;
- light/dark/contrasting matte checks for halos, key-color fringes, holes, or dirty transparency;
- contract-defined small-display previews and cross-item confusion groups;
- split pixels match the approved cell except for documented alpha and deterministic normalization;
- no labels, cell borders, review marks, prompt fragments, or discarded cells enter formal files.

Mechanical success does not replace visual acceptance. The named visual owner must approve the whole board and then verify the split package.

## Status and handoff

Keep the board and split candidates NOT_RUNTIME until the visual owner approves the split package. Copy only approved files to formal archive and runtime destinations, preserving hashes where the contract expects identical files.

Do not write engine code, registries, gameplay data, or UI mappings unless a separate contract assigns them. Remove temporary prompts, failed boards, crop experiments, key-color sources, caches, and disposable previews after required evidence is retained.

Report READY, REVISION_REQUIRED, or BLOCKED. Close and start a new version if the asset set, approved board, style source, cell map, final dimensions, or destinations change.
