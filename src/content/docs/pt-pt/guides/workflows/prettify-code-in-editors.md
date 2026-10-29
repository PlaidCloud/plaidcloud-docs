---
title: Embelezar (formatar) o código nos editores
description: Utilize o botão Embelezar ou Shift+Alt+F para formatar automaticamente código SQL, JSON e de expressões nos editores de passos de fluxos de trabalho do PlaidCloud.
sidebar:
  order: 12
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/prettify-code-in-editors.md
---

## Embelezar o código nos editores

Vários editores de passos de fluxos de trabalho utilizam um editor de código — os passos SQL (Frame Extract SQL, Remote Execute SQL, Remote Direct SQL, Remote Export SQL e Import SQL), o **Result schema** (JSON) do passo LLM e o Editor de expressões utilizado em toda a área de fluxos.

Cada um destes editores tem um botão **Embelezar** que reformata o código no local — indentando-o e dispondo-o de forma consistente para que seja mais fácil de ler e rever. Também pode premir **Shift+Alt+F** (**Shift+Option+F** no macOS) enquanto o cursor estiver no editor.

## O que é formatado

- **SQL** — reformatado numa disposição legível, em várias linhas: uma cláusula por linha, `CASE` / `WHEN` alinhados e funções aninhadas desdobradas. As variáveis de projeto e os tokens de modelo, como `{variable}`, `{{ ... }}` e `{% ... %}`, são preservados exatamente.
- **JSON** — reindentado com indentação de dois espaços (por exemplo, o Result schema do passo LLM).
- **Expressões** — as expressões do PlaidCloud são formatadas com a formatação padrão de Python: espaçamento consistente em torno dos operadores e das vírgulas, e quebras de linha nas expressões longas.

## O que deve saber

- Embelezar nunca altera o que o seu código faz — apenas a forma como está disposto. As palavras-chave e os identificadores de SQL mantêm a capitalização original.
- Se o código não puder ser analisado (um erro de sintaxe), Embelezar deixa-o intacto e mostra uma breve mensagem, pelo que nunca perde o seu trabalho.
- A formatação aplica-se como um único passo — prima **Ctrl+Z** (**Cmd+Z** no macOS) para a anular.
