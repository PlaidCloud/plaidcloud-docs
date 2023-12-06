---
title: func.safe_divide
slug: func-safe-divide
description: Equivalent to the division operator (X / Y), but returns NULL if an error occurs, such as a division by zero error
date: 2022-01-25T07:39:59
---

Equivalent to the division operator (X / Y), but returns NULL if an error occurs, such as a division by zero error

## Syntax
```python
func.safe_divide(numerator numeric, denominator numeric, divide_by_zero_value)
```

## Examples
```python
func.safe_divide(get_column(table, 'VALUE__MC'), table.RATE, 0.0)
```
```python
func.safe_divide(get_column(table, 'Total_Weight'), (table.PickHours + table.BreakHours), 0.00)
```
