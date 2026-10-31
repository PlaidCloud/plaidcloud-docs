---
title: HLL_CARDINALITY (Lakehouse v2)
description: HLL_CARDINALITY — HLL値からカーディナリティの推定値を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/16-scalar-functions/hll-cardinality.md
---

HLL値からカーディナリティの推定値を返します。

## Analyzeの構文

```python
func.hll_cardinality(<hll>)
```

## Analyzeの例

```python
func.hll_cardinality(get_column(table, 'hll_col'))

┌───────┐
│ 10000  │
└───────┘
```

## SQLの構文

```sql
HLL_CARDINALITY(<hll>)
```

## SQLの例

```sql
SELECT HLL_CARDINALITY(hll_col) FROM sketches;

┌───────┐
│ 10000  │
└───────┘
```
