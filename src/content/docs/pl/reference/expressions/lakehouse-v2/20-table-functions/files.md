---
title: FILES (Lakehouse v2)
description: FILES — odczytuje dane bezpośrednio z plików w magazynie w chmurze.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/20-table-functions/files.md
---

Odczytuje dane bezpośrednio z plików w magazynie w chmurze.

## Składnia Analyze

```python
func.files(<path_or_properties>)
```

## Przykłady Analyze

```python
# FILES is a table function used in FROM clauses
# select(func.files(...))

┌─────────┐
│ (table)  │
└─────────┘
```

## Składnia SQL

```sql
FILES(<path_or_properties>)
```

## Przykłady SQL

```sql
SELECT * FROM FILES('path' = 's3://bucket/data.parquet', 'format' = 'parquet') LIMIT 5;

┌─────────────────┐
│ (query results)  │
└─────────────────┘
```
