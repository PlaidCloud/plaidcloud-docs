---
title: ARRAY_AGGREGATE (Lakehouse v1)
description: ARRAY_AGGREGATE — 배열의 요소를 집계 함수로 집계합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-aggregate.md
---

배열의 요소를 집계 함수로 집계합니다.

## Analyze 구문

```python
func.array_aggregate( <array>, '<agg_func>' )
```

- 지원되는 집계 함수에는 `avg`, `count`, `max`, `min`, `sum`, `any`, `stddev_samp`, `stddev_pop`, `stddev`, `std`, `median`, `approx_count_distinct`, `kurtosis`, `skewness`가 있습니다.

- 이 구문은 `func.array_<agg_func>( <array> )`로 바꿔 쓸 수 있습니다. 예를 들어 `func.array_avg( <array> )`입니다.

## Analyze 예제

```python
func.array_aggregate([1, 2, 3, 4], 'sum'), func.array_sum([1, 2, 3, 4])

┌──────────────────────────────────────────────────────────────────────────┐
│ func.array_aggregate([1, 2, 3, 4], 'sum')  │ func.array_sum([1, 2, 3, 4])│
├────────────────────────────────────────────┼─────────────────────────────┤
│                                         10 │                          10 │
└──────────────────────────────────────────────────────────────────────────┘
```

## SQL 구문

```sql
ARRAY_AGGREGATE( <array>, '<agg_func>' )
```

- 지원되는 집계 함수에는 `avg`, `count`, `max`, `min`, `sum`, `any`, `stddev_samp`, `stddev_pop`, `stddev`, `std`, `median`, `approx_count_distinct`, `kurtosis`, `skewness`가 있습니다.

- 이 구문은 `ARRAY_<agg_func>( <array> )`로 바꿔 쓸 수 있습니다. 예를 들어 `ARRAY_AVG( <array> )`입니다.

## SQL 예제

```sql
SELECT ARRAY_AGGREGATE([1, 2, 3, 4], 'SUM'), ARRAY_SUM([1, 2, 3, 4]);

┌────────────────────────────────────────────────────────────────┐
│ array_aggregate([1, 2, 3, 4], 'sum') │ array_sum([1, 2, 3, 4]) │
├──────────────────────────────────────┼─────────────────────────┤
│                                   10 │                      10 │
└────────────────────────────────────────────────────────────────┘
```
