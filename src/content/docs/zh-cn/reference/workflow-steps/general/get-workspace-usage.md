---
title: Get Workspace Usage 步骤
description: 将使用情况报告中的工作区使用情况合计按日或按月写入项目表，以便绘制采用情况图表或供下游步骤使用。
sidebar:
  order: 12
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/general/get-workspace-usage.md
---

## 说明

将工作区的使用情况写入项目表。可用于跟踪一段时间内的采用情况、按部门或团队报告使用情况、构建自己的仪表板，或在计划工作流中标记活动量下降。这些数据与[使用情况报告](/zh-cn/administration/access/usage-reports/)中显示的数据相同。

其中三个数据集只包含合计值：没有任何行指明成员，且笔记本路径会替换为 `*`。其余四个数据集（**Members**、**Daily per member**、**Content** 和 **Content per member**）专为报告而设计。**Members**、**Daily per member** 和 **Content per member** 包含成员身份信息（用户 ID、用户名、电子邮件、名和姓以及安全组），因此应像对待任何成员列表一样对待目标表。该步骤的每次运行都会记录在安全日志中。

## 配置

### 使用数据

**Dataset** 用于选择每行包含的内容：

| 数据集 | 每行对应 | 包含身份信息 |
|---|---|---|
| **Daily per item** | 日期、区域、事件和对象 | 否 |
| **Monthly per item** | 月份、区域、事件和对象 | 否 |
| **Monthly totals**（默认） | 月份和区域 | 否 |
| **Members** | 工作区中的每个人 | 是 |
| **Daily per member** | 人员、日期和区域 | 是 |
| **Content** | 仪表板、应用或笔记本 | 否 |
| **Content per member** | 人员和项目 | 是 |

**Area** 将行限定为一个区域：**PlaidCloud app**、**Dashboards**、**Apps**、**App visits** 或 **Notebooks**。保持为 **All areas** 则包含所有区域。

### 列

#### 按项目每日

`day`、`source`、`event`、`subject`、`events`。

#### 按项目每月

`month`、`source`、`event`、`subject`、`users`、`events`、`unattributed_events`、`coverage_start`、`partial`。

#### 每月合计

`month`、`source`、`active_users`、`coverage_start`、`partial`。

对于历史记录未完整覆盖的月份，`partial` 为 true；`coverage_start` 是开始收集数据的日期。月份在结束并稳定后才会纳入，这需要 3 天。

#### 成员列

**Members**、**Daily per member** 和 **Content per member** 以相同的七列开头：

| 列 | 内容 |
|---|---|
| `user_id` | 成员的 ID。 |
| `user_name` | 成员的用户名。 |
| `email` | 成员的电子邮件地址，小写。 |
| `first_name` | 名。 |
| `last_name` | 姓。 |
| `is_active` | 成员处于活动状态时为 true，已停用时为 false。 |
| `groups` | 成员所属的安全组，以 `; ` 分隔。 |

`groups` 仅列出顶级分组，不会展开子分组。

#### 成员

先是成员列，然后是：

| 列 | 内容 |
|---|---|
| `first_seen` | 成员首次使用 PlaidCloud 的日期，与日期范围无关。 |
| `last_seen` | 成员在该范围内最后一次活动的日期。 |
| `active_days` | 该范围内有活动的天数。 |
| `events` | 该范围内的活动事件数。 |
| `active_minutes` | 活动分钟数。各区域之间重叠的分钟只计一次。 |
| `session_minutes` | 会话分钟数。 |
| `app_open_minutes` | 成员打开 Panel 应用的分钟数。 |

工作区中的每个人都有一行。在该范围内没有活动的成员，`groups` 之后的值为空。合计值与[使用情况报告](/zh-cn/administration/access/usage-reports/)一致，但此后已删除的成员除外。

#### 按成员每日

先是成员列，然后是 `day`、`source`（区域）、`events`、`active_minutes`、`session_minutes`、`first_at` 和 `last_at`（当天首次和最后一次活动的时间）。

#### 内容

| 列 | 内容 |
|---|---|
| `type` | `dashboard`、`panel_app`、`wasm_app` 或 `notebook`。 |
| `subject` | 项目的 ID。所有笔记本共用一行，此处为 `*`。 |
| `name` | 项目的名称；笔记本为 `*`。 |
| `deleted` | 项目此后已被删除时为 true。 |
| `users` | 打开过它的成员数。 |
| `opens` | 被打开的次数。 |
| `last_used` | 最后一次使用的时间。 |
| `app_open_minutes` | Panel 应用被打开的分钟数。 |

#### 按成员的内容

先是成员列，然后是 `type`、`subject`、`name`（与 **Content** 相同）、`opens`（该成员打开此项目的次数）和 `last_day`（该成员最后一次使用的日期）。

### 成员数据集说明

- 来自代理、服务账户以及此后已删除成员的活动，其身份列为空。已删除的成员只保留 `user_id`，其他信息均不保留。
- **Content** 中的打开次数可能超过 **Content per member** 中打开次数之和。差值是无法归属到某个成员的打开次数，例如仪表板的嵌入式视图或访客视图。**Content** 会统计这些次数，而 **Content per member** 无法统计。

### 示例：按部门统计活动分钟数

**Members** 和 **Content per member** 包含成员的小写 `email`，因此可以将其与自己的表（例如人力资源表或组织主表）联接，并按部门报告。

1. 添加 **Get Workspace Usage** 步骤，将 **Dataset** 设置为 **Members**，并指定目标表，例如 `usage_members`。
2. 添加 **表：内联接** 步骤，在小写 `email` 列匹配的位置将 `usage_members` 与组织表联接。保留自己的表中的部门，以及 `usage_members` 中的 `active_minutes` 和 `events` 列。
3. 在同一步骤中按部门聚合，并对 `active_minutes` 求和。

结果即为按部门统计的活动分钟数。不在组织表中的成员会在内联接中被排除，如需查看他们，请改用左联接。在 **Content per member** 上用第二个步骤重复上述操作，并按部门对 `opens` 求和，即可报告谁在使用哪些仪表板和应用。

### 日期范围

**Range** 用于选择要读取的天数：

- **Last number of days**（默认为 30）读取最近的若干天，包括今天。
- **Previous month** 读取上一个完整的日历月。
- **Month to date** 读取从本月 1 日到今天。
- **Between dates** 读取从 **Start Date** 到 **End Date**。将 **End Date** 留空则读取到今天。

天数和日期均为 UTC。**Days**、**Start Date** 和 **End Date** 除数字或 `YYYY-MM-DD` 日期外，还接受[变量](/zh-cn/guides/workflows/manage-workflow-variables/)，例如 `{report_start}`。开始日期不得晚于结束日期。

### 使用情况目标

**Target Table** 接收结果。该步骤会替换表中原有的全部内容，并且始终写入数据集的列，即使没有任何行。

## 警告

这些情况不会导致步骤失败。步骤会在完成时给出说明情况的警告，并仍然写入表：

- 尚未为工作区设置使用情况收集。
- 该范围内没有使用情况。
- 该范围的开始日期早于保留的数据，因此已截断为从历史记录起始处开始。每日数据保留 180 天，每月数据保留 25 个月。

## 安全日志

每次运行都会向安全日志写入一条记录，内容包括数据集、范围、目标表、工作流、步骤和运行，以及写入的行数。

## 相关内容

- [常规步骤](/zh-cn/reference/workflow-steps/general/)
- [使用情况报告](/zh-cn/administration/access/usage-reports/)
- [Get Workspace Members](/zh-cn/reference/workflow-steps/general/get-workspace-members/)
