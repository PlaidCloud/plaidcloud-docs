---
title: Ignorar passos num fluxo de trabalho
description: Ignore passos específicos num fluxo de trabalho do PlaidCloud para contornar operações durante testes, depuração ou execuções de processamento seletivas.
sidebar:
  order: 11
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/skip-steps-in-a-workflow.md
---

Os passos do fluxo de trabalho podem ser definidos para serem ignorados durante a execução. Isto pode ser útil se existirem passos de depuração ou passos antigos que ainda não está preparado para remover por completo do fluxo de trabalho.

Para definir esta opção, desmarque a caixa de verificação **Ativado** do passo na tabela do fluxo de trabalho. A alteração é guardada assim que clica, sem um Guardar separado. O passo deixa de ser executado como parte do fluxo de trabalho, mas continua a poder ser executado através do processo de execução de um único passo.



Os passos que foram definidos como desativados apresentam um indicador de desativado na tabela da hierarquia de passos do fluxo de trabalho.
