---
title: HLL_EMPTY (Lakehouse v2)
description: HLL_EMPTY — 空のHLL値を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/16-scalar-functions/hll-empty.md
---

空のHLL値を返します。

## Analyzeの構文

```python
func.hll_empty()
```

## Analyzeの例

```python
func.hll_empty()

┌─────────────┐
│ (empty hll)  │
└─────────────┘
```

## SQLの構文

```sql
HLL_EMPTY()
```

## SQLの例

```sql
SELECT HLL_CARDINALITY(HLL_EMPTY());

┌───┐
│ 0  │
└───┘
```
