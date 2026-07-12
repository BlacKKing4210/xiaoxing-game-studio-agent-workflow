# F-010 Inventory Pickup Feedback

## Goal

When the player picks up an item through normal gameplay, the accepted quantity enters the inventory and a short visual travels from the real world source to the inventory indicator.

## Rules

- Only accepted inventory quantity is visualized.
- Capacity rejection is not visualized as accepted loot.
- The world source, item identifier, and inventory result are preserved through the event chain.
- UI may use a temporary icon only when no final item icon exists.

## Non-Goals

- Inventory redesign.
- New item categories.
- Debug-only pickup injection.
