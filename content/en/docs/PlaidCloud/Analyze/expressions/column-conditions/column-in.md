---
title: column.in_
slug: column-in
weight: 6.0
description: Checks if column conditions are met
date: 2022-01-25T07:39:54
---

Checks if column conditions are met

## Syntax
```python
.in_([list of values])
```

## Examples
```python
get_column(table, 'Source Country').in_(['CN','SG','BR'])
```
```python
table.MONTH.in_(['01','02','03','04','05','06','07','08','09'])
```
