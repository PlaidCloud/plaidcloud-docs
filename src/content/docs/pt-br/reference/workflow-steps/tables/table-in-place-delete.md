---
title: Table In-Place Delete (etapa)
description: Exclua linhas específicas de uma tabela em uma etapa de fluxo de trabalho do PlaidCloud usando condições de filtro para remover registros selecionados no local.
sidebar:
  order: 9
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/tables/table-in-place-delete.md
---

## Descrição


Executa uma exclusão na tabela usando as condições de filtro especificadas. A operação é realizada diretamente na tabela designada, portanto nenhuma tabela adicional é criada. Somente as linhas que atendem aos critérios do filtro são excluídas. Essa pode ser uma abordagem eficaz quando há preocupações com o tamanho dos dados.



## Parâmetros de exclusão


Selecione a tabela de **Origem** da qual excluir na lista suspensa. Essa lista inclui todas as tabelas de dados de *Projeto* e de *Fluxo de trabalho*.

![Table In-Place Delete](/images/table_inplace_table_selection.png)

## Filtros de dados para exclusão

![Table In-Place Delete](/images/table_in-place_table_filter.png)




## Exemplos
