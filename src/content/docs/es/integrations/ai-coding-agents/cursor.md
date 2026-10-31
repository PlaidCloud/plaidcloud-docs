---
title: Cursor
description: Configure el IDE Cursor para que llame a las herramientas MCP de PlaidCloud mediante su compatibilidad integrada con MCP.
sidebar:
  order: 4
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/integrations/ai-coding-agents/cursor.md
---

[Cursor](https://cursor.com) admite servidores MCP mediante un archivo de configuración `mcp.json`. Su estructura es la misma que la del `.mcp.json` de Claude Code, así que el mismo fragmento con token de portador funciona en ambos.

La ventana **Conecte su IA** de la barra de herramientas del encabezado de PlaidCloud ofrece un enlace de un clic **Instalar en Cursor** que agrega el servidor mediante un inicio de sesión con OAuth, sin necesidad de un archivo de configuración. Pruebe eso primero. La configuración con token de portador que aparece a continuación es la que esta página documenta por completo, y es la alternativa si el enlace de un clic no agrega el servidor o Cursor no está instalado.

## Configuración

1. Obtenga un token de portador visitando `https://<your-workspace>.plaid.cloud/mcp/setup/token` en un navegador donde haya iniciado sesión en PlaidCloud.

2. Abra la configuración de MCP de Cursor:
   - **Ámbito de proyecto**: cree `.cursor/mcp.json` en la raíz de su proyecto.
   - **Ámbito de usuario (todos los proyectos)**: cree `~/.cursor/mcp.json` en su directorio de inicio.

3. Agregue el servidor de PlaidCloud:

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

4. Abra **Settings → MCP** en Cursor para verificar que el servidor esté conectado. Si muestra un error, consulte [Solución de problemas](../troubleshooting/).

## Uso de las herramientas

En el Composer o el panel de chat de Cursor, puede dar indicaciones al agente en lenguaje natural (“describe la estructura del proyecto `Q4 Forecast`”) y elegirá la herramienta `plaidcloud_*` adecuada. Las llamadas a herramientas y las respuestas aparecen en línea: revise las operaciones que modifican datos antes de aprobar.

## Actualización del token

Cuando el token caduque, vuelva a cargar `https://<your-workspace>.plaid.cloud/mcp/setup/token` y pegue el nuevo valor en `mcp.json`. Cursor detecta el cambio sin un reinicio completo; si es necesario, desactive y vuelva a activar el servidor en **Settings → MCP**.

## Varios inquilinos

Repita la entrada con un nombre distinto:

```json
{
  "mcpServers": {
    "plaidcloud-prod": { "url": "https://prod.plaid.cloud/mcp", "headers": { "Authorization": "Bearer …" } },
    "plaidcloud-dev":  { "url": "https://dev.plaid.cloud/mcp",  "headers": { "Authorization": "Bearer …" } }
  }
}
```
