---
title: HLL_RAW_AGG（Lakehouse v2）
description: HLL_RAW_AGG — 複数のHLL値を1つのHLL値に集計します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/hll-raw-agg.md
---

複数のHLL値を1つのHLL値に集計します。

## Analyzeの構文

```python
func.hll_raw_agg(get_column(table, 'hll_col'))
```

## Analyzeの例

```python
func.hll_raw_agg(get_column(table, 'hll_col'))

┌─────────────┐
│ (hll value) │
└─────────────┘
```

## SQLの構文

```sql
HLL_RAW_AGG(<hll_col>)
```

## SQLの例

```sql
SELECT HLL_CARDINALITY(HLL_RAW_AGG(hll_col)) FROM sketches;

┌──────┐
│ 5000 │
└──────┘
```
