---
title: COUNT
description: "Learn how to use the COUNT aggregate function in PlaidCloud Lakehouse. Returns the number of rows or non-NULL values - see syntax, examples, and output."
---

Returns the number of rows or non-NULL values.

## Analyze Syntax

```python
func.count()
```

## Analyze Examples

```python
func.count()
```

## SQL Syntax

```sql
COUNT()
```

## SQL Examples

```sql
SELECT COUNT(*) FROM employees;

┌──────────┐
│ count(*) │
├──────────┤
│     1000 │
└──────────┘

SELECT COUNT(DISTINCT department) FROM employees;

┌──────────────────────────────┐
│ count(distinct department)   │
├──────────────────────────────┤
│                            5 │
└──────────────────────────────┘
```
