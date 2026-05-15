---
title: ARRAY_AGG (Lakehouse v2)
description: ARRAY_AGG — aggregates values into an array.
---

Aggregates values into an array.

## Analyze Syntax

```python
func.array_agg(get_column(table, 'name'))
```

## Analyze Examples

```python
func.array_agg(get_column(table, 'name'))
```

## SQL Syntax

```sql
ARRAY_AGG(<name>)
```

## SQL Examples

```sql
SELECT ARRAY_AGG(name) FROM employees;

┌─────────────────────────────┐
│ array_agg(name)             │
├─────────────────────────────┤
│ ["Alice","Bob","Charlie"]   │
└─────────────────────────────┘
```
