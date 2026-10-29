---
title: Acumatica REST 连接器
description: 在 PlaidCloud 中设置 Acumatica 基于合约的 REST API 连接，以导入主数据和交易数据，并过账日记账交易、发票、账单和付款。
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/acumatica.md
---

## API 文档

Acumatica 的[基于合约的 REST API](https://help.acumatica.com/Help?ScreenId=ShowWiki&pageid=e0dea52d-0339-4f34-a6c0-9615ce6a25c2)记录了此连接器所使用的端点和查询选项。

## 身份验证的工作方式

该连接基于**会话**：PlaidCloud 在每个有界的工作单元中登录一次（`POST <instance>/entity/auth/login`，携带您的用户名、密码、公司以及可选的分支机构），并在该单元内的每次调用中复用生成的会话 Cookie，完成后退出登录。这不是持有者令牌或 OAuth 流程，会话数会计入 Acumatica 许可证的并发会话上限，试用版和较低层级的实例可能将上限限制为 2，因此请避免在同一连接上并行运行大量 Acumatica 步骤。

## 配置

| 字段 | 类型 | 说明 |
|---|---|---|
| 名称 | 文本 | 此连接的显示名称。 |
| 实例基础 URL | 文本 | 您的 Acumatica 实例 URL，例如 `https://yourcompany.acumatica.com`。 |
| 端点名称 | 文本 | 合约端点名称。除非发布了自定义端点，否则为 `Default`。 |
| 端点版本 | 文本 | 可选，例如 `25.200.001`。留空则使用该端点最新发布的版本。 |
| 公司/租户 | 文本 | 此连接登录的 Acumatica 公司 ID，必须完全一致。 |
| 分支机构 | 文本 | 可选。留空则使用登录用户的默认分支机构。 |
| 用户名 | 文本 | PlaidCloud API 用户的登录名。 |
| 密码 | 文本 | PlaidCloud API 用户的密码。加密存储。 |

## 可导入的实体

**Import Acumatica Entity** 步骤涵盖 18 个基于合约的实体：

**主数据和参考数据** — `account`、`subaccount`、`ledger`、`financial_period`、`branch`、`currency`、`currency_rate`、`customer`、`vendor`、`stock_item`、`warehouse`、`employee`、`tax_category`、`project`

**交易数据** — `sales_invoice`、`bill`、`sales_order`、`shipment`

每次拉取均支持 `Active Only` 开关、`Updated After` 截止时间以及按实体设置的服务器端筛选器。完整的字段参考请参阅 [Import Acumatica Entity](/zh-cn/reference/workflow-steps/acumatica/import-acumatica-entity/) 步骤。

## 过账单据

**Acumatica Post** 步骤通过 PlaidCloud 共享的 ERP 写入管道过账 **JournalTransaction**、**SalesInvoice**、**Bill** 和 **Payment** 单据：先以暂挂状态创建，再释放（异步操作），并在报告单据已过账之前确认释放成功。字段参考请参阅 [Acumatica: Post Documents](/zh-cn/reference/workflow-steps/acumatica/acumatica-post/) 步骤，完整的过账操作步骤请参阅[连接到 Acumatica](/zh-cn/guides/connections/acumatica/)。

## 已知限制

| 限制 | 含义 |
|---|---|
| 不涵盖依赖 GI 的读取 | 试算平衡表、总账交易明细、现有库存、预算和公司间数据位于 Acumatica 通用查询（Generic Inquiry）之后，而不在上述 18 个基于合约的实体中。请在 Acumatica 中构建 GI，并通过[通用 REST 连接](/zh-cn/reference/connectors/rest/generic-rest/)拉取。 |
| 写入时没有原生幂等键 | Acumatica 基于 PUT 的写入 API 没有幂等字段；防止重复过账的唯一保障是 PlaidCloud 自身的账本占位。 |
| 冲销需手动进行 | 没有任何单据类型具有文档记载的作废/冲销操作。已过账的单据无法从 PlaidCloud 冲销，请直接在 Acumatica 中更正。 |
| 没有付款关联字段 | Acumatica 没有公开记载的字段，可在结果不明确后将付款与 PlaidCloud 的请求关联；存疑的付款会被隔离，等待手动处理。 |
| 行项目筛选不在服务器端 | `$filter` 风格的筛选器只作用于实体和表头字段，不作用于单据的行项目维度（例如行级成本中心）。请在拉取之后于工作流中限定行范围。 |

## 相关内容

- [连接到 Acumatica（指南）](/zh-cn/guides/connections/acumatica/) — 分步说明：创建连接、测试连接、导入实体并过账批次。
- [Import Acumatica Entity](/zh-cn/reference/workflow-steps/acumatica/import-acumatica-entity/)
- [Acumatica: Post Documents](/zh-cn/reference/workflow-steps/acumatica/acumatica-post/)
- [查看 ERP 过账历史](/zh-cn/guides/connections/erp-post-history/)
