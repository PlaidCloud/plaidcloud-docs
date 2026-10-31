---
title: Set Project Variable Values from Table (passo)
description: Leia valores de uma tabela do projeto e atribua-os a variáveis do projeto que persistem entre execuções de fluxos de trabalho.
sidebar:
  order: 17
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/workflow-control/set-project-variable-from-table.md
---

## Descrição

Lê valores de uma tabela do projeto e atribui-os a variáveis do *projeto*. Ao contrário de [Set Workflow Variable Values from Table](/pt-pt/reference/workflow-steps/workflow-control/set-workflow-variable-from-table/), os valores persistem para além da execução — todos os fluxos de trabalho do projeto os veem até que algo volte a alterá-los.

Utilize-o para estado que sobrevive a uma única execução: o último período carregado com êxito, um carimbo de data/hora de marca-d'água ou o nome do cenário atual.

## Configuração

### Colunas de origem

Mapeie cada coluna de origem para a variável do projeto que preenche. O passo lê uma única linha, pelo que deve reduzir a tabela a uma linha antes da sua execução.

### Selecionar subconjunto de dados

Uma expressão de filtro que reduz as linhas de origem.

### Aplicar filtro secundário aos dados do resultado

Um filtro do tipo `HAVING` aplicado após a agregação.

### Final Data Table Slicing (Limit)

Desativado por predefinição e limitado a uma linha quando ativado. Ative-o com uma ordenação explícita quando a origem puder devolver várias linhas candidatas.

## Ver também

- [Passos de controlo do fluxo de trabalho](/pt-pt/reference/workflow-steps/workflow-control/)
- [Set Project Variable](/pt-pt/reference/workflow-steps/workflow-control/set-project-variable/)
- [Set Workflow Variable Values from Table](/pt-pt/reference/workflow-steps/workflow-control/set-workflow-variable-from-table/)
