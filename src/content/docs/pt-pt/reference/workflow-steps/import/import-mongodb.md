---
title: Importar MongoDB
description: Leia uma coleção MongoDB, ou o resultado de um pipeline de agregação, para uma tabela do PlaidCloud como um passo de fluxo de trabalho.
sidebar:
  order: 17
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/import/import-mongodb.md
---

## Descrição

Lê os documentos de uma coleção MongoDB para uma tabela de projeto, uma linha por documento. Utilize um filtro para ler apenas os documentos de que precisa, ou um pipeline de agregação para os remodelar no MongoDB antes de serem colocados. O passo acede ao MongoDB através de uma [ligação MongoDB](/pt-pt/reference/connectors/databases/mongodb/).

## Origem e destino

| Definição | Obrigatório | O que faz |
| --- | --- | --- |
| Ligação MongoDB | Sim | A ligação através da qual se faz a leitura. |
| Base de dados | Não | A base de dados a ler. Deixe em branco para utilizar a **Base de dados predefinida** da ligação. |
| Coleção | Sim | A coleção a ler. |
| Tabela de destino | Sim | A tabela onde os documentos são colocados. Tem de ser uma tabela, não uma vista. |

## Consulta

| Definição | O que faz |
| --- | --- |
| Filtro (JSON) | Um filtro de consulta MongoDB como objeto JSON, como `{"status": "open"}`. Só são lidos os documentos correspondentes. |
| Pipeline de agregação (JSON) | Um pipeline de agregação como matriz JSON, como `[{"$match": {"status": "open"}}]`. Quando definido, a coleção é agregada em vez de filtrada. Um pipeline com uma fase `$out` ou `$merge` é recusado, porque escreveria no MongoDB. |
| Limite de linhas (0 = todas) | O máximo de documentos a ler. `0` lê todos. |
| Limite de tempo (segundos) | Quanto tempo o MongoDB pode gastar na leitura antes de a interromper. |
| Documentos amostrados para as colunas | Quando o passo não declara colunas, quantos documentos, a partir do primeiro, determinam as colunas e os respetivos tipos: cada campo de nível superior que contêm torna-se uma coluna. A predefinição é 1000. |

O filtro e o pipeline aceitam variáveis de fluxo de trabalho escritas como `{name}`, como `{"region": "{region}"}`. O valor de cada variável é inserido como uma única cadeia ou número JSON, pelo que uma variável não pode acrescentar chaves ou operadores à consulta. Uma variável que não esteja definida interrompe o passo com um erro que a indica.

## Mapeamento de colunas

Mapeie cada campo do documento para uma coluna da tabela de destino no separador de mapeamento. Uma coluna lê o campo do documento com o mesmo nome. Uma coleção que não exista termina com um aviso e deixa a tabela de destino vazia.

## Relacionado

- [Exportar MongoDB](/pt-pt/reference/workflow-steps/export/export-mongodb/)
- [Ligação MongoDB](/pt-pt/reference/connectors/databases/mongodb/)
