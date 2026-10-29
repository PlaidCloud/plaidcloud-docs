---
title: 基于规则的标记
description: 在 PlaidCloud 分摊中配置基于规则的标记，使用既定条件自动对数据记录进行分类和标注。
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/allocations/getting-started/rule-based-tagging.md
---

基于规则的标记可以为源行标注元数据，分摊引擎据此决定这些行的*去向*。当分摊行为需要因行而异时，可以使用它，例如一个成本中心的成本按人数分摊，而另一个成本中心的成本按收入分摊。

## 适用场景

- 单一的固定分摊规则无法体现成本应如何实际分摊（不同成本类型适用不同规则）。
- 希望将某些源行定向到特定目标，同时让其他行按常规方式分摊。
- 正在为多池分摊建模，且每个池使用不同的分摊动因。

## 标记的工作方式

1. **标记源数据。** 在值表中添加一个或多个标记列，对每一行进行分类。
2. **在分摊规则中引用标记。** 配置分摊步骤时，规则的形式为“如果源标记 X = 值 Y，则使用驱动因素 D 和目标维度 T 进行分摊”。
3. **引擎路由各行。** 每个源行按顺序与规则匹配；第一条匹配的规则决定分摊行为。

## 适合标记的源数据模式

- 名为 `cost_category` 的列，其值如 `payroll`、`facilities`、`it`、`marketing`
- 名为 `pool` 的列，用于指明该行所属的分摊池
- 类似 `is_overhead` 的布尔列，用于触发不同的处理方式

## 示例

包含 `cost_center` 和 `cost_category` 的成本表：

| cost_center | cost_category | amount |
|---|---|---|
| 1010 | payroll | 50,000 |
| 1010 | it | 8,000 |
| 1020 | payroll | 35,000 |

可以配置两条分摊规则：

- **工资行**按人数驱动因素分摊
- **IT 行**按用户数驱动因素分摊

两条规则针对同一个源表运行；由标记决定每一行适用哪一条。

## 相关内容

- [分摊快速入门](/zh-cn/guides/allocations/getting-started/allocations-quick-start/)：添加标记之前的基本流程
- [配置分摊](/zh-cn/guides/allocations/setup/configure-an-allocation/)：完整的步骤参考
- [分摊规则步骤](/zh-cn/reference/workflow-steps/allocation/allocation-rules/)：使用已标记数据的工作流步骤
