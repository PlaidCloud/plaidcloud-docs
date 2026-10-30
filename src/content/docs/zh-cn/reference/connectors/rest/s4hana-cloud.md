---
title: SAP S/4HANA Cloud REST 连接器
description: 在 PlaidCloud 中设置 SAP S/4HANA Cloud Public Edition 连接，通过 OData 导入试算平衡表和日记账分录行项目数据，并通过 SOAP 过账日记账分录。
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/s4hana-cloud.md
---

## API 文档

SAP API Business Hub 上 SAP S/4HANA Cloud 的[试算平衡表 API（`API_OPLACCTGDOCITEMCUBE_SRV`）](https://api.sap.com/)和[日记账分录行项目基础 API（`API_JOURNALENTRYITEMBASIC_SRV`）](https://api.sap.com/)记录了此连接器所使用的 OData 端点，此外还有通过通信安排（Communication Arrangement）公开的 SOAP 日记账分录批量创建服务。

## 身份验证的工作方式

该连接使用 **OAuth2 客户端凭据**以应用程序身份进行身份验证：将通信安排的客户端 ID 和密钥，向租户的 OAuth2 令牌端点换取访问令牌。不涉及交互式登录。

## 配置

| 字段 | 类型 | 说明 |
|---|---|---|
| 名称 | 文本 | 此连接的显示名称。 |
| 主机 | 文本 | 您的 S/4HANA Cloud 租户主机，例如 `https://yourorg.s4hana.ondemand.com`。 |
| 令牌 URL | 文本 | 通信安排的 OAuth2 令牌端点。 |
| 客户端 ID | 文本 | 通信安排的 OAuth2 客户端 ID。 |
| 客户端密钥 | 文本 | 通信安排的 OAuth2 客户端密钥。加密存储。 |

## 可导入的实体

**Import S/4HANA Entity** 步骤涵盖两个实体：`trial_balance`（按期间末汇总的总账科目余额，通过 `API_OPLACCTGDOCITEMCUBE_SRV`）和 `journal_entry_items`（已过账的日记账分录行项目，通过 `API_JOURNALENTRYITEMBASIC_SRV`）。两者都支持对 `CompanyCode`、`GLAccount`、`CostCenter`、`ProfitCenter`、`FiscalYear`、`FiscalPeriod` 和 `Ledger` 的服务器端筛选器，其中 `PostingDate`、`FiscalYear` 和 `FiscalPeriod` 接受 `ge`/`le` 范围边界。完整的字段参考请参阅 [Import S/4HANA Entity](/zh-cn/reference/workflow-steps/s4hana-cloud/import-s4hana-entity/) 步骤。

## 过账日记账分录

**S/4HANA: Post Journal Entry** 步骤通过 PlaidCloud 共享的 ERP 写入管道过账总账日记账分录：通过 S/4HANA Cloud 的 `JournalEntryBulkCreateRequest_In` SOAP 服务提交，轮询 `JournalEntryBulkCreateConfirmation_Out` 确认，并在报告分录已过账之前进行确认。更正时会过账一笔借贷互换的新冲销分录，而不是修改原分录。字段参考请参阅 [S/4HANA: Post Journal Entry](/zh-cn/reference/workflow-steps/s4hana-cloud/s4hana-post/) 步骤，完整的过账操作步骤请参阅[连接到 SAP S/4HANA Cloud](/zh-cn/guides/connections/s4hana-cloud/)。

## 已知限制

| 限制 | 含义 |
|---|---|
| 确认延迟 | SOAP 批量创建服务以异步方式处理请求，在数据量相同的情况下明显慢于同步的 OData 写入。 |
| 可筛选字段取决于您的通信场景 | 您的通信场景（Communication Scenario）未公开的成本对象或维度无法在服务器端筛选；请在拉取之后于工作流中限定其范围。 |

## 相关内容

- [连接到 SAP S/4HANA Cloud（指南）](/zh-cn/guides/connections/s4hana-cloud/) — 分步说明：创建连接、测试连接、导入实体并过账日记账。
- [Import S/4HANA Entity](/zh-cn/reference/workflow-steps/s4hana-cloud/import-s4hana-entity/)
- [S/4HANA: Post Journal Entry](/zh-cn/reference/workflow-steps/s4hana-cloud/s4hana-post/)
- [查看 ERP 过账历史](/zh-cn/guides/connections/erp-post-history/)
- [SAP ECC / S/4HANA 连接器](/zh-cn/reference/connectors/erp/sap-s4/) — 适用于本地部署或私有云 S/4HANA 的、基于 RFC/代理的独立连接器。
