---
title: FILES (Lakehouse v2)
description: FILES — lê dados diretamente de arquivos no armazenamento em nuvem.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/20-table-functions/files.md
---

Lê dados diretamente de arquivos no armazenamento em nuvem.

## Sintaxe do Analyze

```python
func.files(<path_or_properties>)
```

## Exemplos do Analyze

```python
# FILES is a table function used in FROM clauses
# select(func.files(...))

┌─────────┐
│ (table)  │
└─────────┘
```

## Sintaxe SQL

```sql
FILES(<path_or_properties>)
```

## Exemplos de SQL

```sql
SELECT * FROM FILES('path' = 's3://bucket/data.parquet', 'format' = 'parquet') LIMIT 5;

┌─────────────────┐
│ (query results)  │
└─────────────────┘
```
