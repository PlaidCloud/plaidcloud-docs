---
title: 位置优化器
description: 从一组候选站点中选出 K 个站点，使到一组需求点的总距离或加权距离最小。
sidebar:
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/optimization/location-optimizer.md
---

位置优化器步骤从候选位置表中选出 **K** 个站点，使到需求点表的总距离或加权距离最小。这是一个 p-median 设施选址模型，在 PlaidCloud 的 HiGHS 求解器上作为混合整数规划求解。

位置优化器在工作流作业 Pod 中运行，使用与[求解器](/zh-cn/reference/workflow-steps/optimization/solver/)相同的作业镜像，并将结果写回项目表。

## 输入

### 候选站点

可能的站点位置表，使用所有表映射输入共用的同一套源/目标列映射、筛选器和聚合进行映射。

### 需求点

需求点表，要使这些点到最近的所选站点的距离最小，映射方式相同。

### 距离表（可选）

预先计算好的候选站点到需求点的距离表。不设置则由步骤自行计算距离。

### K

要从候选站点中选择的站点数量。

## 求解器选项

| 选项 | 描述 |
| --- | --- |
| 时间限制 | 可选的运行时间限制，单位为秒。 |
| MIP 间隙 | 可选的相对 MIP 间隙。 |
| 启用预求解 | 让求解器在求解前简化模型。默认启用。 |
| 使用自定义资源 | 为作业 Pod 设置 CPU 核心数和内存。 |

**时间限制**或 **MIP 间隙**触发的停止，返回的是该限制内找到的最佳解，而不是真正的最优解，这与[求解器](/zh-cn/reference/workflow-steps/optimization/solver/#状态行为)在非最优状态下的取舍相同。两者都不设置则求解至完全最优。

## 输出

位置优化器写入三个输出表，它们的名称必须各不相同。

### 所选站点输出表

每个选中的站点一行。

### 分配输出表

每个需求点一行，注明其被分配到的所选站点。

### 汇总输出表

一行，包含求解器状态、目标值和运行详情。

## 限制与注意事项

此步骤是 **p-median** 模型：它始终使需求点到其最近所选站点的总距离（可选加权）最小。它无法表达重力式评分、自定义评分公式，或任何以得分越高越好而非距离越低越好的目标。需要这些目标的选址问题应改用手工构建的[求解器](/zh-cn/reference/workflow-steps/optimization/solver/)模型。

## 相关内容

- [求解器](/zh-cn/reference/workflow-steps/optimization/solver/)：通用的线性和混合整数优化，适用于此步骤固定的 p-median 模型未涵盖的选址目标。
- [Alteryx 转换矩阵](/zh-cn/reference/alteryx-conversion-matrix/)：Alteryx Location Optimizer 工具仅在线性距离最小化的情形下才会转换为此步骤；重力核或自定义评分宏仍会被拒绝。
