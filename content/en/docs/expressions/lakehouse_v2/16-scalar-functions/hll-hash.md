---
title: HLL_HASH
description: "Learn how to use the HLL_HASH scalar function in PlaidCloud Lakehouse. Computes an HLL hash of a value - see syntax, examples, and output."
---

Computes an HLL hash of a value.

## Analyze Syntax

```python
func.hll_hash(<expr>)
```

## Analyze Examples

```python
func.hll_hash('user_123')

┌───────┐
│ (hll)  │
└───────┘
```

## SQL Syntax

```sql
HLL_HASH(<expr>)
```

## SQL Examples

```sql
SELECT HLL_CARDINALITY(HLL_HASH('user_123'));

┌───┐
│ 1  │
└───┘
```
