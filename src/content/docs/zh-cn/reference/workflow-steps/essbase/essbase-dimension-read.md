---
title: "Essbase：读取维度"
description: 将 Oracle Essbase 维度大纲以云直连方式读入 PlaidCloud 维度的主层次结构，并按名称拒绝任何共享成员、仅标签成员、动态计算成员或属性成员，以及大纲中其他无法表示的内容。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/essbase/essbase-dimension-read.md
---

## 说明

通过您的 [Oracle Essbase 连接](/zh-cn/guides/connections/essbase/)，从 Oracle **Essbase** 多维数据集中读取一个维度大纲，并将其加载到 PlaidCloud 维度的**主层次结构**中。

此步骤在步骤菜单中位于 **Oracle Essbase** 下。

该步骤通过 REST API 以**云直连**方式访问 Essbase — 此步骤没有本地代理路径，也没有远程变体。

## 配置

### Essbase 源

| 字段 | 是否必填 | 备注 |
|---|---|---|
| 连接 | 是 | 用于读取的 [Oracle Essbase 连接](/zh-cn/guides/connections/essbase/)。 |
| 应用程序 | 是 | 要读取的 Essbase 应用程序。选择器会列出连接的服务账户可见的应用程序；如果连接设置了默认应用程序，则会预先选中。 |
| 多维数据集（数据库） | 是 | 所选应用程序中要读取大纲的多维数据集。 |
| 维度 | 是 | 要读取其大纲的 Essbase 维度。 |

### 目标 PlaidCloud 维度

| 字段 | 是否必填 | 备注 |
|---|---|---|
| 目标维度 | 是 | 大纲加载到的 PlaidCloud 维度。 |

## 此步骤无法表示的内容

| 限制 | 含义 |
|---|---|
| 共享成员 | 共享成员在第二个父级下重用另一个成员的数据。PlaidCloud 维度节点只有一个父级，因此共享成员会按名称被拒绝，而不是作为重复项加载或被悄悄丢弃。请将主汇总作为独立的 PlaidCloud 维度读取 — 共享成员的第二个父级在此无法表示。 |
| 仅标签成员 | 仅标签成员仅用于导航，自身从不保存数据。它会按名称被拒绝，而不是作为下游不会预期为空的普通成员加载。 |
| 动态计算成员 | 动态计算成员的值由 Essbase 即时计算，从不存储。此步骤读取的是大纲结构而非计算数据，因此动态计算成员会按名称被拒绝，而不是当作已存储成员加载。 |
| 属性维度 | 属性维度用于对基础维度的成员分类 — 它本身不是事实的层次结构。读取属性维度会被直接拒绝；请改为读取基础维度。 |
| 无法表示的合并运算符 | PlaidCloud 的边带有合并标志（`+`、`-` 或 `~`）。Essbase 的 `+` 和 `-` 运算符可直接映射。`*`、`/` 和 `%` 无法表示为普通的汇总符号 — 使用其中任一运算符的成员会按名称被拒绝，而不是以错误的符号加载。 |
| 超出成员上限的大纲 | 大纲成员总数超过 **5,000** 的维度大纲会被拒绝，而不是部分加载，错误信息中会同时指出实际数量和上限。请读取层次结构中更浅的层级或更小的子树，使其低于上限。 |

## 相关内容

- [连接到 Oracle Essbase（指南）](/zh-cn/guides/connections/essbase/) — 创建连接。
- [Oracle Essbase 连接器](/zh-cn/reference/connectors/erp/oracle-essbase/) — 连接字段参考。
- [Essbase：查询多维数据集](/zh-cn/reference/workflow-steps/essbase/essbase-query/) — 以云直连方式对多维数据集运行实时 MDX 查询。
- [Oracle Essbase 步骤](/zh-cn/reference/workflow-steps/essbase/)
