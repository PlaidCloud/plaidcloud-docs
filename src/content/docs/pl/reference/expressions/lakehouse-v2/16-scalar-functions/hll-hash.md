---
title: HLL_HASH (Lakehouse v2)
description: HLL_HASH — oblicza skrót HLL wartości.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/16-scalar-functions/hll-hash.md
---

Oblicza skrót HLL wartości.

## Składnia Analyze

```python
func.hll_hash(<expr>)
```

## Przykłady Analyze

```python
func.hll_hash('user_123')

┌───────┐
│ (hll)  │
└───────┘
```

## Składnia SQL

```sql
HLL_HASH(<expr>)
```

## Przykłady SQL

```sql
SELECT HLL_CARDINALITY(HLL_HASH('user_123'));

┌───┐
│ 1  │
└───┘
```
