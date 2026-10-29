---
title: Exportar Kafka
description: Envie cada linha de uma tabela PlaidCloud para um tópico Apache Kafka como uma mensagem.
sidebar:
  order: 8
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/export/export-kafka.md
---

## Descrição

Envia cada linha de uma tabela de projeto para um tópico Apache Kafka como uma mensagem. Uma mensagem enviada não pode ser retirada, pelo que executar o passo novamente envia as linhas outra vez. O passo acede ao Kafka através de uma [ligação Apache Kafka](/pt-pt/reference/connectors/databases/apache-kafka/).

## Origem e destino

| Definição | Obrigatório | O que faz |
| --- | --- | --- |
| Tabela de origem | Sim | A tabela a enviar. |
| Ligação Kafka | Sim | A ligação através da qual enviar. |
| Tópico | Sim | O tópico para o qual cada linha é enviada. |

## Mensagem

| Definição | O que faz |
| --- | --- |
| Coluna de chave | A coluna cujo valor é a chave da mensagem. Deixe em branco para enviar mensagens sem chave. |
| Colunas de valor | As colunas, separadas por vírgulas, que compõem o valor da mensagem. Deixe em branco para enviar todas as colunas. |
| Coluna de partição | Uma coluna de números inteiros que indica a partição de cada mensagem. Deixe em branco para que o Kafka escolha. |
| Formato do valor | **JSON**, **Texto** ou **Avro**. |
| Esquema Avro (JSON) | O esquema Avro do valor da mensagem. Obrigatório quando o formato é **Avro**. |

## Entrega

| Definição | Predefinição | O que faz |
| --- | --- | --- |
| Espera da entrega (segundos) | `60` | Quanto tempo o passo aguarda no final que o Kafka confirme todas as mensagens. |
| Limite de tempo (segundos) | `10800` | O tempo máximo que o envio pode durar. |
| Definições adicionais do produtor (JSON) | — | Definições adicionais do produtor Kafka como um objeto JSON, como `{"compression.type": "gzip"}`. Apenas são aceites as definições que o PlaidCloud permite. |

## Relacionado

- [Importar Kafka](/pt-pt/reference/workflow-steps/import/import-kafka/)
- [Ligação Apache Kafka](/pt-pt/reference/connectors/databases/apache-kafka/)
