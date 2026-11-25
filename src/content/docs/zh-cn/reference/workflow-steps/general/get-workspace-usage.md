---
title: Get Workspace Usage 步骤
description: 将工作区使用情况按活动、成员、内容或趋势写入项目表，以便报告采用情况或供下游步骤使用。
sidebar:
  order: 12
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/general/get-workspace-usage.md
---

## 说明

将工作区的使用情况写入项目表。可用于跟踪采用情况的长期变化、按部门或团队报告使用情况、构建自己的仪表板，或在计划工作流中标记活跃度下降。这些数据与[使用情况报告](/zh-cn/administration/access/usage-reports/)使用相同的使用情况数据，且每个数据集都涵盖所有领域。

**活动**和**成员**包含成员身份信息（用户 ID、用户名、电子邮件、名字和姓氏以及安全组）。目标表是普通的项目表，因此任何有权访问该项目的人都可以读取它：应像对待成员列表一样对待它。每次写入该表的运行都会记录在安全日志中。

## 配置

### 使用情况数据

**数据集**用于选择每行保存的内容。其下方的说明行会列出所选数据集的行和列。

| 数据集 | 值 | 每行对应 | 包含身份信息 |
|---|---|---|---|
| **活动**（默认） | `activity` | 日期、成员、操作和项目 | 是 |
| **成员** | `members` | 成员，包括没有活动的成员 | 是 |
| **内容** | `content` | 仪表板、应用和笔记本，包括无人使用的仪表板和应用 | 否 |
| **趋势** | `trends` | 范围内的每一天、每一周和每个月 | 否 |

这些值是通过 API 或 AI 助手创建或编辑步骤时步骤所保存的值。如果步骤保存的数据集不在此列表中，运行时会失败并列出这四个数据集：请打开该步骤，选择一个**数据集**并保存。之前保存的**成员**或**内容**步骤会继续运行并写入下面的列，而之前限定在一个领域的步骤现在会覆盖所有领域。

### 列

日期和天以 UTC 午夜的时间戳写入。

#### 成员列

**活动**和**成员**包含以下列：

| 列 | 内容 |
|---|---|
| `user_id` | 成员的 ID。 |
| `user_name` | 成员的用户名。 |
| `email` | 成员的电子邮件地址，小写。 |
| `first_name` | 名字。 |
| `last_name` | 姓氏。 |
| `is_active` | 成员处于活动状态时为 true，已停用时为 false。 |
| `groups` | 成员所属的安全组，以 `; ` 分隔。 |

`groups` 列出成员直接所属的分组，不会展开子分组。

#### 活动

| 列 | 内容 |
|---|---|
| `day` | 日期。 |
| 成员列 | 同上。 |
| `member` | 成员的名字和姓氏；两者均未设置时为其用户名。 |
| `area` | `PlaidCloud app`、`Dashboards`、`Apps` 或 `Notebooks`。 |
| `action` | `Opened app`、`Opened screen`、`Opened step`、`Saved step`、`Used palette action`、`Viewed dashboard`、`Used chart`、`Opened notebook` 或 `Saved notebook`。 |
| `item_type` | `App area`、`Screen`、`Step`、`Palette action`、`Dashboard`、`Chart`、`App` 或 `Notebook`。 |
| `item_id` | 项目的 ID。笔记本则为其路径。 |
| `item_name` | 项目的名称：屏幕或应用区域的文字名称，例如 `Members List`；步骤类型；仪表板、图表或应用的名称；或笔记本的路径。找不到名称时为项目的 ID。 |
| `events` | 成员当天执行该操作的次数。 |
| `source` | 领域的键，与[使用情况报告](/zh-cn/administration/access/usage-reports/)导出中的名称相同。 |
| `event` | 操作的键，与导出中的名称相同。 |

`member` 和成员列取决于操作者：

- 无法关联到任何成员的活动，其 `member` 为 `Unattributed`，成员列为空。
- 此后被删除的成员仅保留 `user_id`，其 `member` 为 `Deleted user`。
- 任何其他账户，例如服务账户或代理，仅保留 `user_id`，其 `member` 为其用户名。

