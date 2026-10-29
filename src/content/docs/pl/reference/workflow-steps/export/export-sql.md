---
title: Export to SQL (krok)
description: Eksportuj dane do zewnętrznych baz danych SQL z kroku przepływu pracy PlaidCloud, aby ładować wyniki do dalszych systemów bazodanowych.
sidebar:
  order: 9
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/export/export-sql.md
---

## Opis



Zapisuje tabelę projektu PlaidCloud na koncie dokumentów jako plik SQL zawierający instrukcje CREATE TABLE i INSERT. Przydatne, gdy trzeba przekazać dane do systemu, który przyjmuje skrypty SQL zamiast CSV lub Parquet.

Do ładowania bezpośrednio do zdalnej bazy danych użyj odpowiedniego kroku eksportu do bazy danych albo [Agent Remote Import Table into SQL Database (krok)](/pl/reference/workflow-steps/agent/agent-remote-import-table-into-sql-database/) — są szybsze i nie wymagają pliku pośredniego.

## Ustawienia dodatkowe

W sekcji **Kolejność wierszy** opcja **Sortuj wiersze według** (`sort_columns`) porządkuje zapisywane wiersze według tych kolumn źródłowych, od pierwszego klucza, każda z ustawieniami **Kolumna**, **Rosnąco** i **Wartości NULL**. Kolumna klucza nie musi być zapisywana. **Wartości NULL** domyślnie są na początku przy sortowaniu rosnącym i na końcu przy malejącym. Nie jest używana z **Podsumuj** ani **Unikalne**.

## Przykłady


Brak przykładów...
