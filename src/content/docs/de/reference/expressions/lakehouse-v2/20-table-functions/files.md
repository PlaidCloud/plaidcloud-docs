---
title: FILES (Lakehouse v2)
description: FILES — liest Daten direkt aus Dateien im Cloud-Speicher.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/20-table-functions/files.md
---

Liest Daten direkt aus Dateien im Cloud-Speicher.

## Analyze-Syntax

```python
func.files(<path_or_properties>)
```

## Analyze-Beispiele

```python
# FILES is a table function used in FROM clauses
# select(func.files(...))

┌─────────┐
│ (table)  │
└─────────┘
```

## SQL-Syntax

```sql
FILES(<path_or_properties>)
```

## SQL-Beispiele

```sql
SELECT * FROM FILES('path' = 's3://bucket/data.parquet', 'format' = 'parquet') LIMIT 5;

┌─────────────────┐
│ (query results)  │
└─────────────────┘
```
