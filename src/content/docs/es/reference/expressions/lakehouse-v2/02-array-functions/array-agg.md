---
title: ARRAY_AGG (Lakehouse v2)
description: ARRAY_AGG — agrega valores en una matriz.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-agg.md
---

Agrega valores en una matriz.

## Sintaxis de Analyze

```python
func.array_agg(get_column(table, 'name'))
```

## Ejemplos de Analyze

```python
func.array_agg(get_column(table, 'name'))
```

## Sintaxis de SQL

```sql
ARRAY_AGG(<name>)
```

## Ejemplos de SQL

```sql
SELECT ARRAY_AGG(name) FROM employees;

┌─────────────────────────────┐
│ array_agg(name)             │
├─────────────────────────────┤
│ ["Alice","Bob","Charlie"]   │
└─────────────────────────────┘
```
