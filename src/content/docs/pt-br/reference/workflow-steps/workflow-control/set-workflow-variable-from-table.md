---
title: Etapa Set Workflow Variable Values from Table
description: Leia valores de uma tabela do projeto e atribua-os a variáveis do fluxo de trabalho, para que as etapas seguintes se ramifiquem ou filtrem com base em dados, e não em valores fixos no código.
sidebar:
  order: 16
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/workflow-control/set-workflow-variable-from-table.md
---

## Descrição

Lê valores de uma tabela do projeto e os atribui a variáveis do fluxo de trabalho. Use-a para conduzir um fluxo de trabalho a partir de seus próprios dados — leia o último período fechado, uma contagem de linhas ou um caminho de arquivo em uma tabela de controle e deixe as etapas seguintes referenciá-lo.

As variáveis definidas aqui existem durante a execução do fluxo de trabalho. Para definir valores que persistem entre os fluxos de trabalho do projeto, use [Set Project Variable Values from Table](/pt-br/reference/workflow-steps/workflow-control/set-project-variable-from-table/).

## Configuração

### Colunas de origem

Mapeie cada coluna de origem para a variável do fluxo de trabalho que ela preenche. A etapa lê uma única linha; portanto, reduza a tabela a uma linha antes de executá-la.

### Selecionar subconjunto de dados

Uma expressão de filtro que restringe as linhas de origem — normalmente à única linha que contém os valores desejados.

### Aplicar filtro secundário aos dados do resultado

Um filtro no estilo `HAVING` aplicado após a agregação, para quando o valor vem de um cálculo agrupado.

### Final Data Table Slicing (Limit)

Desativado por padrão e limitado a uma linha quando ativado. Ative-o com uma ordenação explícita quando a origem puder retornar várias linhas candidatas e você quiser uma específica.

## Relacionados

- [Etapas de controle de fluxo de trabalho](/pt-br/reference/workflow-steps/workflow-control/)
- [Set Workflow Variable](/pt-br/reference/workflow-steps/workflow-control/set-workflow-variable/)
- [Set Project Variable Values from Table](/pt-br/reference/workflow-steps/workflow-control/set-project-variable-from-table/)
- [Gerenciar variáveis do fluxo de trabalho](/pt-br/guides/workflows/manage-workflow-variables/)
