---
title: HLL_HASH (Lakehouse v2)
description: HLL_HASH — 値のHLLハッシュを計算します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/16-scalar-functions/hll-hash.md
---

値のHLLハッシュを計算します。

## Analyzeの構文

```python
func.hll_hash(<expr>)
```

## Analyzeの例

```python
func.hll_hash('user_123')

┌───────┐
│ (hll)  │
└───────┘
```

## SQLの構文

```sql
HLL_HASH(<expr>)
```

## SQLの例

```sql
SELECT HLL_CARDINALITY(HLL_HASH('user_123'));

┌───┐
│ 1  │
└───┘
```
