---
title: Dimension Clear
description: Limpe todos os membros de uma dimensão do PlaidCloud em uma etapa de fluxo de trabalho, preservando a estrutura e a configuração da dimensão.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/dimensions/dimension-clear.md
---

## Descrição
Limpa o conteúdo de uma dimensão, incluindo estrutura, valores, aliases, propriedades e hierarquias alternativas


![Dimension Clear](/images/dimension_clear.png)



## Seleção de dimensão
### Especificar dimensão dinamicamente
Se as **dimensões** ou os **caminhos** foram criados dinamicamente, as mesmas variáveis podem ser usadas para limpá-los. Usar variáveis no processo de limpeza é útil porque elimina a necessidade de atualizar manualmente a etapa Dimension Clear de tempos em tempos.



Um exemplo que usa a variável `current_month` para limpar dinamicamente a dimensão Materials:

```text
/Dimensions/{current_month}/Products/Materials
```

### Usar dimensão específica

Use o menu suspenso para selecionar uma dimensão específica a ser limpa.
