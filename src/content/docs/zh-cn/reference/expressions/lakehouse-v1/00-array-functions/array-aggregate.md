---
title: ARRAY_AGGREGATE (Lakehouse v1)
description: ARRAY_AGGREGATE：使用聚合函数对数组中的元素进行聚合。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-aggregate.md
---

使用聚合函数对数组中的元素进行聚合。

## Analyze 语法

```python
func.array_aggregate( <array>, '<agg_func>' )
```

- 支持的聚合函数包括 `avg`、`count`、`max`、`min`、`sum`、`any`、`stddev_samp`、`stddev_pop`、`stddev`、`std`、`median`、`approx_count_distinct`、`kurtosis` 和 `skewness`。

- 该语法可以改写为 `func.array_<agg_func>( <array> )`。例如 `func.array_avg( <array> )`。

## Analyze 示例

```python
func.array_aggregate([1, 2, 3, 4], 'sum'), func.array_sum([1, 2, 3, 4])

┌──────────────────────────────────────────────────────────────────────────┐
│ func.array_aggregate([1, 2, 3, 4], 'sum')  │ func.array_sum([1, 2, 3, 4])│
├────────────────────────────────────────────┼─────────────────────────────┤
│                                         10 │                          10 │
└──────────────────────────────────────────────────────────────────────────┘
```

## SQL 语法

```sql
ARRAY_AGGREGATE( <array>, '<agg_func>' )
```

- 支持的聚合函数包括 `avg`、`count`、`max`、`min`、`sum`、`any`、`stddev_samp`、`stddev_pop`、`stddev`、`std`、`median`、`approx_count_distinct`、`kurtosis` 和 `skewness`。

- 该语法可以改写为 `ARRAY_<agg_func>( <array> )`。例如 `ARRAY_AVG( <array> )`。

## SQL 示例

```sql
SELECT ARRAY_AGGREGATE([1, 2, 3, 4], 'SUM'), ARRAY_SUM([1, 2, 3, 4]);

┌────────────────────────────────────────────────────────────────┐
│ array_aggregate([1, 2, 3, 4], 'sum') │ array_sum([1, 2, 3, 4]) │
├──────────────────────────────────────┼─────────────────────────┤
│                                   10 │                      10 │
└────────────────────────────────────────────────────────────────┘
```
