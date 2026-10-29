---
title: ARRAY_AGGREGATE (Lakehouse v1)
description: ARRAY_AGGREGATE — 集計関数を使用して、配列の要素を集計します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-aggregate.md
---

集計関数を使用して、配列の要素を集計します。

## Analyzeの構文

```python
func.array_aggregate( <array>, '<agg_func>' )
```

- 使用できる集計関数には、`avg`、`count`、`max`、`min`、`sum`、`any`、`stddev_samp`、`stddev_pop`、`stddev`、`std`、`median`、`approx_count_distinct`、`kurtosis`、`skewness`があります。

- この構文は、`func.array_<agg_func>( <array> )`の形式に書き換えることができます。たとえば、`func.array_avg( <array> )`です。

## Analyzeの例

```python
func.array_aggregate([1, 2, 3, 4], 'sum'), func.array_sum([1, 2, 3, 4])

┌──────────────────────────────────────────────────────────────────────────┐
│ func.array_aggregate([1, 2, 3, 4], 'sum')  │ func.array_sum([1, 2, 3, 4])│
├────────────────────────────────────────────┼─────────────────────────────┤
│                                         10 │                          10 │
└──────────────────────────────────────────────────────────────────────────┘
```

## SQLの構文

```sql
ARRAY_AGGREGATE( <array>, '<agg_func>' )
```

- 使用できる集計関数には、`avg`、`count`、`max`、`min`、`sum`、`any`、`stddev_samp`、`stddev_pop`、`stddev`、`std`、`median`、`approx_count_distinct`、`kurtosis`、`skewness`があります。

- この構文は、`ARRAY_<agg_func>( <array> )`の形式に書き換えることができます。たとえば、`ARRAY_AVG( <array> )`です。

## SQLの例

```sql
SELECT ARRAY_AGGREGATE([1, 2, 3, 4], 'SUM'), ARRAY_SUM([1, 2, 3, 4]);

┌────────────────────────────────────────────────────────────────┐
│ array_aggregate([1, 2, 3, 4], 'sum') │ array_sum([1, 2, 3, 4]) │
├──────────────────────────────────────┼─────────────────────────┤
│                                   10 │                      10 │
└────────────────────────────────────────────────────────────────┘
```
