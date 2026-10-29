---
title: Ramp REST 连接器
description: 在 PlaidCloud 中设置 Ramp REST API 连接，将公司信用卡支出和费用数据集成到工作流中。
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/ramp.md
---

## API 文档
[厂商 API 参考](https://docs.ramp.com/developer-api/v1)涵盖了此连接器的端点。

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

### 其他

| 字段 | 类型 | 说明 |
|---|---|---|
| OAuth2 客户端 ID | 文本 | — |
| OAuth2 客户端密钥 | 文本 | 机密凭据，加密存储。 |
| Ramp 范围 | 文本 | — |
