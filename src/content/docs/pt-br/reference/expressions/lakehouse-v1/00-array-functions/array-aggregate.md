---
title: ARRAY_AGGREGATE (Lakehouse v1)
description: ARRAY_AGGREGATE agrega os elementos do array com uma função de agregação.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-aggregate.md
---

Agrega os elementos do array com uma função de agregação.

## Sintaxe do Analyze

```python
func.array_aggregate( <array>, '<agg_func>' )
```

- As funções de agregação compatíveis incluem `avg`, `count`, `max`, `min`, `sum`, `any`, `stddev_samp`, `stddev_pop`, `stddev`, `std`, `median`, `approx_count_distinct`, `kurtosis` e `skewness`.

- A sintaxe pode ser reescrita como `func.array_<agg_func>( <array> )`. Por exemplo, `func.array_avg( <array> )`.

## Exemplos do Analyze

```python
func.array_aggregate([1, 2, 3, 4], 'sum'), func.array_sum([1, 2, 3, 4])

┌──────────────────────────────────────────────────────────────────────────┐
│ func.array_aggregate([1, 2, 3, 4], 'sum')  │ func.array_sum([1, 2, 3, 4])│
├────────────────────────────────────────────┼─────────────────────────────┤
│                                         10 │                          10 │
└──────────────────────────────────────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
ARRAY_AGGREGATE( <array>, '<agg_func>' )
```

- As funções de agregação compatíveis incluem `avg`, `count`, `max`, `min`, `sum`, `any`, `stddev_samp`, `stddev_pop`, `stddev`, `std`, `median`, `approx_count_distinct`, `kurtosis` e `skewness`.

- A sintaxe pode ser reescrita como `ARRAY_<agg_func>( <array> )`. Por exemplo, `ARRAY_AVG( <array> )`.

## Exemplos de SQL

```sql
SELECT ARRAY_AGGREGATE([1, 2, 3, 4], 'SUM'), ARRAY_SUM([1, 2, 3, 4]);

┌────────────────────────────────────────────────────────────────┐
│ array_aggregate([1, 2, 3, 4], 'sum') │ array_sum([1, 2, 3, 4]) │
├──────────────────────────────────────┼─────────────────────────┤
│                                   10 │                      10 │
└────────────────────────────────────────────────────────────────┘
```
