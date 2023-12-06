---
title: column.between
slug: column-between
weight: 2.0
description: Returns true if the current column is between the lower bound and upper bound, inclusive
date: 2022-01-25T07:39:54
---

Returns true if the current column is between the lower bound and upper bound, inclusive

## Syntax
```python
.between(value_1, value_2)
```

## Examples
```python
get_column(table, 'LAST_CHANGED_DATE').between({start_date}, {end_date})
```
