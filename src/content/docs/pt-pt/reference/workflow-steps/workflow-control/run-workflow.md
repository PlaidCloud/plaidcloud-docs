---
title: Executar fluxo de trabalho
description: Execute um fluxo de trabalho existente a partir de um passo de fluxo de trabalho do PlaidCloud para encadear execuções de fluxos de trabalho e criar pipelines de processamento com vários fluxos de trabalho.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/workflow-control/run-workflow.md
---

## Descrição

Aciona outro fluxo de trabalho como parte da execução do fluxo de trabalho atual. Utilize-o para encadear fluxos de trabalho quando um processo depende logicamente de outro — por exemplo, um fluxo de trabalho de «fecho do mês» que chama um fluxo de trabalho «carregar valores reais», depois um fluxo de trabalho «executar alocações» e, por fim, um fluxo de trabalho «publicar painéis de controlo».

O fluxo de trabalho chamado é executado de forma independente — pode estar no mesmo projeto ou num diferente. Por predefinição, o fluxo de trabalho chamador continua sem esperar; ative a opção **Wait until processing completes** se os passos seguintes do chamador dependerem da conclusão do fluxo de trabalho chamado.



## Fluxo de trabalho a executar


Em primeiro lugar, selecione o projeto que contém o fluxo de trabalho a executar no menu pendente **Projeto**.



Em seguida, selecione o fluxo de trabalho em causa no menu pendente **Fluxo de trabalho**.



Existe ainda a opção **Wait until processing completes before continuing.** Ao selecionar esta caixa de verificação, a execução do fluxo de trabalho atual fica em espera até que o fluxo de trabalho chamado conclua a sua execução. Por predefinição, esta opção está desativada, o que significa que o fluxo de trabalho atual, onde esta transformação se encontra, continua a ser processado em paralelo com o fluxo de trabalho chamado.







## Exemplos

Ainda não existem exemplos...
