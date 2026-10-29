---
title: Konektor REST QuickBooks
description: Skonfiguruj połączenie z interfejsem REST API QuickBooks w PlaidCloud, aby włączyć dane księgowe i finansowe do przepływów pracy analitycznych.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/quickbooks.md
---

## Dokumentacja API
[Dokumentacja API dostawcy](https://developer.intuit.com/app/developer/qbo/docs/learn/explore-the-quickbooks-online-api) opisuje punkty końcowe tego konektora.

## Konfiguracja

Te pola są widoczne podczas tworzenia lub edytowania tego połączenia. To, które z nich są wymagane, zależy od włączonych opcji uwierzytelniania.

### Identyfikacja

| Pole | Typ | Opis |
|---|---|---|
| Nazwa | Tekst | Wyświetlana nazwa tego połączenia. |
| Alias | Tekst (wielowierszowy) | Opcjonalny alias lub uwagi dotyczące połączenia. |
| Aktywne | Przełącznik | Określa, czy połączenie jest włączone. Wyłącz, aby wstrzymać je bez usuwania. |
| Baza danych tylko do odczytu | Przełącznik | Ogranicza połączenie do operacji tylko do odczytu. |
| Typ dostępu | Lista wyboru | Poziom dostępu dla tego połączenia: tylko odczyt, tylko zapis lub odczyt i zapis. |
