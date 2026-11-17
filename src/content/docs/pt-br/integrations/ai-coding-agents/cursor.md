---
title: Cursor
description: Configure o Cursor IDE para chamar as ferramentas MCP do PlaidCloud por meio do suporte a MCP integrado dele.
sidebar:
  order: 4
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/integrations/ai-coding-agents/cursor.md
---

O [Cursor](https://cursor.com) oferece suporte a servidores MCP por meio de um arquivo de configuração `mcp.json`. O formato é o mesmo do `.mcp.json` do Claude Code, então o mesmo trecho com token de portador funciona nos dois.

A janela **Conecte sua IA**, aberta pelo menu do avatar (usuário) do PlaidCloud, oferece um link de um clique **Instalar no Cursor** que adiciona o servidor por meio de um login OAuth, sem precisar de arquivo de configuração. Tente isso primeiro. A configuração com token de portador abaixo é a que esta página documenta por completo, e serve de alternativa se o link de um clique não adicionar o servidor ou se o Cursor não estiver instalado.

## Configuração

1. Obtenha um token de portador acessando `https://<your-workspace>.plaid.cloud/mcp/setup/token` em um navegador no qual você esteja conectado ao PlaidCloud.

2. Abra a configuração de MCP do Cursor:
   - **No escopo do projeto**: crie `.cursor/mcp.json` na raiz do seu projeto.
   - **No escopo do usuário (todos os projetos)**: crie `~/.cursor/mcp.json` no seu diretório pessoal.

3. Adicione o servidor do PlaidCloud:

    ```json
    {
      "mcpServers": {
        "plaidcloud": {
          "url": "https://<your-workspace>.plaid.cloud/mcp",
          "headers": {
            "Authorization": "Bearer eyJhbGc…"
          }
        }
      }
    }
    ```

4. Abra **Settings → MCP** no Cursor para verificar se o servidor está conectado. Se ele mostrar um erro, consulte [Solução de problemas](../troubleshooting/).

## Usar as ferramentas

No Composer ou no painel de chat do Cursor, você pode dar comandos ao agente em português simples ("descreva a estrutura do projeto `Q4 Forecast`") e ele escolherá a ferramenta `plaidcloud_*` apropriada. As chamadas de ferramentas e as respostas aparecem em linha — revise as operações que alteram dados antes de aprovar.

## Atualizar o token

Quando o token expirar, recarregue `https://<your-workspace>.plaid.cloud/mcp/setup/token` e cole o novo valor em `mcp.json`. O Cursor percebe a alteração sem precisar ser reiniciado por completo — desative e ative o servidor em **Settings → MCP** se necessário.

## Vários locatários

Repita a entrada com um nome diferente:

```json
{
  "mcpServers": {
    "plaidcloud-prod": { "url": "https://prod.plaid.cloud/mcp", "headers": { "Authorization": "Bearer …" } },
    "plaidcloud-dev":  { "url": "https://dev.plaid.cloud/mcp",  "headers": { "Authorization": "Bearer …" } }
  }
}
```
