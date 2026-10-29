---
title: FUSE_TIME_TRAVEL_SIZE (Lakehouse v1)
description: FUSE_TIME_TRAVEL_SIZE — oblicza rozmiar miejsca zajmowanego przez dane historyczne (dla funkcji Time travel) w tabelach.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/16-system-functions/fuse-time-travel-size.md
---

Oblicza rozmiar miejsca zajmowanego przez dane historyczne (dla funkcji Time travel) w tabelach.

## Składnia SQL

```sql
-- Calculate historical data size for all tables in all databases
SELECT ...
FROM fuse_time_travel_size();

-- Calculate historical data size for all tables in a specified database
SELECT ...
FROM fuse_time_travel_size('<database_name>');

-- Calculate historical data size for a specified table in a specified database
SELECT ...
FROM fuse_time_travel_size('<database_name>', '<table_name>'));
```

## Dane wyjściowe

Funkcja zwraca zbiór wyników z następującymi kolumnami:

| Kolumna                           | Opis                                                                                           |
|----------------------------------|-------------------------------------------------------------------------------------------------------|
| `database_name`                  | Nazwa bazy danych, w której znajduje się tabela.                                                  |
| `table_name`                     | Nazwa tabeli.                                                                                |
| `is_dropped`                     | Wskazuje, czy tabela została usunięta (`true` dla usuniętych tabel, w przeciwnym razie `false`).          |
| `time_travel_size`               | Łączny rozmiar danych historycznych (dla funkcji Time travel) tabeli, w bajtach.                  |
| `latest_snapshot_size`           | Rozmiar najnowszej migawki tabeli, w bajtach.                                       |
| `data_retention_period_in_hours` | Okres przechowywania danych Time travel w godzinach (`NULL` oznacza użycie domyślnej polityki przechowywania). |
| `error`                          | Wszelkie błędy napotkane podczas pobierania rozmiaru (`NULL`, jeśli nie wystąpiły żadne błędy).               |

## Przykłady SQL

Ten przykład oblicza dane historyczne dla wszystkich tabel w bazie danych `default`:

```sql
SELECT * FROM fuse_time_travel_size('default')

┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ database_name │ table_name │ is_dropped │ time_travel_size │ latest_snapshot_size │ data_retention_period_in_hours │       error      │
├───────────────┼────────────┼────────────┼──────────────────┼──────────────────────┼────────────────────────────────┼──────────────────┤
│ default       │ books      │ true       │             2810 │                 1490 │                           NULL │ NULL             │
└───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```
