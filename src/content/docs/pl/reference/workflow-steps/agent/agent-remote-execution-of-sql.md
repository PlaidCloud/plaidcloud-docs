---
title: Agent Remote Execution of SQL
description: Wykonuj zapytania SQL zdalnie przez agenta PlaidLink w przepływach pracy PlaidCloud, aby bezpiecznie obsługiwać operacje na bazach danych za zaporami sieciowymi.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/agent/agent-remote-execution-of-sql.md
---

## Opis

Wykonuje SQL w bazie danych, do której PlaidCloud ma dostęp wyłącznie przez agenta PlaidLink — zwykle dlatego, że baza znajduje się za zaporą sieciową, w sieci prywatnej lub w lokalnym centrum danych. Agent uruchamia SQL lokalnie i zgłasza PlaidCloud powodzenie lub niepowodzenie.

Używaj go do wywoływania zdalnych procedur składowanych, procedur odświeżania lub zadań konserwacyjnych w ramach przepływu pracy PlaidCloud bez wystawiania bazy źródłowej do publicznego internetu.

## Uruchamianie instrukcji raz na wiersz

Krok **Zdalne wykonanie: SQL**, który łączy się z bazą danych bezpośrednio, a nie przez agenta, może uruchamiać swoją instrukcję raz dla każdego wiersza tabeli, na przykład aby wywołać procedurę składowaną dla każdego wiersza wejściowego. Ustaw **Uruchom SQL** na **Raz na wiersz**, wybierz **Tabela sterująca** i wypełnij **Parametry**. Zapisz każdą wartość w instrukcji jako symbol zastępczy `:name`, na przykład `CALL load_region(:region, :period)`, i zmapuj każdy symbol zastępczy w polu **Parametr** na **Kolumna sterująca**, która go dostarcza. Każda wartość jest wysyłana do bazy danych jako parametr powiązany i nigdy nie jest wklejana do tekstu instrukcji.

Każdy parametr wymaga zarówno nazwy, jak i kolumny sterującej, a parametru nie można wymienić dwukrotnie. Formularz ostrzega, gdy `:name` w instrukcji nie ma mapowania lub gdy mapowanie nie występuje w instrukcji. Tabela sterująca musi być tabelą, a nie widokiem. Tabela sterująca bez wierszy kończy się ostrzeżeniem i niczego nie uruchamia, a taka z ponad 100 000 wierszy kończy krok niepowodzeniem bez uruchamiania któregokolwiek z nich, więc najpierw ją przefiltruj.

## Uruchamianie skryptu w jednej transakcji

W kroku **Zdalne wykonanie: SQL** zaznacz **Uruchom SQL jako skrypt instrukcji w jednej transakcji: wszystkie albo żadna** (`transaction`), aby uruchomić SQL jako skrypt instrukcji wykonywanych kolejno w jednej transakcji, tak że zostaną zastosowane albo wszystkie instrukcje, albo żadna.
