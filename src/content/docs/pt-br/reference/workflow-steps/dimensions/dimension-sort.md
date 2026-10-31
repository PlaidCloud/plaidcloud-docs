---
title: Dimension Sort
description: Ordene automaticamente os membros de uma dimensão em uma etapa de fluxo de trabalho do PlaidCloud para manter uma ordenação consistente nas suas hierarquias.
sidebar:
  order: 5
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/dimensions/dimension-sort.md
---

## Descrição

Ordena os membros de uma dimensão sob seus pais — em ordem alfabética, por valor, por propriedade ou por uma coluna de ordem personalizada. Evita o trabalho tedioso de arrastar manualmente os membros da hierarquia para a ordem correta, o que é especialmente útil depois de uma carga em massa ou de uma grande reestruturação.

Opera na dimensão diretamente; não é necessária tabela de origem nem de destino.


## Seleção de dimensão
### Especificar dimensão dinamicamente
Se as **dimensões** ou os **caminhos** foram criados dinamicamente, as mesmas variáveis podem ser usadas para ordená-los. Usar variáveis no processo de ordenação é útil porque elimina a necessidade de atualizar manualmente a etapa Dimension Sort de tempos em tempos.



Um exemplo que usa a variável `current_month` para ordenar dinamicamente a dimensão Materials:

```text
/Dimensions/{current_month}/Products/Materials
```

### Usar dimensão específica

Use o menu suspenso para selecionar uma dimensão específica a ser ordenada.
