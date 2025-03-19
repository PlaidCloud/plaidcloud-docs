---
title: JSON_MAP_TRANSFORM_VALUES
---

Applies a transformation to each value in a JSON object using a [lambda expression](../../00-sql-reference/42-lambda-expressions).

## SQL Syntax

```sql
JSON_MAP_TRANSFORM_VALUES(<json_object>, (<key>, <value>) -> <value_transformation>)
```

## Return Type

Returns a JSON object with the same keys as the input JSON object, but with values modified according to the specified lambda transformation.

## SQL Examples

This example appends " - Special Offer" to each product description:

```sql
SELECT JSON_MAP_TRANSFORM_VALUES('{"product1":"laptop", "product2":"phone"}'::VARIANT, (k, v) -> CONCAT(v, ' - Special Offer')) AS promo_descriptions;

┌──────────────────────────────────────────────────────────────────────────┐
│                            promo_descriptions                            │
├──────────────────────────────────────────────────────────────────────────┤
│ {"product1":"laptop - Special Offer","product2":"phone - Special Offer"} │
└──────────────────────────────────────────────────────────────────────────┘
```