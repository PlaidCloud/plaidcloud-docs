---
title: Konektor REST Ramp
description: Skonfiguruj połączenie z interfejsem REST API Ramp w PlaidCloud, aby włączyć dane o wydatkach kartami firmowymi i kosztach do przepływów pracy.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/ramp.md
---

## Dokumentacja API
[Dokumentacja API dostawcy](https://docs.ramp.com/developer-api/v1) opisuje punkty końcowe tego konektora.

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
| Identyfikator klienta OAuth2 | Tekst | — |
| Klucz tajny klienta OAuth2 | Tekst | Poufne dane uwierzytelniające — przechowywane w postaci zaszyfrowanej. |
| Zakres Ramp | Tekst | — |
