---
title: Konektor REST SAP S/4HANA Cloud
description: Skonfiguruj połączenie z SAP S/4HANA Cloud Public Edition w PlaidCloud, aby importować zestawienie obrotów i sald oraz pozycje zapisów dziennika przez OData i księgować zapisy dziennika przez SOAP.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/s4hana-cloud.md
---

## Dokumentacja API

[Interfejs Trial Balance API (`API_OPLACCTGDOCITEMCUBE_SRV`)](https://api.sap.com/) i [Journal Entry Item - Basic API (`API_JOURNALENTRYITEMBASIC_SRV`)](https://api.sap.com/) w SAP API Business Hub opisują punkty końcowe OData używane przez ten konektor, a także usługę SOAP do zbiorczego tworzenia zapisów dziennika udostępnianą przez Communication Arrangement.

## Jak działa uwierzytelnianie

Połączenie uwierzytelnia się jako aplikacja przy użyciu **poświadczeń klienta OAuth2** — identyfikator klienta i klucz tajny Communication Arrangement są wymieniane na token dostępu w punkcie końcowym tokenu OAuth2 tenanta. Nie ma interaktywnego logowania.

## Konfiguracja

| Pole | Typ | Opis |
|---|---|---|
| Nazwa | Tekst | Wyświetlana nazwa tego połączenia. |
| Host | Tekst | Host Twojego tenanta S/4HANA Cloud, np. `https://yourorg.s4hana.ondemand.com`. |
| Adres URL tokenu | Tekst | Punkt końcowy tokenu OAuth2 Communication Arrangement. |
| Identyfikator klienta | Tekst | Identyfikator klienta OAuth2 Communication Arrangement. |
| Klucz tajny klienta | Tekst | Klucz tajny klienta OAuth2 Communication Arrangement. Przechowywany w postaci zaszyfrowanej. |

## Encje dostępne do importu

Krok **Import S/4HANA Entity** obejmuje dwie encje: `trial_balance` (zagregowane salda kont księgi głównej na koniec okresu, przez `API_OPLACCTGDOCITEMCUBE_SRV`) oraz `journal_entry_items` (zaksięgowane pozycje zapisów dziennika, przez `API_JOURNALENTRYITEMBASIC_SRV`). Obie obsługują filtry po stronie serwera dla `CompanyCode`, `GLAccount`, `CostCenter`, `ProfitCenter`, `FiscalYear`, `FiscalPeriod` i `Ledger`, przy czym `PostingDate`, `FiscalYear` i `FiscalPeriod` akceptują granice zakresu `ge`/`le`. Pełny opis pól znajdziesz w opisie kroku [Import S/4HANA Entity](/pl/reference/workflow-steps/s4hana-cloud/import-s4hana-entity/).

## Księgowanie zapisów dziennika

Krok **S/4HANA: Post Journal Entry** księguje zapisy dziennika księgi głównej za pośrednictwem wspólnego potoku zapisu ERP w PlaidCloud: przesyła je przez usługę SOAP `JournalEntryBulkCreateRequest_In` w S/4HANA Cloud, odpytuje o potwierdzenie `JournalEntryBulkCreateConfirmation_Out` i weryfikuje je, zanim zgłosi zapis jako zaksięgowany. Korekta księguje nowy zapis storno z zamienionymi stronami debetu i kredytu, zamiast edytować oryginał. Opis pól znajdziesz w opisie kroku [S/4HANA: Post Journal Entry](/pl/reference/workflow-steps/s4hana-cloud/s4hana-post/), a pełny opis księgowania w artykule [Połączenie z SAP S/4HANA Cloud](/pl/guides/connections/s4hana-cloud/).

## Znane ograniczenia

| Ograniczenie | Co to oznacza |
|---|---|
| Opóźnienie potwierdzenia | Usługa SOAP do zbiorczego tworzenia przetwarza żądania asynchronicznie — wyraźnie wolniej niż synchroniczny zapis OData o tym samym rozmiarze. |
| Pola, które można filtrować, zależą od Twojego Communication Scenario | Obiekt kosztów lub wymiar, który nie jest udostępniony przez Twoje Communication Scenario, nie może być filtrowany po stronie serwera; ogranicz go w przepływie pracy po pobraniu. |
## Powiązane

- [Połączenie z SAP S/4HANA Cloud (przewodnik)](/pl/guides/connections/s4hana-cloud/) — krok po kroku: utwórz połączenie, przetestuj je, zaimportuj encję i zaksięguj dziennik.
- [Import S/4HANA Entity](/pl/reference/workflow-steps/s4hana-cloud/import-s4hana-entity/)
- [S/4HANA: Post Journal Entry](/pl/reference/workflow-steps/s4hana-cloud/s4hana-post/)
- [Przegląd historii księgowań ERP](/pl/guides/connections/erp-post-history/)
- [Konektor SAP ECC / S/4HANA](/pl/reference/connectors/erp/sap-s4/) — oddzielny konektor oparty na RFC i agencie, przeznaczony dla S/4HANA lokalnego lub w chmurze prywatnej.
