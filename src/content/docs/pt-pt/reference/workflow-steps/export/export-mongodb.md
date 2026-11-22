---
title: Exportar MongoDB
description: Escreva uma tabela PlaidCloud numa coleção MongoDB como documentos inseridos, substituídos, atualizados ou com upsert.
sidebar:
  order: 9
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/export/export-mongodb.md
---

## Descrição

Escreve cada linha de uma tabela de projeto numa coleção MongoDB como um documento. A coleção é criada quando não existe. O passo acede ao MongoDB através de uma [ligação MongoDB](/pt-pt/reference/connectors/databases/mongodb/).

## Origem e destino

| Definição | Obrigatório | O que faz |
| --- | --- | --- |
| Tabela de origem | Sim | A tabela a escrever. |
| Ligação MongoDB | Sim | A ligação através da qual escrever. |
| Base de dados | Não | A base de dados onde escrever. Deixe em branco para utilizar a **Base de dados predefinida** da ligação. |
| Coleção | Sim | A coleção onde escrever. |

## Opções de escrita

| Definição | O que faz |
| --- | --- |
| Modo de escrita | **Inserir um documento por linha** (o predefinido), **Substituir o documento correspondente**, **Atualizar os campos do documento correspondente**, **Substituir o documento correspondente ou inserir** ou **Atualizar os campos do documento correspondente ou inserir**. |
| Colunas de correspondência | As colunas, separadas por vírgulas, que identificam um documento. Obrigatórias para todos os modos exceto inserir. |
| Eliminar todos os documentos da coleção antes de escrever | Esvazia primeiro a coleção, para que contenha apenas as linhas desta execução. |
| Parar na primeira escrita falhada | Pára no primeiro documento que o MongoDB recusa. Desmarque para prosseguir com os restantes. |
| Aguardar que a escrita chegue ao diário | Aguarda até o MongoDB ter escrito cada lote no respetivo diário. |
| Write Concern | Em branco para o da ligação, um número de servidores ou `majority`. |
| Documentos por pedido | Quantos documentos são enviados em cada pedido. |

A inserção volta a adicionar os documentos de cada vez que o passo é executado. Os modos que substituem ou atualizam deixam a coleção igual independentemente do número de vezes que o passo é executado, pelo que deve usar um deles quando um fluxo de trabalho possa ser executado duas vezes sobre as mesmas linhas.

## Quando a origem está em falta ou vazia

O passo não falha quando não há nada para escrever. Termina com êxito e regista um aviso que indica a coleção ou a tabela:

- **A tabela de origem não existe.** O aviso é `No table found for path "…", so nothing was written to collection …` e a coleção fica como estava, mesmo com **Eliminar todos os documentos da coleção antes de escrever** ativado.
- **A tabela de origem não tem colunas.** Sem colunas de origem nem de destino mapeadas, o passo escreve todas as colunas da tabela, pelo que isto se aplica a uma tabela sem nenhuma. O aviso é `Table … has no columns; nothing was written to collection …`.
- **A tabela de origem não tem linhas.** O aviso é `The table has no rows; nothing was written to …`. Com **Eliminar todos os documentos da coleção antes de escrever** ativado, a coleção é esvaziada e o aviso di-lo: `… was emptied and nothing was written to it`.

## Relacionado

- [Importar MongoDB](/pt-pt/reference/workflow-steps/import/import-mongodb/)
- [Ligação MongoDB](/pt-pt/reference/connectors/databases/mongodb/)
