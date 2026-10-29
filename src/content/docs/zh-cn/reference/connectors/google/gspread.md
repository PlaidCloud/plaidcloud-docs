---
title: Google 表格
description: 在 PlaidCloud 中设置 Google 表格连接，以便在工作流中导入、导出和同步电子表格数据。
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/google/gspread.md
---

## 连接文档
Google 表格更偏向面向个人用户。如需技术文档，请参阅[开发者文档](https://developers.google.com/workspace/sheets)。

## 配置

创建或编辑此连接时会显示以下字段。是否必填取决于您启用的身份验证选项。

### 标识

| 字段 | 类型 | 说明 |
|---|---|---|
| 名称 | 文本 | 此连接的显示名称。 |
| 别名 | 文本（多行） | 可选的连接别名或备注。 |
| 是否启用 | 开关 | 是否启用该连接。禁用可暂停连接而不删除。 |
| 数据库只读 | 开关 | 将连接限制为只读操作。 |
| 访问类型 | 选择 | 此连接的只读、只写或读写访问级别。 |
