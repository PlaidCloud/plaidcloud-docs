---
title: Konektor Oracle Fusion
description: Skonfiguruj w PlaidCloud połączenie z Oracle Fusion Cloud za pomocą danych uwierzytelniających OAuth2, aby importować salda księgi głównej i partie dziennika przez OData/BIP oraz księgować zapisy dziennika przez FBDI.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/erp/oracle-fusion.md
---

## Dokumentacja API

Dokumentacja [REST API (OData)](https://docs.oracle.com/en/cloud/saas/financials/) oraz [BI Publisher (BIP) i File-Based Data Import (FBDI)](https://docs.oracle.com/en/cloud/saas/applications-common/) Oracle Fusion Cloud opisuje punkty końcowe oraz ścieżkę zbiorczego wyodrębniania i ładowania, z których korzysta ten konektor.

## Jak działa uwierzytelnianie

Połączenie uwierzytelnia się za pomocą danych uwierzytelniających klienta OAuth2 (lub podstawowych danych uwierzytelniających API, które konfiguracja zabezpieczeń Fusion Cloud wystawia użytkownikom integracji) w ramach dedykowanego użytkownika API. Rola użytkownika API określa zarówno to, które jednostki księgi głównej może on odczytywać, jak i przez które funkcje FBDI/GL Interface może księgować.

## Konfiguracja

| Pole | Typ | Opis |
|---|---|---|
| Nazwa | Tekst | Nazwa wyświetlana tego połączenia. |
| Adres URL instancji | Tekst | Adres URL Twojej instancji Fusion Cloud, np. `https://yourorg.fa.us2.oraclecloud.com`. |
| Identyfikator klienta | Tekst | Identyfikator klienta OAuth2 użytkownika API (lub nazwa użytkownika, w przypadku uwierzytelniania podstawowego). |
| Klucz tajny klienta | Tekst | Klucz tajny klienta OAuth2 użytkownika API (lub hasło, w przypadku uwierzytelniania podstawowego). Przechowywany w postaci zaszyfrowanej. |

## Encje dostępne do importu

Dwa kroki importu obejmują różne wielkości pobierań, oba dla `gl_balances` i `journal_batches`:

- **Import Fusion Entity** (krok) — bezpośrednie wywołanie OData/BIP, do rutynowego, ograniczonego pobrania.
- **Import Fusion Bulk Extract** (krok) — asynchroniczne zadanie eksportu FBDI/BIP, do dużego wyodrębnienia.

Oba obsługują filtry zakresu (`ge`/`le`) na polach daty, okresu księgowego oraz numerycznych sald i kwot, a także filtry równości na polach dyskretnych, takich jak księga lub waluta. Pełną dokumentację pól znajdziesz w opisach kroków [Import Fusion Entity](/pl/reference/workflow-steps/oracle-fusion/import-fusion-entity/) i [Import Fusion Bulk Extract](/pl/reference/workflow-steps/oracle-fusion/import-fusion-bulk-extract/).

## Księgowanie zapisów dziennika

Krok **Oracle Fusion: Post Journal Entry** księguje partie dziennika księgi głównej przez wspólny potok zapisu ERP w PlaidCloud: zapisuje partię do tabeli pośredniej GL_INTERFACE Oracle jako plik FBDI, przesyła zadanie ESS Journal Import Launcher i odpytuje je do stanu końcowego, a przed zgłoszeniem partii jako zaksięgowanej potwierdza wynik. Korekta księguje nowy zapis odwracający, z zamienionymi stronami debetu i kredytu, zamiast edytować oryginał. Dokumentację pól znajdziesz w opisie kroku [Oracle Fusion: Post Journal Entry](/pl/reference/workflow-steps/oracle-fusion/oracle-fusion-post/), a pełny opis księgowania w [Połączenie z Oracle Fusion](/pl/guides/connections/oracle-fusion/).

## Znane ograniczenia

| Ograniczenie | Co to oznacza |
|---|---|
| Opóźnienie zadania ESS | Journal Import Launcher działa jako zadanie harmonogramowe, a nie wywołanie synchroniczne — uruchomienie księgowania trwa wyraźnie dłużej niż bezpośredni zapis przez API. |
| Opóźnienie wyodrębniania zbiorczego | `import_fusion_bulk_extract` czeka na zadanie eksportu FBDI/BIP — zarezerwuj go dla pobrań zbyt dużych dla bezpośredniej ścieżki `import_fusion_entity`. |
## Powiązane

- [Połączenie z Oracle Fusion (przewodnik)](/pl/guides/connections/oracle-fusion/) — krok po kroku: utwórz połączenie, przetestuj je, zaimportuj encję i zaksięguj zapis dziennika.
- [Import Fusion Entity](/pl/reference/workflow-steps/oracle-fusion/import-fusion-entity/) (krok)
- [Import Fusion Bulk Extract](/pl/reference/workflow-steps/oracle-fusion/import-fusion-bulk-extract/) (krok)
- [Oracle Fusion: Post Journal Entry](/pl/reference/workflow-steps/oracle-fusion/oracle-fusion-post/) (krok)
- [Przegląd historii księgowań ERP](/pl/guides/connections/erp-post-history/)
