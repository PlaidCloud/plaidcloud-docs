---
title: ARRAY_AGG (Lakehouse v2)
description: ARRAY_AGG — agreguje wartości do tablicy.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-agg.md
---

Agreguje wartości do tablicy.

## Składnia Analyze

```python
func.array_agg(get_column(table, 'name'))
```

## Przykłady Analyze

```python
func.array_agg(get_column(table, 'name'))
```

## Składnia SQL

```sql
ARRAY_AGG(<name>)
```

## Przykłady SQL

```sql
SELECT ARRAY_AGG(name) FROM employees;

┌─────────────────────────────┐
│ array_agg(name)             │
├─────────────────────────────┤
│ ["Alice","Bob","Charlie"]   │
└─────────────────────────────┘
```
