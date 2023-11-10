---
title: func.ntile
slug: func-ntile
description: This is a function that distributes rows of an ordered partition into a specified number of approximately equal groups, or buckets
date: 2022-01-25T07:40:01
---

This is a function that distributes rows of an ordered partition into a specified number of approximately equal groups, or buckets

## Syntax
```python
func.ntile(4).over(partition_by=field, order_by=field)
```
