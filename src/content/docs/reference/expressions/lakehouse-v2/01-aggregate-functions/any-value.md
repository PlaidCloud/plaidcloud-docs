---
title: ANY_VALUE (Lakehouse v2)
description: ANY_VALUE — Returns any arbitrary value from a group of rows.
---

Returns any arbitrary value from a group of rows.

## Analyze Syntax

```python
func.any_value(get_column(table, 'department'))
```

## Analyze Examples

```python
func.any_value(get_column(table, 'department'))

┌───────┐
│ Sales │
└───────┘
```

## SQL Syntax

```sql
ANY_VALUE(<department>)
```

## SQL Examples

```sql
SELECT ANY_VALUE(department) FROM employees;

┌───────┐
│ Sales │
└───────┘
```
