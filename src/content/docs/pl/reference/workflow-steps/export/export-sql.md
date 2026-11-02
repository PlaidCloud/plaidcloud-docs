---
title: Eksport do SQL
description: Eksportuj dane do zewnętrznych baz danych SQL z kroku przepływu pracy PlaidCloud, aby załadować wyniki do dalszych systemów bazodanowych.
sidebar:
  order: 9
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/export/export-sql.md
---

## Opis



Zapisuje tabelę projektu PlaidCloud na koncie dokumentów jako plik SQL zawierający instrukcje CREATE TABLE i INSERT. Przydaje się, gdy trzeba przekazać dane do systemu, który wczytuje skrypty SQL zamiast plików CSV lub Parquet.

Aby załadować dane bezpośrednio do zdalnej bazy danych, użyj odpowiedniego kroku eksportu do bazy danych lub kroku [Agent Remote Import (krok)](/pl/reference/workflow-steps/agent/agent-remote-import-table-into-sql-database/) — są szybsze i nie wymagają pliku pośredniego.

## Podgląd

Przycisk **Podgląd** na karcie **Źródło** pokazuje do 100 wierszy tabeli źródłowej bez uruchamiania kroku. Jeśli tabela ma więcej wierszy, podgląd informuje, że pokazuje pierwsze wiersze. Jeśli tabela źródłowa jeszcze nie istnieje, Podgląd informuje, że nie ma nic do wyświetlenia. Podgląd nie jest dostępny w zablokowanym projekcie.

## Ustawienia dodatkowe

W sekcji **Kolejność wierszy** ustawienie **Sortuj wiersze według** (`sort_columns`) porządkuje zapisywane wiersze według tych kolumn źródłowych, zaczynając od pierwszego klucza; każdy klucz ma ustawienia **Kolumna**, **Rosnąco** i **Wartości NULL**. Kolumna klucza nie musi być zapisywana. Ustawienie **Wartości NULL** domyślnie umieszcza je na początku przy sortowaniu rosnącym i na końcu przy malejącym. Nie jest używane z opcjami **Podsumuj** ani **Unikalne**.

## Przykłady


Brak przykładów.
