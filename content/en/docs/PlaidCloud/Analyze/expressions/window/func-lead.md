---
title: func.lead
slug: func-lead
description: This function provides access to more than one row of a table at the same time without a self join
date: 2022-01-25T07:40:02
---

This function provides access to more than one row of a table at the same time without a self join

## Syntax
```python
func.lead(field, 1).over(partition_by=field, order_by=field)
```
