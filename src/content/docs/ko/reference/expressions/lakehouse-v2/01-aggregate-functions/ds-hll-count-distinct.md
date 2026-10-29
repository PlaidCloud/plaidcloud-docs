---
title: DS_HLL_COUNT_DISTINCT (Lakehouse v2)
description: "PlaidCloud Lakehouse에서 DS_HLL_COUNT_DISTINCT 집계 함수를 사용합니다. DataSketches HLL 알고리즘을 사용하여 근사 고유 개수를 반환하며, 더 정확합니다."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/ds-hll-count-distinct.md
---

DataSketches HLL 알고리즘을 사용하여 근사 고유 개수를 반환합니다. `APPROX_COUNT_DISTINCT`보다 더 정확합니다.

## Analyze 구문

```python
func.ds_hll_count_distinct(get_column(table, 'user_id'))
```

## Analyze 예제

```python
func.ds_hll_count_distinct(get_column(table, 'user_id'))

┌───────┐
│ 10042 │
└───────┘
```

## SQL 구문

```sql
DS_HLL_COUNT_DISTINCT(<expr>)
```

## SQL 예제

```sql
SELECT DS_HLL_COUNT_DISTINCT(user_id) FROM page_views;

┌───────┐
│ 10042 │
└───────┘
```
