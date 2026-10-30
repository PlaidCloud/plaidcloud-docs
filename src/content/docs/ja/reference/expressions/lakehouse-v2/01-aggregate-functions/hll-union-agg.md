---
title: HLL_UNION_AGG（Lakehouse v2）
description: HLL_UNION_AGG — 和集合を計算してHLL値を集計します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/hll-union-agg.md
---

和集合を計算してHLL値を集計します。

## Analyzeの構文

```python
func.hll_union_agg(get_column(table, 'hll_col'))
```

## Analyzeの例

```python
func.hll_union_agg(get_column(table, 'hll_col'))

┌─────────────┐
│ (hll value) │
└─────────────┘
```

## SQLの構文

```sql
HLL_UNION_AGG(<hll_col>)
```

## SQLの例

```sql
SELECT HLL_CARDINALITY(HLL_UNION_AGG(hll_col)) FROM segments;

┌──────┐
│ 8000 │
└──────┘
```
