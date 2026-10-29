---
title: DS_HLL_ESTIMATE（Lakehouse v2）
description: DS_HLL_ESTIMATE — DataSketches HLLスケッチからカーディナリティを推定します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/ds-hll-estimate.md
---

DataSketches HLLスケッチからカーディナリティを推定します。

## Analyzeの構文

```python
func.ds_hll_estimate(get_column(table, 'hll_sketch'))
```

## Analyzeの例

```python
func.ds_hll_estimate(get_column(table, 'hll_sketch'))

┌──────┐
│ 9856 │
└──────┘
```

## SQLの構文

```sql
DS_HLL_ESTIMATE(<sketch>)
```

## SQLの例

```sql
SELECT DS_HLL_ESTIMATE(DS_HLL_ACCUMULATE(user_id)) FROM visits;

┌──────┐
│ 9856 │
└──────┘
```
