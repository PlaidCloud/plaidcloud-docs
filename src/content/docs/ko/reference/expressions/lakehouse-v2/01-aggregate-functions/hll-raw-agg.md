---
title: HLL_RAW_AGG (Lakehouse v2)
description: HLL_RAW_AGG — HLL 값을 하나의 HLL 값으로 집계합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/hll-raw-agg.md
---

HLL 값을 하나의 HLL 값으로 집계합니다.

## Analyze 구문

```python
func.hll_raw_agg(get_column(table, 'hll_col'))
```

## Analyze 예제

```python
func.hll_raw_agg(get_column(table, 'hll_col'))

┌─────────────┐
│ (hll value) │
└─────────────┘
```

## SQL 구문

```sql
HLL_RAW_AGG(<hll_col>)
```

## SQL 예제

```sql
SELECT HLL_CARDINALITY(HLL_RAW_AGG(hll_col)) FROM sketches;

┌──────┐
│ 5000 │
└──────┘
```
