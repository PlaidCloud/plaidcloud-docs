---
title: Google Gemini CLI
description: Skonfiguruj gemini-cli od Google, aby wywoływał narzędzia MCP PlaidCloud.
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/integrations/ai-coding-agents/gemini.md
---

[`gemini-cli`](https://github.com/google-gemini/gemini-cli) od Google obsługuje serwery MCP przez `~/.gemini/settings.json` (zakres użytkownika) lub `.gemini/settings.json` w katalogu głównym projektu (zakres projektu).

## Konfiguracja

1. Uzyskaj token okaziciela, odwiedzając `https://<your-workspace>.plaid.cloud/mcp/setup/token` w przeglądarce, w której jesteś zalogowany do PlaidCloud.

2. Edytuj `~/.gemini/settings.json` (utwórz go, jeśli nie istnieje):

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

3. Uruchom ponownie `gemini`. W sesji wykonaj `/mcp`, aby sprawdzić, czy serwer jest połączony, i wyświetlić jego narzędzia.

## Użycie

Poproś Gemini o bezpośrednie użycie narzędzi PlaidCloud:

- „Użyj plaidcloud, aby wyświetlić przepływy pracy w projekcie `Sales Forecasting`."
- „Opisz kolumny tabeli `customers` oraz jej najnowszą migawkę."

Możesz też wywoływać narzędzia jawnie poleceniem `/tools`, jeśli chcesz przejrzeć schemat wejściowy konkretnego narzędzia przed jego wywołaniem.

## Odświeżanie tokenu

Gdy token wygaśnie, załaduj ponownie `https://<your-workspace>.plaid.cloud/mcp/setup/token` i zaktualizuj wartość `Authorization` w `settings.json`. Uruchom ponownie `gemini`, aby uwzględnić zmianę.

## Gemini Code Assist (IDE)

Gemini Code Assist w VSCode/JetBrains akceptuje tę samą konfigurację `mcpServers` w ustawieniach agenta. Schemat odpowiada postaci CLI — wklej ten sam fragment w panelu ustawień serwerów MCP w IDE.
