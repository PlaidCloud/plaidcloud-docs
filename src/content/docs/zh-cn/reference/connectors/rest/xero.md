---
title: Xero REST 连接器
description: 通过一键 OAuth 授权在 PlaidCloud 中设置 Xero 连接，导入 Accounting API 实体，并过账手工日记账、发票、账单、付款和贷项通知单。
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/xero.md
---

## API 文档

Xero 的 [Accounting API 参考](https://developer.xero.com/documentation/api/accounting/overview)记录了此连接器使用的实体、`where=` 筛选器和创建载荷。

## 身份验证的工作方式

该连接使用 Xero 的 **OAuth 2.0** 授权进行身份验证。PlaidCloud 自行注册 OAuth 应用，因此无需获取或输入客户端 ID 或客户端密钥——只需单击 **连接到 Xero**，登录 Xero 并批准授权即可。PlaidCloud 会将获得的令牌存储在连接上并自动为您刷新，同时持久保存每个轮换后的刷新令牌，使长期闲置的连接仍能正常工作。

一次授权涵盖您批准的所有 Xero 组织。连接只针对其中一个组织：**组织** 选择器列出授权返回的组织，每个请求都带有该组织的租户 ID。若要读取或过账到第二个组织，请创建第二个 Xero 连接并在其上选择该组织。

Xero 的演示公司是组织的属性，而不是连接设置——演示组织与其他组织一样出现在 **组织** 列表中，因此沙盒连接就是指向它的连接。

## 配置

| 字段 | 类型 | 说明 |
|---|---|---|
| 名称 | 文本 | 此连接的显示名称。 |
| 连接到 Xero | 按钮 | 启动 Xero 登录和授权同意流程。 |
| 连接状态 | 状态 | 在授权完成前显示 `Not connected`，之后报告其涵盖的组织数量。 |
| 组织 | 选择 | 此连接读取和过账所针对的 Xero 组织。由授权结果填充。 |

## 速率限制

Xero 将每个组织限制为每分钟 60 次调用、每天 5,000 次调用，且最多 5 个并发调用。PlaidCloud 按连接管控每分钟和并发限制，因此一个组织的限流不会阻塞其他连接的调用，并且在响应被限流时遵循 Xero 的 `Retry-After`。每日上限需要您自行管理——请计划大范围的拉取，而不是同时运行多个。

## 可导入的实体

**Xero：导入实体**步骤涵盖十一种 Accounting API 实体：`accounts`、`contacts`、`invoices`、`credit_notes`、`payments`、`manual_journals`、`bank_transactions`、`items`、`tracking_categories`、`tax_rates` 和 `currencies`。每次拉取都可选择状态范围、日期范围和修改时间起点。完整字段参考请参阅 [Xero：导入实体](/zh-cn/reference/workflow-steps/xero/import-xero-entity/)。

## 过账单据

**Xero：过账单据**步骤通过 PlaidCloud 共享的 ERP 写入管道，根据表头表和明细行表过账手工日记账、发票、账单、付款和贷项通知单。字段参考请参阅 [Xero：过账单据](/zh-cn/reference/workflow-steps/xero/xero-post/)，完整的过账演练请参阅[连接到 Xero](/zh-cn/guides/connections/xero/)。

## 已知限制

| 限制 | 含义 |
|---|---|
| 结果不明确后无法查找手工日记账和付款 | 发票、账单和贷项通知单带有 PlaidCloud 标记且可回查的单据编号。手工日记账的摘要和付款的参考号无法查询，因此这两者中状态存疑的写入会被隔离，由您在 Xero 中处理，而不是靠猜测。 |
| 冲销仅涵盖手工日记账和发票 | 手工日记账以借贷互换的日记账冲销；发票以镜像的贷项通知单冲销。账单、付款和贷项通知单没有记录在案的撤销载荷，因此 PlaidCloud 会拒绝冲销，而不是自行编造。 |
| 筛选器是固定字段，而非查询语言 | Xero 的查询 API 对每种实体只提供状态范围和日期范围，没有开放的筛选语言——因此导入步骤提供这些字段，而不是字段/运算符/值表。 |
| 每个连接一个组织 | 每个请求都带有一个租户 ID。第二个组织需要第二个连接。 |

## 相关内容

- [连接到 Xero（指南）](/zh-cn/guides/connections/xero/)——分步说明：创建连接、测试连接、导入实体并过账单据。
- [Xero：导入实体](/zh-cn/reference/workflow-steps/xero/import-xero-entity/)
- [Xero：过账单据](/zh-cn/reference/workflow-steps/xero/xero-post/)
- [查看 ERP 过账历史](/zh-cn/guides/connections/erp-post-history/)
