---
title: column.is_
slug: column-is
weight: 7.0
description: Checks if column conditions are met
date: 2022-01-25T07:39:54
---

Checks if column conditions are met

## Syntax
```python
.is_(value)
.is_(None)
```

## Examples
```python
get_column(table, 'Min SafetyStock').is_(None)
```
```python
get_column(table, 'date_pod').is_(None)
```
