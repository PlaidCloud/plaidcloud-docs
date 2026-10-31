---
title: ARRAY_AGG (Lakehouse v2)
description: ARRAY_AGG — agrega valores em um array.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-agg.md
---

Agrega valores em um array.

## Sintaxe do Analyze

```python
func.array_agg(get_column(table, 'name'))
```

## Exemplos do Analyze

```python
func.array_agg(get_column(table, 'name'))
```

## Sintaxe SQL

```sql
ARRAY_AGG(<name>)
```

## Exemplos SQL

```sql
SELECT ARRAY_AGG(name) FROM employees;

┌─────────────────────────────┐
│ array_agg(name)             │
├─────────────────────────────┤
│ ["Alice","Bob","Charlie"]   │
└─────────────────────────────┘
```
