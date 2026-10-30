---
title: Stripe REST 连接器
description: 在 PlaidCloud 中配置 Stripe REST API 连接，将支付处理和财务数据集成到工作流中。
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/stripe.md
---

## API 文档
[厂商 API 参考](https://docs.stripe.com/api)涵盖了此连接器的端点。

## 配置

创建或编辑此连接时会显示以下字段。是否必填取决于您启用的身份验证选项。

### 标识

| 字段 | 类型 | 说明 |
|---|---|---|
| 名称 | 文本 | 此连接的显示名称。 |
| 别名 | 文本（多行） | 可选的连接别名或备注。 |
| 是否启用 | 开关 | 是否启用该连接。禁用可暂停连接而不删除。 |

### 其他

| 字段 | 类型 | 说明 |
|---|---|---|
| 主机 | 文本 | — |
| 身份验证类型 | 选择 | — |
| 启用 SSL 验证 | 开关 | — |
| 跟随重定向 | 开关 | — |
| 重定向时沿用 HTTP 方法 | 开关 | — |
| 重定向时沿用身份验证 | 开关 | — |
| 重定向时移除 Referer | 开关 | — |
| 严格 HTTP | 开关 | — |
| 编码 URL | 开关 | URL 端点。 |
| 禁用 Cookie 存储 | 开关 | — |
| 服务器密码套件 | 开关 | — |
| 最大重定向次数 | 数字 | — |
| 测试端点 | 文本 | — |
| 测试方法 | 选择 | — |
