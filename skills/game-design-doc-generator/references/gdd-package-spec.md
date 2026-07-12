# GDD Package Spec

## Document Skeleton

Use this Word structure by default:

1. 版本管理
   - 文件状态、文档编号、作者、当前版本、创建日期、完成日期、版本历史、开发计划。
2. 文档简介
   - 术语缩写、设计目标、系统概述、名词解释。
3. 系统框架
   - 功能模块图、核心循环图、数据流/奖励流图。
4. UI界面
   - 入口、主界面、子界面、弹窗、战斗/结算/奖励界面、帮助说明。
   - Each page: 出现规则、展示内容、交互逻辑、状态规则、红点/提示、异常处理、配置字段、插入效果图。
5. 系统设计
   - 规则描述、开启/关闭、周期刷新、战斗/挑战/结算、奖励、扫荡/重置、排行榜、随机规则、限制条件、边界情况。
6. UE流程
   - After UI/system flows are stable, add UE/客户端实现流程: Widget entry, data request, state machine, event dispatch, refresh triggers, error branches.
7. 配置表需求
   - List all Excel sheets and important fields.
8. 美术资源需求
   - All UI, icon, effect, scene, animation, flowchart, and placeholder assets.
9. 音乐音效需求
10. 功能打点需求
11. 后期扩展
12. 待确认项

## Required Diagrams

Generate diagrams before final DOCX assembly:

- System module diagram: feature modules and ownership.
- Player core loop: enter -> choose -> challenge/upgrade -> reward -> next goal.
- UI interaction flow: every screen and popup route.
- State flow: locked/unlocked/available/completed/expired/rewarded/failed.
- Reward flow: source, claim, storage, mail fallback, repeat limits.
- UE flow: client widget/state/data/event flow. Generate after other diagrams.

Insert each diagram under the closest heading. Use short captions.

## Effect Images

Generate or compose mockups for important screens:

- Entrance state: locked, unlocked, active/red point.
- Main interface: normal state and with active guidance/red point.
- Key popup: locked, available, insufficient resources, completed.
- Reward/settlement page.
- Special gameplay screen if applicable.

If exact art is unknown, create annotated grayscale/wireframe mockups and mark assets as `占位`.

## Art Requirement Priority

Use these priorities:

- P0: Blocks gameplay comprehension or implementation; required for first playable build.
- P1: Required for complete UI/UX and external test.
- P2: Polish, animation, alternate states, later expansion.
- P3: Optional, nice-to-have, seasonal or replaceable.

Art requirement fields:

`AssetID, AssetName, Type, Page/System, Usage, State, SuggestedSize, Format, Dynamic/Static, Priority, Dependencies, Notes`

Every inserted image or chart needs one art row. Flowcharts can use `Type=流程图`.

## Excel Workbook

Create one `.xlsx` with these sheets when relevant:

- `SystemConfig`: feature id, unlock, open time, reset, switches.
- `UIPage`: page id, name, entry, close rule, help id, red point id.
- `StateRule`: state id, trigger, condition, display, interaction, next state.
- `Reward`: reward id, source, condition, item group, repeat limit, mail fallback.
- `Cost`: cost id, action, resource, amount formula, insufficient tip.
- `LevelOrNode`: level/node id, type, unlock, max level, rewards/costs, coordinates if needed.
- `Text`: text id, zh text, usage, variables.
- `ArtResource`: same fields as art requirement list.
- `Telemetry`: event id, trigger, parameters, purpose.
- `TodoConfirm`: unresolved requirement, assumption, owner.

Use stable IDs and avoid merged cells. Freeze the header row. Apply data validation lists where useful.

## Content Rules

- Write implementable rules, not marketing copy.
- Prefer tables for repeated states/config; prefer prose for design intent.
- Mark all inferred content as `假设`.
- Include edge cases: insufficient resources, expired period, reward already claimed, inventory full, disconnect/reopen, server refresh, version expansion.
- Keep rules consistent between Word and Excel.
