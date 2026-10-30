---
title: STREAM_STATUS (Lakehouse v1)
description: STREAM_STATUS gibt zurück, ob ein Stream Change-Data-Capture-Datensätze zum Verarbeiten enthält (true/false).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/17-table-functions/stream-status.md
---

Liefert Informationen zum Status eines angegebenen Streams und gibt ein Ergebnis mit einer einzigen Spalte (`has_data`) zurück, die die Werte `true` oder `false` annehmen kann: 

- `true`: Der Stream **enthält möglicherweise** Change-Data-Capture-Datensätze.
- `false`: Der Stream enthält derzeit keine Change-Data-Capture-Datensätze.

:::note
Ein Wert `true` im Ergebnis (`has_data`) garantiert **nicht**, dass tatsächlich Change-Data-Capture-Datensätze vorhanden sind. Auch andere Vorgänge, etwa das Verdichten einer Tabelle (Compact), können zu einem Wert `true` führen, obwohl keine tatsächlichen Change-Data-Capture-Datensätze vorliegen.
:::

:::note
Wenn Sie `STREAM_STATUS` in Tasks verwenden, müssen Sie beim Verweis auf den Stream den Datenbanknamen angeben (z. B. `STREAM_STATUS('mydb.stream_name')`).
:::

## SQL-Syntax

```sql
SELECT * FROM STREAM_STATUS('<database_name>.<stream_name>');
-- OR
SELECT * FROM STREAM_STATUS('<stream_name>');  -- Uses current database
```

## SQL-Beispiele

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
