---
title: func.round
slug: func-round
description: The PostgreSQL ROUND() function rounds a numeric value to its nearest integer or a number with the number of decimal places
date: 2022-01-25T07:39:59
---

The PostgreSQL ROUND() function rounds a numeric value to its nearest integer or a number with the number of decimal places

## Syntax
```python
func.round(numeric)
```
```python
func.round(v numeric, s int)
```

## Examples
```python
func.round(table.RATE, 5)
```
```python
func.round((get_column(table, 'Order Quantity')/3), 0)
```
