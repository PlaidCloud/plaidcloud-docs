---
title: ARRAY_AGG
description: "Learn how to use the ARRAY_AGG array function in PlaidCloud Lakehouse. Aggregates values into an array - see syntax, examples, and output."
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
