---
title: Łącznik Xero REST
description: Skonfiguruj połączenie Xero w PlaidCloud za pomocą autoryzacji OAuth jednym kliknięciem, importuj jednostki Accounting API i księguj zapisy ręczne, faktury, rachunki, płatności oraz noty kredytowe.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/xero.md
---

## Dokumentacja API

[Dokumentacja Accounting API](https://developer.xero.com/documentation/api/accounting/overview) firmy Xero opisuje jednostki, filtry `where=` i ładunki tworzenia używane przez ten łącznik.

## Jak działa uwierzytelnianie

Połączenie uwierzytelnia się przez autoryzację **OAuth 2.0** Xero. PlaidCloud sam rejestruje aplikację OAuth, więc nie trzeba uzyskiwać ani wpisywać identyfikatora klienta ani klucza tajnego klienta — klikasz **Połącz z Xero**, logujesz się do Xero i zatwierdzasz autoryzację. PlaidCloud zapisuje uzyskane tokeny w połączeniu i odświeża je za Ciebie, zapisując każdy rotowany token odświeżania, dzięki czemu długo nieużywane połączenie nadal działa.

Jedna autoryzacja obejmuje każdą organizację Xero, dla której ją zatwierdzisz. Połączenie dotyczy dokładnie jednej z nich: selektor **Organizacja** wyświetla organizacje zwrócone przez autoryzację, a każde żądanie zawiera identyfikator tenanta tej organizacji. Aby odczytywać dane z drugiej organizacji lub księgować w niej, utwórz drugie połączenie Xero i wybierz w nim tę organizację.

Firma demonstracyjna Xero (Demo Company) jest właściwością organizacji, a nie ustawieniem połączenia — organizacja demonstracyjna pojawia się na liście **Organizacja** jak każda inna, więc połączenie piaskownicy to połączenie wskazujące na nią.

## Konfiguracja

| Pole | Typ | Opis |
|---|---|---|
| Name | Tekst | Wyświetlana nazwa tego połączenia. |
| Połącz z Xero | Przycisk | Rozpoczyna proces logowania i zgody w Xero. |
| Stan połączenia | Stan | Wyświetla `Not connected` do czasu zakończenia autoryzacji, a potem podaje, ile organizacji obejmuje. |
| Organizacja | Lista wyboru | Organizacja Xero, z której to połączenie odczytuje dane i w której księguje. Wypełniana na podstawie autoryzacji. |

## Limity szybkości

Xero ogranicza każdą organizację do 60 wywołań na minutę i 5000 wywołań dziennie, z limitem 5 równoczesnych wywołań. PlaidCloud zarządza limitami na minutę i równoległości osobno dla każdego połączenia, więc ograniczanie jednej organizacji nigdy nie wstrzymuje wywołań innego połączenia, i respektuje nagłówek `Retry-After` Xero w odpowiedzi ograniczającej. Limit dzienny pozostaje po Twojej stronie — planuj duże pobrania w harmonogramie zamiast uruchamiać wiele naraz.

## Jednostki dostępne do importu

Krok **Xero: importuj encję** obejmuje jedenaście jednostek Accounting API: `accounts`, `contacts`, `invoices`, `credit_notes`, `payments`, `manual_journals`, `bank_transactions`, `items`, `tracking_categories`, `tax_rates` i `currencies`. Każde pobranie przyjmuje opcjonalne zawężenie według statusu, zakres dat i datę graniczną ostatniej modyfikacji. Pełny opis pól znajdziesz w [Xero: importuj encję](/pl/reference/workflow-steps/xero/import-xero-entity/).

## Księgowanie dokumentów

Krok **Xero: zaksięguj dokument** księguje zapisy ręczne, faktury, rachunki, płatności i noty kredytowe przez wspólny potok zapisu ERP PlaidCloud, na podstawie tabeli nagłówków i tabeli wierszy. Opis pól znajdziesz w [Xero: zaksięguj dokument](/pl/reference/workflow-steps/xero/xero-post/), a pełny opis księgowania w [Połączenie z Xero](/pl/guides/connections/xero/).

## Znane ograniczenia

| Ograniczenie | Co oznacza |
|---|---|
| Zapisów ręcznych i płatności nie można wyszukać po niejednoznacznym wyniku | Faktury, rachunki i noty kredytowe mają numer dokumentu, który PlaidCloud nadaje i może go odpytać. Opis zapisu ręcznego i numer referencyjny płatności nie są dostępne do zapytań, więc wątpliwy zapis któregokolwiek z nich trafia do kwarantanny, aby go rozstrzygnąć w Xero, zamiast zgadywać. |
| Odwrócenie obejmuje tylko zapisy ręczne i faktury | Zapis ręczny jest odwracany jako zapis z zamienionymi stronami Wn/Ma; faktura jest odwracana przez lustrzaną notę kredytową. Rachunki, płatności i noty kredytowe nie mają udokumentowanego ładunku cofnięcia, więc PlaidCloud odmawia odwrócenia zamiast je wymyślać. |
| Filtry to stałe pola, a nie język zapytań | API zapytań Xero udostępnia dla każdej jednostki zawężenie według statusu i zakres dat, a nie otwarty język filtrów — dlatego krok importu oferuje te pola zamiast tabeli pole/operator/wartość. |
| Jedna organizacja na połączenie | Każde żądanie zawiera jeden identyfikator tenanta. Druga organizacja wymaga drugiego połączenia. |

## Powiązane

- [Połączenie z Xero (przewodnik)](/pl/guides/connections/xero/) — krok po kroku: utwórz połączenie, przetestuj je, zaimportuj jednostkę i zaksięguj dokument.
- [Xero: importuj encję](/pl/reference/workflow-steps/xero/import-xero-entity/)
- [Xero: zaksięguj dokument](/pl/reference/workflow-steps/xero/xero-post/)
- [Przegląd historii księgowań ERP](/pl/guides/connections/erp-post-history/)
