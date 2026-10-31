---
title: Dimension Delete
description: Elimine uma dimensão do PlaidCloud num passo de fluxo de trabalho para remover estruturas de dados hierárquicas que já não são necessárias.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/dimensions/dimension-delete.md
---

## Descrição
Elimina uma dimensão juntamente com toda a estrutura, valores, propriedades, aliases e hierarquias alternativas associados


![Dimension Clear](/images/dimension_clear.png)



## Seleção de dimensão
### Especificar dimensão dinamicamente
Se as **dimensões** ou os **caminhos** foram criados dinamicamente, as mesmas variáveis podem ser usadas para os eliminar. Usar variáveis no processo de eliminação é útil, porque elimina a necessidade de atualizar manualmente o passo Dimension Delete de forma periódica.



Um exemplo que usa a variável `current_month` para eliminar dinamicamente a dimensão Materials:

```text
/Dimensions/{current_month}/Products/Materials
```

### Utilizar dimensão específica

Use o menu pendente para selecionar uma dimensão específica a eliminar.
