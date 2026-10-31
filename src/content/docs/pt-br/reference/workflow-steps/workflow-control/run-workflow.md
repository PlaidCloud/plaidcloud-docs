---
title: Etapa Executar fluxo de trabalho
description: Execute um fluxo de trabalho existente a partir de uma etapa de fluxo de trabalho do PlaidCloud para encadear execuções e montar pipelines de processamento com vários fluxos de trabalho.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/workflow-control/run-workflow.md
---

## Descrição

Aciona outro fluxo de trabalho como parte da execução do fluxo de trabalho atual. Use esta etapa para encadear fluxos de trabalho quando um processo depende logicamente de outro — por exemplo, um fluxo de trabalho de "fechamento do mês" que chama um fluxo de trabalho "carregar valores realizados", depois um fluxo de trabalho "executar alocações" e, por fim, um fluxo de trabalho "publicar painéis".

O fluxo de trabalho chamado é executado de forma independente — ele pode estar no mesmo projeto ou em outro. Por padrão, o fluxo de trabalho chamador continua sem esperar; defina a opção **Wait until processing completes** se as próximas etapas do chamador dependerem da conclusão do fluxo de trabalho chamado.



## Fluxo de trabalho a executar


Primeiro, selecione o projeto que contém o fluxo de trabalho a ser executado no menu suspenso **Projeto**.



Em seguida, selecione o fluxo de trabalho específico a ser executado no menu suspenso **Fluxo de trabalho**.



Além disso, há a opção **Wait until processing completes before continuing.** Marcar essa caixa de seleção adia a execução do fluxo de trabalho atual até que o fluxo de trabalho chamado conclua a sua execução. Por padrão, essa opção está desativada, o que significa que o fluxo de trabalho atual, no qual esta transformação reside, continua o processamento em paralelo com o fluxo de trabalho chamado.







## Exemplos

Ainda não há exemplos...
