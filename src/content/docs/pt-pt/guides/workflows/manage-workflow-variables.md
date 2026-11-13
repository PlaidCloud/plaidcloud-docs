---
title: Gerir variáveis de fluxo de trabalho
description: Faça a gestão das variáveis de fluxo de trabalho no PlaidCloud para armazenar e transmitir valores dinâmicos entre passos, obtendo uma lógica de processamento de dados flexível.
sidebar:
  order: 14
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/manage-workflow-variables.md
---

O PlaidCloud permite variáveis tanto no âmbito do projeto como no âmbito do fluxo de trabalho. Isto permite definir variáveis para todo o projeto ou transmitir facilmente informação entre fluxos de trabalho. As variáveis e os valores são visualizados ao clicar no ícone de variáveis na hierarquia de **Fluxos de trabalho**.



A partir da tabela de variáveis pode ver as variáveis, os valores atuais e editar os valores. Também pode adicionar novas variáveis ou eliminar as existentes.

## Variáveis incorporadas

As definições e as expressões dos passos podem usar estas variáveis incorporadas sem as definir:

| Variável | Valor |
|---|---|
| `{project}`, `{model}`, `{cloud}` | Os nomes do projeto, do modelo e da área de trabalho. |
| `{date}` | A hora UTC atual da execução em formato extenso, como `Wednesday, 11 November 2026 10:30PM UTC +0`. |
| `{date_iso}` | O mesmo momento em ISO 8601, como `2026-11-12T22:49:56+00:00`. |

Use `{date_iso}` quando uma expressão precisar de ler parte da data. Os primeiros 7 carateres dão o mês (`2026-11`) e os primeiros 10 dão o dia (`2026-11-12`). `{date_iso}` funciona em todos os locais onde `{date}` funciona, incluindo os modelos de correio eletrónico de notificação e os passos Forecast, Parity e Solver.
