---
title: Dimension Sort
description: Ordene automaticamente os membros de uma dimensão num passo de fluxo de trabalho do PlaidCloud para manter uma ordenação consistente nas suas hierarquias.
sidebar:
  order: 5
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/dimensions/dimension-sort.md
---

## Descrição

Ordena os membros de uma dimensão sob os respetivos elementos superiores — por ordem alfabética, por valor, por propriedade ou por uma coluna de ordem personalizada. Evita o trabalho fastidioso de arrastar manualmente os membros da hierarquia para a posição certa, sendo especialmente útil após uma carga em massa ou uma reestruturação profunda.

Atua sobre a dimensão no local; não é necessária tabela de origem nem de destino.


## Seleção de dimensão
### Especificar dimensão dinamicamente
Se as **dimensões** ou os **caminhos** foram criados dinamicamente, as mesmas variáveis podem ser usadas para os ordenar. Usar variáveis no processo de ordenação é útil, porque elimina a necessidade de atualizar manualmente o passo Dimension Sort de forma periódica.



Um exemplo que usa a variável `current_month` para ordenar dinamicamente a dimensão Materials:

```text
/Dimensions/{current_month}/Products/Materials
```

### Utilizar dimensão específica

Use o menu pendente para selecionar uma dimensão específica a ordenar.
