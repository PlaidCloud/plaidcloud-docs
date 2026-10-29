---
title: HLL_UNION_AGG (Lakehouse v2)
description: HLL_UNION_AGG：通过计算并集来聚合 HLL 值。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/hll-union-agg.md
---

通过计算并集来聚合 HLL 值。

## Analyze 语法

```python
func.hll_union_agg(get_column(table, 'hll_col'))
```

## Analyze 示例

```python
func.hll_union_agg(get_column(table, 'hll_col'))

┌─────────────┐
│ (hll value) │
└─────────────┘
```

## SQL 语法

```sql
HLL_UNION_AGG(<hll_col>)
```

## SQL 示例

```sql
SELECT HLL_CARDINALITY(HLL_UNION_AGG(hll_col)) FROM segments;

┌──────┐
│ 8000 │
└──────┘
```
