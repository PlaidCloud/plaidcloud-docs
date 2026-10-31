---
title: Konektor REST Stripe
description: Skonfiguruj połączenie z interfejsem REST API Stripe w PlaidCloud, aby włączyć dane o przetwarzaniu płatności i dane finansowe do przepływów pracy.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/stripe.md
---

## Dokumentacja API
[Dokumentacja API dostawcy](https://docs.stripe.com/api) opisuje punkty końcowe tego konektora.

## Konfiguracja

Te pola są widoczne podczas tworzenia lub edytowania tego połączenia. To, które z nich są wymagane, zależy od włączonych opcji uwierzytelniania.

### Identyfikacja

| Pole | Typ | Opis |
|---|---|---|
| Nazwa | Tekst | Wyświetlana nazwa tego połączenia. |
| Alias | Tekst (wielowierszowy) | Opcjonalny alias lub uwagi dotyczące połączenia. |
| Aktywne | Przełącznik | Określa, czy połączenie jest włączone. Wyłącz, aby wstrzymać je bez usuwania. |

### Inne

| Pole | Typ | Opis |
|---|---|---|
| Host | Tekst | — |
| Typ uwierzytelniania | Lista wyboru | — |
| Włącz weryfikację SSL | Przełącznik | — |
| Podążaj za przekierowaniami | Przełącznik | — |
| Przekierowanie z zachowaniem metody HTTP | Przełącznik | — |
| Przekierowanie z zachowaniem uwierzytelniania | Przełącznik | — |
| Przekierowanie z usunięciem referera | Przełącznik | — |
| Ścisły parser HTTP | Przełącznik | — |
| Koduj adres URL | Przełącznik | Punkt końcowy adresu URL. |
| Wyłącz magazyn plików cookie | Przełącznik | — |
| Szyfr serwera | Przełącznik | — |
| Maksymalna liczba przekierowań | Liczba | — |
| Testowy punkt końcowy | Tekst | — |
| Testowa metoda | Lista wyboru | — |
