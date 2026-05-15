---
title: SUM (Lakehouse v2)
description: SUM — returns the sum of all values in a group.
---

Returns the sum of all values in a group.

## Analyze Syntax

```python
func.sum(get_column(table, 'amount'))
```

## Analyze Examples

```python
func.sum(get_column(table, 'amount'))
```

## SQL Syntax

```sql
SUM(<amount>)
```

## SQL Examples

```sql
SELECT department, SUM(salary) FROM employees GROUP BY department;

┌────────────┬─────────────┐
│ department │ sum(salary) │
├────────────┼─────────────┤
│ Sales      │      195000 │
│ IT         │      246000 │
│ HR         │      210000 │
└────────────┴─────────────┘
```
