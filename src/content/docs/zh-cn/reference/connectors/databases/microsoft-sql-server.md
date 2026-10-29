---
title: Microsoft SQL Server
description: 在 PlaidCloud 中配置 Microsoft SQL Server 连接，以查询、导入和导出 SQL Server 数据库中的数据。
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/databases/microsoft-sql-server.md
---

**Microsoft SQL Server** 是本地部署的 Microsoft 企业技术栈中常见的关系型数据库。使用此连接器可读写 SQL Server 表。同时支持 SQL Server 身份验证（用户名/密码）和集成身份验证；对于非扁平网络部署，可使用 SSL 和 SSH 隧道。

## 上游文档
[Microsoft SQL Server 文档](https://learn.microsoft.com/en-us/sql/sql-server/)。

## 配置

创建或编辑此连接时会显示这些字段。必填或可选取决于所启用的身份验证选项。

### 标识

| 字段 | 类型 | 说明 |
|---|---|---|
| 名称 | 文本 | 此连接的显示名称。 |
| 别名 | 文本（多行） | 可选的别名或连接备注。 |
| 是否启用 | 开关 | 是否启用该连接。禁用可暂停使用而无需删除。 |
| 数据库只读 | 开关 | 将连接限制为只读操作。 |
| 访问类型 | 选择 | 此连接的访问级别：只读、只写或读写。 |

### 连接

| 字段 | 类型 | 说明 |
|---|---|---|
| 数据库主机 | 文本 | 数据库服务器的主机名或 IP 地址。 |
| 数据库端口 | 数字 | 数据库连接的端口号。 |
| 数据库目录 | 文本 | 要连接的数据库、目录或模式。 |

### 身份验证

| 字段 | 类型 | 说明 |
|---|---|---|
| 数据库用户 | 文本 | 用于数据库身份验证的用户名。 |
| 数据库密码 | 密码 | 用于数据库身份验证的密码。 |

### SSL / TLS

| 字段 | 类型 | 说明 |
|---|---|---|
| 使用 SSL | 开关 | 使用 SSL/TLS 加密连接。 |
| SSL 模式 | 选择 | SSL 验证模式（例如 disable、require、verify-ca、verify-full）。 |
| SSL 客户端证书 | 文本（多行） | 用于双向 TLS 身份验证的客户端证书（PEM）。 |
| SSL 客户端密钥 | 文本（多行） | 用于双向 TLS 身份验证的客户端私钥（PEM）。 |
| SSL 根证书 | 文本（多行） | 用于验证服务器证书的根 CA 证书（PEM）。 |
| SSL 证书吊销 | 文本（多行） | 证书吊销列表（如果环境使用）。 |

### SSH 隧道

| 字段 | 类型 | 说明 |
|---|---|---|
| 使用 SSH | 开关 | 通过 SSH 堡垒机建立隧道连接。 |
| SSH 主机 | 文本 | SSH 堡垒机主机名。 |
| SSH 端口 | 数字 | SSH 堡垒机端口（默认 22）。 |
| SSH 用户 | 文本 | SSH 堡垒机用户名。 |
| SSH 密码 | 密码 | SSH 堡垒机密码（使用密码身份验证时）。 |
| 使用 SSH 证书 | 开关 | 使用私钥而非密码向 SSH 堡垒机进行身份验证。 |
| SSH 私钥 | 文本（多行） | 用于堡垒机身份验证的 SSH 私钥（PEM）。 |
| SSH 主机密钥 | 文本（多行） | 用于校验堡垒机指纹的预期 SSH 主机密钥。 |

### 其他

| 字段 | 类型 | 说明 |
|---|---|---|
| 信任证书 | 开关 | — |
| 驱动类型 | 选择 | — |
| 用户身份验证 | 开关 | — |
