---
title: Get Workspace Usage 步骤
description: 将使用情况报告中的工作区使用情况合计按日或按月写入项目表，以便绘制采用情况图表或供下游步骤使用。
sidebar:
  order: 12
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/general/get-workspace-usage.md
---

## 说明

将工作区的使用情况写入项目表。可用于跟踪采用情况的长期变化、按部门或团队报告使用情况、构建自己的仪表板，或在计划工作流中标记活跃度下降。这些数据与[使用情况报告](/zh-cn/administration/access/usage-reports/)中显示的数据一致。

有三个数据集只保存合计值：没有任何行指向具体成员，且笔记本路径会替换为 `*`。其余四个（**成员**、**按成员每日**、**内容**和**按成员的内容**）专为报表而设计。**成员**、**按成员每日**和**按成员的内容**包含成员身份信息（用户 ID、用户名、电子邮件、名字和姓氏以及安全组），因此应像对待成员列表一样对待目标表。该步骤的每次运行都会记录在安全日志中。

## 配置

### 使用情况数据

**数据集**用于选择每行保存的内容：

| 数据集 | 值 | 每行对应 | 包含身份信息 |
|---|---|---|---|
| **按项目每日** | `daily_item` | 日期、领域、事件和主体 | 否 |
| **按项目每月** | `monthly_item` | 月份、领域、事件和主体 | 否 |
| **月度合计**（默认） | `monthly_tenant` | 月份和领域 | 否 |
| **成员** | `members` | 工作区中的每个人 | 是 |
| **按成员每日** | `daily_user` | 人员、日期和领域 | 是 |
| **内容** | `content` | 仪表板、应用或笔记本 | 否 |
| **按成员的内容** | `content_user` | 人员和项目 | 是 |

**领域**将行限定为某一个领域。保持为**所有领域**则包含全部领域。

| 领域 | 值 |
|---|---|
| **所有领域**（默认） | `""` |
| **PlaidCloud 应用** | `plaidclient` |
| **仪表板** | `superset` |
| **应用** | `panel` |
| **应用访问** | `panel_visit` |
| **笔记本服务器** | `jupyterhub` |
| **笔记本** | `jupyter` |

这些值是通过 API 或 AI 助手创建或编辑步骤时步骤所保存的值。

### 列

#### 按项目每日

`day`、`source`、`event`、`subject`、`events`。

#### 按项目每月

`month`、`source`、`event`、`subject`、`users`、`events`、`unattributed_events`、`coverage_start`、`partial`。

#### 月度合计

`month`、`source`、`active_users`、`coverage_start`、`partial`。

对于历史数据未完整覆盖的月份，`partial` 为 true；`coverage_start` 是开始收集数据的日期。某个月份在结束 3 天后、数据稳定时才会被纳入。

#### 成员列

**成员**、**按成员每日**和**按成员的内容**都以相同的七列开头：

| 列 | 内容 |
|---|---|
| `user_id` | 成员的 ID。 |
| `user_name` | 成员的用户名。 |
| `email` | 成员的电子邮件地址，小写。 |
| `first_name` | 名字。 |
| `last_name` | 姓氏。 |
| `is_active` | 成员处于活动状态时为 true，已停用时为 false。 |
| `groups` | 成员所属的安全组，以 `; ` 分隔。 |

`groups` 仅列出顶级分组，不会展开子分组。

#### 成员

先是成员列，然后是：

| 列 | 内容 |
|---|---|
| `first_seen` | 成员首次使用 PlaidCloud 的日期，与日期范围无关。设置**领域**后，则为该领域中的首次使用日期。 |
| `last_seen` | 成员在该范围内最后一次活动的日期。 |
| `active_days` | 该范围内有活动的天数。 |
| `events` | 该范围内的活动事件数。 |
| `active_minutes` | 活动分钟数。各领域之间重叠的分钟只计一次。 |
| `session_minutes` | 会话分钟数。 |
| `app_open_minutes` | 成员打开 Panel 应用的分钟数。 |

每个成员都有一行，但使用数据已被清除的成员除外。服务账户和代理不会列出。在该范围内没有活动的成员，`groups` 之后的值为空。合计值与[使用情况报告](/zh-cn/administration/access/usage-reports/)一致，但此后被删除的成员除外。

