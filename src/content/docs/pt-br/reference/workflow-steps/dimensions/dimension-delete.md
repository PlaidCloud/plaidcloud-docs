---
title: Dimension Delete
description: Exclua uma dimensão do PlaidCloud em uma etapa de fluxo de trabalho para remover estruturas de dados hierárquicas que não são mais necessárias.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/dimensions/dimension-delete.md
---

## Descrição
Exclui uma dimensão junto com toda a estrutura, valores, propriedades, aliases e hierarquias alternativas associados


![Dimension Clear](/images/dimension_clear.png)



## Seleção de dimensão
### Especificar dimensão dinamicamente
Se as **dimensões** ou os **caminhos** foram criados dinamicamente, as mesmas variáveis podem ser usadas para excluí-los. Usar variáveis no processo de exclusão é útil porque elimina a necessidade de atualizar manualmente a etapa Dimension Delete de tempos em tempos.



Um exemplo que usa a variável `current_month` para excluir dinamicamente a dimensão Materials:

```text
/Dimensions/{current_month}/Products/Materials
```

### Usar dimensão específica

Use o menu suspenso para selecionar uma dimensão específica a ser excluída.
