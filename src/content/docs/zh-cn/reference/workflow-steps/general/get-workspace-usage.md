---
title: Get Workspace Usage 步骤
description: 将使用情况报告中的工作区使用情况合计按天或按月写入项目表，以便绘制采用情况图表或驱动下游步骤。
sidebar:
  order: 12
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/general/get-workspace-usage.md
---

## 说明

将工作区的使用情况摘要写入项目表。可用于跟踪长期采用情况、基于使用情况构建自己的仪表板，或在计划工作流中标记活动下降。这些数据与[使用情况报告](/zh-cn/administration/access/usage-reports/)显示的数据相同。

输出仅包含合计值，没有任何一行指明具体成员，笔记本路径会替换为 `*`。使用情况已被清除的成员不包含在内。

## 配置

### 使用情况数据

**数据集**决定每行包含的内容：

| 数据集 | 每行对应 | 列 |
|---|---|---|
| **每日明细** | 日、区域、事件和主题 | `day`、`source`、`event`、`subject`、`events` |
| **每月明细** | 月、区域、事件和主题 | `month`、`source`、`event`、`subject`、`users`、`events`、`unattributed_events`、`coverage_start`、`partial` |
| **每月合计**（默认） | 月和区域 | `month`、`source`、`active_users`、`coverage_start`、`partial` |

对于历史记录未完整覆盖的月份，`partial` 为 true；`coverage_start` 是开始收集的日期。

**区域**将行限制为某一个区域：**PlaidCloud 应用**、**仪表板**、**应用**、**应用访问**或**笔记本**。保持为**所有区域**则包含所有区域。

### 日期范围

**范围**决定要读取的天数：

- **最近天数**（默认 30）读取最近的天数，包含今天。
- **上个月**读取上一个完整的日历月。
- **本月截至目前**读取从本月 1 日到今天的数据。
- **日期之间**读取从**开始日期**到**结束日期**的数据。将**结束日期**留空则读取到今天。

日和日期均按 UTC 计算。**天**、**开始日期**和**结束日期**除了数字或 `YYYY-MM-DD` 日期外，还接受[变量](/zh-cn/guides/workflows/manage-workflow-variables/)，例如 `{report_start}`。开始日期不得晚于结束日期。

### 使用情况目标

**目标表**接收结果。该步骤会替换表中原有的全部内容，并且始终写入数据集的列，即使没有任何行。

## 警告

以下情况不会导致步骤失败。步骤会带着说明情况的警告完成，并仍然写入表：

- 工作区尚未设置使用情况收集。
- 该范围内没有使用情况。
- 该范围的起点早于保留的数据，因此已截断为从历史记录开始处起算。每日数据保留 180 天，每月数据保留 25 个月。

## 安全日志

每次运行都会向安全日志写入一条记录，记录数据集、范围、目标表、工作流、步骤和运行，以及写入的行数。

## 相关内容

- [常规步骤](/zh-cn/reference/workflow-steps/general/)
- [使用情况报告](/zh-cn/administration/access/usage-reports/)
- [Get Workspace Members 步骤](/zh-cn/reference/workflow-steps/general/get-workspace-members/)
