---
title: Macro Run (passo)
description: Invoque um fluxo de trabalho de macro como uma subinvocação isolada, com associações de portas de entrada/saída declaradas — cada chamada é executada no seu próprio esquema temporário.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/workflow-control/run-macro.md
---

## Descrição

Invoca um fluxo de trabalho de [macro](/pt-pt/guides/workflows/create-a-macro/) como uma subinvocação com execução isolada. Ao contrário de [Executar fluxo de trabalho](/pt-pt/reference/workflow-steps/workflow-control/run-workflow/), cada chamada do passo Macro Run:

- Recebe um `run_id` novo e único.
- É executada no seu próprio esquema temporário efémero (`macrorun_<run_id>`) no catálogo do projeto.
- Associa as tabelas e variáveis do lado do chamador às portas de entrada declaradas da macro na cópia de entrada.
- Copia as tabelas de saída declaradas da macro para os destinos do lado do chamador em caso de êxito.
- Elimina sempre o esquema temporário quando a chamada termina (êxito, erro ou paragem).

Este isolamento torna seguro chamar a mesma macro em simultâneo — a partir de um ciclo principal, de fluxos de trabalho independentes executados ao mesmo tempo, ou recursivamente a partir de outra macro — sem colisões de nomes de tabelas intermédias entre execuções.

O fluxo de trabalho de destino tem de estar assinalado como macro. Um passo Macro Run que tenha como destino um fluxo de trabalho que não é macro falha com uma mensagem de erro clara; inversamente, um passo [Executar fluxo de trabalho](/pt-pt/reference/workflow-steps/workflow-control/run-workflow/) ou [Workflow Loop](/pt-pt/reference/workflow-steps/workflow-control/workflow-loop/) não pode ter uma macro como destino (esses passos não têm o ciclo de vida de isolamento por execução).

## Macro a executar

- **Projeto** — o projeto que contém a macro. Na v1, tem de ser o mesmo projeto do chamador.
- **Macro** — o fluxo de trabalho de macro a invocar. Depois de selecionada, as portas de entrada e de saída declaradas da macro preenchem as listas de associações abaixo.

## Associações de portas de entrada

Para cada porta de entrada declarada na macro, adicione uma associação. As associações são processadas em duas passagens — primeiro as entradas escalares / de dimensões (escritas na camada de variáveis da macro com âmbito de execução) e depois as entradas de tabelas — pelo que um filtro de entrada de tabela pode referenciar as entradas escalares.

**Portas de entrada de tabelas:**

- **Origem** — uma tabela do lado do chamador (por nome ou id) cujo conteúdo é copiado para o esquema temporário da macro com o nome da porta.
- **Colunas** — projeção opcional de colunas. Escolha um subconjunto e mude os nomes, se necessário (`source` → `target`); as colunas são delimitadas por aspas e aplicadas na cópia de entrada, pelo que apenas as colunas projetadas são materializadas.
- **Filtro** — cláusula `WHERE` opcional aplicada na cópia de entrada. Pode referenciar pelo nome as variáveis de entrada da macro (resolvidas a partir das associações escalares acima). Por exemplo, `month = {month}` restringe a cópia de entrada à fatia de um mês de uma tabela plurianual.

**Portas de entrada escalares / de dimensões:**

- **Variável** — o nome da variável do lado da macro a definir (corresponde a uma porta declarada na macro).
- **Valor** — o valor a associar, seja um literal ou uma referência a uma variável do lado do chamador (resolvida com base nas variáveis do chamador antes de ser escrita na camada da subinvocação).

## Associações de portas de saída

Para cada porta de saída declarada na macro, adicione uma associação que aponte para uma tabela de destino do lado do chamador. O destino é criado automaticamente se ainda não existir. A cópia de saída:

- Ocorre depois de a macro terminar com êxito (estado `done` ou `warn`).
- É **ignorada** se a macro for parada manualmente a meio (estado `stop`) — caso contrário, as saídas parciais acabariam silenciosamente no esquema duradouro do chamador.
- A projeção opcional de **colunas** funciona da mesma forma que nas associações de entrada.

## Comportamento em caso de falha

| Resultado da macro      | Efeito no lado do chamador                                                    |
|-------------------------|-------------------------------------------------------------------------------|
| `done` / `warn`         | Tabelas de saída copiadas para os destinos do chamador; esquema temporário eliminado. |
| `stop` (paragem manual) | Cópia de saída ignorada; esquema temporário eliminado; aviso registado no lado do chamador. |
| Erro a meio da execução | O passo Macro Run falha; esquema temporário eliminado; saídas não escritas.   |

Quando o fluxo de trabalho da macro falha, o registo do passo Macro Run mostra a mensagem de erro da própria macro («Child workflow run failed:» seguida da mensagem), para que possa ver o que corrigir sem abrir a execução da macro.

O esquema temporário é sempre recuperado num bloco `finally`, pelo que uma macro que falhe ou seja parada nunca deixa tabelas intermédias no esquema do projeto.

## Exemplos

Ainda não existem exemplos…

## Ver também

- [Criar uma macro](/pt-pt/guides/workflows/create-a-macro/) — declare um fluxo de trabalho como macro e defina o seu contrato de portas.
- [Executar fluxo de trabalho](/pt-pt/reference/workflow-steps/workflow-control/run-workflow/) — o chamador de subfluxos de trabalho sem isolamento (não pode ter uma macro como destino).
