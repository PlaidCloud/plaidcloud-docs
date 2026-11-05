---
title: Get Workspace Usage
description: 将使用情况报告中的工作区使用情况合计按天或按月写入项目表，以便绘制采用情况图表或驱动下游步骤。
sidebar:
  order: 12
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/general/get-workspace-usage.md
---

## 说明

将工作区使用情况的摘要写入项目表。可用于跟踪一段时间内的采用情况、基于使用情况构建自己的仪表板，或在计划的工作流中标记活动下降。其数据与[使用情况报告](/zh-cn/administration/access/usage-reports/)中显示的数据相同。

输出仅包含合计值。没有任何行会指明具体成员，笔记本路径会替换为 `*`。使用数据已被清除的成员不包含在内。

## 配置

### Usage Data

**Dataset** 选择每一行包含的内容：

| 数据集 | 每一行对应 | 列 |
|---|---|---|
| **Daily per item** | 日、领域、事件和主题 | `day`、`source`、`event`、`subject`、`events` |
| **Monthly per item** | 月、领域、事件和主题 | `month`、`source`、`event`、`subject`、`users`、`events`、`unattributed_events`、`coverage_start`、`partial` |
| **Monthly totals**（默认） | 月和领域 | `month`、`source`、`active_users`、`coverage_start`、`partial` |

对于历史记录未完整覆盖的月份，`partial` 为 true；`coverage_start` 是开始收集的日期。

**Area** 将行限定为一个领域：**PlaidCloud 应用**、**仪表板**、**应用**、**App visits** 或 **Notebooks**。保持为 **All areas** 则包含全部领域。

### Date Range

**Range** 选择要读取的天数：

- **Last number of days**（默认 30）读取最近的天数，包括今天。
- **Previous month** 读取上一个完整的日历月。
- **本月截至目前** 读取从本月 1 日到今天的数据。
- **Between dates** 读取从 **开始日期** 到 **结束日期** 的数据。将 **结束日期** 留空则读取到今天。

天数和日期均为 UTC。**天**、**开始日期** 和 **结束日期** 除接受数字或 `YYYY-MM-DD` 日期外，也接受[变量](/zh-cn/guides/workflows/manage-workflow-variables/)，例如 `{report_start}`。开始日期不得晚于结束日期。

### Usage Target

**目标表** 接收结果。该步骤会替换表中原有的所有内容，并且始终写入数据集的列，即使没有行也是如此。

## 警告

这些情况不会导致步骤失败。步骤会以警告结束并说明发生了什么，同时仍会写入表：

- 尚未为工作区设置使用情况收集。
- 该范围内没有使用数据。
- 范围的起点早于所保留的数据，因此已截短为从历史记录开始处起算。每日数据保留 180 天，月度数据保留 25 个月。

## 安全日志

每次运行都会向安全日志写入一条记录，记录数据集、范围、目标表，以及工作流、步骤和运行，还有写入的行数。

## 相关内容

- [常规步骤](/zh-cn/reference/workflow-steps/general/)
- [使用情况报告](/zh-cn/administration/access/usage-reports/)
- [Get Workspace Members](/zh-cn/reference/workflow-steps/general/get-workspace-members/) 步骤
