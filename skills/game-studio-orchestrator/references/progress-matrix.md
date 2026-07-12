# Feature Progress Matrix

## Row Definition

One row equals one complete product feature. The row references:

- functional document or filed producer directive;
- numeric/configuration table;
- source type;
- priority and feature ID;
- owner, stage, next milestone, and blocker.

Do not create separate rows for every document, asset, or QA artifact.

## Nine Dimensions

1. Design document
2. Numeric table
3. Code
4. Scene
5. UI
6. Icon/image
7. Scene integration
8. Image integration
9. UI integration

Use numeric percentages for applicable dimensions. Display `Not needed` for non-applicable dimensions and exclude text from averages.

## Order

Sort unfinished features by priority, then ascending feature ID. Put completed features last. Record any dependency, shared lock, or safety blocker that causes a temporary skip.

## Source Collection

Refresh from formal functional documents, numeric/configuration tables, version plans and unimplemented lists, filed producer directives, and latest accountable-role receipts. Verify unchanged sources by index and hash; expand changed sources only.

## Refresh Cadence

Use a short exception-monitoring interval and a slower workbook refresh interval. Update immediately on explicit producer request. Do not save when no tracked state changed.
