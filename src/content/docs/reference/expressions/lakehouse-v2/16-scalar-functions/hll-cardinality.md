---
title: HLL_CARDINALITY (Lakehouse v2)
description: HLL_CARDINALITY — Returns the cardinality estimate from an HLL value.
---

Returns the cardinality estimate from an HLL value.

## Analyze Syntax

```python
func.hll_cardinality(<hll>)
```

## Analyze Examples

```python
func.hll_cardinality(get_column(table, 'hll_col'))

┌───────┐
│ 10000  │
└───────┘
```

## SQL Syntax

```sql
HLL_CARDINALITY(<hll>)
```

## SQL Examples

```sql
SELECT HLL_CARDINALITY(hll_col) FROM sketches;

┌───────┐
│ 10000  │
└───────┘
```
