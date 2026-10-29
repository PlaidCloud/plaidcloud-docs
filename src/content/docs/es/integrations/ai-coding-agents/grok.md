---
title: Grok
description: Conecte Grok de xAI al servidor MCP de PlaidCloud mediante sus conectores personalizados.
sidebar:
  order: 8
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/integrations/ai-coding-agents/grok.md
---

[Grok](https://grok.com) admite servidores MCP mediante conectores personalizados, que se configuran en grok.com.

## Configuración

1. Vaya a [grok.com/connectors](https://grok.com/connectors) y haga clic en **New Connector → Custom**.
2. Pegue la URL del servidor MCP: `https://<your-workspace>.plaid.cloud/mcp`.
3. Complete el inicio de sesión cuando Grok le redirija a PlaidCloud. Verá una página **Application Access Request** que indica la aplicación solicitante y el URI de redirección al que enviará las credenciales; compruebe que ambos corresponden a Grok antes de aprobar.

## Planes para empresas

Los espacios de trabajo Business y Enterprise canalizan la configuración de conectores a través de un administrador del equipo: un administrador del espacio de trabajo aprovisiona el conector en grok.com/connectors y, después, los miembros conectan su propia cuenta a él.

## Renovar el acceso

Si Grok indica que la conexión necesita volver a autorizarse, repita el paso de inicio de sesión: el conector conserva su URL, por lo que no necesita volver a agregarlo desde cero.
