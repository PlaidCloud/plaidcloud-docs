---
title: Etapa Set Project Variable Values from Table
description: Leia valores de uma tabela do projeto e atribua-os a variáveis do projeto que persistem entre execuções de fluxos de trabalho.
sidebar:
  order: 17
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/workflow-control/set-project-variable-from-table.md
---

## Descrição

Lê valores de uma tabela do projeto e os atribui a variáveis do *projeto*. Diferentemente de [Set Workflow Variable Values from Table](/pt-br/reference/workflow-steps/workflow-control/set-workflow-variable-from-table/), os valores persistem além da execução — todo fluxo de trabalho do projeto os enxerga até que algo os altere novamente.

Use-a para estados que sobrevivem a uma única execução: o último período carregado com sucesso, um carimbo de data/hora de marca d'água ou o nome do cenário atual.

## Configuração

### Colunas de origem

Mapeie cada coluna de origem para a variável do projeto que ela preenche. A etapa lê uma única linha; portanto, reduza a tabela a uma linha antes de executá-la.

### Selecionar subconjunto de dados

Uma expressão de filtro que restringe as linhas de origem.

### Aplicar filtro secundário aos dados do resultado

Um filtro no estilo `HAVING` aplicado após a agregação.

### Final Data Table Slicing (Limit)

Desativado por padrão e limitado a uma linha quando ativado. Ative-o com uma ordenação explícita quando a origem puder retornar várias linhas candidatas.

## Relacionados

- [Etapas de controle de fluxo de trabalho](/pt-br/reference/workflow-steps/workflow-control/)
- [Set Project Variable](/pt-br/reference/workflow-steps/workflow-control/set-project-variable/)
- [Set Workflow Variable Values from Table](/pt-br/reference/workflow-steps/workflow-control/set-workflow-variable-from-table/)
