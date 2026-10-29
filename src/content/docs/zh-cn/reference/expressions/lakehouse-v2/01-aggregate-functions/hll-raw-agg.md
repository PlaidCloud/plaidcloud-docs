---
title: HLL_RAW_AGG (Lakehouse v2)
description: HLL_RAW_AGG：将多个 HLL 值聚合为单个 HLL 值。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/hll-raw-agg.md
---

将多个 HLL 值聚合为单个 HLL 值。

## Analyze 语法

```python
func.hll_raw_agg(get_column(table, 'hll_col'))
```

## Analyze 示例

```python
func.hll_raw_agg(get_column(table, 'hll_col'))

┌─────────────┐
│ (hll value) │
└─────────────┘
```

## SQL 语法

```sql
HLL_RAW_AGG(<hll_col>)
```

## SQL 示例

```sql
SELECT HLL_CARDINALITY(HLL_RAW_AGG(hll_col)) FROM sketches;

┌──────┐
│ 5000 │
└──────┘
```
