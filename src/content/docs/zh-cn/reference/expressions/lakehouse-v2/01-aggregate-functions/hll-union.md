---
title: HLL_UNION (Lakehouse v2)
description: HLL_UNION：返回多个 HLL 值的并集。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/hll-union.md
---

返回多个 HLL 值的并集。

## Analyze 语法

```python
func.hll_union(get_column(table, 'hll_col'))
```

## Analyze 示例

```python
func.hll_union(get_column(table, 'hll_col'))

┌─────────────┐
│ (hll value) │
└─────────────┘
```

## SQL 语法

```sql
HLL_UNION(<hll_col>)
```

## SQL 示例

```sql
SELECT HLL_CARDINALITY(HLL_UNION(hll_col)) FROM daily_sketches;

┌───────┐
│ 12500 │
└───────┘
```
