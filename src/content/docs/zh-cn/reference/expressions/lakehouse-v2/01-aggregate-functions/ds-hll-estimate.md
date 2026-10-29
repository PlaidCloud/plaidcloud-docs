---
title: DS_HLL_ESTIMATE (Lakehouse v2)
description: DS_HLL_ESTIMATE：根据 DataSketches HLL 草图估算基数。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/ds-hll-estimate.md
---

根据 DataSketches HLL 草图估算基数。

## Analyze 语法

```python
func.ds_hll_estimate(get_column(table, 'hll_sketch'))
```

## Analyze 示例

```python
func.ds_hll_estimate(get_column(table, 'hll_sketch'))

┌──────┐
│ 9856 │
└──────┘
```

## SQL 语法

```sql
DS_HLL_ESTIMATE(<sketch>)
```

## SQL 示例

```sql
SELECT DS_HLL_ESTIMATE(DS_HLL_ACCUMULATE(user_id)) FROM visits;

┌──────┐
│ 9856 │
└──────┘
```
