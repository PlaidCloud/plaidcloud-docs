---
title: Etapa Set Workflow Variable
description: Defina variáveis do fluxo de trabalho durante a execução em uma etapa de fluxo de trabalho do PlaidCloud para passar valores dinâmicos entre as etapas do seu fluxo de trabalho.
sidebar:
  order: 8
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/workflow-control/set-workflow-variable.md
---

## Descrição


“Set Workflow Variable” define variáveis do fluxo de trabalho para uso durante o fluxo de trabalho. O nome e o valor de uma variável podem conter qualquer combinação de caracteres válidos, inclusive espaços. As variáveis são referenciadas no fluxo de trabalho colocando-as entre chaves. Por exemplo, *a_variable* é referenciada em uma transformação como *\{a_variable}*, de modo que possa ser usada em algo como uma fórmula ou um valor de campo (por exemplo, \{a_variable} * 2).



## Lista de variáveis


A tabela lista todas as variáveis registradas no fluxo de trabalho, cada uma com seu **Valor atual** e seu **Memorando**, lidos novamente toda vez que você abre a etapa — assim, você vê o que uma variável contém agora antes de decidir qual valor atribuir a ela.

Para definir uma variável, marque **Definir** na linha dela e digite o novo valor em **Definir valor**. Somente as linhas marcadas são gravadas quando a etapa é executada; portanto, um valor digitado sem marcar **Definir** é ignorado. Também é possível definir uma variável que ainda não foi registrada: adicione uma linha e defina-a da mesma forma — a execução da etapa a cria.







## Exemplos

Ainda não há exemplos...
