---
title: Importar MongoDB
description: Leia uma coleção do MongoDB, ou o resultado de um pipeline de agregação, para uma tabela do PlaidCloud como uma etapa de fluxo de trabalho.
sidebar:
  order: 17
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/import/import-mongodb.md
---

## Descrição

Lê os documentos de uma coleção do MongoDB para uma tabela de projeto, uma linha por documento. Use um filtro para ler apenas os documentos de que precisa, ou um pipeline de agregação para remodelá-los no MongoDB antes de serem gravados. A etapa acessa o MongoDB por meio de uma [conexão do MongoDB](/pt-br/reference/connectors/databases/mongodb/).

## Origem e destino

| Configuração | Obrigatório | O que faz |
| --- | --- | --- |
| Conexão do MongoDB | Sim | A conexão usada para a leitura. |
| Banco de dados | Não | O banco de dados a ser lido. Deixe em branco para usar o **Banco de dados padrão** da conexão. |
| Coleção | Sim | A coleção a ser lida. |
| Tabela de destino | Sim | A tabela em que os documentos são gravados. Deve ser uma tabela, não uma visão. |

## Consulta

| Configuração | O que faz |
| --- | --- |
| Filtro (JSON) | Um filtro de consulta do MongoDB como objeto JSON, como `{"status": "open"}`. Apenas os documentos correspondentes são lidos. |
| Pipeline de agregação (JSON) | Um pipeline de agregação como array JSON, como `[{"$match": {"status": "open"}}]`. Quando definido, a coleção é agregada em vez de filtrada. Um pipeline com um estágio `$out` ou `$merge` é recusado, porque gravaria no MongoDB. |
| Limite de linhas (0 = todas) | O máximo de documentos a serem lidos. `0` lê todos. |
| Limite de tempo (segundos) | Quanto tempo o MongoDB pode gastar na leitura antes de interrompê-la. |
| Documentos amostrados para as colunas | Quando a etapa não declara colunas, quantos documentos, a partir do primeiro, definem as colunas e seus tipos: cada campo de nível superior que eles contêm vira uma coluna. O padrão é 1000. |

O filtro e o pipeline aceitam variáveis de fluxo de trabalho escritas como `{name}`, como `{"region": "{region}"}`. O valor de cada variável é inserido como uma única string ou número JSON, de modo que uma variável não pode adicionar chaves ou operadores à consulta. Uma variável que não está definida interrompe a etapa com um erro que a nomeia.

## Mapeamento de colunas

Mapeie cada campo do documento para uma coluna da tabela de destino na guia de mapeamento. Uma coluna lê o campo do documento de mesmo nome. Uma coleção que não existe termina com um aviso e deixa a tabela de destino vazia.

## Relacionados

- [Exportar MongoDB](/pt-br/reference/workflow-steps/export/export-mongodb/)
- [Conexão do MongoDB](/pt-br/reference/connectors/databases/mongodb/)
