---
title: Agentes de IA (MCP)
description: Ligue o Claude, o Cursor, o GitHub Copilot, o Gemini e outros agentes de IA ao seu inquilino do PlaidCloud através do servidor Model Context Protocol (MCP).
sidebar:
  label: Agentes de IA (MCP)
  order: 13
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/integrations/ai-coding-agents/index.md
---

O PlaidCloud expõe um servidor [Model Context Protocol](https://modelcontextprotocol.io) (MCP) selecionado em `/mcp` em cada área de trabalho. Os agentes de IA ligam-se-lhe da mesma forma que a qualquer outro servidor MCP e, depois, chamam as ferramentas para ler projetos, executar fluxos de trabalho, consultar tabelas, gerir dimensões e muito mais.

As páginas desta secção descrevem o que o servidor expõe, como autenticar e a configuração passo a passo para os clientes de IA mais comuns. Para a arquitetura subjacente — o caminho governado que cada pedido de IA percorre, como funciona a obtenção de informação e como executar o seu próprio modelo — consulte [Arquitetura de IA e LLM](/pt-pt/integrations/ai-architecture/).

## O que distingue a análise com IA do PlaidCloud

- **[Respostas em que pode confiar](./honest-answers/)** — cada resposta inclui um indicador de confiança e advertências em linguagem simples, e o PlaidCloud nunca inventa um número. É esta honestidade que lhe permite agir com base numa resposta de IA sem a voltar a verificar manualmente.
- **[Rastrear alocações](./tracing-allocations/)** — pergunte *porque* é que um resultado alocado mudou, o que o alimenta e o que faria uma alteração hipotética — em linguagem simples.
- **[Caminhos de análise](./analysis-paths/)** — atribua nomes amigáveis e uma predefinição às suas tabelas principais, para poder simplesmente perguntar "porque é que isto subiu no último trimestre?"
- **[Definições de indicadores](./metric-definitions/)** — acorde uma só vez como se calcula um número de negócio, para que todas as respostas que o utilizam o calculem da mesma forma.

## Ligar o seu assistente

O caminho mais rápido é o botão **Ligue a sua IA** na barra de ferramentas do cabeçalho do próprio PlaidCloud — escolha o seu cliente e siga os passos apresentados, incluindo o URL do servidor MCP.

- [Primeiros passos](./getting-started/) — o que o servidor MCP expõe e como autenticar.
- [Microsoft 365 Copilot](/pt-pt/integrations/microsoft-365-copilot/) — leve o PlaidCloud a toda a sua equipa no Teams e no Outlook.
- Configuração por cliente: [Claude Code](./claude-code/), [Claude Desktop](./claude-desktop/), [Cursor](./cursor/), [GitHub Copilot](./copilot/), [Gemini](./gemini/), [ChatGPT](./chatgpt/), [Grok](./grok/).
