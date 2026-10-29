---
title: 排查分摊问题
description: 排查 PlaidCloud 分摊问题，包括常见错误、配置问题以及调试结果的技巧。
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/allocations/results/troubleshooting-allocations.md
---

## 分摊步骤无法保存的原因

保存分摊步骤时，PlaidCloud 会检查其列映射。无法运行的映射会在此时被拒绝，并显示**无法保存**通知，列出需要修复的内容，表单会切换到包含问题的选项卡。以前，这样的步骤可以毫无提示地保存，然后在运行过程中途（通常是几分钟后）使工作流停止，而且消息中指出的是一个数量，而不是某个字段。

在您同时选择**待分摊值表**和**驱动因素数据表**之前，不会进行任何检查。列映射是根据这两个表构建的，因此在两者都设置之前，步骤只会要求提供这些表本身。

### 分摊源映射

**“No columns specified for allocation.”**
将至少一列的**角色**设置为**待分摊值**。该列保存要在各目标之间分摊的值。

**“Only numeric columns can be allocated, but ... is not numeric.”**
标记为**待分摊值**的列的**类型**不是数值类型。请将类型更改为数值类型：Numeric、Currency、Integer、大整数、小整数、微整数、Float、Double、Decimal、Serial 或大序列。

**“Rename the `alloc_status` target column.”**
分摊会在结果表中写入自己的 `alloc_status` 列，因此同名的目标列会与之冲突。请重命名您的列。

### 驱动因素数据映射

**“No driver split value column found.”**
将其中一个驱动因素列的**角色**设置为**拆分值**。该列保存分摊所依据的权重或百分比。

**“The driver value column ... must be numeric.”**
将**拆分值**列的**类型**更改为数值类型。

**“No driver relation columns specified.”**
将至少一个驱动因素列的**角色**设置为**源关系（分母）**。这用于将驱动因素行与源行关联起来。

**“No allocation target columns are indicated.”**
将至少一个驱动因素列的**角色**设置为**分摊目标（分子）**。这些列将成为分摊的目标，并出现在结果表中。

**“Driver relation columns do not exist in the source data.”**
标记为**源关系（分母）**的列在**分摊源映射**中没有同名的匹配列。请将其重命名以匹配，或将该列添加到源映射中。

**“Allocation value column ... is also used as a numerator or denominator column.”**
同一个列名既是源映射中的**待分摊值**，又是驱动因素映射中的**源关系（分母）**或**分摊目标（分子）**。请重命名其中一个，使被分摊的值有别于描述其去向的列。

### 仅限按维度拆分

**“Please select a hierarchy to use for the allocation dimension.”**
在**数据表设置**选项卡上选择一个**分配维度层次结构**。请参阅[配置分摊](/zh-cn/guides/allocations/setup/configure-an-allocation/)。

## 滞留成本


滞留成本是……



## 成本过度分摊


成本过度分摊是指最终得到的输出成本多于……



## 成本分摊不正确


成本分摊不正确发生在……
