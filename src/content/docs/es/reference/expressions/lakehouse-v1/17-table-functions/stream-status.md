---
title: STREAM_STATUS (Lakehouse v1)
description: STREAM_STATUS devuelve si una secuencia tiene registros de captura de datos de cambios para consumir (true/false).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/17-table-functions/stream-status.md
---

Proporciona información sobre el estado de una secuencia especificada y devuelve un resultado de una sola columna (`has_data`) que puede tomar los valores `true` o `false`: 

- `true`: indica que la secuencia **podría contener** registros de captura de datos de cambios.
- `false`: indica que la secuencia no contiene actualmente ningún registro de captura de datos de cambios.

:::note
La presencia de `true` en el resultado (`has_data`) **no** garantiza la existencia definitiva de registros de captura de datos de cambios. Otras operaciones, como una operación de compactación de la tabla, también pueden producir un valor `true` aunque no haya registros reales de captura de datos de cambios.
:::

:::note
Al usar `STREAM_STATUS` en tareas, debe incluir el nombre de la base de datos al hacer referencia a la secuencia (por ejemplo, `STREAM_STATUS('mydb.stream_name')`).
:::

## Sintaxis de SQL

```sql
SELECT * FROM STREAM_STATUS('<database_name>.<stream_name>');
-- OR
SELECT * FROM STREAM_STATUS('<stream_name>');  -- Uses current database
```

## Ejemplos de SQL

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
