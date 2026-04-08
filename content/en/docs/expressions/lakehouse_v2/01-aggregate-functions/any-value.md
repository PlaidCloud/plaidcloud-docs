---
title: ANY_VALUE
description: "Learn how to use the ANY_VALUE aggregate function in PlaidCloud Lakehouse. Returns any arbitrary value from a group of rows - with syntax and examples."
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
