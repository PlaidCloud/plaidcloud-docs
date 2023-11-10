---
title: func.to_date
slug: func-to-date
weight: 3.0
description: The TO_DATE function accepts an argument of a character data type and converts this value to a DATETIME value
date: 2022-01-25T07:39:54
---

The TO_DATE function accepts an argument of a character data type and converts this value to a DATETIME value

## Syntax
```python
func.to_date(text, text)
```

## Examples
```python
func.to_date(get_column(table, 'File Creation Date'), 'YYYYMMDD')
```
```python
func.to_date(table.Created_on, 'DD-MM-YYYY')
```
