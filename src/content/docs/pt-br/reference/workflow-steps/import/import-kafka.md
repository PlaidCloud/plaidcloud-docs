---
title: Importar Kafka
description: Leia as mensagens de tópicos do Apache Kafka entre dois offsets para uma tabela do PlaidCloud, uma linha por mensagem.
sidebar:
  order: 16
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/import/import-kafka.md
---

## Descrição

Lê as mensagens de um ou mais tópicos do Apache Kafka para uma tabela de projeto, uma linha por mensagem. A etapa lê um intervalo fixo: dos offsets iniciais aos offsets finais, em que `latest` significa o fim de cada partição no momento em que a etapa começa. As mensagens que chegam enquanto a etapa é executada não são lidas. A etapa acessa o Kafka por meio de uma [conexão do Apache Kafka](/pt-br/reference/connectors/databases/apache-kafka/).

## Origem e destino

| Configuração | Obrigatório | O que faz |
| --- | --- | --- |
| Conexão do Kafka | Sim | A conexão usada para a leitura. |
| Tópicos | Um dos dois | Os tópicos a serem lidos, um por linha. |
| Padrão de tópicos | Um dos dois | Uma expressão regular que seleciona os tópicos a serem lidos, usada no lugar de **Tópicos**. |
| Tabela de destino | Sim | A tabela em que as mensagens são gravadas. |

## Intervalo de mensagens

| Configuração | Padrão | O que faz |
| --- | --- | --- |
| Offsets iniciais | `earliest` | `earliest`, `latest` ou JSON que informa um offset para cada partição, como `{"orders": {"0": 1200, "1": 980}}`. Em JSON, `-2` significa earliest e `-1`, latest. |
| Offsets finais | `latest` | `latest` ou JSON no mesmo formato dos offsets iniciais. |
| Limite de mensagens (0 = todas) | `0` | O máximo de mensagens a serem lidas. `0` lê todas as mensagens do intervalo. |
| Tempo limite de inatividade (segundos) | `10` | A leitura termina após essa quantidade de segundos sem uma nova mensagem. |
| Limite de tempo (segundos) | `10800` | O tempo máximo que a leitura pode durar. |

Os offsets aceitam variáveis de fluxo de trabalho escritas como `{name}`.

## Valor da mensagem

| Configuração | O que faz |
| --- | --- |
| Formato do valor | **JSON**, **Texto** ou **Avro**. |
| Esquema Avro (JSON) | O esquema Avro do valor da mensagem. Obrigatório quando o formato é **Avro**. |
| Configurações extras do consumidor (JSON) | Configurações adicionais do consumidor Kafka como um objeto JSON, como `{"fetch.min.bytes": 1}`. Apenas as configurações permitidas pelo PlaidCloud são aceitas. |

## Mapeamento de colunas

Mapeie pelo menos uma coluna na guia de mapeamento. Uma coluna lê uma das partes da mensagem, `key`, `value`, `topic`, `partition`, `offset`, `timestamp`, `timestamp_type` ou `headers`, ou um campo do valor analisado pelo seu caminho. Não há **Inspecionar origem** para esta etapa, portanto informe as colunas manualmente.

## Relacionados

- [Exportar Kafka](/pt-br/reference/workflow-steps/export/export-kafka/)
- [Conexão do Apache Kafka](/pt-br/reference/connectors/databases/apache-kafka/)
