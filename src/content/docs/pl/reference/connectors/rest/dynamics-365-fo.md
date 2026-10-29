---
title: Konektor REST Dynamics 365 Finance & Operations
description: Skonfiguruj połączenie z Dynamics 365 Finance & Operations w PlaidCloud, aby importować encje OData/DMF i asynchronicznie księgować zapisy dziennika.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/dynamics-365-fo.md
---

## Dokumentacja API

[Punkty końcowe OData v4](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/data-entities/odata) oraz [Data Management Framework](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/data-entities/data-management-import-export) w D365 F&O opisują punkty końcowe i ścieżkę zbiorczego wyodrębniania używane przez ten konektor.

## Jak działa uwierzytelnianie

Połączenie uwierzytelnia się jako aplikacja przy użyciu **poświadczeń klienta** Entra ID (Azure AD) — identyfikator klienta i klucz tajny rejestracji aplikacji są wymieniane na token dostępu z zakresem odpowiadającym zasobowi środowiska. Nie ma interaktywnego logowania.

## Konfiguracja

| Pole | Typ | Opis |
|---|---|---|
| Nazwa | Tekst | Wyświetlana nazwa tego połączenia. |
| Adres URL środowiska | Tekst | Adres URL Twojego środowiska D365 F&O, np. `https://yourorg.operations.dynamics.com`. |
| Identyfikator klienta | Tekst | Identyfikator aplikacji (klienta) rejestracji aplikacji Entra. |
| Klucz tajny klienta | Tekst | Klucz tajny klienta rejestracji aplikacji. Przechowywany w postaci zaszyfrowanej. |
| ID tenanta | Tekst | Identyfikator Twojego tenanta Azure AD. |
| Zasób/zakres | Tekst | Żądany zakres OAuth2, zwykle adres URL środowiska z dodanym `/.default`. |

## Encje dostępne do importu

Krok **Import D365 F&O Entity** obejmuje sześć encji: `main_accounts`, `currencies`, `customers`, `vendors`, `released_products`, `ledger_journal_headers`. Każde pobranie działa w trybie synchronizacji `odata` (wywołanie bezpośrednie, do rutynowych pobrań) lub w trybie zbiorczym `dmf` (asynchroniczne zadanie eksportu Data Management Framework, do dużych wyodrębnień) i obsługuje filtry po stronie serwera dla poszczególnych encji, w tym zakresy dat, kont i wymiarów. Pełny opis pól znajdziesz w opisie kroku [Import D365 F&O Entity](/pl/reference/workflow-steps/dynamics-365-fo/import-d365fo-entity/).

## Księgowanie zapisów dziennika

Krok **D365 F&O: Post Journal Entry** księguje zapisy dziennika księgi głównej za pośrednictwem wspólnego potoku zapisu ERP w PlaidCloud: przesyła je do asynchronicznej akcji księgowania dziennika w usłudze niestandardowej D365 F&O, odpytuje do osiągnięcia stanu końcowego i potwierdza wynik, zanim zgłosi zapis jako zaksięgowany. Korekta księguje nowy zapis storno z zamienionymi stronami debetu i kredytu, zamiast edytować oryginał. Opis pól znajdziesz w opisie kroku [D365 F&O: Post Journal Entry](/pl/reference/workflow-steps/dynamics-365-fo/dynamics-365-fo-post/), a pełny opis księgowania w artykule [Połączenie z Dynamics 365 Finance & Operations](/pl/guides/connections/dynamics-365-fo/).

## Znane ograniczenia

| Ograniczenie | Co to oznacza |
|---|---|
| Tryb synchronizacji DMF ma opóźnienie wyodrębniania | Pobranie w trybie `dmf` czeka na asynchroniczne zadanie eksportu — jest wyraźnie wolniejsze niż pobranie `odata` o tym samym rozmiarze. |
| Filtrowanie według wymiarów zależy od struktury | Wymiaru finansowego, który nie należy do struktury kont, nie można filtrować po stronie serwera; ogranicz go w przepływie pracy po pobraniu. |
## Powiązane

- [Połączenie z Dynamics 365 Finance & Operations (przewodnik)](/pl/guides/connections/dynamics-365-fo/) — krok po kroku: utwórz połączenie, przetestuj je, zaimportuj encję i zaksięguj dziennik.
- [Import D365 F&O Entity](/pl/reference/workflow-steps/dynamics-365-fo/import-d365fo-entity/)
- [D365 F&O: Post Journal Entry](/pl/reference/workflow-steps/dynamics-365-fo/dynamics-365-fo-post/)
- [Przegląd historii księgowań ERP](/pl/guides/connections/erp-post-history/)
