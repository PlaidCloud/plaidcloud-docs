---
title: COUNT_IF
description: "Learn how to use the COUNT_IF aggregate function in PlaidCloud Lakehouse. Returns the number of rows for which the expression is TRUE."
---

Returns the number of rows for which the expression is TRUE.

## Analyze Syntax

```python
func.count_if(get_column(table, 'salary') > 80000)
```

## Analyze Examples

```python
func.count_if(get_column(table, 'salary') > 80000)

┌────┐
│ 42 │
└────┘
```

## SQL Syntax

```sql
COUNT_IF(<salary> > 80000)
```

## SQL Examples

```sql
SELECT COUNT_IF(salary > 80000) FROM employees;

┌────┐
│ 42 │
└────┘
```
