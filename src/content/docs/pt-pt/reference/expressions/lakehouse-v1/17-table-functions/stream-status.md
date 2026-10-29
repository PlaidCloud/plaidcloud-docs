---
title: STREAM_STATUS (Lakehouse v1)
description: STREAM_STATUS — indica se um fluxo tem registos de captura de dados de alterações para consumir (true/false).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/17-table-functions/stream-status.md
---

Fornece informação sobre o estado de um fluxo especificado, devolvendo um resultado de uma só coluna (`has_data`) que pode assumir os valores `true` ou `false`: 

- `true`: indica que o fluxo **pode conter** registos de captura de dados de alterações.
- `false`: indica que o fluxo não contém atualmente nenhum registo de captura de dados de alterações.

:::note
A presença de `true` no resultado (`has_data`) **não** garante a existência efetiva de registos de captura de dados de alterações. Outras operações, como a compactação de uma tabela, também podem originar o valor `true` mesmo quando não existem registos de captura de dados de alterações.
:::

:::note
Ao utilizar `STREAM_STATUS` em tarefas, tem de incluir o nome da base de dados ao referenciar o fluxo (por exemplo, `STREAM_STATUS('mydb.stream_name')`).
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
