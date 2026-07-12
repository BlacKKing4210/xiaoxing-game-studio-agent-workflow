# Art And Engineering Parallelism

## Default Delivery

1. Design defines the player-visible behavior and asset contract.
2. Engineering builds the real behavior path immediately.
3. Art produces final-quality assets in parallel.
4. When art reaches its mechanical gate, engineering places it into a development preview.
5. The producer reviews the result in the game.

Art-owner visual review is optional before the first development preview unless the producer explicitly requests it or the asset presents a safety, identity, or compliance risk.

## Asset Priority

- Existing complete final asset: use it.
- Final asset missing: use an explicit `dev_only` placeholder.
- UI: temporary visual resources are allowed.
- Non-UI art: produce at final quality from the first art task.
- `NOT_RUNTIME` means not yet accepted or integrated; it does not permit lower quality.

## Batch Art

For same-use raster assets, review one coherent whole-set board, then split only approved pixels into final files. The board may be assembled deterministically from isolated final-quality cell sources; the board remains the sole visual approval surface.

## Looping Scenes

Approve one complete looping mother image first. Then deterministically split or derive runtime layers such as background and road. Do not repair failed seams indefinitely with local patches; version the method when the approach is exhausted.

## Runtime Handoff

Art approval or formal runtime placement is not the same as behavior integration. Engineering receives explicit asset identifiers, dimensions, anchors, timing, facing, loop behavior, return transitions, and approved runtime paths.
