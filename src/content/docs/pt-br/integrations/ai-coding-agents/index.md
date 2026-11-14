---
title: Agentes de IA (MCP)
description: Conecte o Claude, o Cursor, o GitHub Copilot, o Gemini e outros agentes de IA ao seu locatário do PlaidCloud por meio do servidor do Model Context Protocol (MCP).
sidebar:
  label: Agentes de IA (MCP)
  order: 13
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/integrations/ai-coding-agents/index.md
---

O PlaidCloud expõe um servidor curado do [Model Context Protocol](https://modelcontextprotocol.io) (MCP) em `/mcp` em todos os espaços de trabalho. Os agentes de IA se conectam a ele da mesma forma que a qualquer outro servidor MCP e depois chamam as ferramentas para ler projetos, executar fluxos de trabalho, consultar tabelas, gerenciar dimensões e muito mais.

As páginas desta seção abordam o que o servidor expõe, como autenticar e a configuração passo a passo para os clientes de IA mais comuns. Para ver a arquitetura por trás delas — o caminho governado que toda solicitação de IA percorre, como funciona a recuperação e como executar seu próprio modelo — consulte [Arquitetura de IA e LLM](/pt-br/integrations/ai-architecture/).

## O que torna a análise de IA do PlaidCloud diferente

- **[Respostas em que você pode confiar](./honest-answers/)** — toda resposta traz um indicador de confiança e ressalvas em linguagem simples, e o PlaidCloud nunca inventa um número. É essa honestidade que permite agir com base em uma resposta de IA sem conferi-la manualmente.
- **[Rastrear alocações](./tracing-allocations/)** — pergunte *por que* um resultado alocado mudou, o que o alimenta e o que uma alteração hipotética faria — em linguagem simples.
- **[Caminhos de análise](./analysis-paths/)** — dê nomes amigáveis e um padrão às suas tabelas principais, para poder simplesmente perguntar "por que isso subiu no último trimestre?"
- **[Criar painéis](./build-dashboards/)** — peça gráficos e painéis sobre suas tabelas e visões publicadas, pela mesma conexão do PlaidCloud.
- **[Definições de métricas](./metric-definitions/)** — combine uma única vez como um número de negócio é calculado, para que toda resposta que o use seja calculada da mesma forma.

## Conecte seu assistente

O caminho mais rápido é o item **Conecte sua IA** no próprio menu do avatar (usuário) do PlaidCloud — escolha seu cliente e siga as etapas exibidas, incluindo a URL do servidor MCP.

- [Primeiros passos](./getting-started/) — o que o servidor MCP expõe e como autenticar.
- [Microsoft 365 Copilot](/pt-br/integrations/microsoft-365-copilot/) — leve o PlaidCloud para toda a sua equipe no Teams e no Outlook.
- Configuração por cliente: [Claude Code](./claude-code/), [Claude Desktop](./claude-desktop/), [Cursor](./cursor/), [GitHub Copilot](./copilot/), [Gemini](./gemini/), [ChatGPT](./chatgpt/), [Grok](./grok/).
