---
title: FUSE_TIME_TRAVEL_SIZE (Lakehouse v1)
description: FUSE_TIME_TRAVEL_SIZE — calcula o tamanho de armazenamento dos dados históricos (para Time travel) das tabelas.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/16-system-functions/fuse-time-travel-size.md
---

Calcula o tamanho de armazenamento dos dados históricos (para Time travel) das tabelas.

## Sintaxe SQL

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

## Saída

A função devolve um conjunto de resultados com as seguintes colunas:

| Coluna                           | Descrição                                                                                           |
|----------------------------------|-------------------------------------------------------------------------------------------------------|
| `database_name`                  | O nome da base de dados onde a tabela se encontra.                                                  |
| `table_name`                     | O nome da tabela.                                                                                |
| `is_dropped`                     | Indica se a tabela foi eliminada (`true` para tabelas eliminadas, `false` caso contrário).          |
| `time_travel_size`               | O tamanho total de armazenamento dos dados históricos (para Time travel) da tabela, em bytes.                  |
| `latest_snapshot_size`           | O tamanho de armazenamento do instantâneo mais recente da tabela, em bytes.                                       |
| `data_retention_period_in_hours` | O período de retenção dos dados de Time travel, em horas (`NULL` significa que se utiliza a política de retenção predefinida). |
| `error`                          | Qualquer erro encontrado ao obter o tamanho de armazenamento (`NULL` se não ocorreram erros).               |

## Exemplos de SQL

Este exemplo calcula os dados históricos de todas as tabelas da base de dados `default`:

```sql
SELECT * FROM fuse_time_travel_size('default')

┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ database_name │ table_name │ is_dropped │ time_travel_size │ latest_snapshot_size │ data_retention_period_in_hours │       error      │
├───────────────┼────────────┼────────────┼──────────────────┼──────────────────────┼────────────────────────────────┼──────────────────┤
│ default       │ books      │ true       │             2810 │                 1490 │                           NULL │ NULL             │
└───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```
