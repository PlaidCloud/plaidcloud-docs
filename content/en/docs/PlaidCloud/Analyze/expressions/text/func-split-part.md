---
title: func.split_part
slug: func-split-part
description: The split_part function is used to split a given string based on a delimiter and pick out the desired field from the string
date: 2022-01-25T07:40:03
---

The split_part function is used to split a given string based on a delimiter and pick out the desired field from the string

## Syntax
```python
func.split_part(value_string, split_on_string, group_number_int)
```

## Examples
```python
func.split_part(table.PERIOD,  '_', 1)
```
