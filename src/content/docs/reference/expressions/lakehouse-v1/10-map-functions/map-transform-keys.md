---
title: MAP_TRANSFORM_KEYS
description: "Learn how to use the MAP_TRANSFORM_KEYS map function in PlaidCloud Lakehouse. Applies a transformation to each key in a map using a lambda expression."
---

Applies a transformation to each key in a map using a lambda expression.

## SQL Syntax

```sql
MAP_TRANSFORM_KEYS(<map>, (<key>, <value>) -> <key_transformation>)
```

## Return Type

Returns a map with the same values as the input map but with keys modified according to the specified lambda transformation.

## SQL Examples

This example adds 1,000 to each product ID, creating a new map with updated keys while keeping the associated prices the same:

```sql
SELECT MAP_TRANSFORM_KEYS({101: 29.99, 102: 45.50, 103: 15.00}, (product_id, price) -> product_id + 1000) AS updated_product_ids;

┌────────────────────────────────────┐
│         updated_product_ids        │
├────────────────────────────────────┤
│ {1101:29.99,1102:45.50,1103:15.00} │
└────────────────────────────────────┘
```
