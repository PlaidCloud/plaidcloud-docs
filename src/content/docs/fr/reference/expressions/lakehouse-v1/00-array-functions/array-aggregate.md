---
title: ARRAY_AGGREGATE (Lakehouse v1)
description: "ARRAY_AGGREGATE : agrège les éléments du tableau avec une fonction d'agrégation."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-aggregate.md
---

Agrège les éléments du tableau avec une fonction d'agrégation.

## Syntaxe Analyze

```python
func.array_aggregate( <array>, '<agg_func>' )
```

- Les fonctions d'agrégation prises en charge incluent `avg`, `count`, `max`, `min`, `sum`, `any`, `stddev_samp`, `stddev_pop`, `stddev`, `std`, `median`, `approx_count_distinct`, `kurtosis` et `skewness`.

- La syntaxe peut être réécrite sous la forme `func.array_<agg_func>( <array> )`. Par exemple, `func.array_avg( <array> )`.

## Exemples Analyze

```python
func.array_aggregate([1, 2, 3, 4], 'sum'), func.array_sum([1, 2, 3, 4])

┌──────────────────────────────────────────────────────────────────────────┐
│ func.array_aggregate([1, 2, 3, 4], 'sum')  │ func.array_sum([1, 2, 3, 4])│
├────────────────────────────────────────────┼─────────────────────────────┤
│                                         10 │                          10 │
└──────────────────────────────────────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
ARRAY_AGGREGATE( <array>, '<agg_func>' )
```

- Les fonctions d'agrégation prises en charge incluent `avg`, `count`, `max`, `min`, `sum`, `any`, `stddev_samp`, `stddev_pop`, `stddev`, `std`, `median`, `approx_count_distinct`, `kurtosis` et `skewness`.

- La syntaxe peut être réécrite sous la forme `ARRAY_<agg_func>( <array> )`. Par exemple, `ARRAY_AVG( <array> )`.

## Exemples SQL

```sql
SELECT ARRAY_AGGREGATE([1, 2, 3, 4], 'SUM'), ARRAY_SUM([1, 2, 3, 4]);

┌────────────────────────────────────────────────────────────────┐
│ array_aggregate([1, 2, 3, 4], 'sum') │ array_sum([1, 2, 3, 4]) │
├──────────────────────────────────────┼─────────────────────────┤
│                                   10 │                      10 │
└────────────────────────────────────────────────────────────────┘
```
