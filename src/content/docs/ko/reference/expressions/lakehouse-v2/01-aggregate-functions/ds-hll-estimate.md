---
title: DS_HLL_ESTIMATE (Lakehouse v2)
description: DS_HLL_ESTIMATE — DataSketches HLL 스케치에서 카디널리티를 추정합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/ds-hll-estimate.md
---

DataSketches HLL 스케치에서 카디널리티를 추정합니다.

## Analyze 구문

```python
func.ds_hll_estimate(get_column(table, 'hll_sketch'))
```

## Analyze 예제

```python
func.ds_hll_estimate(get_column(table, 'hll_sketch'))

┌──────┐
│ 9856 │
└──────┘
```

## SQL 구문

```sql
DS_HLL_ESTIMATE(<sketch>)
```

## SQL 예제

```sql
SELECT DS_HLL_ESTIMATE(DS_HLL_ACCUMULATE(user_id)) FROM visits;

┌──────┐
│ 9856 │
└──────┘
```
