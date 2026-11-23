---
title: 分析学习路径
description: 参加 PlaidCloud 分析实践者和专家实验之前应阅读的内容，以及每个实验的要求。
sidebar:
  label: 分析
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/certification/analytics.md
---

分析赛道关注的是无论如何拆分都只有一个正确答案的指标，以及各表之间共享的含义。请先从[基础](/zh-cn/guides/certification/foundations/)学习路径开始。有关实验的运作方式，请参阅 [PlaidCloud 认证](/zh-cn/guides/certification/)。

## 实践者

### 阅读顺序

1. [运行工作流](/zh-cn/guides/workflows/run-a-workflow/)
2. [查看工作流日志](/zh-cn/guides/workflows/viewing-workflow-log/)
3. [指标定义](/zh-cn/integrations/ai-coding-agents/metric-definitions/)，包括如何从其他指标派生指标
4. [基于已发布的表构建仪表板](/zh-cn/get-started/tutorials/build-a-dashboard/)，用于可选的仪表板

### 实验要求

该实验名为 *分析：为三个问题定义指标*。

您需要运行一个准备销售表的工作流，然后在该表上定义指标，每个指标的粒度都包含区域和渠道：按区域的收入、按渠道的平均订单价值（由订单数派生），以及按区域的成本占收入的比例（由成本指标派生）。每个指标都基于准备好的表而不是原始表构建。为这三个答案创建仪表板是不错的后续步骤，但不计入评分。

实验会检查工作流是否运行，以及这三个指标是否都给出正确答案。

## 专家

专家实验限时：从开始之时起您有 4 小时。

### 阅读顺序

1. [指标定义](/zh-cn/integrations/ai-coding-agents/metric-definitions/)
2. [数据模型和项目元素](/zh-cn/guides/projects/data-model/)
3. [分析路径](/zh-cn/integrations/ai-coding-agents/analysis-paths/)

### 实验要求

该实验名为 *分析专家：保持一致的指标*。

两个指标会因拆分方式不同而给出不同的答案，并且收入合计超过了订单加总的结果。您需要修复它们，使每个指标按区域和按产品都返回唯一正确的答案，并保留其名称。然后，将含义相同的列变为一个共享元素：一个用于区域，覆盖以不同列名保存区域的各个表；另一个用于产品。

实验会检查工作流是否运行，按区域和按产品的收入以及按产品的数量是否正确，以及这些元素是否覆盖了正确的列。
