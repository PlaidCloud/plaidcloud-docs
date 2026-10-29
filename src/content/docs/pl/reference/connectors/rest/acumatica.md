---
title: Konektor REST Acumatica
description: Skonfiguruj połączenie z interfejsem REST API Acumatica opartym na kontraktach w PlaidCloud, aby importować dane główne i transakcyjne oraz księgować transakcje dziennika, faktury, rachunki i płatności.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/acumatica.md
---

## Dokumentacja API

[Interfejs REST API Acumatica oparty na kontraktach](https://help.acumatica.com/Help?ScreenId=ShowWiki&pageid=e0dea52d-0339-4f34-a6c0-9615ce6a25c2) opisuje punkty końcowe i opcje zapytań używane przez ten konektor.

## Jak działa uwierzytelnianie

Połączenie jest **oparte na sesji**: PlaidCloud loguje się raz na ograniczoną jednostkę pracy (`POST <instance>/entity/auth/login` z Twoją nazwą użytkownika, hasłem, firmą i opcjonalnym oddziałem) i używa uzyskanego pliku cookie sesji przy każdym wywołaniu w tej jednostce, a po zakończeniu wylogowuje się. Nie jest to przepływ z tokenem okaziciela ani OAuth — sesje wliczają się do limitu równoczesnych sesji licencji Acumatica, który w instancjach próbnych i niższych poziomach może wynosić zaledwie 2, dlatego unikaj uruchamiania wielu kroków Acumatica równolegle na jednym połączeniu.

## Konfiguracja

| Pole | Typ | Opis |
|---|---|---|
| Nazwa | Tekst | Wyświetlana nazwa tego połączenia. |
| Bazowy adres URL instancji | Tekst | Adres URL Twojej instancji Acumatica, np. `https://yourcompany.acumatica.com`. |
| Nazwa punktu końcowego | Tekst | Nazwa punktu końcowego kontraktu. `Default`, chyba że opublikowano niestandardowy punkt końcowy. |
| Wersja punktu końcowego | Tekst | Opcjonalnie, np. `25.200.001`. Pozostaw puste, aby użyć najnowszej opublikowanej wersji punktu końcowego. |
| Firma / tenant | Tekst | Dokładny identyfikator firmy Acumatica, do której loguje się to połączenie. |
| Oddział | Tekst | Opcjonalnie. Pozostaw puste, aby użyć domyślnego oddziału użytkownika logującego się. |
| Nazwa użytkownika | Tekst | Login użytkownika API PlaidCloud. |
| Hasło | Tekst | Hasło użytkownika API PlaidCloud. Przechowywane w postaci zaszyfrowanej. |

## Encje dostępne do importu

Krok **Import Acumatica Entity** obejmuje 18 encji opartych na kontraktach:

**Dane główne i referencyjne** — `account`, `subaccount`, `ledger`, `financial_period`, `branch`, `currency`, `currency_rate`, `customer`, `vendor`, `stock_item`, `warehouse`, `employee`, `tax_category`, `project`

**Dane transakcyjne** — `sales_invoice`, `bill`, `sales_order`, `shipment`

Każde pobranie obsługuje przełącznik `Active Only`, granicę `Updated After` oraz filtry po stronie serwera dla poszczególnych encji. Pełny opis pól znajdziesz w opisie kroku [Import Acumatica Entity](/pl/reference/workflow-steps/acumatica/import-acumatica-entity/).

## Księgowanie dokumentów

Krok **Acumatica Post** księguje dokumenty **JournalTransaction**, **SalesInvoice**, **Bill** i **Payment** za pośrednictwem wspólnego potoku zapisu ERP w PlaidCloud: tworzy dokument w stanie Hold, zwalnia go (akcja asynchroniczna) i potwierdza zwolnienie, zanim zgłosi dokument jako zaksięgowany. Opis pól znajdziesz w opisie kroku [Acumatica: Post Documents](/pl/reference/workflow-steps/acumatica/acumatica-post/), a pełny opis księgowania w artykule [Połączenie z Acumatica](/pl/guides/connections/acumatica/).

## Znane ograniczenia

| Ograniczenie | Co to oznacza |
|---|---|
| Brak obsługi odczytów zależnych od GI | Zestawienie obrotów i sald, szczegóły transakcji księgi głównej, stany magazynowe, budżety i dane międzyfirmowe są dostępne za pośrednictwem zapytań ogólnych (Generic Inquiries) Acumatica, a nie 18 encji opartych na kontraktach wymienionych powyżej. Utwórz zapytanie ogólne w Acumatica i pobierz je za pomocą [ogólnego połączenia REST](/pl/reference/connectors/rest/generic-rest/). |
| Brak natywnego klucza idempotentności przy zapisie | Interfejs zapisu Acumatica oparty na PUT nie ma pola idempotentności; jedynym zabezpieczeniem przed podwójnym zaksięgowaniem jest własne zajęcie księgi w PlaidCloud. |
| Storno wykonuje się ręcznie | Żaden typ dokumentu nie ma udokumentowanej akcji anulowania ani storna. Zaksięgowanego dokumentu nie można odwrócić z poziomu PlaidCloud — popraw go bezpośrednio w Acumatica. |
| Brak pola korelacji płatności | Acumatica nie udostępnia udokumentowanego pola do powiązania płatności z żądaniem PlaidCloud po niejednoznacznym wyniku; płatność w stanie niepewności trafia do kwarantanny w celu ręcznego rozstrzygnięcia. |
| Filtrowanie pozycji nie odbywa się po stronie serwera | Filtry w stylu `$filter` obejmują pola encji i nagłówka, ale nie wymiary pozycji dokumentu (na przykład centrum kosztów na poziomie pozycji). Ogranicz pozycje w przepływie pracy po pobraniu. |
## Powiązane

- [Połączenie z Acumatica (przewodnik)](/pl/guides/connections/acumatica/) — krok po kroku: utwórz połączenie, przetestuj je, zaimportuj encję i zaksięguj partię.
- [Import Acumatica Entity](/pl/reference/workflow-steps/acumatica/import-acumatica-entity/)
- [Acumatica: Post Documents](/pl/reference/workflow-steps/acumatica/acumatica-post/)
- [Przegląd historii księgowań ERP](/pl/guides/connections/erp-post-history/)
