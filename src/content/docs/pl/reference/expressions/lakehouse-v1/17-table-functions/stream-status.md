---
title: STREAM_STATUS (Lakehouse v1)
description: STREAM_STATUS — zwraca informację, czy strumień zawiera rekordy przechwytywania zmian danych (change data capture) do przetworzenia (true/false).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/17-table-functions/stream-status.md
---

Udostępnia informacje o stanie wskazanego strumienia, zwracając wynik z jedną kolumną (`has_data`), która może przyjmować wartości `true` lub `false`: 

- `true`: oznacza, że strumień **może zawierać** rekordy przechwytywania zmian danych (change data capture).
- `false`: oznacza, że strumień obecnie nie zawiera żadnych rekordów przechwytywania zmian danych.

:::note
Wartość `true` w wyniku (`has_data`) **nie** gwarantuje, że rekordy przechwytywania zmian danych na pewno istnieją. Inne operacje, takie jak kompaktowanie tabeli, również mogą skutkować wartością `true`, nawet gdy nie ma żadnych rzeczywistych rekordów przechwytywania zmian danych.
:::

:::note
Używając `STREAM_STATUS` w zadaniach, musisz podać nazwę bazy danych przy odwoływaniu się do strumienia (np. `STREAM_STATUS('mydb.stream_name')`).
:::

## Składnia SQL

```sql
SELECT * FROM STREAM_STATUS('<database_name>.<stream_name>');
-- OR
SELECT * FROM STREAM_STATUS('<stream_name>');  -- Uses current database
```

## Przykłady SQL

```sql
-- Create a table 't' with a column 'c'
CREATE TABLE t (c int);

-- Create a stream 's' on the table 't'
CREATE STREAM s ON TABLE t;

-- Check the initial status of the stream 's'
SELECT * FROM STREAM_STATUS('s');

-- The result should be 'false' indicating no change data capture records initially
┌──────────┐
│ has_data │
├──────────┤
│ false    │
└──────────┘

-- Insert a value into the table 't'
INSERT INTO t VALUES (1);

-- Check the updated status of the stream 's' after the insertion
SELECT * FROM STREAM_STATUS('s');

-- The result should now be 'true' indicating the presence of change data capture records
┌──────────┐
│ has_data │
├──────────┤
│ true     │
└──────────┘

-- Example with database name specified
SELECT * FROM STREAM_STATUS('mydb.s');
```
