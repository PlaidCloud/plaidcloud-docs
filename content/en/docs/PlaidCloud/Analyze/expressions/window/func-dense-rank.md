---
title: func.dense_rank
slug: func-dense-rank
description: The DENSE_RANK() is a window function that assigns a rank to each row within a partition of a result set
date: 2022-01-25T07:40:02
---

The DENSE_RANK() is a window function that assigns a rank to each row within a partition of a result set

## Syntax
```python
func.dense_rank().over(partition_by=field, order_by=field)
```
