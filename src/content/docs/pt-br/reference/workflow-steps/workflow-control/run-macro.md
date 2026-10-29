---
title: Etapa Macro Run
description: Invoque um fluxo de trabalho Macro como uma subinvocação isolada, com vínculos de portas de entrada e saída declarados — cada chamada é executada em seu próprio esquema temporário.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/workflow-control/run-macro.md
---

## Descrição

Invoca um fluxo de trabalho [Macro](/pt-br/guides/workflows/create-a-macro/) como uma subinvocação isolada por execução. Diferentemente de [Executar fluxo de trabalho](/pt-br/reference/workflow-steps/workflow-control/run-workflow/), cada chamada de Macro Run:

- Recebe um `run_id` novo e exclusivo.
- É executada em seu próprio esquema temporário efêmero (`macrorun_<run_id>`) no catálogo do projeto.
- Vincula tabelas e variáveis do lado do chamador às portas de entrada declaradas da Macro na cópia de entrada.
- Copia as tabelas de saída declaradas da Macro de volta para os destinos do lado do chamador em caso de sucesso.
- Sempre descarta o esquema temporário quando a chamada termina (sucesso, erro ou interrupção).

Esse isolamento torna seguro chamar a mesma Macro de forma simultânea — a partir de um loop pai, de fluxos de trabalho independentes executados ao mesmo tempo ou recursivamente a partir de outra Macro — sem colisões de nomes de tabelas intermediárias entre execuções.

O fluxo de trabalho de destino deve estar marcado como Macro. Uma etapa Macro Run que aponta para um fluxo de trabalho que não é Macro falha com uma mensagem de erro clara; por outro lado, uma etapa [Executar fluxo de trabalho](/pt-br/reference/workflow-steps/workflow-control/run-workflow/) ou [Worklow Loop](/pt-br/reference/workflow-steps/workflow-control/workflow-loop/) não pode ter uma Macro como destino (essas etapas não possuem o ciclo de vida de isolamento por execução).

## Macro a executar

- **Projeto** — o projeto que contém a Macro. Deve ser o mesmo projeto do chamador na v1.
- **Macro** — o fluxo de trabalho Macro a invocar. As portas de entrada e saída declaradas da Macro preenchem as listas de vínculos abaixo depois de selecionada.

## Vínculos das portas de entrada

Para cada porta de entrada declarada na Macro, adicione um vínculo. Os vínculos são processados em duas passagens — primeiro as entradas escalares e de dimensão (gravadas na sobreposição de variáveis da Macro com escopo de execução) e depois as entradas de tabela — de modo que um filtro de entrada de tabela pode referenciar as entradas escalares.

**Portas de entrada de tabela:**

- **Origem** — uma tabela do lado do chamador (por nome ou id) cujo conteúdo é copiado para o esquema temporário da Macro com o nome da porta.
- **Colunas** — projeção de colunas opcional. Escolha um subconjunto e renomeie, se necessário (`source` → `target`); as colunas são entre aspas e aplicadas na cópia de entrada, de modo que somente as colunas projetadas são materializadas.
- **Filtro** — cláusula `WHERE` opcional aplicada na cópia de entrada. Pode referenciar pelo nome as variáveis de entrada da Macro (resolvidas a partir dos vínculos escalares acima). Por exemplo, `month = {month}` restringe a cópia de entrada à fatia de um mês de uma tabela de vários anos.

**Portas de entrada escalares / de dimensão:**

- **Variável** — o nome da variável do lado da Macro a definir (corresponde a uma porta declarada na Macro).
- **Valor** — o valor a vincular, seja um literal ou uma referência a uma variável do lado do chamador (resolvida com as variáveis do chamador antes de ser gravada na sobreposição da subinvocação).

## Vínculos das portas de saída

Para cada porta de saída declarada na Macro, adicione um vínculo que aponte para uma tabela de destino do lado do chamador. O destino é criado na hora se ainda não existir. A cópia de saída:

- Ocorre depois que a Macro termina com sucesso (estado `done` ou `warn`).
- É **ignorada** se a Macro for interrompida manualmente durante a execução (estado `stop`) — caso contrário, saídas parciais cairiam silenciosamente no esquema durável do chamador.
- A projeção opcional de **colunas** funciona da mesma forma que nos vínculos de entrada.

## Comportamento em caso de falha

| Resultado da Macro | Efeito no lado do chamador |
|-------------------------|-----------------------------------------------------------------------|
| `done` / `warn`         | Tabelas de saída copiadas para os destinos do chamador; esquema temporário descartado. |
| `stop` (interrupção manual)    | Cópia de saída ignorada; esquema temporário descartado; aviso registrado no log do chamador.      |
| Erro durante a execução           | A etapa Macro Run gera erro; esquema temporário descartado; saídas não gravadas.   |

Quando o fluxo de trabalho da Macro falha, o log da etapa Macro Run mostra a mensagem de erro da própria Macro (“Child workflow run failed:” seguida da mensagem), para que você veja o que corrigir sem abrir a execução da Macro.

O esquema temporário é sempre recuperado em um bloco `finally`, de modo que uma Macro que falhou ou foi interrompida nunca deixa tabelas intermediárias no esquema do projeto.

## Exemplos

Ainda não há exemplos…

## Relacionados

- [Criar uma Macro](/pt-br/guides/workflows/create-a-macro/) — declare um fluxo de trabalho como Macro e defina seu contrato de portas.
- [Executar fluxo de trabalho](/pt-br/reference/workflow-steps/workflow-control/run-workflow/) — o chamador de subfluxo de trabalho não isolado (não pode ter uma Macro como destino).
