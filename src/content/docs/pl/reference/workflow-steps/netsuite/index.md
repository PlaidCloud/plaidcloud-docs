---
title: Kroki NetSuite
description: Kroki przepływu pracy NetSuite — import sald, szczegółów księgi głównej, danych podstawowych lub własnego zapytania SuiteQL oraz księgowanie zapisów dziennika przez połączenie NetSuite.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/netsuite/index.md
---

Kroki przepływu pracy, które odczytują dane z NetSuite i zapisują je do NetSuite przez [połączenie NetSuite](/pl/guides/connections/netsuite/). Gotowe kroki importu to najprostszy sposób pobierania typowych danych finansowych i referencyjnych — wybierasz połączenie, tabelę docelową oraz zakres dat lub typ rekordu, bez pisania SuiteQL.

## Kroki importu

- [NetSuite: importuj salda](/pl/reference/workflow-steps/netsuite/import-balances/) — salda kont (zestawienie obrotów i sald) dla zakresu dat i spółki zależnej.
- [NetSuite: importuj szczegóły księgi głównej](/pl/reference/workflow-steps/netsuite/import-gl-detail/) — szczegóły linii transakcji księgi głównej dla zakresu dat i spółki zależnej.
- [NetSuite: importuj dane główne](/pl/reference/workflow-steps/netsuite/import-master-data/) — listy danych podstawowych: konta, spółki zależne, działy, klasy, lokalizacje, dostawcy lub klienci.
- [NetSuite: importuj zapytanie SuiteQL](/pl/reference/workflow-steps/netsuite/import-suiteql-query/) — uruchom własne zapytanie SuiteQL i załaduj wynik do tabeli z typami kolumn, z obsługą okien dat i stronicowania.

## Kroki księgowania

- [Post NetSuite Journal Entry](/pl/reference/workflow-steps/netsuite/post-netsuite-journal-entry/) — zaksięguj zapisy dziennika (nagłówek/linie) z powrotem w NetSuite.

## Własne pobrania

Dla danych, których nie obejmują gotowe kroki importu — własnego zapytania lub rekordu NetSuite bez gotowego kroku — użyj kroku [NetSuite: importuj zapytanie SuiteQL](/pl/reference/workflow-steps/netsuite/import-suiteql-query/) z własnym SuiteQL. Punkty wyjścia znajdziesz w [Przykładach zapytań SuiteQL dla NetSuite](/pl/guides/connections/netsuite-financial-queries/).

## Powiązane

- [Konektor REST NetSuite](/pl/reference/connectors/rest/netsuite/)
- [Połączenie z NetSuite](/pl/guides/connections/netsuite/)
- [Import danych finansowych z NetSuite](/pl/guides/connections/import-netsuite-financials/)
