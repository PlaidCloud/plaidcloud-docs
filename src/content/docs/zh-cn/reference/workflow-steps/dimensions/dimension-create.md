---
title: Dimension Create 步骤
description: 在 PlaidCloud 工作流步骤中创建新的层次结构维度，以组织和构建数据分类体系。
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/dimensions/dimension-create.md
---

## 说明
创建可供使用和加载的维度。


![Dimension Create](/images/dimension_create.png)

## 要创建的维度
### 名称
可以为要创建的维度使用固定名称，也可以加入变量实现动态命名。


当维度需要定期更新并希望保留历史视图时，变量非常有用。

以下示例使用 `current_month` 变量动态命名维度：

```text
dimension_name_{current_month}
```
### 路径
通过路径可以创建用于存放维度的文件夹结构。此处同样可以使用变量，使文件夹结构动态变化。
以下示例使用 `current_month` 变量动态命名文件夹：

```text
/Dimensions/{current_month}/Product/
```

### 备注
备注字段用于存放评论或说明。
