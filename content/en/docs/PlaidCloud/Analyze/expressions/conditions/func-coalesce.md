---
title: func.coalesce
slug: func-coalesce
weight: 3.0
description: The COALESCE() function returns the first non-null value in a list
date: 2022-01-25T07:39:53
---

The COALESCE() function returns the first non-null value in a list

## Syntax
```python
func.coalesce(value, value, value...)
```

## Examples
```python
func.coalesce(table.UOM,  'none', \n)
```
```python
func.coalesce(get_column(table2, 'TECHNOLOGY_RATE'), 0.0)
```
