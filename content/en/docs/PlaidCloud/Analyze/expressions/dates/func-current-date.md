---
title: func.current_date
slug: func-current-date
weight: 3.0
description: Returns current date value based on the start of the current transaction
date: 2022-01-25T07:39:55
---

Returns current date value based on the start of the current transaction

## Syntax
```python
func.current_date()
```

## Examples
```python
func.current_date()
```
```python
get_column(table, 'Created On')>=(func.current_date()-120)
```
