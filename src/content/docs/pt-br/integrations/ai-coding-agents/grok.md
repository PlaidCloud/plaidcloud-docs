---
title: Grok
description: Conecte o Grok, da xAI, ao servidor MCP do PlaidCloud por meio dos conectores personalizados.
sidebar:
  order: 8
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/integrations/ai-coding-agents/grok.md
---

O [Grok](https://grok.com) oferece suporte a servidores MCP por meio de conectores personalizados, configurados em grok.com.

## Configuração

1. Acesse [grok.com/connectors](https://grok.com/connectors) e clique em **New Connector → Custom**.
2. Cole a URL do servidor MCP: `https://<your-workspace>.plaid.cloud/mcp`.
3. Conclua o login quando o Grok redirecionar você ao PlaidCloud. Você verá uma página **Application Access Request** com o nome do aplicativo solicitante e o URI de redirecionamento para o qual ele enviará as credenciais. Confirme que ambos correspondem ao Grok antes de aprovar.

## Planos Empresariais

Os espaços de trabalho Business e Enterprise encaminham a configuração de conectores a um administrador da equipe: um administrador do espaço de trabalho provisiona o conector em grok.com/connectors e, depois disso, os membros conectam a própria conta a ele.

## Atualizando o Acesso

Se o Grok informar que a conexão precisa ser autorizada novamente, repita a etapa de login. O conector mantém a URL, então você não precisa adicioná-lo de novo do zero.
