---
title: Set Project Variable (passo)
description: Defina variáveis ao nível do projeto a partir de um passo de fluxo de trabalho do PlaidCloud para armazenar valores acessíveis a todos os fluxos de trabalho do projeto.
sidebar:
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/workflow-control/set-project-variable.md
---

## Descrição


«Set Project Variable» define variáveis do projeto para utilização durante o fluxo de trabalho. O nome e o valor de uma variável podem conter qualquer combinação de carateres válidos, incluindo espaços. As variáveis são referenciadas no fluxo de trabalho colocando-as entre chavetas. Por exemplo, *a_variable* é referenciada numa transformação como *\{a_variable}*, pelo que pode ser utilizada, por exemplo, numa fórmula ou no valor de um campo (por exemplo, \{a_variable} * 2).



## Lista de variáveis


A tabela lista todas as variáveis registadas no projeto, cada uma com o seu **Valor atual** e **Memorando**, lidos de novo sempre que abre o passo — para que possa ver o que uma variável contém neste momento antes de decidir o que lhe atribuir.

Para definir uma, assinale **Definir** na respetiva linha e introduza o novo valor em **Definir valor**. Apenas as linhas assinaladas são escritas quando o passo é executado, pelo que um valor introduzido sem assinalar **Definir** é ignorado. Também é possível definir uma variável que ainda não foi registada: adicione uma linha e defina-a da mesma forma — a execução do passo cria-a.







## Exemplos


Ainda não existem exemplos...
