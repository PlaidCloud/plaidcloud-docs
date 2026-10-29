---
title: ARRAY_AGGREGATE (Lakehouse v1)
description: ARRAY_AGGREGATE — agrega los elementos del arreglo con una función de agregación.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-aggregate.md
---

Agrega los elementos del arreglo con una función de agregación.

## Sintaxis de Analyze

```python
func.array_aggregate( <array>, '<agg_func>' )
```

- Las funciones de agregación admitidas incluyen `avg`, `count`, `max`, `min`, `sum`, `any`, `stddev_samp`, `stddev_pop`, `stddev`, `std`, `median`, `approx_count_distinct`, `kurtosis` y `skewness`.

- La sintaxis se puede reescribir como `func.array_<agg_func>( <array> )`. Por ejemplo, `func.array_avg( <array> )`.

## Ejemplos de Analyze

```python
func.array_aggregate([1, 2, 3, 4], 'sum'), func.array_sum([1, 2, 3, 4])

┌──────────────────────────────────────────────────────────────────────────┐
│ func.array_aggregate([1, 2, 3, 4], 'sum')  │ func.array_sum([1, 2, 3, 4])│
├────────────────────────────────────────────┼─────────────────────────────┤
│                                         10 │                          10 │
└──────────────────────────────────────────────────────────────────────────┘
```

## Sintaxis de SQL

```sql
ARRAY_AGGREGATE( <array>, '<agg_func>' )
```

- Las funciones de agregación admitidas incluyen `avg`, `count`, `max`, `min`, `sum`, `any`, `stddev_samp`, `stddev_pop`, `stddev`, `std`, `median`, `approx_count_distinct`, `kurtosis` y `skewness`.

- La sintaxis se puede reescribir como `ARRAY_<agg_func>( <array> )`. Por ejemplo, `ARRAY_AVG( <array> )`.

## Ejemplos de SQL

```sql
SELECT ARRAY_AGGREGATE([1, 2, 3, 4], 'SUM'), ARRAY_SUM([1, 2, 3, 4]);

┌────────────────────────────────────────────────────────────────┐
│ array_aggregate([1, 2, 3, 4], 'sum') │ array_sum([1, 2, 3, 4]) │
├──────────────────────────────────────┼─────────────────────────┤
│                                   10 │                      10 │
└────────────────────────────────────────────────────────────────┘
```
