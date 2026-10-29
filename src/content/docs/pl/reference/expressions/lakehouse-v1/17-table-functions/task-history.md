---
title: TASK_HISTORY (Lakehouse v1)
description: TASK_HISTORY — wyświetla historię uruchomień zadań dla podanych zmiennych.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/17-table-functions/task-history.md
---

Wyświetla historię uruchomień zadań dla podanych zmiennych.

## Składnia SQL
```sql
TASK_HISTORY(
      [ SCHEDULED_TIME_RANGE_START => <constant_expr> ]
      [, SCHEDULED_TIME_RANGE_END => <constant_expr> ]
      [, RESULT_LIMIT => <integer> ]
      [, TASK_NAME => '<string>' ]
      [, ERROR_ONLY => { TRUE | FALSE } ]
      [, ROOT_TASK_ID => '<string>'] )
```



## Argumenty

Wszystkie argumenty są opcjonalne.

`SCHEDULED_TIME_RANGE_START => <constant_expr>`, `SCHEDULED_TIME_RANGE_END => <constant_expr>`

Zakres czasu (w formacie TIMESTAMP_LTZ), obejmujący ostatnie 7 dni, w którym zaplanowano wykonanie zadania. Jeśli zakres czasu nie mieści się w ostatnich 7 dniach, zwracany jest błąd.

* Jeśli `SCHEDULED_TIME_RANGE_END` nie zostanie podany, funkcja zwraca zadania, które już się zakończyły, są obecnie uruchomione lub zaplanowano je w przyszłości.
* Jeśli `SCHEDULED_TIME_RANGE_END` ma wartość CURRENT_TIMESTAMP, funkcja zwraca zadania, które już się zakończyły lub są obecnie uruchomione. Zadanie wykonane tuż przed bieżącym czasem może nadal być oznaczone jako zaplanowane.
* Aby zapytać wyłącznie o zadania, które już się zakończyły lub są obecnie uruchomione, dodaj filtr `WHERE query_id IS NOT NULL`. Kolumna QUERY_ID w danych wyjściowych TASK_HISTORY jest wypełniana dopiero po rozpoczęciu uruchomienia zadania.

Jeśli nie podano czasu początkowego ani końcowego, zwracane są najnowsze zadania, do wartości RESULT_LIMIT.

`RESULT_LIMIT => <integer>`

Liczba określająca maksymalną liczbę wierszy zwracanych przez funkcję.

Jeśli liczba pasujących wierszy jest większa od tego limitu, zwracane są wykonania zadań z najnowszą sygnaturą czasową, do wskazanego limitu.

Zakres: od `1` do `10000`

Domyślnie: `100`.

`TASK_NAME => <string>`

Ciąg znaków bez rozróżniania wielkości liter, określający zadanie. Obsługiwane są tylko nazwy zadań bez kwalifikatorów. Zwracane są tylko wykonania wskazanego zadania. Jeśli wiele zadań ma tę samą nazwę, funkcja zwraca historię każdego z nich.

`ERROR_ONLY => { TRUE | FALSE }`

Po ustawieniu na TRUE funkcja zwraca tylko uruchomienia zadań, które zakończyły się niepowodzeniem lub zostały anulowane.

`ROOT_TASK_ID => <string>`

Unikatowy identyfikator zadania głównego w grafie zadań. Ten identyfikator odpowiada wartości w kolumnie ID w danych wyjściowych SHOW TASKS dla tego samego zadania. Podaj ROOT_TASK_ID, aby wyświetlić historię zadania głównego oraz wszystkich zadań podrzędnych należących do grafu zadań.

## Uwagi dotyczące użycia
* Ta funkcja zwraca maksymalnie 10 000 wierszy, ustawionych wartością argumentu RESULT_LIMIT. Wartość domyślna to 100.
* Ta funkcja zwraca wyniki tylko dla roli ACCOUNTADMIN.


## Przykłady SQL

```sql
SELECT
  *
FROM TASK_HISTORY() order by scheduled_time;
```
Powyższe zapytanie SQL pobiera wszystkie rekordy historii zadań z funkcji TASK_HISTORY, uporządkowane według kolumny scheduled_time (maksymalnie 10 000).



```sql
SELECT *
  FROM TASK_HISTORY(
    SCHEDULED_TIME_RANGE_START=>TO_TIMESTAMP('2022-01-02T01:12:00-07:00'),
    SCHEDULED_TIME_RANGE_END=>TO_TIMESTAMP('2022-01-02T01:12:30-07:00'))
```

Powyższe zapytanie SQL pobiera wszystkie rekordy historii zadań z funkcji TASK_HISTORY, w których zaplanowany zakres czasu zaczyna się o '2022-01-02T01:12:00-07:00' i kończy o '2022-01-02T01:12:30-07:00'. Oznacza to, że zwróci zadania zaplanowane do uruchomienia w tym konkretnym 30-sekundowym oknie czasowym. Wynik będzie zawierał szczegóły zadań spełniających to kryterium.