#### 按成员每日

先是成员列，然后是 `day`、`source`（领域）、`events`、`active_minutes`、`session_minutes`、`first_at` 和 `last_at`（当天首次和最后一次活动的时间）。

#### 内容

| 列 | 内容 |
|---|---|
| `type` | `dashboard`、`panel_app`、`wasm_app` 或 `notebook`。 |
| `subject` | 项目的 ID。所有笔记本共用一行，此处为 `*`。 |
| `name` | 项目的名称，笔记本则为 `*`。 |
| `deleted` | 项目此后已被删除时为 true。 |
| `users` | 打开过它的成员。 |
| `opens` | 被打开的次数。 |
| `last_used` | 最后一次使用的时间。 |
| `app_open_minutes` | Panel 应用被打开的分钟数。 |

#### 按成员的内容

先是成员列，然后是 `type`、`subject`、`name`（与**内容**中相同）、`opens`（该成员打开该项目的次数）和 `last_day`（该成员最后一次使用的日期）。

### 成员数据集说明

- 来自代理、服务账户以及此后被删除成员的活动，其身份列为空。被删除的成员仅保留 `user_id`。
- **内容**中的打开次数可能超过**按成员的内容**中打开次数之和。差值是无法归属到某个成员的打开次数，例如仪表板的嵌入视图或访客视图。**内容**会统计这些次数，而**按成员的内容**无法统计。

### 示例：按部门统计活动分钟数

**成员**和**按成员的内容**带有成员的小写 `email`，因此可以将其与自己的表（例如人力资源表或组织主数据表）联接，并按部门报告。

1. 添加一个 **Get Workspace Usage** 步骤，将**数据集**设置为**成员**，并指定目标表，例如 `usage_members`。
2. 添加一个 **表：内联接** 步骤，在小写的 `email` 列匹配处将 `usage_members` 与组织表联接。保留组织表中的部门，以及 `usage_members` 中的 `active_minutes` 和 `events` 列。
3. 在同一步骤中按部门聚合，并对 `active_minutes` 求和。

结果即为按部门统计的活动分钟数。不在组织表中的成员会在内联接中被排除，如需查看这些成员，请使用左联接。再对**按成员的内容**使用第二个步骤重复上述操作，并按部门对 `opens` 求和，即可报告哪些部门使用哪些仪表板和应用。

### 日期范围

**范围**用于选择要读取的日期：

| 范围 | 值 | 读取内容 |
|---|---|---|
| **最近天数**（默认 30） | `last_days` | 最近的若干天，包含今天。 |
| **上个月** | `previous_month` | 上一个完整的日历月。 |
| **本月截至目前** | `month_to_date` | 从本月第一天到今天。 |
| **日期之间** | `dates` | 从**开始日期**到**结束日期**。将**结束日期**留空则读取到今天。 |

天数和日期均为 UTC。**天**、**开始日期**和**结束日期**除了数字或 `YYYY-MM-DD` 日期外，也接受[变量](/zh-cn/guides/workflows/manage-workflow-variables/)，例如 `{report_start}`。开始日期不得晚于结束日期。

### 使用情况目标

**目标表**用于接收结果。该步骤会替换表中原有的全部内容，并且始终写入数据集的列，即使没有任何行。

## 警告

这些情况不会导致步骤失败。步骤会在完成时给出说明情况的警告，并仍然写入表：

- 尚未为该工作区设置使用情况收集。
- 该范围内没有使用情况。
- 该范围的起点早于保留的数据，因此已截断为从历史数据起点开始。每日数据保留 180 天，每月数据保留 25 个月。

## 安全日志

每次运行都会向安全日志写入一条记录，记录数据集、范围、目标表、工作流、步骤和运行，以及写入的行数。

## 相关内容

- [General 步骤](/zh-cn/reference/workflow-steps/general/)
- [使用情况报告](/zh-cn/administration/access/usage-reports/)
- [Get Workspace Members 步骤](/zh-cn/reference/workflow-steps/general/get-workspace-members/)
