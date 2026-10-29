---
title: ARRAY_AGGREGATE (Lakehouse v1)
description: ARRAY_AGGREGATE — agreguje elementy tablicy za pomocą funkcji agregującej.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-aggregate.md
---

Agreguje elementy tablicy za pomocą funkcji agregującej.

## Składnia Analyze

```python
func.array_aggregate( <array>, '<agg_func>' )
```

- Obsługiwane funkcje agregujące to m.in. `avg`, `count`, `max`, `min`, `sum`, `any`, `stddev_samp`, `stddev_pop`, `stddev`, `std`, `median`, `approx_count_distinct`, `kurtosis` oraz `skewness`.

- Składnię można zapisać jako `func.array_<agg_func>( <array> )`. Na przykład `func.array_avg( <array> )`.

## Przykłady Analyze

```python
func.array_aggregate([1, 2, 3, 4], 'sum'), func.array_sum([1, 2, 3, 4])

┌──────────────────────────────────────────────────────────────────────────┐
│ func.array_aggregate([1, 2, 3, 4], 'sum')  │ func.array_sum([1, 2, 3, 4])│
├────────────────────────────────────────────┼─────────────────────────────┤
│                                         10 │                          10 │
└──────────────────────────────────────────────────────────────────────────┘
```

## Składnia SQL

```sql
ARRAY_AGGREGATE( <array>, '<agg_func>' )
```

- Obsługiwane funkcje agregujące to m.in. `avg`, `count`, `max`, `min`, `sum`, `any`, `stddev_samp`, `stddev_pop`, `stddev`, `std`, `median`, `approx_count_distinct`, `kurtosis` oraz `skewness`.

- Składnię można zapisać jako `ARRAY_<agg_func>( <array> )`. Na przykład `ARRAY_AVG( <array> )`.

## Przykłady SQL

```sql
SELECT ARRAY_AGGREGATE([1, 2, 3, 4], 'SUM'), ARRAY_SUM([1, 2, 3, 4]);

┌────────────────────────────────────────────────────────────────┐
│ array_aggregate([1, 2, 3, 4], 'sum') │ array_sum([1, 2, 3, 4]) │
├──────────────────────────────────────┼─────────────────────────┤
│                                   10 │                      10 │
└────────────────────────────────────────────────────────────────┘
```
