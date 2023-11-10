---
title: cast
slug: cast
weight: 1.0
description: The CAST() function converts a value (of any type) into a specified datatype
date: 2022-01-25T07:39:54
---

The CAST() function converts a value (of any type) into a specified datatype

## Syntax
```python
cast(value, target_type)
```

## Examples
```python
cast(table.transaction_year, Numeric)
```
```python
cast(get_column(table, 'End_Date'),Text)
```
