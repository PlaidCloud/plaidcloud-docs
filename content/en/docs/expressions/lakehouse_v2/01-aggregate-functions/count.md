---
title: COUNT
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
