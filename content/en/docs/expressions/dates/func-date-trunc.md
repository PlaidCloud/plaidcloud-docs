---
title: func.date_trunc
slug: func-date-trunc
weight: 7.0
description: Truncate input value to specified precision
date: 2022-01-25T07:39:55
---

Truncate input value to specified precision

## Syntax
```python
func.date_trunc(text, timestamp)
```

## Examples
```python
func.date_trunc('week', get_column(table, 'Date' ))
```
