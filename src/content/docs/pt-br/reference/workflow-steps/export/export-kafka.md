---
title: Exportar Kafka
description: Envie cada linha de uma tabela do PlaidCloud a um tópico do Apache Kafka como uma mensagem.
sidebar:
  order: 8
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/export/export-kafka.md
---

## Descrição

Envia cada linha de uma tabela de projeto a um tópico do Apache Kafka como uma mensagem. Uma mensagem enviada não pode ser desfeita, portanto executar a etapa novamente envia as linhas de novo. A etapa acessa o Kafka por meio de uma [conexão do Apache Kafka](/pt-br/reference/connectors/databases/apache-kafka/).

## Origem e destino

| Configuração | Obrigatória | O que faz |
| --- | --- | --- |
| Tabela de origem | Sim | A tabela a enviar. |
| Conexão do Kafka | Sim | A conexão por meio da qual enviar. |
| Tópico | Sim | O tópico para o qual todas as linhas são enviadas. |

## Mensagem

| Configuração | O que faz |
| --- | --- |
| Coluna de chave | A coluna cujo valor é a chave da mensagem. Deixe em branco para enviar mensagens sem chave. |
| Colunas de valor | As colunas, separadas por vírgula, que compõem o valor da mensagem. Deixe em branco para enviar todas as colunas. |
| Coluna de partição | Uma coluna de inteiros que indica a partição de cada mensagem. Deixe em branco para que o Kafka escolha. |
| Formato do valor | **JSON**, **Texto** ou **Avro**. |
| Esquema Avro (JSON) | O esquema Avro do valor da mensagem. Obrigatório quando o formato é **Avro**. |

## Entrega

| Configuração | Padrão | O que faz |
| --- | --- | --- |
| Espera da entrega (segundos) | `60` | Quanto tempo a etapa espera, no final, que o Kafka confirme todas as mensagens. |
| Limite de tempo (segundos) | `10800` | O tempo máximo que o envio pode durar. |
| Configurações extras do produtor (JSON) | — | Configurações adicionais do produtor Kafka como um objeto JSON, como `{"compression.type": "gzip"}`. Somente as configurações permitidas pelo PlaidCloud são aceitas. |

## Relacionados

- [Importar Kafka](/pt-br/reference/workflow-steps/import/import-kafka/)
- [Conexão do Apache Kafka](/pt-br/reference/connectors/databases/apache-kafka/)
