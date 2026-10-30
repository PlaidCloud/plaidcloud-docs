---
title: HLL_HASH (Lakehouse v2)
description: HLL_HASH – berechnet einen HLL-Hash eines Werts.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/16-scalar-functions/hll-hash.md
---

Berechnet einen HLL-Hash eines Werts.

## Analyze-Syntax

```python
func.hll_hash(<expr>)
```

## Analyze-Beispiele

```python
func.hll_hash('user_123')

┌───────┐
│ (hll)  │
└───────┘
```

## SQL-Syntax

```sql
HLL_HASH(<expr>)
```

## SQL-Beispiele

```sql
SELECT HLL_CARDINALITY(HLL_HASH('user_123'));

┌───┐
│ 1  │
└───┘
```
