---
title: Embelezar (formatar) código nos editores
description: Use o botão Embelezar ou Shift+Alt+F para formatar automaticamente código SQL, JSON e de expressões nos editores de etapas de fluxo de trabalho do PlaidCloud.
sidebar:
  order: 12
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/prettify-code-in-editors.md
---

## Embelezar código nos editores

Vários editores de etapas de fluxo de trabalho usam um editor de código — as etapas de SQL (Extrair SQL, Executar SQL remotamente, Remote Direct SQL, Remote Export SQL e Importar SQL), o **Result schema** (JSON) da etapa de LLM e o Editor de expressões usado em todas as áreas de fluxo.

Cada um desses editores tem um botão **Embelezar** que reformata o código no próprio local — indentando-o e organizando-o de forma consistente para facilitar a leitura e a revisão. Você também pode pressionar **Shift+Alt+F** (**Shift+Option+F** no macOS) enquanto o cursor estiver no editor.

## O que é formatado

- **SQL** — reformatado em um layout legível de várias linhas: uma cláusula por linha, `CASE` / `WHEN` alinhados e funções aninhadas desdobradas. Variáveis de projeto e tokens de modelo como `{variable}`, `{{ ... }}` e `{% ... %}` são preservados exatamente.
- **JSON** — reindentado com dois espaços (por exemplo, o Result schema da etapa de LLM).
- **Expressões** — as expressões do PlaidCloud são formatadas com a formatação padrão do Python: espaçamento consistente em torno de operadores e vírgulas e quebras de linha em expressões longas.

## O que você deve saber

- Embelezar nunca altera o que o seu código faz — apenas como ele é organizado. As palavras-chave e os identificadores do SQL mantêm a capitalização original.
- Se o código não puder ser analisado (um erro de sintaxe), Embelezar o deixa intacto e mostra uma mensagem breve, para que você nunca perca o seu trabalho.
- A formatação é aplicada como uma única ação — pressione **Ctrl+Z** (**Cmd+Z** no macOS) para desfazê-la.
