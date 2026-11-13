---
title: Gerenciar variáveis de fluxo de trabalho
description: Gerencie variáveis de fluxo de trabalho no PlaidCloud para armazenar e passar valores dinâmicos entre etapas e obter uma lógica de processamento de dados flexível.
sidebar:
  order: 14
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/manage-workflow-variables.md
---

O PlaidCloud permite variáveis tanto no escopo do projeto quanto no escopo do fluxo de trabalho. Isso permite definir variáveis para todo o projeto ou passar informações facilmente entre fluxos de trabalho. As variáveis e seus valores são exibidos ao clicar no ícone de variáveis na hierarquia de **Fluxos de trabalho**.



Na tabela de variáveis, você pode ver as variáveis, os valores atuais e editar os valores. Você também pode adicionar novas variáveis ou excluir as existentes.

## Variáveis internas

As configurações e expressões das etapas podem usar estas variáveis internas sem defini-las:

| Variável | Valor |
|---|---|
| `{project}`, `{model}`, `{cloud}` | Os nomes do projeto, do modelo e do espaço de trabalho. |
| `{date}` | A hora UTC atual da execução em formato longo, como `Wednesday, 11 November 2026 10:30PM UTC +0`. |
| `{date_iso}` | O mesmo instante no formato ISO 8601, como `2026-11-12T22:49:56+00:00`. |

Use `{date_iso}` quando uma expressão precisar ler uma parte da data. Os 7 primeiros caracteres dão o mês (`2026-11`) e os 10 primeiros dão o dia (`2026-11-12`). `{date_iso}` funciona em todos os lugares em que `{date}` funciona, incluindo modelos de e-mail de notificação e as etapas Forecast, Parity e Solver.
