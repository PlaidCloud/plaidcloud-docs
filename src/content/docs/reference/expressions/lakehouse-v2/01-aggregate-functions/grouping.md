---
title: GROUPING (Lakehouse v2)
description: "Use the GROUPING aggregate function in PlaidCloud Lakehouse. Indicates whether a specified column in a GROUP BY clause is aggregated. Returns 1 if aggregated."
---

Indicates whether a specified column in a GROUP BY clause is aggregated. Returns 1 if aggregated, 0 otherwise.

## Analyze Syntax

```python
func.grouping(get_column(table, 'department'))
```

## Analyze Examples

```python
func.grouping(get_column(table, 'department'))
```

## SQL Syntax

```sql
GROUPING(<department>)
```

## SQL Examples

```sql
SELECT department, GROUPING(department), SUM(salary)
FROM employees GROUP BY ROLLUP(department);

┌────────────┬───────────────────────┬─────────────┐
│ department │ grouping(department)  │ sum(salary)  │
├────────────┼───────────────────────┼─────────────┤
│ Sales      │                     0 │      195000 │
│ IT         │                     0 │      246000 │
│ NULL       │                     1 │      441000 │
└────────────┴───────────────────────┴─────────────┘
```
