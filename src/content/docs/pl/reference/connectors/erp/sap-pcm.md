---
title: Konektor SAP Profitability and Cost Management (PCM)
description: Skonfiguruj w PlaidCloud połączenie z SAP Profitability and Cost Management, aby włączyć do przepływów pracy dane alokacji kosztów.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/erp/sap-pcm.md
---

## Dokumentacja producenta
[Starsza dokumentacja SAP PCM](https://help.sap.com/docs/SAP_PROFITABILITY_AND_COST_MANAGEMENT).

## Konfiguracja

Te pola są widoczne podczas tworzenia lub edycji tego połączenia. To, które są wymagane, a które opcjonalne, zależy od włączonych opcji uwierzytelniania.

### Identyfikacja

| Pole | Typ | Opis |
|---|---|---|
| Nazwa | Tekst | Nazwa wyświetlana tego połączenia. |
| Alias | Tekst (wielowierszowy) | Opcjonalny alias lub uwagi o połączeniu. |
| Aktywne | Przełącznik | Określa, czy połączenie jest włączone. Wyłącz, aby wstrzymać je bez usuwania. |
| Baza danych tylko do odczytu | Przełącznik | Ogranicza połączenie do operacji tylko do odczytu. |
| Typ dostępu | Lista wyboru | Poziom dostępu dla tego połączenia: tylko odczyt, tylko zapis lub odczyt i zapis. |

### Uwierzytelnianie

| Pole | Typ | Opis |
|---|---|---|
| Użytkownik bazy danych | Tekst | Nazwa użytkownika do uwierzytelniania w bazie danych. |
| Użyj SSO | Przełącznik | Uwierzytelnianie za pomocą logowania jednokrotnego (SSO) zamiast nazwy użytkownika i hasła. |
| Hasło bazy danych | Hasło | Hasło do uwierzytelniania w bazie danych. |
