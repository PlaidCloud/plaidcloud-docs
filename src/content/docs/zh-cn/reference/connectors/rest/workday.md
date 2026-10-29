---
title: Workday REST 连接器
description: 在 PlaidCloud 中配置 Workday REST API 连接，将 HR、财务和计划数据集成到工作流中。
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/workday.md
---

## API 文档
[厂商 API 参考](https://community.workday.com/sites/default/files/file-hosting/restapi/)涵盖了此连接器的端点。

## 配置

创建或编辑此连接时会显示这些字段。必填还是可选取决于您启用的身份验证选项。

### 标识

| 字段 | 类型 | 说明 |
|---|---|---|
| 名称 | 文本 | 此连接的显示名称。 |
| 别名 | 文本（多行） | 有关此连接的可选别名或备注。 |
| 是否启用 | 开关 | 是否启用此连接。禁用可暂停连接而不删除。 |
| 数据库只读 | 开关 | 将连接限制为只读操作。 |
| 访问类型 | 选择 | 此连接的只读、只写或读写访问级别。 |

### 其他

| 字段 | 类型 | 说明 |
|---|---|---|
| Oauth2 客户端 ID | 文本 | — |
| Oauth2 客户端密钥 | 文本 | 密钥凭据，加密存储。 |
| Workday URL | 文本 | URL 端点。 |
| Oauth2 刷新令牌 | 文本 | — |
