---
title: Google Gemini CLI
description: Configure o gemini-cli do Google para chamar as ferramentas MCP do PlaidCloud.
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/integrations/ai-coding-agents/gemini.md
---

O [`gemini-cli`](https://github.com/google-gemini/gemini-cli) do Google oferece suporte a servidores MCP por meio de `~/.gemini/settings.json` (escopo do usuário) ou `.gemini/settings.json` na raiz de um projeto (escopo do projeto).

## Configuração

1. Obtenha um token de portador acessando `https://<your-workspace>.plaid.cloud/mcp/setup/token` em um navegador em que você esteja conectado ao PlaidCloud.

2. Edite `~/.gemini/settings.json` (crie-o se não existir):

    ```json
    {
      "mcpServers": {
        "plaidcloud": {
          "httpUrl": "https://<your-workspace>.plaid.cloud/mcp",
          "headers": {
            "Authorization": "Bearer eyJhbGc…"
          }
        }
      }
    }
    ```

3. Reinicie o `gemini`. Dentro de uma sessão, execute `/mcp` para verificar se o servidor está conectado e listar suas ferramentas.

## Uso

Peça ao Gemini que use as ferramentas do PlaidCloud diretamente:

- "Use o plaidcloud para listar os fluxos de trabalho do projeto `Sales Forecasting`."
- "Descreva as colunas da tabela `customers` e o instantâneo mais recente."

Você também pode chamar ferramentas explicitamente com o comando `/tools` se quiser inspecionar o esquema de entrada de uma ferramenta específica antes de invocá-la.

## Atualização do token

Quando o token expirar, recarregue `https://<your-workspace>.plaid.cloud/mcp/setup/token` e atualize o valor de `Authorization` em `settings.json`. Reinicie o `gemini` para aplicar a alteração.

## Gemini Code Assist (IDE)

O Gemini Code Assist no VSCode/JetBrains aceita a mesma configuração `mcpServers` nas configurações de agente. O esquema é igual ao da CLI — cole o mesmo trecho no painel de configurações de servidor MCP da IDE.
