---
title: Apache Kafka
description: 在 PlaidCloud 中设置 Apache Kafka 连接，将主题消息读入表，并将表行作为消息发送。
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/databases/apache-kafka.md
---

**Apache Kafka** 是一个分布式事件流平台。将此连接与 [导入 Kafka](/zh-cn/reference/workflow-steps/import/import-kafka/) 步骤配合使用，可将主题的消息读入表；与 [导出 Kafka](/zh-cn/reference/workflow-steps/export/export-kafka/) 步骤配合使用，可将表的每一行作为一条消息发送。创建时，请选择 **Apache Kafka** 作为连接类型。

## 上游文档
[Apache Kafka 文档](https://kafka.apache.org/documentation/)。

## 配置

### Kafka 连接

| 字段 | 是否必填 | 说明 |
|---|---|---|
| Brokers | 是 | 要连接的 broker，以逗号分隔，例如 `broker1:9092,broker2:9092`。 |
| 安全协议 | 否 | `PLAINTEXT`（默认）、`SSL`、`SASL_PLAINTEXT` 或 `SASL_SSL`。 |
| 会话超时（毫秒） | 否 | broker 在多长时间内未收到 PlaidCloud 的消息，就将其从消费者组中移除。至少为 1000。 |

### SASL 凭据

当安全协议为 `SASL_PLAINTEXT` 或 `SASL_SSL` 时使用。

| 字段 | 说明 |
|---|---|
| SASL 机制 | `PLAIN`（默认）、`SCRAM-SHA-256`、`SCRAM-SHA-512` 或 `OAUTHBEARER`。不支持 Kerberos（`GSSAPI`）。 |
| 用户 | 连接时使用的用户，适用于 `PLAIN` 和 `SCRAM`。 |
| 密码 | 该用户的密码（只写），适用于 `PLAIN` 和 `SCRAM`。 |

### OAuth（OAUTHBEARER）

当 SASL 机制为 `OAUTHBEARER` 时使用。PlaidCloud 使用 OAuth 客户端凭据授权从您的身份提供商获取令牌，并在令牌过期时获取新令牌。

| 字段 | 说明 |
|---|---|
| 令牌端点 URL | 身份提供商的令牌端点。必须是公共互联网上的 `https` 地址。 |
| 客户端 ID | 请求令牌时使用的客户端。必填。 |
| 客户端密钥 | 客户端的密钥（只写）。必填。 |
| 范围 | 当您的提供商需要时，要请求的范围。 |
| SASL 扩展 | 可选的 `key=value` 键值对，以逗号分隔，随令牌一起发送，例如 Confluent Cloud 要求的 `logicalCluster` 和 `identityPoolId`。 |

### TLS

| 字段 | 说明 |
|---|---|
| CA 证书（PEM） | 签发 broker 证书的证书颁发机构（如果它不是公共机构）。编辑时留空可保留已保存的证书。 |
