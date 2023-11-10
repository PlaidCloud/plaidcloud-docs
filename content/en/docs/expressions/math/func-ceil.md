---
title: func.ceil
slug: func-ceil
description: The ceil() function is used to return the value, after rounded up any positive or negative decimal value as greater than the argument
date: 2022-01-25T07:40:00
---

The ceil() function is used to return the value, after rounded up any positive or negative decimal value as greater than the argument

## Syntax
```python
func.ceil(numeric)
```

## Examples
```python
func.ceil(func.extract('seconds', table.OutlierTime) / 60)
```
