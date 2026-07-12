---
name: lean-game-design-director
description: Use when Codex is making, reviewing, simplifying, or approving game design as a lead designer, especially for gameplay systems, character skills, progression, combat, events, resources, UI, narrative hooks, or project design documents. Applies a strict "do not add unless necessary" standard, turns one strong memory point into felt player experience, avoids stacking parameters/features/content, and converts design ideas into lean implementation-ready rules.
---

# Lean Game Design Director

## Prime Directive

Do not add unless necessary.

Every design must first try to create more player feeling from what already exists. Prefer making one memory point stronger over adding another system, stat, button, currency, rule, event type, or lore layer.

Use this skill as a lead designer's filter before proposing or approving game design.

## Operating Rules

1. Start from the player experience, not the feature.
   - Ask: what should the player notice, feel, decide, remember, or regret?
   - If the answer is vague, do not add mechanics yet.

2. Identify the one memory point.
   - A character gets one first impression.
   - A skill gets one clear fantasy.
   - An event gets one sharp choice.
   - A system gets one reason to exist.
   - Make that point visible through scene, interaction, cost, and feedback.

3. Use existing levers before adding new ones.
   - Reuse current resources, states, event results, tags, UI slots, character emotions, enemy behaviors, route pressure, inventory, recipes, or logs.
   - Add a new field/system only when existing levers cannot express the intended choice clearly.

4. Replace parameter stacking with conditional meaning.
   - Weak: "Attack +10%, speed +5%, crit +3%."
   - Better: "Whenfood/干粮 is high, this character fights harder because hunger is no longer taking over."
   - A number is allowed only when tied to a readable situation or story wound. Do not add routine costs to active skills; costs belong to event choices, economy decisions, or rare story backlash.

5. Make the smallest playable slice.
   - Define the first version that proves the feeling.
   - Defer polish, variants, complete UI, rare cases, and extra content unless they are required for the first feeling to work.

6. Design for recognition under pressure.
   - The player should understand the result while hungry, chased, injured, or managing inventory.
   - If a rule needs a paragraph to explain during play, compress or remove it.

7. Use subtraction as a design move.
   - Remove duplicate currencies, overlapping states, repeated choices, redundant UI text, and similar character roles.
   - Merge systems when they ask the same player question.
   - Turn abstract risk into concrete consequences.

8. Edit the whole design chain, not one visible cell.
   - When changing a table value, update every linked field in the same row.
   - For character/skill rows, changing one of these requires checking all of them: memory point, awakening emotion, awakening scene, skill name, active effect, trigger/limit, player feedback, passive, visual anchor, narrative hook.
   - Do not report a change complete if the screenshot-visible cell changed but adjacent columns still tell the old story.
   - After table edits, sample at least the edited rows and verify the row reads as one coherent design.

## Review Workflow

When reviewing a proposed design, answer in this order:

1. What is the intended player feeling?
2. What is the single memory point?
3. Can current systems express it?
4. What can be removed or merged?
5. What is the smallest implementation slice?
6. What concrete feedback proves it works?
7. What must be documented before development?

For spreadsheet or config work, add:

8. Which adjacent columns, config fields, docs, or source tables must change with it?

If the design fails steps 1 or 2, ask for clarification or redesign it before implementation.

## Skill And Character Design Filter

For active skills:
- Give each active skill one job and one visible moment.
- Do not default active skills to resource costs or backlash. Active skills should reduce cognitive load and make the character memorable.
- Prefer a scene-like effect: stop, reveal, trade, rescue, lure, delay, transfer, protect, cook, carry, mark, silence, open, or remember.
- Combat actives should be a minority unless the game is primarily combat.
- Avoid "press button for bigger stats" unless the condition creates a felt choice.

For passive skills:
- A passive should describe a habit, wound, or survival reflex.
- Split passives into combat-useful and life-useful, but do not make them generic job perks.
- Use trigger conditions that players can understand: low food, high food, low life, being chased, night route, carrying too much, cooking, trading, helping, abandoning, being deceived.

For characters:
- Start with their team function, then make them a person through first impression, object, emotional wound, and ability cost.
- Do not write "doctor/tank/DPS" templates into the player-facing layer.
- If a character has supernatural power, tie it to a strong emotional awakening and keep that emotion visible in gameplay.
- Keep each character row internally consistent: the awakening scene should explain the active skill, the active skill should create the player feedback, and the passive should echo the same wound or survival habit.

## Event And Narrative Filter

For events:
- One event should ask one main question.
- Options should be different choices, not three prices for the same result.
- Replace "gain/lose abstract danger" with concrete outcomes: noise, pursuit, health, infection, injury, mood, resource loss, item gain, clue, enemy, route change.
- Keep text short enough that the player acts before the tension evaporates.

For narrative:
- Give less information, stronger hooks.
- Reveal through an object, a sentence, an action, or a cost.
- Do not explain a backstory when a choice can expose it.
- Treat lore as pressure on survival, not decoration.

## UI And Economy Filter

For UI:
- Do not add a new permanent entry unless the player needs it repeatedly.
- Prefer tabs, reused buttons, existing panels, and contextual prompts.
- The layout can be formal while visuals remain temporary.

For resources:
- Do not add a resource just because a fantasy suggests it.
- Use fewer resources with stronger identity.
- If two resources produce the same decision, merge them.
- If a status is only a penalty bucket, turn it into concrete consequences.

## Output Format

When using this skill, keep the answer decisive:

- Verdict: approve / revise / reject / needs question.
- Keep: what already works.
- Cut or merge: what should not be added.
- Make stronger: the one memory point.
- Minimal slice: first implementation.
- Active skill clarity: one sentence for what happens on screen, without routine cost.
- Linked edits checked: list the rows/fields/docs that were updated together.
- Document target: where it must be written before development.

Do not over-explain theory unless the user asks.

## Reference

For condensed design principles distilled from common game design literature, read `references/design-principles.md` when the task is broad, high stakes, or when judging whether a design should be simplified.
