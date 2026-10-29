---
title: Dimension Create
description: Crie uma nova dimensão hierárquica em uma etapa de fluxo de trabalho do PlaidCloud para organizar e estruturar seu sistema de classificação de dados.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/dimensions/dimension-create.md
---

## Descrição
Cria uma dimensão para uso e carregamento


![Dimension Create](/images/dimension_create.png)

## Dimensão a criar
### Nome
Você pode usar um nome específico para a dimensão a ser criada ou incluir variáveis para nomeação dinâmica.


As variáveis são úteis quando as dimensões são atualizadas periodicamente e você quer manter a visão histórica.

Exemplo que usa a variável `current_month` para nomear a dimensão dinamicamente:

```text
dimension_name_{current_month}
```
### Caminho
Os caminhos permitem criar estruturas de pastas nas quais as dimensões são armazenadas. Você também pode usar variáveis aqui para tornar a estrutura de pastas dinâmica.
Exemplo que usa a variável `current_month` para nomear uma pasta dinamicamente:

```text
/Dimensions/{current_month}/Product/
```

### Memorando
O campo Memorando serve para armazenar comentários ou observações.
