---
title: 递归与交互分摊
description: 通过将分摊步骤链接成明确的分阶段处理，在 PlaidCloud 中为多轮和交互式成本分配建模。
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/allocations/setup/recursive-allocations.md
---

某些成本模型需要将一次分摊的目标变成下一次分摊的*源*，例如相互消耗的共享服务（IT 为 HR 提供服务，HR 也为 IT 提供服务）。PlaidCloud 通过**将分摊步骤链接成明确的分阶段处理**来建模，而不是通过单一的自动求解器。

## 何时需要多轮处理

- **交互服务**：两个相互消耗的成本池。
- **分层分摊**：部门成本沿层次结构逐级传递，较低层级必须先承接较高层级的成本，然后再重新分摊。
- **迭代平衡**：模型经过几轮处理后趋于稳定结果（成本池 A 向 B 分摊一部分，B 又向 A 分摊回来，依此类推）。

## 如何建模

PlaidCloud **没有内置的“递归模式”，也没有自动收敛求解器**。您需要自己构建递归：为每一轮添加一个单独的[分摊拆分步骤](/zh-cn/reference/workflow-steps/allocation/allocation-split/)，并按顺序将它们连接起来：

1. 将第一轮作为普通的分摊拆分运行。
2. 对于下一轮，构建一个包含上一轮输出的源（通常是将上一轮的结果合并或联接回成本池），然后再次分摊。
3. 根据模型需要重复任意轮数。

由于每一轮都是明确的步骤，因此**由您决定运行多少轮**。引擎不会把交互关系作为单一联立方程求解，也没有能自动停止循环的容差设置。请不断增加轮数，直到尚待重新分摊的残余额小到满足您的目的。

## 提示

- 先从**单轮**分摊开始，确认简单模型的行为符合预期，再增加轮数。
- 每一轮之后，检查剩余的未分摊残余额。如果它没有逐轮减小，请重新检查驱动因素关系；真正的循环依赖无论增加多少轮都不会收敛。
- 每一轮都会重新处理其源，因此在大型数据集上递归的开销很大。请先在一个切片上测试，再对完整的源运行。

## 相关内容

- [配置分摊](/zh-cn/guides/allocations/setup/configure-an-allocation/)：基本配置
- [Allocation Split 步骤](/zh-cn/reference/workflow-steps/allocation/allocation-split/)：每一轮要链接的工作流步骤
- [排查分摊问题](/zh-cn/guides/allocations/results/troubleshooting-allocations/)：残余额不合理时
