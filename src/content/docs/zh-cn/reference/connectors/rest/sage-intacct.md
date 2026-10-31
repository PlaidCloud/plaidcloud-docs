---
title: Sage Intacct REST 连接器
description: 在 PlaidCloud 中设置 Sage Intacct REST API 连接，将财务和会计数据集成到工作流中。
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/sage-intacct.md
---

## API 文档

Sage Intacct REST API 文档可在 [Sage 开发者网站](https://developer.sage.com/intacct/docs/1/sage-intacct-rest-api/get-started/quick-start)上查阅。


## 安全要求

PlaidCloud 在 REST 连接系列中提供专用的 **Intacct** 连接（列为 **REST - Intacct**）。它使用针对 Intacct REST API 的 OAuth2 客户端凭据进行身份验证：Sage Intacct **Web Services** 的 Sender ID/Sender 密码对分别作为连接的**客户端 ID** 和**客户端密钥**输入，另外还需要 Web 服务用户名和公司 ID。发送方凭据必须由 Sage 支持团队为您的公司启用；Web Services 用户必须对连接器将读取的每个 Intacct 对象具有权限。

请将客户端 ID 和客户端密钥视为机密：仅通过 PlaidCloud 的**凭据**区域存储它们，并在连接中引用。


## 获取凭据

1. 打开 Sage Intacct 的 **Company Setup** 区域
2. 为 Sage 提供的 Sender ID 启用 Web Services
3. 为 PlaidCloud 创建或选择一个 Web Services 用户
4. 授予该用户对您要查询的每个对象的权限
5. 记录公司 ID、Web 服务用户名、Sender ID 和 Sender 密码


## 创建 Sage Intacct 连接器

1. 转到 **Tools > Connections** 并点击 `Add Connection`
2. 在 **REST** 下选择 **Intacct**（列为 **REST - Intacct**）
3. 输入：
    * **连接名称** — 工作流步骤中显示的易记名称
    * **客户端 ID** — 您的 Intacct Sender ID
    * **客户端密钥** — 您的 Intacct Sender 密码
    * **Web 服务用户名** — Web Services 用户的登录名
    * **公司 ID** — 您要连接的 Intacct 公司
4. 点击 `Test` 以验证凭据
5. 点击 `Save`


## 在工作流步骤中使用

同一个连接既可用于从 Intacct 读取，也可用于向其过账。可在以下步骤中选择它：

* [Import Sage AP](../../../workflow-steps/sage-intacct/import-sage-ap/) 步骤 — 应付账单表头
* [Import Sage AP Lines](../../../workflow-steps/sage-intacct/import-sage-ap-lines/) 步骤 — 应付账单行明细
* [Import Sage Intacct Query](../../../workflow-steps/sage-intacct/import-intacct-query/) 步骤 — 针对任意 Intacct 对象的通用查询
* [Import Intacct Entity](../../../workflow-steps/sage-intacct/import-intacct-entity/) 步骤 — 总账明细、余额、分录和维度主数据，支持自动分页
* [Intacct：过账日记账分录](../../../workflow-steps/sage-intacct/export-to-sage/) — 过账日记账分录
