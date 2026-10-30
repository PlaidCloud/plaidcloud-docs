---
title: Google BigQuery 连接器
description: 在 PlaidCloud 中配置 Google BigQuery 连接，以运行分析查询并将大规模数据集成到工作流中。
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/google/big-query.md
---

## 连接文档
[Google BigQuery 文档](https://docs.cloud.google.com/bigquery/docs)。

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

### BigQuery 连接

| 字段 | 必填 | 说明 |
|---|---|---|
| 项目 | 是 | 包含数据集的 Google Cloud 项目。 |
| 数据集 | 是 | 要读取和写入的 BigQuery 数据集。 |
| 表 | 是 | 数据集中的表。 |

### 身份验证凭据

| 字段 | 必填 | 说明 |
|---|---|---|
| 服务账号密钥（JSON） | 是 | 粘贴可读取该数据集的 Google 服务账号的完整 JSON 密钥文件。仅当需要向数据集写入时才授予其写入权限。密钥为只写：编辑时留空可保留已保存的密钥。 |

该连接仅使用您提供的服务账号密钥进行身份验证。[导入 SQL](/zh-cn/reference/workflow-steps/import/import-sql/) 步骤通过此连接读取 BigQuery，[Export External Database Tables](/zh-cn/reference/workflow-steps/export/export-external-tables/) 步骤则通过 BigQuery 加载作业向其写入。
