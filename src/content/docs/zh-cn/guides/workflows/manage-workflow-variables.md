---
title: 管理工作流变量
description: 在 PlaidCloud 中管理工作流变量，以存储动态值并在步骤之间传递，实现灵活的数据处理逻辑。
sidebar:
  order: 14
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/manage-workflow-variables.md
---

PlaidCloud 支持项目范围和工作流范围的变量，既可以设置项目级变量，也可以在工作流之间轻松传递信息。单击 **工作流** 层次结构中的变量图标即可查看变量及其值。



在变量表中可以查看变量及其当前值，并编辑这些值。还可以添加新变量或删除现有变量。

## 内置变量

步骤设置和表达式无需定义即可使用以下内置变量：

| 变量 | 值 |
|---|---|
| `{project}`、`{model}`、`{cloud}` | 项目、模型和工作区的名称。 |
| `{date}` | 运行时的当前 UTC 时间的长格式，例如 `Wednesday, 11 November 2026 10:30PM UTC +0`。 |
| `{date_iso}` | 同一时刻的 ISO 8601 格式，例如 `2026-11-12T22:49:56+00:00`。 |

当表达式需要读取日期的某一部分时，请使用 `{date_iso}`。取其前 7 个字符得到月份（`2026-11`），取其前 10 个字符得到日期（`2026-11-12`）。`{date_iso}` 可用于 `{date}` 能用的所有位置，包括通知电子邮件模板，以及 Forecast、Parity 和 Solver 步骤。
