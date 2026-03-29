---
title: BOOL_OR
---

Returns TRUE if any value in the group is TRUE.

## Analyze Syntax

```python
func.bool_or(get_column(table, 'is_active'))
```

## Analyze Examples

```python
func.bool_or(get_column(table, 'is_active'))
```

## SQL Syntax

```sql
BOOL_OR(<is_active>)
```

## SQL Examples

```sql
SELECT department, BOOL_OR(is_active) FROM employees GROUP BY department;

┌────────────┬─────────────────────┐
│ department │ bool_or(is_active)  │
├────────────┼─────────────────────┤
│ Sales      │                   1 │
│ IT         │                   1 │
└────────────┴─────────────────────┘
```
