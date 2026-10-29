---
title: Cursor
description: Skonfiguruj IDE Cursor, aby wywoływało narzędzia MCP PlaidCloud przez wbudowaną obsługę MCP.
sidebar:
  order: 4
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/integrations/ai-coding-agents/cursor.md
---

[Cursor](https://cursor.com) obsługuje serwery MCP przez plik konfiguracyjny `mcp.json`. Jego postać jest taka sama jak `.mcp.json` w Claude Code, więc ten sam fragment z tokenem okaziciela działa w obu.

Okno **Połącz swoją AI** na pasku narzędzi nagłówka PlaidCloud oferuje jednoklikowy link **Install in Cursor**, który dodaje serwer przez logowanie OAuth, bez pliku konfiguracyjnego. Spróbuj najpierw tego. Poniższa konfiguracja z tokenem okaziciela jest konfiguracją w pełni udokumentowaną na tej stronie oraz rozwiązaniem awaryjnym, jeśli jednoklikowy link nie doda serwera lub Cursor nie jest zainstalowany.

## Konfiguracja

1. Uzyskaj token okaziciela, odwiedzając `https://<your-workspace>.plaid.cloud/mcp/setup/token` w przeglądarce, w której jesteś zalogowany do PlaidCloud.

2. Otwórz konfigurację MCP w Cursor:
   - **Zakres projektu**: utwórz `.cursor/mcp.json` w katalogu głównym projektu.
   - **Zakres użytkownika (wszystkie projekty)**: utwórz `~/.cursor/mcp.json` w katalogu domowym.

3. Dodaj serwer PlaidCloud:

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

4. Otwórz **Settings → MCP** w Cursor, aby sprawdzić, czy serwer jest połączony. Jeśli pokazuje błąd, zobacz [Rozwiązywanie problemów](../troubleshooting/).

## Korzystanie z narzędzi

W Composerze lub panelu czatu Cursor możesz wydawać agentowi polecenia zwykłym językiem („opisz strukturę projektu `Q4 Forecast`"), a on wybierze odpowiednie narzędzie `plaidcloud_*`. Wywołania narzędzi i odpowiedzi pojawiają się w tekście — przejrzyj operacje modyfikujące przed zatwierdzeniem.

## Odświeżanie tokenu

Gdy token wygaśnie, załaduj ponownie `https://<your-workspace>.plaid.cloud/mcp/setup/token` i wklej nową wartość do `mcp.json`. Cursor uwzględnia zmianę bez pełnego restartu — w razie potrzeby wyłącz i włącz serwer w **Settings → MCP**.

## Wiele dzierżaw

Powtórz wpis pod inną nazwą:

```json
{
  "mcpServers": {
    "plaidcloud-prod": { "url": "https://prod.plaid.cloud/mcp", "headers": { "Authorization": "Bearer …" } },
    "plaidcloud-dev":  { "url": "https://dev.plaid.cloud/mcp",  "headers": { "Authorization": "Bearer …" } }
  }
}
```
