---
title: FILES (Lakehouse v2)
description: FILES — Lee datos directamente de archivos de almacenamiento en la nube.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/20-table-functions/files.md
---

Lee datos directamente de archivos de almacenamiento en la nube.

## Sintaxis de Analyze

```python
func.files(<path_or_properties>)
```

## Ejemplos de Analyze

```python
# FILES is a table function used in FROM clauses
# select(func.files(...))

┌─────────┐
│ (table)  │
└─────────┘
```

## Sintaxis de SQL

```sql
FILES(<path_or_properties>)
```

## Ejemplos de SQL

```sql
SELECT * FROM FILES('path' = 's3://bucket/data.parquet', 'format' = 'parquet') LIMIT 5;

┌─────────────────┐
│ (query results)  │
└─────────────────┘
```
