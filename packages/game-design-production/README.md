# 游戏策划与资源交接总流程包

版本：1.0.0 · 整理日期：2026-11-06 · 中文公开分享版

把需求、视频或当前稿整理成可以交给程序、美术和音频同事执行的资料：**策划案 → 配置表 → 美术需求 → 资源目录 → 音乐音效 → 检查交付 → 调整留档**。也支持只做其中一项，或只改现有文档的局部内容。

这是独立的流程与模板包。无需安装上层仓库的旧版工作室角色插件，也不继承其长期角色编排。本包不绑定任何游戏项目，不包含真实公司策划案、原版专用 Word/Excel 模板、生产素材、聊天记录或账号资料。下面的模板为可改写的 Markdown 骨架和 JSON 表结构定义，**不是已经排版好的 DOCX/XLSX**。

## 给朋友的三个入口

- [直接下载完整 ZIP](https://github.com/xiaoxingwang986-cyber/game-studio-agent-workflow/raw/refs/heads/main/downloads/game-design-production-v1.0.0.zip)
- [从零使用与安装](docs/getting-started.md)
- [查看完整虚构案例](.agents/skills/game-design-handoff/references/example.md)

下载后解压整个文件夹，保留隐藏的 `.agents` 目录。可以直接人工照流程使用；在 Codex 中使用时，按安装说明复制整个 Skill 文件夹，先确认它出现在当前会话的可用列表中，再调用 `$game-design-handoff`。

## 按需求调用

| 你现在要做什么 | 打开哪里 | 会得到什么 |
|---|---|---|
| 从需求、视频起案 | [需求与证据](.agents/skills/game-design-handoff/references/01-intake.md) | 范围、事实、推断、未知项、来源清单 |
| 写或改正式策划案 | [策划文档](.agents/skills/game-design-handoff/references/02-design.md) | 规则、流程、边界、UI、表图和验收 |
| 配套程序配置 | [配置表](.agents/skills/game-design-handoff/references/03-configuration.md) | 中文说明／类型／字段／数据与 Guide |
| 提美术需求 | [美术需求](.agents/skills/game-design-handoff/references/04-art.md) | 资源拆分、数量、复用、参考和验收 |
| 整理资源目录 | [目录与进度](.agents/skills/game-design-handoff/references/05-directory.md) | 分类索引、详情定位、去重和制作状态 |
| 提音乐与音效 | [音频需求](.agents/skills/game-design-handoff/references/06-audio.md) | 13 列交接表、触发／停止／循环 |
| 新 UI、参考图和出图 | [UI 与媒体](.agents/skills/game-design-handoff/references/07-ui-media.md) | 可实施的交互、状态、视觉说明 |
| 检查和交付 | [验证与交付](.agents/skills/game-design-handoff/references/08-quality.md) | 关联核对、原生检查、结果与缺口 |
| 保留调整、下次接续 | [修订与知识](.agents/skills/game-design-handoff/references/09-revisions.md) | 改动来源、当前稿、规则确认和按需索引 |
| 快速取模板 | [模板索引](.agents/skills/game-design-handoff/assets/templates/index.md) | 空白骨架与字段合同 |

## 总流程

1. **接单定范围**：确定当前作者源、要做的交付物、完成标准和不能动的内容。
2. **看资料与取证**：视频记时间点，文件记版本和位置，区分直接事实、推断与待确认。
3. **整理玩法合同**：写清入口、步骤、规则、状态、结果和异常；必要的产品决定由负责人确认。
4. **拆配置及资源**：文档、表、UI、美术和音频共享一致的名称、ID、数量、版本范围。
5. **制作与局部核验**：先核关键页面／状态，再批量制作；小改只验证受影响链。
6. **实际验收**：结构、语义、视觉、原生交互分别留证据，不能用文件存在代替完成。
7. **独立目录交付**：每案、每轮留版本和改动记录，当前稿与历史不混淆。
8. **调整留档**：普通案例改动如实记录；永久规则变更逐次展示差异并取得明确确认。

## 用前知道

- 新项目初始为 `UNBOUND`；由使用者填写自己的项目、来源和输出位置。
- 本分享版默认文档版本 1.0，作者由使用者填写，制作起止日期为当日；不自动递增版本。
- 文档和配表修订默认新增／修改标黄，保留语义颜色和用户手改。正式项目约定或当前用户指令优先。
- 自动加载本包不授权安装软件、登录、发布、跨对话发消息或启动后台任务。
- 本包记录规则和工作方法，不提供永久后台记忆。接新任务仍须回读当前来源和新增记录。
- 静态校验命令：`python scripts/verify_package.py`。它检查包的完整性，不证明任何新项目已完成验收。

[许可](LICENSE) · [公开边界与来源说明](docs/publication.md) · [验证说明](docs/validation.md)
