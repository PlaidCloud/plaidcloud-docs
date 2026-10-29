---
title: Dimension Create
description: Crie uma nova dimensão hierárquica num passo de fluxo de trabalho do PlaidCloud para organizar e estruturar o seu sistema de classificação de dados.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/dimensions/dimension-create.md
---

## Descrição
Cria uma dimensão para utilização e carregamento


![Dimension Create](/images/dimension_create.png)

## Dimensão a criar
### Nome
Pode utilizar um nome específico para a dimensão a criar ou incluir variáveis para uma nomenclatura dinâmica.


As variáveis são úteis quando as dimensões são atualizadas periodicamente e se pretende manter a vista histórica.

Um exemplo que utiliza a variável `current_month` para dar um nome dinâmico à dimensão:

```text
dimension_name_{current_month}
```
### Caminho
Os caminhos permitem criar estruturas de pastas onde as dimensões são guardadas. Também pode utilizar variáveis aqui para tornar a estrutura de pastas dinâmica.
Um exemplo que utiliza a variável `current_month` para dar um nome dinâmico a uma pasta:

```text
/Dimensions/{current_month}/Product/
```

### Memorando
O campo Memorando serve para guardar comentários ou notas.
