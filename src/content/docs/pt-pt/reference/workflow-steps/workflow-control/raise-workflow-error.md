---
title: Gerar erro de fluxo de trabalho
description: Gere um erro personalizado num passo de fluxo de trabalho do PlaidCloud para acionar o tratamento de erros e interromper a execução quando as condições não são cumpridas.
sidebar:
  order: 10
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/workflow-control/raise-workflow-error.md
---

## Descrição

Força o fluxo de trabalho para um estado de erro com uma mensagem personalizada. Utilize-o quando um passo tiver de fazer falhar o fluxo de trabalho com base numa condição dos dados detetada por passos anteriores — por exemplo, «falhar se a contagem de linhas for zero», «falhar se uma tabela de validação de chaves tiver valores sem correspondência» ou «falhar se uma verificação de saldos não reconciliar».

Combine-o com [condições de passo](/pt-pt/guides/workflows/step-conditions/) para que o erro só seja acionado quando algo estiver realmente errado. Quando o passo é executado, interrompe de imediato o fluxo de trabalho e escreve o erro no registo do fluxo de trabalho, o que, por sua vez, pode acionar o fluxo de trabalho de correção, se estiver configurado um.


## Gerar erro de fluxo de trabalho


Destinado sobretudo a ser usado com condições de passo, o passo pode ser definido para ser executado se as condições forem cumpridas e gerar um erro no fluxo de trabalho.
