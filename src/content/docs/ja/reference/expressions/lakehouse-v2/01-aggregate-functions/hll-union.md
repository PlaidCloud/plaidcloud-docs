---
title: HLL_UNION（Lakehouse v2）
description: HLL_UNION — 複数のHLL値の和集合を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/hll-union.md
---

複数のHLL値の和集合を返します。

## Analyzeの構文

```python
func.hll_union(get_column(table, 'hll_col'))
```

## Analyzeの例

```python
func.hll_union(get_column(table, 'hll_col'))

┌─────────────┐
│ (hll value) │
└─────────────┘
```

## SQLの構文

```sql
HLL_UNION(<hll_col>)
```

## SQLの例

```sql
SELECT HLL_CARDINALITY(HLL_UNION(hll_col)) FROM daily_sketches;

┌───────┐
│ 12500 │
└───────┘
```
