---
title: Google Gemini CLI
description: Konfigurieren Sie die gemini-cli von Google so, dass sie die MCP-Werkzeuge von PlaidCloud aufruft.
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/integrations/ai-coding-agents/gemini.md
---

Die [`gemini-cli`](https://github.com/google-gemini/gemini-cli) von Google unterstützt MCP-Server über `~/.gemini/settings.json` (benutzerbezogen) oder `.gemini/settings.json` im Projektstamm (projektbezogen).

## Einrichtung

1. Besorgen Sie sich ein Bearer-Token, indem Sie `https://<your-workspace>.plaid.cloud/mcp/setup/token` in einem Browser aufrufen, in dem Sie bei PlaidCloud angemeldet sind.

2. Bearbeiten Sie `~/.gemini/settings.json` (erstellen Sie die Datei, falls sie nicht existiert):

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

3. Starten Sie `gemini` neu. Führen Sie in einer Sitzung `/mcp` aus, um zu prüfen, ob der Server verbunden ist, und um seine Werkzeuge aufzulisten.

## Verwendung

Fordern Sie Gemini auf, die PlaidCloud-Werkzeuge direkt zu verwenden:

- „Verwende plaidcloud, um die Workflows im Projekt `Sales Forecasting` aufzulisten.“
- „Beschreibe die Spalten der Tabelle `customers` und den neuesten Snapshot.“

Sie können Werkzeuge auch ausdrücklich mit dem Befehl `/tools` aufrufen, wenn Sie das Eingabeschema eines bestimmten Werkzeugs vor dem Aufruf prüfen möchten.

## Das Token aktualisieren

Wenn das Token abläuft, laden Sie `https://<your-workspace>.plaid.cloud/mcp/setup/token` neu und aktualisieren Sie den Wert von `Authorization` in `settings.json`. Starten Sie `gemini` neu, um die Änderung zu übernehmen.

## Gemini Code Assist (IDE)

Gemini Code Assist in VSCode/JetBrains akzeptiert dieselbe `mcpServers`-Konfiguration in seinen Agent-Einstellungen. Das Schema entspricht der CLI-Form – fügen Sie dasselbe Snippet im MCP-Server-Einstellungsbereich der IDE ein.
