---
title: PERCENTILE_APPROX_WEIGHT
description: "Learn how to use the PERCENTILE_APPROX_WEIGHT aggregate function in PlaidCloud Lakehouse. Returns a weighted approximate percentile value."
---

Returns a weighted approximate percentile value.

## Analyze Syntax

```python
func.percentile_approx_weight(get_column(table, 'val'), get_column(table, 'weight'), 0.5)
```

## Analyze Examples

```python
func.percentile_approx_weight(get_column(table, 'val'), get_column(table, 'weight'), 0.5)

┌──────┐
│ 72.5 │
└──────┘
```

## SQL Syntax

```sql
PERCENTILE_APPROX_WEIGHT(<val>, <weight>, 0.5)
```

## SQL Examples

```sql
SELECT PERCENTILE_APPROX_WEIGHT(val, weight, 0.5) FROM data;

┌──────┐
│ 72.5 │
└──────┘
```
