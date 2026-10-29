---
title: SAP Profitability and Cost Management（PCM）连接器
description: 在 PlaidCloud 中配置 SAP Profitability and Cost Management 连接，将成本分摊数据集成到工作流中。
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/erp/sap-pcm.md
---

## 上游文档
[SAP PCM 旧版文档](https://help.sap.com/docs/SAP_PROFITABILITY_AND_COST_MANAGEMENT)。

## 配置

创建或编辑此连接时会显示这些字段。必填或可选取决于所启用的身份验证选项。

### 标识

| 字段 | 类型 | 说明 |
|---|---|---|
| 名称 | 文本 | 此连接的显示名称。 |
| 别名 | 文本（多行） | 可选的别名或连接备注。 |
| 是否启用 | 开关 | 是否启用该连接。禁用可暂停使用而无需删除。 |
| 数据库只读 | 开关 | 将连接限制为只读操作。 |
| 访问类型 | 选择 | 此连接的访问级别：只读、只写或读写。 |

### 身份验证

| 字段 | 类型 | 说明 |
|---|---|---|
| 数据库用户 | 文本 | 用于数据库身份验证的用户名。 |
| 使用 SSO | 开关 | 通过单点登录而非用户名/密码进行身份验证。 |
| 数据库密码 | 密码 | 用于数据库身份验证的密码。 |