`Used chart` 在每个 5 分钟窗口内按成员和图表各计一次，因此衡量的是使用情况，而不是查询次数。

#### 成员

| 列 | 内容 |
|---|---|
| 成员列 | 同上。 |
| `member` | 成员的名字和姓氏；两者均未设置时为其用户名。 |
| `created` | 成员被添加到工作区的日期（已知时）。 |
| `status` | 成员在该范围内有活动时为 `Active`；以前使用过 PlaidCloud 但在该范围内没有使用时为 `Dormant`；截至该范围结束没有任何使用记录时为 `Never active`。 |
| `first_seen` | 记录中成员首次使用 PlaidCloud 的日期，与范围无关。 |
| `last_seen` | 成员在该范围内最后一次活动的日期。 |
| `active_days` | 该范围内有活动的天数。 |
| `events` | 该范围内的活动事件数。 |
| `active_minutes` | 该范围内的活动分钟数。 |
| `session_minutes` | 该范围内的会话分钟数。 |
| `app_open_minutes` | 成员在该范围内打开 Panel 应用的分钟数。不统计 Studio 预览。 |

每个成员都有一行，包括已停用的成员，但使用数据已被清除的成员除外。服务账户和代理不会列出。在该范围内没有活动的成员没有 `last_seen`，其他活动列为空或为零。

#### 内容

| 列 | 内容 |
|---|---|
| `type` | `Dashboard`、`App` 或 `Notebook`。 |
| `item_id` | 仪表板或应用的 ID，或笔记本的路径。 |
| `name` | 仪表板或应用的名称，或笔记本的路径。项目已被删除或无法读取名称时为空。 |
| `deleted` | 仪表板或应用此后已被删除时为 true。 |
| `unused` | 仪表板或应用在该范围内无人使用时为 true。 |
| `users` | 在该范围内使用过它的成员。 |
| `opens` | 在该范围内被打开的次数，包括无法关联到成员的打开。 |
| `last_used` | 在该范围内最后一次使用的日期。对于未使用的项目，为范围结束前最后一次被打开的日期，或为空。 |
| `app_open_minutes` | Panel 应用在该范围内被打开的分钟数。仪表板、笔记本以及 Dash 和 WASM 应用为空。 |

每个笔记本路径各占一行。各行先列出已使用的内容（使用成员最多的在前），然后是无人使用的仪表板和应用。这些是已发布的仪表板，以及范围开始时已经存在的应用。只有当范围起点在保留的每日数据之内、当时已在收集该类项目的使用情况且能读取名称时，才会列出它们。应用的 Studio 预览不包括在内。

#### 趋势

| 列 | 内容 |
|---|---|
| `period` | `Day`、`Week` 或 `Month`。 |
| `period_start` | 该周期的第一天。每周从周一开始。 |
| `active_members` | 该周期内、范围内活动的成员。 |
| `events` | 该周期内的活动事件数。 |
| `active_minutes` | 该周期内的活动分钟数。 |
| `session_minutes` | 该周期内的会话分钟数。 |
| `active_members_7d` | 在 `Day` 行上，截至当天的 7 天内活动的成员。 |
| `active_members_28d` | 在 `Day` 行上，截至当天的 28 天内活动的成员。 |
| `stickiness` | 在 `Day` 行上，`active_members` 除以 `active_members_28d`。 |
| `complete` | 对于今天、包含今天的周或月，以及被范围截断的周或月，为 false。 |

从保留的每日数据开始之处起，范围内的每一天都有一行，即使没有使用情况，这些天所在的每一周和每个月也是如此。在 `Week` 和 `Month` 行上，以及其 7 天或 28 天跨到保留的每日数据之前的 `Day` 行上，`active_members_7d`、`active_members_28d` 和 `stickiness` 为空。始于保留的每日数据之前且完全位于范围内的月份来自月度摘要：它有 `active_members`，但事件和分钟数为空，`complete` 表示该摘要是否覆盖了整个月。

