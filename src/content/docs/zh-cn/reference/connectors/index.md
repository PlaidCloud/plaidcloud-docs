---
title: 数据与服务连接器
description: 将 PlaidCloud 连接到外部数据源和服务，包括数据库、ERP、REST API、云存储和 Git 仓库。
sidebar:
  label: 连接器
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/index.md
---

PlaidCloud 通过专用连接器连接到外部数据源和服务。每个连接器负责处理一类提供商的身份验证、协议和数据形态等细节。

## 分类

### 数据库与数据湖

关系型数据库、云数据仓库、查询引擎和 Lakehouse 格式。

- [数据库](/zh-cn/reference/connectors/databases/) — PostgreSQL、MySQL、SQL Server、Oracle、Snowflake、Redshift、BigQuery、Databricks、MongoDB、Kafka 等 15 种以上
- [开放表](/zh-cn/reference/connectors/open-tables/) — Apache Iceberg、Delta Lake、Hudi、Hive 开放表格式

### 云与 SaaS 服务

- [REST](/zh-cn/reference/connectors/rest/) — Salesforce、NetSuite、Workday、QuickBooks、Stripe、Dynamics 等
- [ERP 系统](/zh-cn/reference/connectors/erp/) — SAP ECC / S/4HANA、Oracle EBS/Fusion、Infor、JD Edwards
- [云服务](/zh-cn/reference/connectors/cloud-services/) — 第三方数据服务
- [Google](/zh-cn/reference/connectors/google/) — BigQuery、Google 表格
- [协作](/zh-cn/reference/connectors/collaboration/) — Slack、Microsoft Teams、Tableau
- [Singer 源](/zh-cn/reference/connectors/singer-sources/) — 130 多个 Singer tap 源：Stripe、GitHub、HubSpot、数据库等

### 开发与源代码管理

- [Git 提供商](/zh-cn/reference/connectors/git/) — PlaidCloud Git（托管、内置），以及 GitHub、GitLab、Bitbucket、Azure Repos、CodeCommit

## 相关内容

- [连接指南](/zh-cn/guides/connections/) — 创建和管理连接的任务式操作指南
- [工作流步骤参考](/zh-cn/reference/workflow-steps/) — 连接配置完成后可以做什么
