---
title: HLL_EMPTY
description: "Learn how to use the HLL_EMPTY scalar function in PlaidCloud Lakehouse. Returns an empty HLL value - see syntax, examples, and output."
---

Returns an empty HLL value.

## Analyze Syntax

```python
func.hll_empty()
```

## Analyze Examples

```python
func.hll_empty()

┌─────────────┐
│ (empty hll)  │
└─────────────┘
```

## SQL Syntax

```sql
HLL_EMPTY()
```

## SQL Examples

```sql
SELECT HLL_CARDINALITY(HLL_EMPTY());

┌───┐
│ 0  │
└───┘
```
