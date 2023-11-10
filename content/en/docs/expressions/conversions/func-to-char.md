---
title: func.to_char
slug: func-to-char
weight: 2.0
description: The TO_CHAR function converts a number or date to a string
date: 2022-01-25T07:39:54
---

The TO_CHAR function converts a number or date to a string

## Syntax
```python
func.to_char(value, text)
```

## Examples
```python
to_char("Sales_Order_w_Status"."WeekName")
```
```python
func.to_char(func.date_trunc('week', get_column(table, 'date_sol_delivery_required')), 'YYYY-MM-DD')
```
