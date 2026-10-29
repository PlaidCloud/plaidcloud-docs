---
title: DS_HLL_COMBINE (Lakehouse v2)
description: DS_HLL_COMBINE：将多个 DataSketches HLL 草图合并为单个草图。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/ds-hll-combine.md
---

将多个 DataSketches HLL 草图合并为单个草图。

## Analyze 语法

```python
func.ds_hll_combine(get_column(table, 'hll_sketch'))
```

## Analyze 示例

```python
func.ds_hll_combine(get_column(table, 'hll_sketch'))

┌───────────────────┐
│ (combined sketch) │
└───────────────────┘
```

## SQL 语法

```sql
DS_HLL_COMBINE(<sketch_column>)
```

## SQL 示例

```sql
SELECT DS_HLL_ESTIMATE(DS_HLL_COMBINE(sketch_col)) FROM daily_sketches;

┌───────┐
│ 25000 │
└───────┘
```
