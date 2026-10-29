---
title: Workflow Explorer
description: Use o Workflow Explorer do PlaidCloud para ver detalhes do fluxo de trabalho, configurações de etapas, histórico de execução e informações de dependência.
sidebar:
  order: 1.1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/workflow-explorer.md
---

Para ver os detalhes dentro de um fluxo de trabalho, encontre-o no projeto e clique duas vezes nele para abri-lo no explorador.

![Workflow Explorer](/images/workflow_explorer.png)

A partir daqui, você pode gerenciar as etapas do fluxo de trabalho, incluindo criar ou modificar etapas existentes, alterar a ordem, executar etapas e assim por diante.

## Criar uma etapa

Clique em **Criar etapa** e escolha um tipo de etapa. Se uma etapa estiver selecionada na lista, uma nova etapa Table Extract, Table Inner Join, Table Outer Join, Table Anti Join, Table Cross Join ou Table Lookup começa a partir da tabela que essa etapa grava: ela se torna a origem da nova etapa (**Table 1** em uma junção), e as colunas são preenchidas como **Inspecionar origem** as preencheria. Uma observação na parte inferior do formulário informa isso. Altere a origem se a nova etapa deve ler outra coisa. Nada é salvo até que você salve a etapa.
