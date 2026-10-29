---
title: STREAM_STATUS (Lakehouse v1)
description: STREAM_STATUS — retorna se um stream tem registros de captura de dados de alteração para consumir (true/false).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/17-table-functions/stream-status.md
---

Fornece informações sobre o status de um stream especificado, produzindo um resultado de uma única coluna (`has_data`) que pode assumir os valores `true` ou `false`: 

- `true`: indica que o stream **pode conter** registros de captura de dados de alteração.
- `false`: indica que o stream não contém, no momento, nenhum registro de captura de dados de alteração.

:::note
A presença de `true` no resultado (`has_data`) **não** garante a existência de registros de captura de dados de alteração. Outras operações, como uma operação de compactação de tabela, também podem levar a um valor `true` mesmo quando não há registros reais de captura de dados de alteração.
:::

:::note
Ao usar `STREAM_STATUS` em tarefas, você deve incluir o nome do banco de dados ao referenciar o stream (por exemplo, `STREAM_STATUS('mydb.stream_name')`).
:::

## Sintaxe SQL

```sql
SELECT * FROM STREAM_STATUS('<database_name>.<stream_name>');
-- OR
SELECT * FROM STREAM_STATUS('<stream_name>');  -- Uses current database
```

## Exemplos de SQL

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
