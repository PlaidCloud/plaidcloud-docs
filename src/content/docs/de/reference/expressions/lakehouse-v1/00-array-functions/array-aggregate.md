---
title: ARRAY_AGGREGATE (Lakehouse v1)
description: ARRAY_AGGREGATE – aggregiert die Elemente des Arrays mit einer Aggregatfunktion.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-aggregate.md
---

Aggregiert die Elemente des Arrays mit einer Aggregatfunktion.

## Analyze-Syntax

```python
func.array_aggregate( <array>, '<agg_func>' )
```

- Zu den unterstützten Aggregatfunktionen gehören `avg`, `count`, `max`, `min`, `sum`, `any`, `stddev_samp`, `stddev_pop`, `stddev`, `std`, `median`, `approx_count_distinct`, `kurtosis` und `skewness`.

- Die Syntax lässt sich als `func.array_<agg_func>( <array> )` schreiben. Beispiel: `func.array_avg( <array> )`.

## Analyze-Beispiele

```python
func.array_aggregate([1, 2, 3, 4], 'sum'), func.array_sum([1, 2, 3, 4])

┌──────────────────────────────────────────────────────────────────────────┐
│ func.array_aggregate([1, 2, 3, 4], 'sum')  │ func.array_sum([1, 2, 3, 4])│
├────────────────────────────────────────────┼─────────────────────────────┤
│                                         10 │                          10 │
└──────────────────────────────────────────────────────────────────────────┘
```

## SQL-Syntax

```sql
ARRAY_AGGREGATE( <array>, '<agg_func>' )
```

- Zu den unterstützten Aggregatfunktionen gehören `avg`, `count`, `max`, `min`, `sum`, `any`, `stddev_samp`, `stddev_pop`, `stddev`, `std`, `median`, `approx_count_distinct`, `kurtosis` und `skewness`.

- Die Syntax lässt sich als `ARRAY_<agg_func>( <array> )` schreiben. Beispiel: `ARRAY_AVG( <array> )`.

## SQL-Beispiele

```sql
SELECT ARRAY_AGGREGATE([1, 2, 3, 4], 'SUM'), ARRAY_SUM([1, 2, 3, 4]);

┌────────────────────────────────────────────────────────────────┐
│ array_aggregate([1, 2, 3, 4], 'sum') │ array_sum([1, 2, 3, 4]) │
├──────────────────────────────────────┼─────────────────────────┤
│                                   10 │                      10 │
└────────────────────────────────────────────────────────────────┘
```
