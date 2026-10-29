---
title: HLL_CARDINALITY (Lakehouse v2)
description: HLL_CARDINALITY — 返回 HLL 值的基数估计值。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/16-scalar-functions/hll-cardinality.md
---

返回 HLL 值的基数估计值。

## Analyze 语法

```python
func.hll_cardinality(<hll>)
```

## Analyze 示例

```python
func.hll_cardinality(get_column(table, 'hll_col'))

┌───────┐
│ 10000  │
└───────┘
```

## SQL 语法

```sql
HLL_CARDINALITY(<hll>)
```

## SQL 示例

```sql
SELECT HLL_CARDINALITY(hll_col) FROM sketches;

┌───────┐
│ 10000  │
└───────┘
```