### 示例：按部门统计活动分钟数

**活动**和**成员**带有成员的小写 `email`，因此可以将其与自己的表（例如人力资源表或组织主数据表）联接，并按部门报告。

1. 添加一个 **Get Workspace Usage** 步骤，将**数据集**设置为**成员**，并指定目标表，例如 `usage_members`。
2. 添加一个 **表：内联接** 步骤，在小写的 `email` 列匹配处将 `usage_members` 与组织表联接。保留组织表中的部门，以及 `usage_members` 中的 `active_minutes` 和 `events` 列。
3. 在同一步骤中按部门聚合，并对 `active_minutes` 求和。

结果即为按部门统计的活动分钟数。不在组织表中的成员会在内联接中被排除，如需查看这些成员，请使用左联接。再对**活动**使用第二个步骤重复上述操作，并按部门和 `item_name` 对 `events` 求和，即可报告哪些部门使用哪些仪表板和应用。

### 日期范围

**范围**用于选择要读取的日期：

| 范围 | 值 | 读取内容 |
|---|---|---|
| **最近天数**（默认 30） | `last_days` | 最近的若干天，包含今天。 |
| **上个月** | `previous_month` | 上一个完整的日历月。 |
| **本月截至目前** | `month_to_date` | 从本月第一天到今天。 |
| **日期之间** | `dates` | 从**开始日期**到**结束日期**。将**结束日期**留空则读取到今天。 |

天数和日期均为 UTC。**天**接受整数。**开始日期**和**结束日期**接受 `YYYY-MM-DD` 日期或[变量](/zh-cn/guides/workflows/manage-workflow-variables/)，例如 `{report_start}`。开始日期不得晚于结束日期。

每日数据保留 180 天，月度摘要保留 25 个月。

### 使用情况目标

**目标表**用于接收结果。该步骤会替换表中原有的全部内容，并且始终写入数据集的列，即使没有任何行。

## 警告

这些情况不会导致步骤失败。步骤会在完成时给出该警告，并仍然替换表，写入数据集的列：

| 警告 | 含义 |
|---|---|
| "Usage data is not available yet: the usage database has not been set up on this workspace." | 尚未为该工作区设置使用情况收集。 |
| "Usage data is not available right now: the usage database could not be reached." | 无法读取使用情况数据。请稍后再次运行该步骤。 |
| "No usage from *start* to *end*." | 该范围内没有使用情况。 |
| "Usage before *date* isn't kept, so the range was clipped to start there." | 该范围的起点早于保留的每日数据，因此从 *date* 起统计活动。**趋势**仍然通过月度摘要包含此前的完整月份。 |
| "This took too long to compute: narrow the date range." | 读取超时，因此表中没有行。请选择更短的范围。 |
| "Some names are unavailable right now, so those items are named by their id." | 仅限**活动**。部分仪表板、图表或应用的名称无法读取，因此 `item_name` 为 ID。 |
| "Members could not be read right now, so they are named by their id." | 仅限**活动**。无法读取成员列表，因此 `member` 为成员的 ID，成员列中只填充 `user_id`。 |
| "Names are unavailable right now, so items nobody used are not listed." | 仅限**内容**。无法读取仪表板或应用的名称，因此只列出已使用的项目。 |
| "Activity before *date* isn't kept, so items nobody used in this range can't be listed." | 仅限**内容**。该范围的起点早于保留的每日数据，因此只列出已使用的项目。 |

当无法读取成员列表时，**成员**会失败，并保持目标表不变。

## 安全日志

每次写入该表的运行都会向安全日志写入一条记录，记录数据集、范围、目标表及其项目、工作流、步骤和运行、写入的行数，以及（对于**活动**和**成员**）这些行包含成员身份信息。

## 相关内容

- [General 步骤](/zh-cn/reference/workflow-steps/general/)
- [使用情况报告](/zh-cn/administration/access/usage-reports/)
- [Get Workspace Members 步骤](/zh-cn/reference/workflow-steps/general/get-workspace-members/)
