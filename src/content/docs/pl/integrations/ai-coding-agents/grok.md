---
title: Grok
description: Połącz Grok firmy xAI z serwerem MCP PlaidCloud za pomocą własnych łączników.
sidebar:
  order: 8
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/integrations/ai-coding-agents/grok.md
---

[Grok](https://grok.com) obsługuje serwery MCP za pomocą własnych łączników konfigurowanych na grok.com.

## Konfiguracja

1. Przejdź do [grok.com/connectors](https://grok.com/connectors) i kliknij **New Connector → Custom**.
2. Wklej adres URL serwera MCP: `https://<your-workspace>.plaid.cloud/mcp`.
3. Dokończ logowanie, gdy Grok przekieruje Cię do PlaidCloud. Zobaczysz stronę **Application Access Request** z nazwą aplikacji żądającej dostępu i adresem przekierowania, na który zostaną wysłane poświadczenia — przed zatwierdzeniem sprawdź, czy oba zgadzają się z Grok.

## Plany firmowe

W obszarach roboczych Business i Enterprise konfiguracja łącznika odbywa się przez administratora zespołu: administrator obszaru roboczego udostępnia łącznik na grok.com/connectors, a następnie członkowie łączą z nim własne konta.

## Odświeżanie dostępu

Jeśli Grok zgłosi, że połączenie wymaga ponownej autoryzacji, powtórz krok logowania — łącznik zachowuje swój adres URL, więc nie musisz dodawać go od nowa.
