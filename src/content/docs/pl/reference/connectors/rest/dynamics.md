---
title: Konektor REST Microsoft Dynamics 365
description: Skonfiguruj połączenie z interfejsem REST API Microsoft Dynamics w PlaidCloud, aby włączyć dane ERP i CRM do przepływów pracy analitycznych.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/dynamics.md
---

## Dokumentacja API
[Dokumentacja API dostawcy](https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/) opisuje punkty końcowe tego konektora.

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

### Inne

| Pole | Typ | Opis |
|---|---|---|
| Tenant Dynamics | Tekst | — |
| Identyfikator klienta OAuth2 | Tekst | — |
| Klucz tajny klienta OAuth2 | Tekst | Poufne dane uwierzytelniające — przechowywane w postaci zaszyfrowanej. |
| Dynamics CRM | Tekst | — |
