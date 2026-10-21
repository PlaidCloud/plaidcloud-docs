---
title: Apache Kafka
description: Set up an Apache Kafka connection in PlaidCloud to read topic messages into tables and send table rows as messages.
sidebar:
  order: 1
---

**Apache Kafka** is a distributed event streaming platform. Use this connection with [Import Kafka](/reference/workflow-steps/import/import-kafka/) to read the messages of topics into a table, and with [Export Kafka](/reference/workflow-steps/export/export-kafka/) to send each row of a table as a message. To create one, choose **Apache Kafka** as the connection type.

## Upstream Documentation
[The Apache Kafka documentation](https://kafka.apache.org/documentation/).

## Configuration

### Kafka Connection

| Field | Required | Description |
|---|---|---|
| Brokers | Yes | The brokers to connect to, separated by commas, such as `broker1:9092,broker2:9092`. |
| Security Protocol | No | `PLAINTEXT` (the default), `SSL`, `SASL_PLAINTEXT`, or `SASL_SSL`. |
| Session Timeout (ms) | No | How long the brokers wait without hearing from PlaidCloud before they drop it from the consumer group. At least 1000. |

### SASL Credentials

Used when the security protocol is `SASL_PLAINTEXT` or `SASL_SSL`.

| Field | Description |
|---|---|
| SASL Mechanism | `PLAIN` (the default), `SCRAM-SHA-256`, `SCRAM-SHA-512`, or `OAUTHBEARER`. Kerberos (`GSSAPI`) isn't available. |
| User | The user to connect as, for `PLAIN` and `SCRAM`. |
| Password | The user's password (write-only), for `PLAIN` and `SCRAM`. |

### OAuth (OAUTHBEARER)

Used when the SASL mechanism is `OAUTHBEARER`. PlaidCloud fetches its token from your identity provider with the OAuth client-credentials grant, and fetches a new one when it expires.

| Field | Description |
|---|---|
| Token Endpoint URL | The identity provider's token endpoint. It must be an `https` address on the public internet. |
| Client ID | The client to request the token as. Required. |
| Client Secret | The client's secret (write-only). Required. |
| Scope | The scope to request, when your provider needs one. |
| SASL Extensions | Optional `key=value` pairs, separated by commas, sent with the token, such as the `logicalCluster` and `identityPoolId` that Confluent Cloud asks for. |

### TLS

| Field | Description |
|---|---|
| CA Certificate (PEM) | The certificate authority that signed the brokers' certificates, when it is not a public one. Leave it blank on edit to keep the saved certificate. |
