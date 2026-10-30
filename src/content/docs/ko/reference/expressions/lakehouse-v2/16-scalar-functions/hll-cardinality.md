---
title: HLL_CARDINALITY (Lakehouse v2)
description: HLL_CARDINALITY — HLL 값에서 카디널리티 추정치를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/16-scalar-functions/hll-cardinality.md
---

HLL 값에서 카디널리티 추정치를 반환합니다.

## Analyze 구문

```python
func.hll_cardinality(<hll>)
```

## Analyze 예제

```python
func.hll_cardinality(get_column(table, 'hll_col'))

┌───────┐
│ 10000  │
└───────┘
```

## SQL 구문

```sql
HLL_CARDINALITY(<hll>)
```

## SQL 예제

```sql
SELECT HLL_CARDINALITY(hll_col) FROM sketches;

┌───────┐
│ 10000  │
└───────┘
```
