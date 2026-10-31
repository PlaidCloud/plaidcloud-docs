---
title: Apache Kafka
description: Configure uma conexão do Apache Kafka no PlaidCloud para ler mensagens de tópicos em tabelas e enviar linhas de tabelas como mensagens.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/databases/apache-kafka.md
---

O **Apache Kafka** é uma plataforma distribuída de streaming de eventos. Use esta conexão com [Importar Kafka](/pt-br/reference/workflow-steps/import/import-kafka/) para ler as mensagens de tópicos em uma tabela e com [Exportar Kafka](/pt-br/reference/workflow-steps/export/export-kafka/) para enviar cada linha de uma tabela como uma mensagem. Para criar uma, escolha **Apache Kafka** como o tipo de conexão.

## Documentação de origem
[A documentação do Apache Kafka](https://kafka.apache.org/documentation/).

## Configuração

### Conexão do Kafka

| Campo | Obrigatório | Descrição |
|---|---|---|
| Brokers | Sim | Os brokers aos quais se conectar, separados por vírgulas, como `broker1:9092,broker2:9092`. |
| Protocolo de segurança | Não | `PLAINTEXT` (o padrão), `SSL`, `SASL_PLAINTEXT` ou `SASL_SSL`. |
| Tempo limite da sessão (ms) | Não | Por quanto tempo os brokers aguardam sem notícias do PlaidCloud antes de removê-lo do grupo de consumidores. No mínimo 1000. |

### Credenciais SASL

Usado quando o protocolo de segurança é `SASL_PLAINTEXT` ou `SASL_SSL`.

| Campo | Descrição |
|---|---|
| Mecanismo SASL | `PLAIN` (o padrão), `SCRAM-SHA-256`, `SCRAM-SHA-512` ou `OAUTHBEARER`. O Kerberos (`GSSAPI`) não está disponível. |
| Usuário | O usuário com o qual se conectar, para `PLAIN` e `SCRAM`. |
| Senha | A senha do usuário (somente gravação), para `PLAIN` e `SCRAM`. |

### OAuth (OAUTHBEARER)

Usado quando o mecanismo SASL é `OAUTHBEARER`. O PlaidCloud obtém o token do seu provedor de identidade com a concessão de credenciais de cliente do OAuth e obtém um novo quando ele expira.

| Campo | Descrição |
|---|---|
| URL do endpoint do token | O endpoint de token do provedor de identidade. Deve ser um endereço `https` na internet pública. |
| ID do cliente | O cliente com o qual solicitar o token. Obrigatório. |
| Segredo do cliente | O segredo do cliente (somente gravação). Obrigatório. |
| Escopo | O escopo a solicitar, quando o seu provedor exigir um. |
| Extensões SASL | Pares `key=value` opcionais, separados por vírgulas, enviados com o token, como `logicalCluster` e `identityPoolId`, que o Confluent Cloud solicita. |

### TLS

| Campo | Descrição |
|---|---|
| Certificado de CA (PEM) | A autoridade certificadora que assinou os certificados dos brokers, quando não for uma pública. Deixe em branco ao editar para manter o certificado salvo. |
