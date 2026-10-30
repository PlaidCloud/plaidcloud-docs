---
title: ARRAY_AGG (Lakehouse v2)
description: ARRAY_AGG — agrège des valeurs dans un tableau.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-agg.md
---

Agrège des valeurs dans un tableau.

## Syntaxe Analyze

```python
func.array_agg(get_column(table, 'name'))
```

## Exemples Analyze

```python
func.array_agg(get_column(table, 'name'))
```

## Syntaxe SQL

```sql
ARRAY_AGG(<name>)
```

## Exemples SQL

```sql
SELECT ARRAY_AGG(name) FROM employees;

┌─────────────────────────────┐
│ array_agg(name)             │
├─────────────────────────────┤
│ ["Alice","Bob","Charlie"]   │
└─────────────────────────────┘
```
