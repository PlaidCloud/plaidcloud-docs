---
title: Executar um intervalo de etapas em um fluxo de trabalho
description: Execute um intervalo específico de etapas em um fluxo de trabalho do PlaidCloud para executar seletivamente partes do seu pipeline de processamento de dados.
sidebar:
  order: 8
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/running-a-range-of-steps-in-a-workflow.md
---

Embora executar etapas individuais seja útil, também pode ser útil executar subconjuntos de um fluxo de trabalho inteiro para desenvolvimento, teste ou solução de problemas. Para executar um subconjunto de etapas, selecione todas as etapas que você deseja executar e selecione **Executar etapa(s) selecionada(s)** no menu **Ações** na parte superior da hierarquia de etapas do fluxo de trabalho. Isso dispara um processamento normal do fluxo de trabalho, mas começa no início das etapas selecionadas e termina quando a última etapa selecionada é concluída.

Se a última etapa selecionada estiver dentro de um grupo definido como [**Execute in Parallel**](/pt-br/guides/workflows/controlling-parallel-execution/), a execução também aguarda a conclusão de todas as outras etapas selecionadas nesse grupo antes de terminar.
