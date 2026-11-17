---
title: Cursor
description: Skonfiguruj IDE Cursor, aby wywoływało narzędzia MCP PlaidCloud za pomocą wbudowanej obsługi MCP.
sidebar:
  order: 4
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/integrations/ai-coding-agents/cursor.md
---

[Cursor](https://cursor.com) obsługuje serwery MCP za pomocą pliku konfiguracyjnego `mcp.json`. Ma on taki sam kształt jak `.mcp.json` w Claude Code, więc ten sam fragment z tokenem okaziciela działa w obu.

Okno **Połącz swoją AI**, otwierane z menu awatara (użytkownika) PlaidCloud, oferuje jednokrokowy link **Install in Cursor**, który dodaje serwer przez logowanie OAuth, bez pliku konfiguracyjnego. Wypróbuj go w pierwszej kolejności. Konfiguracja z tokenem okaziciela poniżej to ustawienie w pełni opisane na tej stronie oraz rozwiązanie zapasowe, gdy jednokrokowy link nie doda serwera lub Cursor nie jest zainstalowany.

## Konfiguracja

1. Pobierz token okaziciela, otwierając `https://<your-workspace>.plaid.cloud/mcp/setup/token` w przeglądarce, w której logujesz się do PlaidCloud.

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

4. Otwórz **Settings → MCP** w Cursor, aby sprawdzić, czy serwer jest połączony. Jeśli wyświetla błąd, zobacz [Rozwiązywanie problemów](../troubleshooting/).

## Korzystanie z narzędzi

W Composerze lub panelu czatu Cursor możesz wydawać agentowi polecenia zwykłym językiem („opisz strukturę projektu `Q4 Forecast`”), a on wybierze odpowiednie narzędzie `plaidcloud_*`. Wywołania narzędzi i odpowiedzi pojawiają się w tekście — przed zatwierdzeniem sprawdź operacje modyfikujące.

## Odświeżanie tokenu

Gdy token wygaśnie, ponownie otwórz `https://<your-workspace>.plaid.cloud/mcp/setup/token` i wklej nową wartość do `mcp.json`. Cursor wykrywa zmianę bez pełnego restartu — w razie potrzeby wyłącz i włącz serwer w **Settings → MCP**.

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
