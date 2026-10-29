---
title: HLL_UNION (Lakehouse v2)
description: HLL_UNION — 여러 HLL 값의 합집합을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/hll-union.md
---

여러 HLL 값의 합집합을 반환합니다.

## Analyze 구문

```python
func.hll_union(get_column(table, 'hll_col'))
```

## Analyze 예제

```python
func.hll_union(get_column(table, 'hll_col'))

┌─────────────┐
│ (hll value) │
└─────────────┘
```

## SQL 구문

```sql
HLL_UNION(<hll_col>)
```

## SQL 예제

```sql
SELECT HLL_CARDINALITY(HLL_UNION(hll_col)) FROM daily_sketches;

┌───────┐
│ 12500 │
└───────┘
```
