---
title: Krok Export to SQL
description: Eksportuj dane do zewnętrznych baz danych SQL z kroku przepływu pracy PlaidCloud, aby ładować wyniki do dalszych systemów bazodanowych.
sidebar:
  order: 9
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/export/export-sql.md
---

## Opis



Zapisuje tabelę projektu PlaidCloud na koncie dokumentów jako plik SQL zawierający instrukcje CREATE TABLE i INSERT. Przydatne, gdy trzeba przekazać dane do systemu, który przyjmuje skrypty SQL zamiast CSV lub Parquet.

Do ładowania bezpośrednio do zdalnej bazy danych użyj zamiast tego odpowiedniego kroku eksportu do bazy danych lub [Agent Remote Import](/pl/reference/workflow-steps/agent/agent-remote-import-table-into-sql-database/) — są szybsze i nie wymagają pliku pośredniego.

## Podgląd

**Podgląd** pokazuje do 100 wierszy zapytania, które krok odczytuje z tabeli źródłowej, bez jego uruchamiania. Kliknij **Podgląd** na karcie **Źródło**. Jeśli wierszy jest więcej, podgląd informuje, że pokazuje pierwsze wiersze i że aby odczytać wszystkie, trzeba uruchomić krok. Podgląd podstawia zmienne tak samo jak uruchomienie, ale nie obsługuje formatów zmiennych, takich jak `{x:>9}`.

Podgląd tylko odczytuje dane. Jeśli zapytanie używa funkcji, której Podgląd nie może sprawdzić jako tylko do odczytu, wyświetla *Podgląd obsługuje tylko standardowe funkcje SQL. Uruchom krok, aby zobaczyć wyniki.* Uruchom krok, aby zobaczyć wynik. Podgląd nie jest dostępny w zablokowanym projekcie.

## Ustawienia dodatkowe

W **Kolejność wierszy** opcja **Sortuj wiersze według** (`sort_columns`) porządkuje zapisywane wiersze według tych kolumn źródłowych, od pierwszego klucza, każda z ustawieniami **Kolumna**, **Rosnąco** i **Wartości NULL**. Kolumna klucza nie musi być zapisywana. **Wartości NULL** domyślnie są na początku przy sortowaniu rosnącym i na końcu przy malejącym. Nie jest używane z **Podsumuj** ani **Unikalne**.

## Przykłady


Brak przykładów...
