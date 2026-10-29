---
title: MongoDB
description: 在 PlaidCloud 中设置 MongoDB 连接，将集合读入表，并将表以文档形式写回。
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/databases/mongodb.md
---

**MongoDB** 是一种文档数据库。将此连接与[导入 MongoDB](/zh-cn/reference/workflow-steps/import/import-mongodb/) 配合使用，可将集合或聚合管道的结果读入表；与[导出 MongoDB](/zh-cn/reference/workflow-steps/export/export-mongodb/) 配合使用，可将表以文档形式写回。创建时，请选择 **MongoDB** 作为连接类型。

## 上游文档
[MongoDB 文档](https://www.mongodb.com/docs/)。

## 配置

### MongoDB 连接

| 字段 | 必填 | 说明 |
|---|---|---|
| 主机 | 是 | 服务器的主机名。 |
| 使用 SRV 地址（mongodb+srv://，不含端口） | 否 | 通过 DNS 种子列表连接，MongoDB Atlas 即采用这种方式。不使用端口。 |
| 端口 | 否 | 服务器的端口。默认为 `27017`。 |
| 默认数据库 | 否 | 步骤未指定数据库时使用的数据库。 |

### 身份验证凭据

| 字段 | 说明 |
|---|---|
| 用户 | 用于连接的用户。 |
| 密码 | 用户的密码（只写）。 |

### 选项

| 字段 | 说明 |
|---|---|
| 连接选项 | 以 `&` 连接的 MongoDB URI 选项，例如 `authSource=admin&tls=true`。仅接受 PlaidCloud 允许的选项。编辑时留空可保留已保存的选项。 |

### TLS

| 字段 | 说明 |
|---|---|
| CA 证书（PEM） | 为服务器证书签名的证书颁发机构（当其不是公共机构时）。编辑时留空可保留已保存的证书。 |
