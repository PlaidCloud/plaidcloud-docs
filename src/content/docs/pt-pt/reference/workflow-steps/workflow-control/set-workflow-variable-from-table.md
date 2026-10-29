---
title: Set Workflow Variable Values from Table (passo)
description: Leia valores de uma tabela do projeto e atribua-os a variáveis do fluxo de trabalho, para que os passos seguintes ramifiquem ou filtrem com base em dados e não em valores fixos no código.
sidebar:
  order: 16
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/workflow-control/set-workflow-variable-from-table.md
---

## Descrição

Lê valores de uma tabela do projeto e atribui-os a variáveis do fluxo de trabalho. Utilize-o para conduzir um fluxo de trabalho a partir dos seus próprios dados — leia o último período fechado, uma contagem de linhas ou um caminho de ficheiro de uma tabela de controlo e deixe que os passos a jusante o referenciem.

As variáveis definidas aqui existem durante a execução do fluxo de trabalho. Para definir valores que persistem entre os fluxos de trabalho do projeto, utilize [Set Project Variable Values from Table](/pt-pt/reference/workflow-steps/workflow-control/set-project-variable-from-table/).

## Configuração

### Colunas de origem

Mapeie cada coluna de origem para a variável do fluxo de trabalho que preenche. O passo lê uma única linha, pelo que deve reduzir a tabela a uma linha antes da sua execução.

### Selecionar subconjunto de dados

Uma expressão de filtro que reduz as linhas de origem — normalmente à linha que contém os valores pretendidos.

### Aplicar filtro secundário aos dados do resultado

Um filtro do tipo `HAVING` aplicado após a agregação, para quando o valor provém de um cálculo agrupado.

### Final Data Table Slicing (Limit)

Desativado por predefinição e limitado a uma linha quando ativado. Ative-o com uma ordenação explícita quando a origem puder devolver várias linhas candidatas e pretender uma específica.

## Ver também

- [Passos de controlo do fluxo de trabalho](/pt-pt/reference/workflow-steps/workflow-control/)
- [Set Workflow Variable](/pt-pt/reference/workflow-steps/workflow-control/set-workflow-variable/)
- [Set Project Variable Values from Table](/pt-pt/reference/workflow-steps/workflow-control/set-project-variable-from-table/)
- [Gerir variáveis do fluxo de trabalho](/pt-pt/guides/workflows/manage-workflow-variables/)
