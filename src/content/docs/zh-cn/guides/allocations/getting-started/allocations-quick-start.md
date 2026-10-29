---
title: 分摊快速入门
description: 通过涵盖源数据、分摊动因和目标映射的分步指南，在 PlaidCloud 中快速设置基本的成本分摊。
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/allocations/getting-started/allocations-quick-start.md
---

本演练带您在大约 30 分钟内，从原始成本数据开始搭建出可用的分摊模型。

## 准备工作

- 一个至少包含两个表的项目：
  - **待分摊值**：要分摊的成本（或收入、数量）。每个源单元一行，并有一列存放金额。
  - **驱动因素数据**：分摊的依据，例如人数、平方英尺面积、交易笔数、收入，也就是想要*按什么*进行分摊。
- 一个将源与目标关联起来的维度（成本中心、部门、产品，选用适合模型的分类即可）。

如果还没有准备好这些内容，[表和视图](/zh-cn/guides/data/)与[维度](/zh-cn/guides/dimensions/)指南介绍了如何加载输入数据。

## 步骤

1. **打开项目**，其中包含值表和驱动因素表。
2. **创建新工作流。** 分摊始终在工作流中运行，不能在工作流之外直接对表进行操作。
3. **添加分摊步骤。** 在工作流中，从**分摊**类别添加一个步骤。最常见的起点是 **Allocation Rules** 步骤，用于直接基于驱动因素的分摊。
4. **配置源。** 让步骤指向值表，并选择存放待分摊金额的列。
5. **配置驱动因素。** 让步骤指向驱动因素表，并选择存放驱动因素值的列。
6. **映射维度。** 确定每个表中哪一列代表维度成员。分摊步骤据此将源行与驱动因素行匹配。
7. **运行步骤。** 输出是一个新表，每个分摊金额占一行。
8. **检查结果。** 确认合计与预期一致：分摊金额之和应等于源金额之和（在舍入容差范围内）。

## 常见后续操作

- **递归分摊**：如果某个目标本身包含用于进一步分摊的驱动因素，请参阅[递归分摊](/zh-cn/guides/allocations/setup/recursive-allocations/)。
- **为分摊标记行**：要控制*哪些*行分摊到哪些目标，请参阅[基于规则的标记](/zh-cn/guides/allocations/getting-started/rule-based-tagging/)。
- **排查意外结果**：如果合计无法对平，或个别行看起来不对，请参阅[分摊故障排除](/zh-cn/guides/allocations/results/troubleshooting-allocations/)。

## 后续步骤

- [为什么分摊很有用？](/zh-cn/guides/allocations/getting-started/why-are-allocations-useful/)：何时使用分摊
- [配置分摊](/zh-cn/guides/allocations/setup/configure-an-allocation/)：更深入的配置参考
- [分摊步骤类型](/zh-cn/reference/workflow-steps/allocation/)：“分摊”类别中的所有工作流步骤
