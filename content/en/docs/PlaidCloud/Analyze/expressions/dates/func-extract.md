---
title: func.extract
slug: func-extract
weight: 8.0
description: Retrieves subfields such as year or hour from date/time values
date: 2022-01-25T07:39:55
---

Retrieves subfields such as year or hour from date/time values

## Syntax
```python
func.extract(field, timestamp or interval)
```

## Examples
```python
func.extract('seconds', table.OutlierTime)
```
