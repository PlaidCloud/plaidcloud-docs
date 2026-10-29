---
title: Dimension Delete 步骤
description: 在工作流步骤中从 PlaidCloud 删除维度，以移除不再需要的层次数据结构。
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/dimensions/dimension-delete.md
---

## 说明
删除维度及其所有相关的结构、值、属性、别名和备用层次结构


![Dimension Clear 步骤](/images/dimension_clear.png)



## 维度选择
### 动态指定维度
如果**维度**或**路径**是动态创建的，则可以使用相同的变量来删除它们。在删除过程中使用变量很有用，因为这样无需定期手动更新 Dimension Delete 步骤。



下面的示例使用 `current_month` 变量动态删除 Materials 维度：

```text
/Dimensions/{current_month}/Products/Materials
```

### 使用特定维度

使用下拉菜单选择要删除的特定维度。
