---
title: Workflow Explorer
description: Utilize o Workflow Explorer do PlaidCloud para ver detalhes do fluxo de trabalho, configurações de passos, histórico de execuções e informações de dependências.
sidebar:
  order: 1.1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/workflow-explorer.md
---

Para ver os detalhes de um fluxo de trabalho, localize-o no projeto e faça duplo clique nele para abrir o fluxo de trabalho no explorador.

![Vista do Workflow Explorer](/images/workflow_explorer.png)

A partir daqui, pode gerir os passos do fluxo de trabalho, incluindo criar ou modificar passos existentes, alterar a ordem, executar passos, etc.

## Criar um passo

Clique em **Criar passo** e escolha um tipo de passo. Se um passo estiver selecionado na lista, um novo passo Table Extract, Table Inner Join, Table Outer Join, Table Anti Join, Table Cross Join ou Table Lookup começa a partir da tabela que esse passo escreve: esta passa a ser a origem do novo passo (**Table 1** numa junção) e as colunas são preenchidas como **Inspecionar origem** as preencheria. Uma nota na parte inferior do formulário di-lo. Altere a origem se o novo passo deva ler outra coisa. Nada é guardado até guardar o passo.
