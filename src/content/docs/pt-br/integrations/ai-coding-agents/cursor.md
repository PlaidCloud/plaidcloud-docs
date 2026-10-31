---
title: Cursor
description: Configure a IDE Cursor para chamar as ferramentas MCP do PlaidCloud por meio do suporte a MCP integrado.
sidebar:
  order: 4
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/integrations/ai-coding-agents/cursor.md
---

O [Cursor](https://cursor.com) oferece suporte a servidores MCP por meio de um arquivo de configuração `mcp.json`. O formato é o mesmo do `.mcp.json` do Claude Code, então o mesmo trecho com token de portador funciona nos dois.

A janela **Conecte sua IA**, na barra de ferramentas do cabeçalho do PlaidCloud, oferece um link de um clique **Instalar no Cursor** que adiciona o servidor por meio de um login OAuth, sem precisar de arquivo de configuração. Experimente isso primeiro. A configuração com token de portador abaixo é a que esta página documenta por completo, e é a alternativa caso o link de um clique não adicione o servidor ou o Cursor não esteja instalado.

## Configuração

1. Obtenha um token de portador acessando `https://<your-workspace>.plaid.cloud/mcp/setup/token` em um navegador em que você esteja conectado ao PlaidCloud.

2. Abra a configuração de MCP do Cursor:
   - **No escopo do projeto**: crie `.cursor/mcp.json` na raiz do projeto.
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

4. Abra **Configurações → MCP** no Cursor para verificar se o servidor está conectado. Se aparecer um erro, veja [Solução de problemas](../troubleshooting/).

## Como usar as ferramentas

No Composer ou no painel de chat do Cursor, você pode dar instruções ao agente em linguagem natural ("descreva a estrutura do projeto `Q4 Forecast`") e ele escolherá a ferramenta `plaidcloud_*` apropriada. As chamadas de ferramentas e as respostas aparecem em linha — revise as operações que alteram dados antes de aprovar.

## Atualização do token

Quando o token expirar, recarregue `https://<your-workspace>.plaid.cloud/mcp/setup/token` e cole o novo valor no `mcp.json`. O Cursor reconhece a alteração sem uma reinicialização completa — desative e reative o servidor em **Configurações → MCP**, se necessário.

## Vários tenants

Repita a entrada com um nome diferente:

```json
{
  "mcpServers": {
    "plaidcloud-prod": { "url": "https://prod.plaid.cloud/mcp", "headers": { "Authorization": "Bearer …" } },
    "plaidcloud-dev":  { "url": "https://dev.plaid.cloud/mcp",  "headers": { "Authorization": "Bearer …" } }
  }
}
```
