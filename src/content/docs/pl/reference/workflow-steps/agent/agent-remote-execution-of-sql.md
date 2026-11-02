---
title: Krok Agent Remote Execution of SQL
description: Wykonuj zapytania SQL zdalnie przez agenta PlaidLink w przepływach pracy PlaidCloud, aby bezpiecznie obsługiwać operacje na bazach danych za zaporami sieciowymi.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/agent/agent-remote-execution-of-sql.md
---

## Opis

Wykonuje SQL w bazie danych, do której PlaidCloud ma dostęp tylko przez agenta PlaidLink — zwykle dlatego, że baza znajduje się za zaporą sieciową, w sieci prywatnej lub w lokalnym centrum danych. Agent uruchamia SQL lokalnie i zgłasza do PlaidCloud powodzenie lub niepowodzenie.

Używaj tego do wyzwalania zdalnych procedur składowanych, procedur odświeżania lub zadań konserwacyjnych w ramach przepływu pracy PlaidCloud bez wystawiania źródłowej bazy danych do publicznego internetu.

## Podgląd zapytania

W kroku **Zdalne wykonanie: SQL** **Podgląd** na karcie **Źródło** pokazuje do 100 wierszy bez uruchamiania instrukcji, więc możesz sprawdzić `SELECT` przed jego uruchomieniem. Podgląd podstawia zmienne tak samo jak uruchomienie, ale nie obsługuje formatów zmiennych, takich jak `{x:>9}`. Tylko odczytuje dane: instrukcja, która zapisuje, lub funkcja, której Podgląd nie może sprawdzić jako tylko do odczytu, jest odrzucana z komunikatem *Podgląd obsługuje tylko standardowe funkcje SQL. Uruchom krok, aby zobaczyć wyniki.* Podgląd nie jest dostępny w zablokowanym projekcie ani dla instrukcji, które używają symboli zastępczych `:name` z tabelą sterującą. Nie jest dostępny dla kroku opartego na agencie, który opisuje ta strona, ponieważ tylko agent może dotrzeć do tych baz danych.

## Uruchamianie instrukcji raz na wiersz

Krok **Zdalne wykonanie: SQL**, który łączy się z bazą danych bezpośrednio, a nie przez agenta, może uruchamiać swoją instrukcję raz dla każdego wiersza tabeli, na przykład aby wywołać procedurę składowaną dla każdego wiersza wejściowego. Ustaw **Uruchom SQL** na **Raz na wiersz**, wybierz **Tabela sterująca** i wypełnij **Parametry**. Zapisz każdą wartość w instrukcji jako symbol zastępczy `:name`, na przykład `CALL load_region(:region, :period)`, i zmapuj każdy symbol zastępczy w **Parametr** na **Kolumna sterująca**, która go dostarcza. Każda wartość jest wysyłana do bazy danych jako powiązany parametr, nigdy nie jest wklejana do tekstu instrukcji.

Każdy parametr potrzebuje zarówno nazwy, jak i kolumny sterującej, a parametru nie można wymienić dwukrotnie. Formularz ostrzega, gdy `:name` w instrukcji nie ma mapowania lub mapowania nie ma w instrukcji. Tabela sterująca musi być tabelą, a nie widokiem. Tabela sterująca bez wierszy kończy się ostrzeżeniem i nic nie uruchamia, a tabela z ponad 100 000 wierszy powoduje niepowodzenie kroku bez uruchamiania któregokolwiek z nich, więc najpierw ją przefiltruj.

## Uruchamianie skryptu w jednej transakcji

W kroku **Zdalne wykonanie: SQL** zaznacz **Uruchom SQL jako skrypt instrukcji w jednej transakcji: wszystkie albo żadna** (`transaction`), aby uruchomić SQL jako skrypt instrukcji, jedna po drugiej, w pojedynczej transakcji, tak aby zastosowana została każda instrukcja albo żadna.
