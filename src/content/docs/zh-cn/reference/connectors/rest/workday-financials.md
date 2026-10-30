---
title: Workday Financials 连接器
description: 在 PlaidCloud 中使用集成系统用户设置 Workday Financials 连接，通过 RaaS 报表导入数据，并通过 SOAP 过账日记账分录。
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/workday-financials.md
---

## API 文档

Workday 的 [SOAP Web 服务](https://community.workday.com/sites/default/files/file-hosting/productionapi/)和[报表即服务 (RaaS)](https://doc.workday.com/)文档介绍了此连接器使用的接口。

## 身份验证的工作方式

连接使用**集成系统用户 (ISU)** 进行身份验证。这是专为系统间集成而设计的 Workday 用户类型，由集成系统安全组保护，仅授予此连接器所需的访问权限（读取需要报表访问权限，过账需要“提交会计日记账”业务流程）。请求携带 ISU 的用户名和密码，不涉及交互式登录。

## 配置

| 字段 | 类型 | 说明 |
|---|---|---|
| 名称 | 文本 | 此连接的显示名称。 |
| 租户主机 | 文本 | 您的 Workday 主机，例如 `wd5-impl.workday.com`。 |
| 租户名称 | 文本 | 您的 Workday 租户名称。 |
| ISU 用户名 | 文本 | 集成系统用户的用户名。 |
| ISU 密码 | 文本 | 集成系统用户的密码。加密存储。 |

## 导入数据

Workday Financials 没有固定的预置实体集。**Import Workday Entity** 步骤会调用您在 Workday 中构建并发布、且启用了 Web 服务访问的**报表即服务 (RaaS) 报表**，其 URL 由您提供。该步骤支持对 `company`、`ledger`、`period`、`accounting_date`（范围）、`ledger_account`（范围）和 `cost_center` 进行筛选，每个筛选条件都会作为报表参数传递，因此只有报表定义了匹配的提示时，筛选才会生效。完整的字段参考请参见 [Import Workday Entity](/zh-cn/reference/workflow-steps/workday-financials/import-workday-entity/)。

## 过账日记账分录

**Workday Financials: Post Journal Entry** 步骤通过 PlaidCloud 共享的 ERP 写入管道过账会计日记账，使用 Workday 的 `Submit_Accounting_Journal` SOAP 操作，并轮询该分录的业务流程状态直至终态，然后才报告为已过账。更正会过账一笔新的、借贷方向互换的冲销分录，而不是编辑原分录。字段参考请参见 [Workday Financials: Post Journal Entry](/zh-cn/reference/workflow-steps/workday-financials/workday-post/)，完整的过账操作流程请参见[连接到 Workday Financials](/zh-cn/guides/connections/workday-financials/)。

## 已知限制

| 限制 | 含义 |
|---|---|
| 导入的结构取决于您的 RaaS 报表 | PlaidCloud 没有适用于 Workday Financials 的预置实体，报表的字段、提示和访问控制都位于 Workday 中。在 Workday 中更改报表，可能会改变导入的结构，而 PlaidCloud 一侧无需任何更改。 |
| 业务流程审批会增加延迟 | 如果日记账在“提交会计日记账”业务流程中经过审批步骤，则在 Workday 中获得批准之前会一直保持 `pending` 状态，终态轮询会等待这一过程。 |

## 相关内容

- [连接到 Workday Financials（指南）](/zh-cn/guides/connections/workday-financials/)：分步说明如何创建连接、测试连接、导入报表和过账日记账。
- [Import Workday Entity](/zh-cn/reference/workflow-steps/workday-financials/import-workday-entity/)
- [Workday Financials: Post Journal Entry](/zh-cn/reference/workflow-steps/workday-financials/workday-post/)
- [查看 ERP 过账历史](/zh-cn/guides/connections/erp-post-history/)
- [Workday REST 连接器](/zh-cn/reference/connectors/rest/workday/)：独立的通用 Workday 连接器，用于 HR/薪资 REST 数据。
