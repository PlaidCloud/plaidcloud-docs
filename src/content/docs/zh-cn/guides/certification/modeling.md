---
title: 建模学习路径
description: 参加 PlaidCloud 建模实践者和专家实验之前应阅读的内容，以及每个实验的要求。
sidebar:
  label: 建模
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/certification/modeling.md
---

建模赛道关注的是维度和分摊：构建层次结构、按动因分摊成本，并证明结果能够核对一致。请先从[基础](/zh-cn/guides/certification/foundations/)学习路径开始。有关实验的运作方式，请参阅 [PlaidCloud 认证](/zh-cn/guides/certification/)。

## 实践者

### 阅读顺序

1. [维度入门](/zh-cn/guides/dimensions/getting-started/)
2. [管理层次结构](/zh-cn/guides/projects/managing-hierarchies/)
3. [设计维度层次结构](/zh-cn/get-started/tutorials/design-a-dimension/)
4. [分摊快速入门](/zh-cn/guides/allocations/getting-started/allocations-quick-start/)
5. [Allocation Split 步骤](/zh-cn/reference/workflow-steps/allocation/allocation-split/)
6. [构建分摊模型](/zh-cn/get-started/tutorials/build-an-allocation/)
7. [分摊结果](/zh-cn/guides/allocations/results/allocation-results/)
8. [查看工作流日志](/zh-cn/guides/workflows/viewing-workflow-log/)

### 实验要求

该实验名为 *建模：分配共享 IT 成本*。

一张表列出了每个部门及其上级。您需要构建一个维度，其主层次结构与该树完全一致。然后在实验的工作流中，按部门的人数比例将一个成本池分摊到各部门，每个部门一行结果。另有第二张驱动因素表，但它不是该成本池的动因。

实验会检查工作流是否运行、层次结构是否正确、分摊后的总额是否与源数据一致，以及每个部门获得的金额是否正确。

## 专家

专家实验限时：从开始之时起您有 4 小时。

### 阅读顺序

1. [配置分摊](/zh-cn/guides/allocations/setup/configure-an-allocation/)
2. [分摊故障排除](/zh-cn/guides/allocations/results/troubleshooting-allocations/)
3. [使用 MCP 连接的 AI 代理追踪分摊](/zh-cn/integrations/ai-coding-agents/tracing-allocations/)
4. [分摊结果](/zh-cn/guides/allocations/results/allocation-results/)
5. [尝试动因假设分析](/zh-cn/guides/allocations/results/driver-what-if/)
6. [管理层次结构](/zh-cn/guides/projects/managing-hierarchies/)

### 实验要求

该实验名为 *建模专家：修复分配模型*。

一个两阶段分摊模型不再与总账一致，并且有些部门明显有误。您需要追查原因并修复模型：每个阶段恰好分摊其成本池，部门总额正确且与总账相符，并且部门维度只包含实际存在的部门。不得使用平衡行来使任何数据对平。然后，您需要添加一个步骤，显示如果按占地面积而不是人数分摊，IT 会为每个部门带来多少成本。

实验会检查工作流是否运行、层次结构是否正确、每个阶段和部门总额是否与总账一致、每个部门的总额是否正确，以及占地面积方案是否正确。
