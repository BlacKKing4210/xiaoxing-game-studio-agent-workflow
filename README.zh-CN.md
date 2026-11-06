# 游戏工作室智能体工作流

> **中文策划与资源交接总流程包（独立使用）**：[在线说明](packages/game-design-production/README.md) · [下载 ZIP](downloads/game-design-production-v1.0.0.zip)  
> 覆盖策划案、配置、美术需求、资源目录、音效、UI、修订与验收，附空白模板和可复制 Skill。此包无需启用下方旧版多角色插件；使用范围及能力边界见包内说明。

一套以制作人为唯一决策入口、以真实游戏内证据为验收标准的 Codex 多智能体游戏开发流程。

它把自然语言需求转换为策划、程序、美术、QA 和交接任务，同时保留明确的负责人、写入边界、共享文件锁、卡死替换和功能级九维进度。

## 核心特点

- 一个制作人入口统一收需求和排优先级。
- 主策、主程、主美长期保留，自主管理本领域短生命周期执行任务。
- 每个执行任务先提交只读收据，再获得写入授权。
- 美术和程序在边界分离时并行，优先尽快形成游戏内可玩预览。
- 有正式资源时必须使用完整正式资源；缺资源时才允许明确标记的开发占位。
- 九维进度以完整功能为行，不按单个文档或素材拆散。
- 任务卡死时先建立只读候选接管，再归档旧任务，避免双写和资料丢失。
- 每30分钟只查当前批次异常，每6小时更新功能进度表；无异常保持静默。

## 快速开始

```powershell
git clone https://github.com/xiaoxingwang986-cyber/game-studio-agent-workflow.git
cd game-studio-agent-workflow
./scripts/init-project.ps1 -ProjectRoot "D:\Games\MyGame" -ProjectName "我的游戏" -Engine Godot
```

随后在项目 Codex 对话中说：

```text
你是PM，读取项目工作流和交接资料，接管后按最高优先级READY功能继续推进。
```

## 九维功能进度

每个完整功能记录：

1. 策划案
2. 数值表
3. 代码
4. 场景
5. UI
6. 图标图片
7. 场景落地
8. 图片落地
9. UI落地

不适用项显示“Not needed / 不需要”，不参与平均。功能先按优先级排列，同优先级按功能 ID 升序，已完成项置后。

## 隐私

公开仓库不包含任何具体游戏的路径、线程ID、哈希、角色资料、数值、素材或内部任务记录。所有项目事实都应放入本地 Profile 与活动范围文件。

## 内置 Skill

公开插件当前包含14个通用 Skill：工作室总控、PM执行巡检、精简主策、策划文档交付、系统交付、Godot切片、UI优先级、角色图、侧视单位、序列帧接入、动画管线、循环场景、场景层转换和批量资产整板。

项目专用上下文不会直接公开；使用 `templates/project-adapter-skill/SKILL.md` 创建本地适配器。系统自带的 `imagegen`、`documents`、`spreadsheets` 和 `skill-creator` 作为依赖使用，不重复打包。
