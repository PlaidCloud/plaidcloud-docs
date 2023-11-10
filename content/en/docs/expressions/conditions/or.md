---
title: or_
slug: or
weight: 5.0
description: The or_ operator allows checking two or more conditions to determine if the evaluation is true or false.
date: 2022-01-25T07:39:47
---

The or_ operator allows checking two or more conditions to determine if the evaluation is true or false.

## Examples

**Example 1**
This example checks if the `period` is any of the three specified dates.
```python
or_(  
    table.period == '2020_10',  
    table.period == '2020_11',  
    table.period == '2020_12'  
)
```

**Example 2**
This example is checking if `order_reason_Include` is `null` or has the word `KEEP` as a value.
```python
or_(  
    table.order_reason_Include == 'KEEP',  
    table.order_reason_Include.is_(None)  
)
```
