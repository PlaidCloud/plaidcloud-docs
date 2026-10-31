---
title: Cursor
description: Konfigurieren Sie die Cursor-IDE so, dass sie die MCP-Werkzeuge von PlaidCloud über ihre integrierte MCP-Unterstützung aufruft.
sidebar:
  order: 4
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/integrations/ai-coding-agents/cursor.md
---

[Cursor](https://cursor.com) unterstützt MCP-Server über die Konfigurationsdatei `mcp.json`. Die Struktur ist dieselbe wie bei der `.mcp.json` von Claude Code, sodass dasselbe Bearer-Token-Snippet in beiden funktioniert.

Das Fenster **Ihre KI verbinden** in der Kopf-Symbolleiste von PlaidCloud bietet einen Ein-Klick-Link **In Cursor installieren**, der den Server über eine OAuth-Anmeldung hinzufügt, ohne Konfigurationsdatei. Versuchen Sie zuerst diesen. Die Bearer-Token-Konfiguration unten ist die Einrichtung, die diese Seite vollständig dokumentiert, und die Rückfalloption, wenn der Ein-Klick-Link den Server nicht hinzufügt oder Cursor nicht installiert ist.

## Einrichtung

1. Besorgen Sie sich ein Bearer-Token, indem Sie `https://<your-workspace>.plaid.cloud/mcp/setup/token` in einem Browser aufrufen, in dem Sie bei PlaidCloud angemeldet sind.

2. Öffnen Sie die MCP-Konfiguration von Cursor:
   - **Projektbezogen**: Erstellen Sie `.cursor/mcp.json` im Stammverzeichnis Ihres Projekts.
   - **Benutzerbezogen (alle Projekte)**: Erstellen Sie `~/.cursor/mcp.json` in Ihrem Home-Verzeichnis.

3. Fügen Sie den PlaidCloud-Server hinzu:

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

4. Öffnen Sie **Einstellungen → MCP** in Cursor, um zu prüfen, ob der Server verbunden ist. Wird ein Fehler angezeigt, siehe [Fehlerbehebung](../troubleshooting/).

## Die Werkzeuge verwenden

Im Composer oder Chatfenster von Cursor können Sie den Agent in einfachem Deutsch auffordern („beschreibe die Struktur des Projekts `Q4 Forecast`“), und er wählt das passende `plaidcloud_*`-Werkzeug. Werkzeugaufrufe und Antworten erscheinen inline – prüfen Sie verändernde Vorgänge, bevor Sie genehmigen.

## Das Token aktualisieren

Wenn das Token abläuft, laden Sie `https://<your-workspace>.plaid.cloud/mcp/setup/token` neu und fügen Sie den neuen Wert in `mcp.json` ein. Cursor übernimmt die Änderung ohne vollständigen Neustart – schalten Sie den Server bei Bedarf unter **Einstellungen → MCP** aus und wieder ein.

## Mehrere Tenants

Wiederholen Sie den Eintrag unter einem anderen Namen:

```json
{
  "mcpServers": {
    "plaidcloud-prod": { "url": "https://prod.plaid.cloud/mcp", "headers": { "Authorization": "Bearer …" } },
    "plaidcloud-dev":  { "url": "https://dev.plaid.cloud/mcp",  "headers": { "Authorization": "Bearer …" } }
  }
}
```
