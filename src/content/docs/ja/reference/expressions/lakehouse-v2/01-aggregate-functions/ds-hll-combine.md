---
title: DS_HLL_COMBINE（Lakehouse v2）
description: DS_HLL_COMBINE — 複数のDataSketches HLLスケッチを1つのスケッチに結合します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/ds-hll-combine.md
---

複数のDataSketches HLLスケッチを1つのスケッチに結合します。

## Analyzeの構文

```python
func.ds_hll_combine(get_column(table, 'hll_sketch'))
```

## Analyzeの例

```python
func.ds_hll_combine(get_column(table, 'hll_sketch'))

┌───────────────────┐
│ (combined sketch) │
└───────────────────┘
```

## SQLの構文

```sql
DS_HLL_COMBINE(<sketch_column>)
```

## SQLの例

```sql
SELECT DS_HLL_ESTIMATE(DS_HLL_COMBINE(sketch_col)) FROM daily_sketches;

┌───────┐
│ 25000 │
└───────┘
```
