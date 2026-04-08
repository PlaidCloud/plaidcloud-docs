---
title: AVG
description: "Learn how to use the AVG aggregate function in PlaidCloud Lakehouse. Returns the average value of a numeric column - see syntax, examples, and output."
---

Returns the average value of a numeric column.

## Analyze Syntax

```python
func.avg(get_column(table, 'salary'))
```

## Analyze Examples

```python
func.avg(get_column(table, 'salary'))
```

## SQL Syntax

```sql
AVG(<salary>)
```

## SQL Examples

```sql
SELECT department, AVG(salary) FROM employees GROUP BY department;

┌────────────┬──────────────┐
│ department │ avg(salary)  │
├────────────┼──────────────┤
│ Sales      │     65000.00 │
│ IT         │     82000.00 │
└────────────┴──────────────┘
```
