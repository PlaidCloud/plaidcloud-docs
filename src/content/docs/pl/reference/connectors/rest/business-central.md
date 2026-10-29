---
title: Konektor REST Business Central
description: Skonfiguruj połączenie z Microsoft Dynamics 365 Business Central w PlaidCloud z użyciem poświadczeń klienta Azure AD, aby importować encje OData i księgować pozycje dziennika ogólnego.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/business-central.md
---

## Dokumentacja API

[Standardowy interfejs OData v2.0](https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/) Business Central opisuje encje oraz opcje `$filter`/`$orderby` używane przez ten konektor.

## Jak działa uwierzytelnianie

Połączenie uwierzytelnia się jako aplikacja przy użyciu **poświadczeń klienta (S2S)** Entra ID (Azure AD) — identyfikator klienta i klucz tajny rejestracji aplikacji są wymieniane na token dostępu pod adresem `https://login.microsoftonline.com/<tenant id>/oauth2/v2.0/token` z zakresem `https://api.businesscentral.dynamics.com/.default`. Nie ma interaktywnego logowania. Rejestracja aplikacji wymaga uprawnień API przyznanych dla Business Central (`API.ReadWrite.All` lub węższego zakresu wydanego przez administratora).

Każde żądanie dotyczy jednego **środowiska** (np. `Production` lub środowiska piaskownicy) oraz jednej **firmy** w nim — oba ustawienia są określone w połączeniu i nie są wybierane dla poszczególnych żądań.

## Konfiguracja

| Pole | Typ | Opis |
|---|---|---|
| Nazwa | Tekst | Wyświetlana nazwa tego połączenia. |
| Identyfikator klienta | Tekst | Identyfikator aplikacji (klienta) rejestracji aplikacji Entra. |
| Klucz tajny klienta | Tekst | Klucz tajny klienta rejestracji aplikacji. Przechowywany w postaci zaszyfrowanej. |
| ID tenanta | Tekst | Identyfikator Twojego tenanta Azure AD. |
| Środowisko | Tekst | Nazwa środowiska Business Central, np. `Production`. |
| Firma | Tekst | Identyfikator firmy Business Central, z której to połączenie odczytuje dane i w której księguje. |

## Encje dostępne do importu

Krok **Import Business Central Entity** obejmuje sześć encji: `accounts`, `generalLedgerEntries`, `customers`, `vendors`, `items`, `journals`. Każde pobranie obsługuje filtry po stronie serwera dla poszczególnych encji. Pełny opis pól znajdziesz w opisie kroku [Import Business Central Entity](/pl/reference/workflow-steps/business-central/import-business-central-entity/).

`generalLedgerEntries` jest tylko do odczytu i zawiera wyłącznie zapisy zaksięgowane — to encja, którą należy pobrać do zestawienia obrotów i sald lub szczegółów księgi głównej, ponieważ nigdy nie zawiera pozycji pozostających w niezaksięgowanej partii dziennika.

## Księgowanie pozycji dziennika ogólnego

Krok **Business Central Post** tworzy pozycje w **istniejącej** partii dziennika i księguje tę partię za pośrednictwem wspólnego potoku zapisu ERP w PlaidCloud; przed zaksięgowaniem sprawdza, czy partia zawiera wyłącznie pozycje z tego żądania, a zaksięgowanie potwierdza względem `generalLedgerEntries` (a nie samej partii dziennika). Opis pól znajdziesz w opisie kroku [Business Central: Post General Journal Lines](/pl/reference/workflow-steps/business-central/business-central-post/), a pełny opis księgowania w artykule [Połączenie z Business Central](/pl/guides/connections/business-central/).

## Znane ograniczenia

| Ograniczenie | Co to oznacza |
|---|---|
| Jeden typ dokumentu do zapisu | Obsługiwane jest wyłącznie księgowanie pozycji dziennika ogólnego. Przepływ dokumentów roboczych (faktury sprzedaży i zakupu, wersja robocza → zaksięgowany) nie jest obsługiwany — akcja księgowania dla tego przepływu nie jest określona w opublikowanej dokumentacji Microsoft. |
| Księgowanie tylko do istniejącej partii | Ten konektor nigdy nie tworzy partii dziennika w Business Central — utwórz ją tam wcześniej. |
| Równoczesne księgowanie do tej samej partii | Zabezpieczenie idempotentności obejmuje numer dokumentu, a nie partię dziennika — nie ma gwarancji, że dwa różne numery dokumentów księgowane równocześnie do tej samej partii zostaną zserializowane. |
## Powiązane

- [Połączenie z Business Central (przewodnik)](/pl/guides/connections/business-central/) — krok po kroku: utwórz połączenie, przetestuj je, zaimportuj encję i zaksięguj dziennik.
- [Import Business Central Entity](/pl/reference/workflow-steps/business-central/import-business-central-entity/)
- [Business Central: Post General Journal Lines](/pl/reference/workflow-steps/business-central/business-central-post/)
- [Przegląd historii księgowań ERP](/pl/guides/connections/erp-post-history/)
