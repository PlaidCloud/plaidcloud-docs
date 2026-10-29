---
title: FUSE_TIME_TRAVEL_SIZE (Lakehouse v1)
description: FUSE_TIME_TRAVEL_SIZE calcula el tamaño de almacenamiento de los datos históricos (para Time travel) de las tablas.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/16-system-functions/fuse-time-travel-size.md
---

Calcula el tamaño de almacenamiento de los datos históricos (para Time travel) de las tablas.

## Sintaxis de SQL

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

## Salida

La función devuelve un conjunto de resultados con las siguientes columnas:

| Columna                          | Descripción                                                                                           |
|----------------------------------|-------------------------------------------------------------------------------------------------------|
| `database_name`                  | El nombre de la base de datos en la que se encuentra la tabla.                                        |
| `table_name`                     | El nombre de la tabla.                                                                                |
| `is_dropped`                     | Indica si la tabla se ha eliminado (`true` para las tablas eliminadas, `false` en caso contrario).    |
| `time_travel_size`               | El tamaño de almacenamiento total de los datos históricos (para Time travel) de la tabla, en bytes.   |
| `latest_snapshot_size`           | El tamaño de almacenamiento de la instantánea más reciente de la tabla, en bytes.                     |
| `data_retention_period_in_hours` | El período de retención de los datos de Time travel en horas (`NULL` significa que se usa la política de retención predeterminada). |
| `error`                          | Cualquier error encontrado al obtener el tamaño de almacenamiento (`NULL` si no se produjo ningún error). |

## Ejemplos de SQL

Este ejemplo calcula los datos históricos de todas las tablas de la base de datos `default`:

```sql
SELECT * FROM fuse_time_travel_size('default')

┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ database_name │ table_name │ is_dropped │ time_travel_size │ latest_snapshot_size │ data_retention_period_in_hours │       error      │
├───────────────┼────────────┼────────────┼──────────────────┼──────────────────────┼────────────────────────────────┼──────────────────┤
│ default       │ books      │ true       │             2810 │                 1490 │                           NULL │ NULL             │
└───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```
