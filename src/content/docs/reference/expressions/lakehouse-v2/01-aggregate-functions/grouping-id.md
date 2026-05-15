---
title: GROUPING_ID (Lakehouse v2)
description: GROUPING_ID — returns a bitmask corresponding to the grouping of columns.
---

Returns a bitmask corresponding to the grouping of columns.

## Analyze Syntax

```python
func.grouping_id(get_column(table, 'a'), get_column(table, 'b'))
```

## Analyze Examples

```python
func.grouping_id(get_column(table, 'department'), get_column(table, 'year'))

┌───┐
│ 0 │
└───┘
```

## SQL Syntax

```sql
GROUPING_ID(<a>, <b>)
```

## SQL Examples

```sql
SELECT department, year, GROUPING_ID(department, year), SUM(salary)
FROM employees GROUP BY ROLLUP(department, year);

┌───┐
│ 0 │
└───┘
```
