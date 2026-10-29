---
title: Google Gemini CLI
description: Configure gemini-cli de Google para que llame a las herramientas MCP de PlaidCloud.
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/integrations/ai-coding-agents/gemini.md
---

[`gemini-cli`](https://github.com/google-gemini/gemini-cli) de Google admite servidores MCP mediante `~/.gemini/settings.json` (ámbito de usuario) o `.gemini/settings.json` en la raíz de un proyecto (ámbito de proyecto).

## Configuración

1. Obtenga un token de portador visitando `https://<your-workspace>.plaid.cloud/mcp/setup/token` en un navegador donde haya iniciado sesión en PlaidCloud.

2. Edite `~/.gemini/settings.json` (créelo si no existe):

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

3. Reinicie `gemini`. Dentro de una sesión, ejecute `/mcp` para verificar que el servidor esté conectado y enumerar sus herramientas.

## Uso

Pida a Gemini que use directamente las herramientas de PlaidCloud:

- “Usa plaidcloud para enumerar los flujos de trabajo del proyecto `Sales Forecasting`.”
- “Describe las columnas de la tabla `customers` y la instantánea más reciente.”

También puede llamar a las herramientas de forma explícita con el comando `/tools` si desea inspeccionar el esquema de entrada de una herramienta concreta antes de invocarla.

## Actualización del token

Cuando el token caduque, vuelva a cargar `https://<your-workspace>.plaid.cloud/mcp/setup/token` y actualice el valor de `Authorization` en `settings.json`. Reinicie `gemini` para que detecte el cambio.

## Gemini Code Assist (IDE)

Gemini Code Assist en VSCode/JetBrains acepta la misma configuración de `mcpServers` en los ajustes de su agente. El esquema coincide con el de la CLI: pegue el mismo fragmento en el panel de configuración de servidores MCP del IDE.
