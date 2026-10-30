---
title: Grok
description: Ligue o Grok da xAI ao servidor MCP do PlaidCloud através dos respetivos conectores personalizados.
sidebar:
  order: 8
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/integrations/ai-coding-agents/grok.md
---

O [Grok](https://grok.com) suporta servidores MCP através de conectores personalizados, configurados em grok.com.

## Configuração

1. Aceda a [grok.com/connectors](https://grok.com/connectors) e clique em **New Connector → Custom**.
2. Cole o URL do servidor MCP: `https://<your-workspace>.plaid.cloud/mcp`.
3. Conclua o início de sessão quando o Grok o redirecionar para o PlaidCloud. Verá uma página **Application Access Request** que indica a aplicação requerente e o URI de redirecionamento para onde enviará as credenciais — verifique se ambos correspondem ao Grok antes de aprovar.

## Planos empresariais

As áreas de trabalho Business e Enterprise encaminham a configuração de conectores através de um administrador da equipa: um administrador da área de trabalho disponibiliza o conector em grok.com/connectors e, depois disso, os membros ligam a sua própria conta a esse conector.

## Atualizar o acesso

Se o Grok indicar que a ligação necessita de nova autorização, repita o passo de início de sessão — o conector mantém o seu URL, pelo que não precisa de o adicionar novamente de raiz.
