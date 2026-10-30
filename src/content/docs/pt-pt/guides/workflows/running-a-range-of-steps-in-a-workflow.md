---
title: Executar um intervalo de passos num fluxo de trabalho
description: Execute um intervalo específico de passos num fluxo de trabalho do PlaidCloud para processar seletivamente partes do seu pipeline de dados.
sidebar:
  order: 8
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/running-a-range-of-steps-in-a-workflow.md
---

Embora executar passos individuais seja útil, também pode ser útil executar subconjuntos de um fluxo de trabalho completo para desenvolvimento, teste ou resolução de problemas. Para executar um subconjunto de passos, selecione todos os passos que pretende executar e selecione **Executar passos selecionados** no menu **Ações** na parte superior da hierarquia de passos do fluxo de trabalho. Isto desencadeia um processamento normal do fluxo de trabalho, mas começa no início dos passos selecionados e termina quando o último passo selecionado estiver concluído.

Se o último passo selecionado estiver dentro de um grupo definido como [**Execute in Parallel**](/pt-pt/guides/workflows/controlling-parallel-execution/), a execução também aguarda que todos os outros passos selecionados nesse grupo terminem antes de parar.
