---
title: "TM1：读取维度"
description: 通过 REST 云端直连，将 IBM TM1 / Planning Analytics 层次结构（元素、父子关系边和元素属性）读取到 PlaidCloud 维度中。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/ibm-planning-analytics/tm1-dimension-read.md
---

## 说明

通过 [TM1 连接](/zh-cn/guides/connections/tm1/)从 IBM **TM1 / Planning Analytics** 维度读取一个层次结构，并将其加载到 PlaidCloud 维度中。TM1 层次结构的元素、父子关系边和元素属性会先以父子行的形式暂存到表中，再由该暂存表构建 PlaidCloud 维度——这与 PlaidCloud 自身的 Dimension Load 步骤执行的加载相同，因此 TM1 层次结构的加载结果与手工构建的或任何其他外部来源的层次结构完全一致。

此步骤在步骤菜单中位于 **IBM TM1 / Planning Analytics** 下。

该步骤通过 REST API **云端直连** TM1——不涉及本地代理。本地方式请参见 [TM1：查询多维数据集（代理）](/zh-cn/reference/workflow-steps/ibm-planning-analytics/tm1-query-remote/)。

## 配置

### TM1 源

| 字段 | 是否必填 | 说明 |
|---|---|---|
| TM1 连接 | 是 | 用于读取的 [TM1 连接](/zh-cn/guides/connections/tm1/)。 |
| 环境 | 是 | 连接的环境。 |
| 数据库 | 是 | 要读取的 TM1 数据库（实例）。如果设置了连接的默认数据库，则默认使用它。 |
| TM1 维度 | 是 | 要读取的 TM1 维度。可从已连接的数据库实时发现，也可手动输入。 |
| TM1 层次结构 | 否 | 维度内的层次结构。选择维度后可实时发现，也可手动输入。留空则读取该维度自身的（隐式）层次结构，TM1 以维度名称命名它。 |
| 暂存表 | 是 | 原始父/子/属性行在用于构建 PlaidCloud 维度之前存放的表。 |

选择维度和层次结构后，表单会显示哪些 TM1 元素属性将作为 PlaidCloud **别名**加载、哪些将作为**属性**加载——由 TM1 自身的属性类型决定（`Alias` 与 `Numeric`/`String`）。每个元素自身的 TM1 类型（Numeric、String 或 Consolidated）也会作为属性加载，名为 `tm1_element_type`。

### 目标 PlaidCloud 维度

| 字段 | 是否必填 | 说明 |
|---|---|---|
| 动态指定维度 | 二选一 | 目标维度名称，可包含在运行时解析的 `{variable}` 标记。默认选中。 |
| 使用特定维度 | 二选一 | 改为从树中选取已有的 PlaidCloud 维度。 |
| 备用层次结构 | 否 | 要加载到的 PlaidCloud 备用层次结构键。留空则加载主层次结构。 |

加载到备用层次结构时，会在写入任何内容之前进行验证：PlaidCloud 备用层次结构不得为维度主层次结构中已存在的节点重新指定父节点，而 TM1 备用层次结构按定义与 TM1 自身的主层次结构共享元素，因此这是该选项的正常形态，而不是边缘情况。如果任何已解析行的父节点已存在于目标维度的主层次结构中，步骤会在动用暂存表之前直接失败，并指明冲突的父节点。

## 此步骤无法表示的内容

| 限制 | 含义 |
|---|---|
| 拒绝多父元素 | PlaidCloud 维度节点在每个层次结构中恰好有一个父节点。位于同一层次结构中两个合并项下的 TM1 元素无法加载——步骤会以带名称的错误失败，列出每个有问题的元素及其父节点，而不是悄悄把该元素从第一个合并项中丢掉。请将备用汇总读取为单独的 PlaidCloud 维度，或先在 TM1 中解决重复的父级关系。 |
| 合并权重只保留符号 | PlaidCloud 的边带有合并标志（`+`、`-` 或 `~`），而不是系数。TM1 权重 `0` 变为 `~`（该成员不汇总到其父节点）；负权重变为 `-`；正权重变为 `+`；缺失的权重（TM1 自身的默认值）视为 `+`。**小数或乘数权重——0.5、2.0——无法表示**：它会变成普通的 `+`，乘数丢失。这会被计数并指明，而不是悄悄忽略——运行的步骤警告会报告受影响的边数，并以 `parent -> child (weight)` 的形式列出，例如 `Total Revenue -> Product A (0.5)`，最多列出 10 条，超出部分以“(and N more)”表示。根边（没有父节点）命名为 `(root)`，而不是留空。存在但非数值的权重会被直接拒绝，而不是猜测。 |
| 不支持经代理的发现 | 此步骤仅支持云端直连——要读取云端无法访问的 TM1 服务器，请参见 [TM1：查询多维数据集（代理）](/zh-cn/reference/workflow-steps/ibm-planning-analytics/tm1-query-remote/)。 |

## 相关内容

- [连接到 TM1（指南）](/zh-cn/guides/connections/tm1/)——创建连接。
- [TM1 连接器](/zh-cn/reference/connectors/rest/tm1/)——连接字段参考，包括本地代理路径。
- [TM1：查询多维数据集](/zh-cn/reference/workflow-steps/ibm-planning-analytics/tm1-query/)——云端直连读取多维数据集数据。
- [TM1：查询多维数据集（代理）](/zh-cn/reference/workflow-steps/ibm-planning-analytics/tm1-query-remote/)——通过本地 PlaidLink 代理读取多维数据集数据。
- [Dimension Load](/zh-cn/reference/workflow-steps/dimensions/dimension-load/)——此步骤所基于的同一种维度加载机制。
- [IBM TM1 / Planning Analytics 步骤](/zh-cn/reference/workflow-steps/ibm-planning-analytics/)
