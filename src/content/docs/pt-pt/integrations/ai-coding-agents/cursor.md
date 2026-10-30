---
title: Cursor
description: Configure o IDE Cursor para chamar as ferramentas MCP do PlaidCloud através do seu suporte MCP integrado.
sidebar:
  order: 4
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/integrations/ai-coding-agents/cursor.md
---

O [Cursor](https://cursor.com) suporta servidores MCP através de um ficheiro de configuração `mcp.json`. A estrutura é a mesma do `.mcp.json` do Claude Code, pelo que o mesmo excerto com token de portador funciona em ambos.

A janela **Ligue a sua IA** na barra de ferramentas do cabeçalho do PlaidCloud oferece uma ligação de um clique **Instalar no Cursor** que adiciona o servidor através de um início de sessão OAuth, sem necessidade de ficheiro de configuração. Experimente-a primeiro. A configuração com token de portador abaixo é a configuração que esta página documenta na íntegra, e a alternativa caso a ligação de um clique não adicione o servidor ou o Cursor não esteja instalado.

## Configuração

1. Obtenha um token de portador visitando `https://<your-workspace>.plaid.cloud/mcp/setup/token` num navegador em que tenha sessão iniciada no PlaidCloud.

2. Abra a configuração MCP do Cursor:
   - **Ao nível do projeto**: crie `.cursor/mcp.json` na raiz do projeto.
   - **Ao nível do utilizador (todos os projetos)**: crie `~/.cursor/mcp.json` na sua pasta pessoal.

3. Adicione o servidor PlaidCloud:

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

4. Abra **Settings → MCP** no Cursor para verificar que o servidor está ligado. Se mostrar um erro, consulte [Resolução de problemas](../troubleshooting/).

## Utilizar as ferramentas

No Composer ou no painel de conversação do Cursor, pode dar instruções ao agente em linguagem corrente ("descreve a estrutura do projeto `Q4 Forecast`") e ele escolherá a ferramenta `plaidcloud_*` adequada. As chamadas a ferramentas e as respostas aparecem em linha — reveja as operações que alteram dados antes de aprovar.

## Atualizar o token

Quando o token expirar, recarregue `https://<your-workspace>.plaid.cloud/mcp/setup/token` e cole o novo valor em `mcp.json`. O Cursor aplica a alteração sem reinício completo — desative e volte a ativar o servidor em **Settings → MCP**, se necessário.

## Vários inquilinos

Repita a entrada com um nome diferente:

```json
{
  "mcpServers": {
    "plaidcloud-prod": { "url": "https://prod.plaid.cloud/mcp", "headers": { "Authorization": "Bearer …" } },
    "plaidcloud-dev":  { "url": "https://dev.plaid.cloud/mcp",  "headers": { "Authorization": "Bearer …" } }
  }
}
```
