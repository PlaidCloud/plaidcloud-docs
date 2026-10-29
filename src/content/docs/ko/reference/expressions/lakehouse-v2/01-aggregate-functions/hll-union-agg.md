---
title: HLL_UNION_AGG (Lakehouse v2)
description: HLL_UNION_AGG — 합집합을 계산하여 HLL 값을 집계합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/hll-union-agg.md
---

합집합을 계산하여 HLL 값을 집계합니다.

## Analyze 구문

```python
func.hll_union_agg(get_column(table, 'hll_col'))
```

## Analyze 예제

```python
func.hll_union_agg(get_column(table, 'hll_col'))

┌─────────────┐
│ (hll value) │
└─────────────┘
```

## SQL 구문

```sql
HLL_UNION_AGG(<hll_col>)
```

## SQL 예제

```sql
SELECT HLL_CARDINALITY(HLL_UNION_AGG(hll_col)) FROM segments;

┌──────┐
│ 8000 │
└──────┘
```
