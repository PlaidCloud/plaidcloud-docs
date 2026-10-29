---
title: ARRAY_AGG (Lakehouse v2)
description: ARRAY_AGG – aggregiert Werte zu einem Array.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-agg.md
---

Aggregiert Werte zu einem Array.

## Analyze-Syntax

```python
func.array_agg(get_column(table, 'name'))
```

## Analyze-Beispiele

```python
func.array_agg(get_column(table, 'name'))
```

## SQL-Syntax

```sql
ARRAY_AGG(<name>)
```

## SQL-Beispiele

```sql
SELECT ARRAY_AGG(name) FROM employees;

┌─────────────────────────────┐
│ array_agg(name)             │
├─────────────────────────────┤
│ ["Alice","Bob","Charlie"]   │
└─────────────────────────────┘
```
