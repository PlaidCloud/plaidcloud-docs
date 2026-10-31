---
title: Google Gemini CLI
description: Configure o gemini-cli da Google para chamar as ferramentas MCP do PlaidCloud.
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/integrations/ai-coding-agents/gemini.md
---

O [`gemini-cli`](https://github.com/google-gemini/gemini-cli) da Google suporta servidores MCP através de `~/.gemini/settings.json` (ao nível do utilizador) ou de `.gemini/settings.json` na raiz de um projeto (ao nível do projeto).

## Configuração

1. Obtenha um token de portador visitando `https://<your-workspace>.plaid.cloud/mcp/setup/token` num navegador em que tenha sessão iniciada no PlaidCloud.

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

3. Reinicie o `gemini`. Dentro de uma sessão, execute `/mcp` para verificar que o servidor está ligado e listar as suas ferramentas.

## Utilização

Peça ao Gemini que utilize diretamente as ferramentas do PlaidCloud:

- "Usa o plaidcloud para listar os fluxos de trabalho do projeto `Sales Forecasting`."
- "Descreve as colunas da tabela `customers` e o instantâneo mais recente."

Também pode chamar ferramentas explicitamente com o comando `/tools` se quiser inspecionar o esquema de entrada de uma ferramenta específica antes de a invocar.

## Atualizar o token

Quando o token expirar, recarregue `https://<your-workspace>.plaid.cloud/mcp/setup/token` e atualize o valor de `Authorization` em `settings.json`. Reinicie o `gemini` para aplicar a alteração.

## Gemini Code Assist (IDE)

O Gemini Code Assist no VSCode/JetBrains aceita a mesma configuração `mcpServers` nas definições do respetivo agente. O esquema é igual ao da CLI — cole o mesmo excerto no painel de definições de servidores MCP do IDE.
