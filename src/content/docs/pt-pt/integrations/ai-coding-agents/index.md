---
title: Agentes de IA (MCP)
description: Ligue o Claude, o Cursor, o GitHub Copilot, o Gemini e outros agentes de IA ao seu inquilino PlaidCloud através do servidor Model Context Protocol (MCP).
sidebar:
  label: Agentes de IA (MCP)
  order: 13
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/integrations/ai-coding-agents/index.md
---

O PlaidCloud expõe um servidor [Model Context Protocol](https://modelcontextprotocol.io) (MCP) selecionado em `/mcp` em cada área de trabalho. Os agentes de IA ligam-se a ele da mesma forma que se ligam a qualquer outro servidor MCP e depois chamam as ferramentas para ler projetos, executar fluxos de trabalho, consultar tabelas, gerir dimensões e muito mais.

As páginas desta secção abrangem o que o servidor expõe, como autenticar e a configuração passo a passo para os clientes de IA mais comuns. Para a arquitetura por trás deles — o caminho governado que cada pedido de IA percorre, como funciona a recuperação e como executar o seu próprio modelo — consulte [Arquitetura de IA e LLM](/pt-pt/integrations/ai-architecture/).

## O que distingue a análise de IA do PlaidCloud

- **[Respostas em que pode confiar](./honest-answers/)** — cada resposta traz um sinal de confiança e ressalvas em linguagem simples, e o PlaidCloud nunca inventa um número. Esta honestidade é o que permite agir com base numa resposta de IA sem a voltar a verificar manualmente.
- **[Rastrear alocações](./tracing-allocations/)** — pergunte *porque* é que um resultado alocado mudou, o que o alimenta e o que faria uma alteração hipotética — em linguagem simples.
- **[Caminhos de análise](./analysis-paths/)** — dê às suas tabelas principais nomes simples e uma predefinição, para poder perguntar simplesmente "porque é que isto subiu no último trimestre?"
- **[Criar painéis de controlo](./build-dashboards/)** — peça gráficos e painéis de controlo sobre as suas tabelas e vistas publicadas, através da mesma ligação ao PlaidCloud.
- **[Definições de indicadores](./metric-definitions/)** — acorde uma só vez como se calcula um número de negócio, para que todas as respostas que o utilizam sejam calculadas da mesma forma.

## Ligar o seu assistente

O caminho mais rápido é o item **Ligue a sua IA** no menu do avatar (utilizador) do próprio PlaidCloud — escolha o seu cliente e siga os passos apresentados, incluindo o URL do servidor MCP.

- [Introdução](./getting-started/) — o que o servidor MCP expõe e como autenticar.
- [Microsoft 365 Copilot](/pt-pt/integrations/microsoft-365-copilot/) — leve o PlaidCloud a toda a sua equipa no Teams e no Outlook.
- Configuração por cliente: [Claude Code](./claude-code/), [Claude Desktop](./claude-desktop/), [Cursor](./cursor/), [GitHub Copilot](./copilot/), [Gemini](./gemini/), [ChatGPT](./chatgpt/), [Grok](./grok/).
