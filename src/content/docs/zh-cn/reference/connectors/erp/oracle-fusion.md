---
title: Oracle Fusion 连接器
description: 在 PlaidCloud 中使用 OAuth2 凭据设置 Oracle Fusion Cloud 连接，通过 OData/BIP 导入总账余额和日记账批次，并通过 FBDI 过账日记账。
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/erp/oracle-fusion.md
---

## API 文档

Oracle Fusion Cloud 的 [REST API (OData)](https://docs.oracle.com/en/cloud/saas/financials/) 以及 [BI Publisher (BIP) 和基于文件的数据导入 (FBDI)](https://docs.oracle.com/en/cloud/saas/applications-common/) 参考文档记录了此连接器所使用的端点以及批量提取/加载路径。

## 身份验证的工作方式

连接针对专用的 API 用户，使用 OAuth2 客户端凭据（或 Fusion Cloud 安全设置为集成用户签发的基本身份验证 API 凭据）进行身份验证。API 用户的角色既控制其可读取哪些总账实体，也控制其可通过哪些 FBDI/GL Interface 功能过账。

## 配置

| 字段 | 类型 | 说明 |
|---|---|---|
| 名称 | 文本 | 此连接的显示名称。 |
| 实例 URL | 文本 | Fusion Cloud 实例的 URL，例如 `https://yourorg.fa.us2.oraclecloud.com`。 |
| 客户端 ID | 文本 | API 用户的 OAuth2 客户端 ID（基本身份验证时为用户名）。 |
| 客户端密钥 | 文本 | API 用户的 OAuth2 客户端密钥（基本身份验证时为密码）。加密存储。 |

## 可导入的实体

两个导入步骤对应不同的拉取规模，均针对 `gl_balances` 和 `journal_batches`：

- **Import Fusion Entity** 步骤 — 直接调用 OData/BIP，适用于常规的小批量拉取。
- **Import Fusion Bulk Extract** 步骤 — 异步 FBDI/BIP 导出作业，适用于大规模提取。

两者都支持对日期、会计期间以及数值型余额/金额字段进行范围筛选（`ge`/`le`），也支持对账套或货币等离散字段进行等值筛选。完整字段参考请参阅 [Import Fusion Entity](/zh-cn/reference/workflow-steps/oracle-fusion/import-fusion-entity/) 和 [Import Fusion Bulk Extract](/zh-cn/reference/workflow-steps/oracle-fusion/import-fusion-bulk-extract/)。

## 过账日记账分录

**Oracle Fusion: Post Journal Entry** 步骤通过 PlaidCloud 共享的 ERP 写入管道过账总账日记账批次：将批次作为 FBDI 文件写入 Oracle 的 GL_INTERFACE 暂存表，提交并轮询 Journal Import Launcher ESS 作业直至进入终止状态，并在报告批次已过账之前进行确认。更正会过账一笔新的借贷互换的冲销分录，而不是编辑原分录。字段参考请参阅 [Oracle Fusion: Post Journal Entry](/zh-cn/reference/workflow-steps/oracle-fusion/oracle-fusion-post/)，完整的过账演练请参阅[连接到 Oracle Fusion](/zh-cn/guides/connections/oracle-fusion/)。

## 已知限制

| 限制 | 含义 |
|---|---|
| ESS 作业延迟 | Journal Import Launcher 作为计划作业运行，而非同步调用——一次过账运行所需时间明显长于直接 API 写入。 |
| 批量提取延迟 | `import_fusion_bulk_extract` 需等待 FBDI/BIP 导出作业——请留给 `import_fusion_entity` 的直接路径无法处理的大规模拉取。 |

## 相关内容

- [连接到 Oracle Fusion（指南）](/zh-cn/guides/connections/oracle-fusion/) — 分步说明：创建连接、测试连接、导入实体以及过账日记账。
- [Import Fusion Entity](/zh-cn/reference/workflow-steps/oracle-fusion/import-fusion-entity/)
- [Import Fusion Bulk Extract](/zh-cn/reference/workflow-steps/oracle-fusion/import-fusion-bulk-extract/)
- [Oracle Fusion: Post Journal Entry](/zh-cn/reference/workflow-steps/oracle-fusion/oracle-fusion-post/)
- [查看 ERP 过账历史](/zh-cn/guides/connections/erp-post-history/)
