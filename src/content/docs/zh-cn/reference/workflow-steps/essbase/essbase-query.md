---
title: "Essbase：查询多维数据集"
description: 对 Oracle Essbase 多维数据集运行实时 MDX 查询，并将结果网格写入工作流表，列由网格推导而来，并对结果应用行访问权限。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/essbase/essbase-query.md
---

## 说明

**Essbase：查询多维数据集**步骤对 Oracle Essbase 多维数据集运行 MDX `SELECT`，并将返回的网格写入目标表。它是**真正的实时查询** — 步骤发送 MDX 并同步读取返回的网格，因此每次运行都反映多维数据集的当前数值。它不是提取，也不是轮询：没有需要等待的暂存作业，也没有在两次运行之间过期的快照。

可用它将多维数据集的特定切片 — 按期间划分的一组科目、方案对比，或分摊所用的一组动因 — 拉取到 PlaidCloud 表中，然后与其余数据一起转换、联接或报表。

## 先决条件

- 一个指向 Essbase 21c+ 或 Oracle Analytics Cloud (OAC) 的 [Oracle Essbase 连接](/zh-cn/reference/connectors/erp/oracle-essbase/)，其服务账户能够读取要查询的应用程序和多维数据集。

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 720 120" role="img" aria-label="从 Essbase 连接，经所选应用程序和多维数据集、MDX 查询以及返回的网格，到目标表的流程。" style="width:100%;max-width:720px;height:auto;">
<defs><marker id="eq-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
<rect x="10" y="42" width="120" height="42" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="70" y="68" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">连接</text>
<rect x="176" y="42" width="130" height="42" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="241" y="63" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">应用程序</text><text x="241" y="78" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">/ 多维数据集</text>
<rect x="352" y="42" width="120" height="42" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="412" y="68" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">MDX SELECT</text>
<rect x="518" y="42" width="80" height="42" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="558" y="68" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">网格</text>
<rect x="632" y="42" width="80" height="42" rx="8" fill="var(--sl-color-accent)" stroke="var(--sl-color-accent)" /><text x="672" y="68" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">表</text>
<path d="M130 63 L172 63" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#eq-arrow)" /><path d="M306 63 L348 63" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#eq-arrow)" /><path d="M472 63 L514 63" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#eq-arrow)" /><path d="M598 63 L628 63" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#eq-arrow)" />
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">MDX 对多维数据集实时运行；返回的网格写入目标表，列由网格本身推导。</figcaption>
</figure>

## 配置

- **连接** — Oracle Essbase 连接。选择器旁的编辑快捷方式会打开连接编辑器，用于查看或编辑。
- **应用程序** — 要查询的 Essbase 应用程序。选择器会列出连接的服务账户可见的应用程序；如果连接设置了默认应用程序，则会预先选中。
- **多维数据集（数据库）** — 所选应用程序中要查询的多维数据集。
- **MDX** — 要运行的 MDX `SELECT` 语句。可通过引导式成员选择构建，也可直接编写（见下文）。
- **目标表** — 返回的网格写入的表。

## 构建查询

可以通过两种方式生成 MDX：

- **引导式成员选择。** 浏览多维数据集的维度和成员，选取放在列和行上的内容；步骤会为您组装 MDX。成员在展开时按层级逐级加载，因此大型大纲也能保持响应。
- **原始 MDX。** 直接编写或粘贴 MDX `SELECT` — 用于引导式选择器未涵盖的内容，例如计算成员、函数或集合运算符。

两种方式生成的是步骤运行的同一个 `MDX` 值；引导式选择器只是起点，您始终可以手动编辑。

## 选项

| 字段 | 默认 | 备注 |
|---|---|---|
| 隐藏 #Missing 单元格 | 关 | 服务器端：在 `#Missing` 和其他结构上无关的单元格通过网络传输之前将其丢弃。安全 — 从不丢弃已过账的零值。 |
| 同时隐藏零值单元格（有损） | 关 | 单独的可选筛选器，在获取之后同时丢弃任何值恰好为 `0` 的单元格。**有损**：在计划多维数据集中，已过账的零是真实的事实，而不是没有数据 — 仅当您明确希望从结果中排除零值时才启用。 |
| 行数限制 | 250,000 | 限制返回的行数。留空则使用默认上限 250,000；也可显式调高或调低。超出限制的查询会被拒绝，而不是被悄悄截断 — 请缩小查询范围（添加切片器、`NON EMPTY` 或更精确的成员集），或调高行数限制，然后重试。 |

## 预览

保存之前，**预览**会对多维数据集运行当前的 MDX，并显示返回的列和前几行 — 可快速检查查询的形态是否符合预期，与步骤本身配置的行数限制无关。

## 结果与读时模式

Essbase 返回的网格会写入目标表，其**列由返回的网格推导**而来 — 即读时模式。无需预先声明列清单：

- 列名来自网格的标题行。不跨越任何内容的标题单元格（行标签上方的角落）会变为 `column_1`、`column_2`，依此类推；重复的名称会通过数字后缀变为唯一。
- 数据单元格全为数字的列会被定为数值类型；其他列定为文本类型。Essbase 的空单元格写入后为空值。
- 网格中的成员标签和别名标签来自连接上配置的别名表，每次运行都一致应用 — 而不是 Essbase 自身的每会话默认值，后者可能因查询运行时登录的用户不同而显示不同的标签文本。

由于表的形态跟随查询，更改 MDX 放在列上的内容会在下次运行时改变表的列 — 请在引用特定列名的下游步骤中留意这一点。

## 行访问

[行级安全](/zh-cn/administration/access/managing-security-groups-and-assignments/#管理行访问)对写入的表的应用方式与对任何其他 PlaidCloud 表完全相同。治理作用于步骤写入的结果，因此带有行限制的读者只能看到其安全组允许的行 — 查询使用连接的服务账户运行，但它生成的表与您的其余数据一样受到治理。

## 示例

此 MDX 将两个度量值放在列上，将两个产品放在行上：

```mdx
SELECT
  {Sales, COGS} ON COLUMNS,
  {[100-10], [200-10]} ON ROWS
FROM Sample.Basic
```

对返回这四个数字的多维数据集运行后，会写入如下的表：

| column_1 | Sales | COGS |
|---|---|---|
| 100-10 | 678.0 | 271.0 |
| 200-10 | 551.0 | 235.0 |

行标签列在网格中没有标题，因此变为 `column_1`（文本）；`Sales` 和 `COGS` 全为数字，因此写入为数值列。

## 相关内容

- [连接到 Oracle Essbase（指南）](/zh-cn/guides/connections/essbase/) — 创建连接并构建查询。
- [Oracle Essbase 连接器](/zh-cn/reference/connectors/erp/oracle-essbase/) — 连接字段参考。
- [Essbase：读取维度](/zh-cn/reference/workflow-steps/essbase/essbase-dimension-read/) — 以云直连方式将 Essbase 维度大纲加载到 PlaidCloud 维度。
- [Oracle Essbase 步骤](/zh-cn/reference/workflow-steps/essbase/)
- [REST 请求](/zh-cn/reference/workflow-steps/general/rest-request/) — 用于其他实时 HTTP 请求的通用步骤。
