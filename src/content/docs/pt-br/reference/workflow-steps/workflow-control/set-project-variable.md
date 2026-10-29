---
title: Etapa Set Project Variable
description: Defina variáveis em nível de projeto a partir de uma etapa de fluxo de trabalho do PlaidCloud para armazenar valores acessíveis a todos os fluxos de trabalho do projeto.
sidebar:
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/workflow-control/set-project-variable.md
---

## Descrição


“Set Project Variable” define variáveis do projeto para uso durante o fluxo de trabalho. O nome e o valor de uma variável podem conter qualquer combinação de caracteres válidos, inclusive espaços. As variáveis são referenciadas no fluxo de trabalho colocando-as entre chaves. Por exemplo, *a_variable* é referenciada em uma transformação como *\{a_variable}*, de modo que possa ser usada em algo como uma fórmula ou um valor de campo (por exemplo, \{a_variable} * 2).



## Lista de variáveis


A tabela lista todas as variáveis registradas no projeto, cada uma com seu **Valor atual** e seu **Memorando**, lidos novamente toda vez que você abre a etapa — assim, você vê o que uma variável contém agora antes de decidir qual valor atribuir a ela.

Para definir uma variável, marque **Definir** na linha dela e digite o novo valor em **Definir valor**. Somente as linhas marcadas são gravadas quando a etapa é executada; portanto, um valor digitado sem marcar **Definir** é ignorado. Também é possível definir uma variável que ainda não foi registrada: adicione uma linha e defina-a da mesma forma — a execução da etapa a cria.







## Exemplos


Ainda não há exemplos...
