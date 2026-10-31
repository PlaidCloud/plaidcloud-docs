---
title: STREAM_STATUS (Lakehouse v1)
description: STREAM_STATUS — indique si un flux contient des enregistrements de capture de données modifiées à consommer (true/false).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/17-table-functions/stream-status.md
---

Fournit des informations sur l'état d'un flux spécifié et produit un résultat à une seule colonne (`has_data`) qui peut valoir `true` ou `false` : 

- `true` : indique que le flux **peut contenir** des enregistrements de capture de données modifiées.
- `false` : indique que le flux ne contient actuellement aucun enregistrement de capture de données modifiées.

:::note
La présence de `true` dans le résultat (`has_data`) ne garantit **pas** l'existence effective d'enregistrements de capture de données modifiées. D'autres opérations, comme un compactage de table, peuvent aussi produire la valeur `true` même en l'absence d'enregistrements de capture de données modifiées.
:::

:::note
Lorsque vous utilisez `STREAM_STATUS` dans des tâches, vous devez inclure le nom de la base de données pour référencer le flux (par exemple, `STREAM_STATUS('mydb.stream_name')`).
:::

## Syntaxe SQL

```sql
SELECT * FROM STREAM_STATUS('<database_name>.<stream_name>');
-- OR
SELECT * FROM STREAM_STATUS('<stream_name>');  -- Uses current database
```

## Exemples SQL

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
