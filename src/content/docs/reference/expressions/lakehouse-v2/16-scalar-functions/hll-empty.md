---
title: HLL_EMPTY (Lakehouse v2)
description: HLL_EMPTY — returns an empty HLL value.
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
