---
title: Apache Kafka
description: Configure uma ligação do Apache Kafka no PlaidCloud para ler mensagens de tópicos para tabelas e enviar linhas de tabelas como mensagens.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/databases/apache-kafka.md
---

O **Apache Kafka** é uma plataforma distribuída de transmissão de eventos em fluxo. Utilize esta ligação com [Importar Kafka](/pt-pt/reference/workflow-steps/import/import-kafka/) para ler as mensagens de tópicos para uma tabela e com [Exportar Kafka](/pt-pt/reference/workflow-steps/export/export-kafka/) para enviar cada linha de uma tabela como uma mensagem. Para criar uma, escolha **Apache Kafka** como tipo de ligação.

## Documentação de origem
[A documentação do Apache Kafka](https://kafka.apache.org/documentation/).

## Configuração

### Ligação Kafka

| Campo | Obrigatório | Descrição |
|---|---|---|
| Brokers | Sim | Os brokers aos quais ligar, separados por vírgulas, como `broker1:9092,broker2:9092`. |
| Protocolo de segurança | Não | `PLAINTEXT` (a predefinição), `SSL`, `SASL_PLAINTEXT` ou `SASL_SSL`. |
| Tempo limite da sessão (ms) | Não | Durante quanto tempo os brokers esperam sem ter notícias do PlaidCloud antes de o retirarem do grupo de consumidores. No mínimo, 1000. |

### Credenciais SASL

Utilizadas quando o protocolo de segurança é `SASL_PLAINTEXT` ou `SASL_SSL`.

| Campo | Descrição |
|---|---|
| Mecanismo SASL | `PLAIN` (a predefinição), `SCRAM-SHA-256`, `SCRAM-SHA-512` ou `OAUTHBEARER`. O Kerberos (`GSSAPI`) não está disponível. |
| Utilizador | O utilizador com o qual ligar, para `PLAIN` e `SCRAM`. |
| Palavra-passe | A palavra-passe do utilizador (só de escrita), para `PLAIN` e `SCRAM`. |

### OAuth (OAUTHBEARER)

Utilizado quando o mecanismo SASL é `OAUTHBEARER`. O PlaidCloud obtém o seu token junto do seu fornecedor de identidade com a concessão de credenciais de cliente do OAuth e obtém um novo quando este expira.

| Campo | Descrição |
|---|---|
| URL do ponto final do token | O ponto final de tokens do fornecedor de identidade. Tem de ser um endereço `https` na Internet pública. |
| ID do cliente | O cliente com o qual pedir o token. Obrigatório. |
| Segredo do cliente | O segredo do cliente (só de escrita). Obrigatório. |
| Âmbito | O âmbito a pedir, quando o seu fornecedor precisar de um. |
| Extensões SASL | Pares `key=value` opcionais, separados por vírgulas, enviados com o token, como o `logicalCluster` e o `identityPoolId` que o Confluent Cloud pede. |

### TLS

| Campo | Descrição |
|---|---|
| Certificado CA (PEM) | A autoridade de certificação que assinou os certificados dos brokers, quando não é uma autoridade pública. Deixe em branco ao editar para manter o certificado guardado. |
