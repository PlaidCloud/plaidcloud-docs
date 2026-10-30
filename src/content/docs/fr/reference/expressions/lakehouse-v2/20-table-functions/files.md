---
title: FILES (Lakehouse v2)
description: FILES — lit les données directement à partir de fichiers du stockage cloud.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/20-table-functions/files.md
---

Lit les données directement à partir de fichiers du stockage cloud.

## Syntaxe Analyze

```python
func.files(<path_or_properties>)
```

## Exemples Analyze

```python
# FILES is a table function used in FROM clauses
# select(func.files(...))

┌─────────┐
│ (table)  │
└─────────┘
```

## Syntaxe SQL

```sql
FILES(<path_or_properties>)
```

## Exemples SQL

```sql
SELECT * FROM FILES('path' = 's3://bucket/data.parquet', 'format' = 'parquet') LIMIT 5;

┌─────────────────┐
│ (query results)  │
└─────────────────┘
```
