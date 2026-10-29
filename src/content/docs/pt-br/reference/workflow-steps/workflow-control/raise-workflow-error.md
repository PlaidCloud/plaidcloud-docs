---
title: Etapa Gerar erro no fluxo de trabalho
description: Gere um erro personalizado em uma etapa de fluxo de trabalho do PlaidCloud para acionar o tratamento de erros e interromper a execução quando as condições não forem atendidas.
sidebar:
  order: 10
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/workflow-control/raise-workflow-error.md
---

## Descrição

Força o fluxo de trabalho a um estado de erro com uma mensagem personalizada. Use esta etapa quando for preciso fazer o fluxo de trabalho falhar com base em uma condição de dados detectada por etapas anteriores — por exemplo, "falhar se a contagem de linhas for zero", "falhar se uma tabela de validação de chaves tiver valores sem mapeamento" ou "falhar se uma verificação de saldo não fechar".

Combine-a com [condições de etapa](/pt-br/guides/workflows/step-conditions/) para que o erro só seja acionado quando algo realmente estiver errado. Quando a etapa é executada, ela interrompe o fluxo de trabalho imediatamente e grava o erro no log do fluxo de trabalho, o que, por sua vez, pode acionar o fluxo de trabalho de correção, se houver um configurado.


## Gerar erro no fluxo de trabalho


Voltada principalmente para uso com condições de etapa, a etapa pode ser configurada para ser executada quando as condições forem atendidas e gerar um erro dentro do fluxo de trabalho.
