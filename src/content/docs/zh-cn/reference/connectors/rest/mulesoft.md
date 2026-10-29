---
title: MuleSoft REST 连接器
description: 将 PlaidCloud 连接到 MuleSoft Anypoint 网关并附加 API 定义，使工作流步骤能够列出其端点。
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/mulesoft.md
---

MuleSoft Anypoint 是一个 API 网关：它位于贵组织发布的各项服务之前，地址因部署而异。因此，与针对单一服务构建的连接器不同，MuleSoft 连接并不知道自己的端点，需要您告知 API 及其定义所在的位置。

## API 文档

此连接的 API 文档就是记载网关所代理服务的文档。

## 配置

MuleSoft 使用与[通用 REST 连接](/zh-cn/reference/connectors/rest/generic-rest/)相同的表单：相同的四个选项卡、相同的字段，行为也完全一致。其中有两项最为重要：

- **主机或 IP 地址** — Anypoint 网关的地址。没有默认值，因为 MuleSoft 地址因部署而异。
- **身份验证类型** — 网关所要求的 `None`、`Basic`、`API Key`、`Bearer Token` 或 `OAuth 2.0` 之一。系统不会替您做任何假设。

## 在工作流中列出端点

由于网关没有内置的端点列表，请在**API 定义**下将 API 的 OpenAPI 3.x 或 Swagger 2.0 定义附加到连接上，可以是其发布地址，也可以是存储在 Document 中的 `.json` 或 `.yaml` 文件。字段请参阅 [API 定义](/zh-cn/reference/connectors/rest/generic-rest/#api-定义)。

之后，使用此连接的 [REST 请求步骤](/zh-cn/guides/workflows/rest-request-step/)可将**端点来源**设置为**来自连接的 API 定义**并选择**加载目录**，从 API 的端点中选取，而无需手动输入每个路径。

## 相关内容

- [通用 REST 连接](/zh-cn/reference/connectors/rest/generic-rest/) — 此表单的完整字段参考。
- [创建和管理连接](/zh-cn/guides/connections/create-connection/)
- [REST 请求工作流步骤](/zh-cn/guides/workflows/rest-request-step/)
