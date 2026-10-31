---
title: Agentes de IA (MCP)
description: Conecte Claude, Cursor, GitHub Copilot, Gemini e outros agentes de IA ao seu tenant do PlaidCloud por meio do servidor Model Context Protocol (MCP).
sidebar:
  label: Agentes de IA (MCP)
  order: 13
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/integrations/ai-coding-agents/index.md
---

O PlaidCloud expõe um servidor [Model Context Protocol](https://modelcontextprotocol.io) (MCP) selecionado em `/mcp` em cada espaço de trabalho. Os agentes de IA se conectam a ele da mesma forma que a qualquer outro servidor MCP e, em seguida, chamam as ferramentas para ler projetos, executar fluxos de trabalho, consultar tabelas, gerenciar dimensões e muito mais.

As páginas desta seção abordam o que o servidor expõe, como autenticar e a configuração passo a passo dos clientes de IA mais comuns. Para conhecer a arquitetura por trás delas — o caminho governado que toda solicitação de IA percorre, como funciona a recuperação e como executar seu próprio modelo —, consulte [Arquitetura de IA e LLM](/pt-br/integrations/ai-architecture/).

## O que torna diferente a análise de IA do PlaidCloud

- **[Respostas em que você pode confiar](./honest-answers/)** — cada resposta traz um indicador de confiança e ressalvas em linguagem simples, e o PlaidCloud nunca inventa um número. Essa honestidade permite que você aja com base em uma resposta de IA sem precisar conferi-la manualmente.
- **[Rastreamento de alocações](./tracing-allocations/)** — pergunte *por que* um resultado alocado mudou, o que o alimenta e o que uma alteração hipotética causaria, tudo em linguagem simples.
- **[Caminhos de análise](./analysis-paths/)** — dê nomes amigáveis e um padrão às suas tabelas principais, para poder simplesmente perguntar "por que isso subiu no último trimestre?"
- **[Criar painéis](./build-dashboards/)** — peça gráficos e painéis sobre suas tabelas e visões publicadas, pela mesma conexão do PlaidCloud.
- **[Definições de métricas](./metric-definitions/)** — defina uma única vez como um número de negócio é calculado, para que toda resposta que o use seja calculada da mesma forma.

## Conecte seu assistente

O caminho mais rápido é o botão **Conecte sua IA** na barra de ferramentas do cabeçalho do próprio PlaidCloud: escolha seu cliente e siga as etapas exibidas, com a URL do servidor MCP já incluída.

- [Primeiros passos](./getting-started/) — o que o servidor MCP expõe e como autenticar.
- [Microsoft 365 Copilot](/pt-br/integrations/microsoft-365-copilot/) — leve o PlaidCloud para toda a sua equipe no Teams e no Outlook.
- Configuração por cliente: [Claude Code](./claude-code/), [Claude Desktop](./claude-desktop/), [Cursor](./cursor/), [GitHub Copilot](./copilot/), [Gemini](./gemini/), [ChatGPT](./chatgpt/), [Grok](./grok/).
