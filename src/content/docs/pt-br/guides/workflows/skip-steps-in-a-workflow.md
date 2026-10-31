---
title: Ignorar etapas em um fluxo de trabalho
description: Ignore etapas específicas em um fluxo de trabalho do PlaidCloud para pular operações durante testes, depuração ou execuções seletivas.
sidebar:
  order: 11
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/skip-steps-in-a-workflow.md
---

As etapas do fluxo de trabalho podem ser definidas para serem ignoradas durante a execução do fluxo de trabalho. Isso pode ser útil se houver etapas de depuração ou etapas antigas que você ainda não está pronto para remover completamente do fluxo de trabalho.

Para definir essa opção, desmarque a caixa de seleção **Ativado** da etapa na tabela do fluxo de trabalho. A alteração é salva assim que você clica, sem um Salvar separado. A etapa deixará de ser executada como parte do fluxo de trabalho, mas ainda poderá ser executada usando o processo de execução de etapa única.



As etapas definidas como desativadas terão um indicador de desativada na tabela da hierarquia de etapas do fluxo de trabalho.
