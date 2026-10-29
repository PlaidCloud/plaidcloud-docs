---
title: Amazon Redshift
description: 在 PlaidCloud 中设置 Amazon Redshift 数据库连接，以查询、导入和导出 Redshift 数据仓库中的数据。
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/databases/amazon-redshift.md
---

**Amazon Redshift** 是 AWS 的托管云数据仓库，专为大型数据集上的分析型工作负载而设计。使用此连接器可在 PlaidCloud 工作流中读取和写入 Redshift 表。该连接器使用 PostgreSQL 有线协议；身份验证可使用标准数据库凭据或基于 IAM 的临时凭据。

## 上游文档
有关指南和参考资料，请参阅 [Amazon Redshift 文档](https://docs.aws.amazon.com/redshift/)。

## 配置

创建或编辑此连接时会显示以下字段。是否必填取决于您启用的身份验证选项。

### 标识

| 字段 | 类型 | 说明 |
|---|---|---|
| Name | 文本 | 此连接的显示名称。 |
| Alias | 文本（多行） | 连接的可选别名或备注。 |
| Is active | 开关 | 是否启用该连接。禁用可暂停连接而不删除。 |
| Db read only | 开关 | 将连接限制为只读操作。 |
| Access type | 选择 | 此连接的只读、只写或读写访问级别。 |

### 连接

| 字段 | 类型 | 说明 |
|---|---|---|
| Db host | 文本 | 数据库服务器的主机名或 IP 地址。 |
| Db port | 数字 | 数据库连接的端口号。 |
| Db catalog | 文本 | 要连接的数据库、目录或模式。 |

### 身份验证

| 字段 | 类型 | 说明 |
|---|---|---|
| Db user | 文本 | 数据库身份验证的用户名。 |
| Use sso | 开关 | 使用单点登录代替用户名/密码进行身份验证。 |
| Db password | 密码 | 数据库身份验证的密码。 |

### SSL / TLS

| 字段 | 类型 | 说明 |
|---|---|---|
| Use ssl | 开关 | 使用 SSL/TLS 加密连接。 |
| Ssl mode | 选择 | SSL 验证模式（例如 disable、require、verify-ca、verify-full）。 |
| Ssl auth client cert | 文本（多行） | 用于双向 TLS 身份验证的客户端证书（PEM）。 |
| Ssl auth client key | 文本（多行） | 用于双向 TLS 身份验证的客户端私钥（PEM）。 |
| Ssl auth root cert | 文本（多行） | 用于验证服务器证书的根 CA 证书（PEM）。 |
| Ssl auth cert revoke | 文本（多行） | 证书吊销列表（如果您的环境使用）。 |

### SSH 隧道

| 字段 | 类型 | 说明 |
|---|---|---|
| Use ssh | 开关 | 通过 SSH 堡垒机建立连接隧道。 |
| Ssh host | 文本 | SSH 堡垒机主机名。 |
| Ssh port | 数字 | SSH 堡垒机端口（默认 22）。 |
| Ssh user | 文本 | SSH 堡垒机用户名。 |
| Ssh password | 密码 | SSH 堡垒机密码（使用密码身份验证时）。 |
| Use ssh cert | 开关 | 使用私钥代替密码向 SSH 堡垒机进行身份验证。 |
| Ssh private key | 文本（多行） | 用于堡垒机身份验证的 SSH 私钥（PEM）。 |
| Ssh host key | 文本（多行） | 用于验证堡垒机指纹的预期 SSH 主机密钥。 |
