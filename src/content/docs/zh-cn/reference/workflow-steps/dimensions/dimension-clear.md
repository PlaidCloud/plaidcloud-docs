---
title: Dimension Clear 步骤
description: 在工作流步骤中清除 PlaidCloud 维度的所有成员，同时保留维度的结构和配置。
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/dimensions/dimension-clear.md
---

## 说明
清除维度的内容，包括结构、值、别名、属性和备用层次结构


![Dimension Clear 步骤](/images/dimension_clear.png)



## 维度选择
### 动态指定维度
如果**维度**或**路径**是动态创建的，则可以使用相同的变量来清除它们。在清除过程中使用变量很有用，因为这样无需定期手动更新 Dimension Clear 步骤。



下面的示例使用 `current_month` 变量动态清除 Materials 维度：

```text
/Dimensions/{current_month}/Products/Materials
```

### 使用特定维度

使用下拉菜单选择要清除的特定维度。
