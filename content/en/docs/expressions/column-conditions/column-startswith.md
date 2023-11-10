---
title: column.startswith
slug: column-startswith
weight: 13.0
description: The system function 'starts_with()' is used to determine whether the provided string starts with the specified prefix
date: 2022-01-25T07:39:53
---

The system function 'starts_with()' is used to determine whether the provided string starts with the specified prefix

## Syntax
```python
.startswith(string)
```

## Examples
```python
get_column(table, 'Zip Code').startswith('9')
```
```python
get_column(table1, 'GL Account').startswith('CORP')
```
