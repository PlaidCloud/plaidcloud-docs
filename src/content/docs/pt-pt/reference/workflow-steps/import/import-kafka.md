---
title: Importar Kafka
description: Leia as mensagens de tópicos Apache Kafka entre dois offsets para uma tabela do PlaidCloud, uma linha por mensagem.
sidebar:
  order: 16
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/import/import-kafka.md
---

## Descrição

Lê as mensagens de um ou mais tópicos Apache Kafka para uma tabela de projeto, uma linha por mensagem. O passo lê um intervalo fixo: dos offsets iniciais aos offsets finais, em que `latest` significa o fim de cada partição quando o passo começa. As mensagens que chegam enquanto o passo é executado não são lidas. O passo acede ao Kafka através de uma [ligação Apache Kafka](/pt-pt/reference/connectors/databases/apache-kafka/).

## Origem e destino

| Definição | Obrigatório | O que faz |
| --- | --- | --- |
| Ligação Kafka | Sim | A ligação através da qual se faz a leitura. |
| Tópicos | Um dos dois | Os tópicos a ler, um por linha. |
| Padrão de tópicos | Um dos dois | Uma expressão regular que seleciona os tópicos a ler, utilizada em vez de **Tópicos**. |
| Tabela de destino | Sim | A tabela onde as mensagens são colocadas. |

## Intervalo de mensagens

| Definição | Predefinição | O que faz |
| --- | --- | --- |
| Offsets iniciais | `earliest` | `earliest`, `latest` ou JSON que indica um offset para cada partição, como `{"orders": {"0": 1200, "1": 980}}`. Em JSON, `-2` significa earliest e `-1` latest. |
| Offsets finais | `latest` | `latest` ou JSON na mesma forma que os offsets iniciais. |
| Limite de mensagens (0 = todas) | `0` | O máximo de mensagens a ler. `0` lê todas as mensagens do intervalo. |
| Tempo limite de inatividade (segundos) | `10` | A leitura termina após este número de segundos sem uma nova mensagem. |
| Limite de tempo (segundos) | `10800` | O tempo máximo que a leitura pode durar. |

Os offsets aceitam variáveis de fluxo de trabalho escritas como `{name}`.

## Valor da mensagem

| Definição | O que faz |
| --- | --- |
| Formato do valor | **JSON**, **Texto** ou **Avro**. |
| Esquema Avro (JSON) | O esquema Avro do valor da mensagem. Obrigatório quando o formato é **Avro**. |
| Definições adicionais do consumidor (JSON) | Definições adicionais do consumidor Kafka como um objeto JSON, como `{"fetch.min.bytes": 1}`. Só são aceites as definições que o PlaidCloud permite. |

## Mapeamento de colunas

Mapeie pelo menos uma coluna no separador de mapeamento. Uma coluna lê uma das partes da mensagem, `key`, `value`, `topic`, `partition`, `offset`, `timestamp`, `timestamp_type` ou `headers`, ou um campo do valor analisado pelo seu caminho. Este passo não tem **Inspecionar origem**, pelo que deve introduzir as colunas manualmente.

## Relacionado

- [Exportar Kafka](/pt-pt/reference/workflow-steps/export/export-kafka/)
- [Ligação Apache Kafka](/pt-pt/reference/connectors/databases/apache-kafka/)
