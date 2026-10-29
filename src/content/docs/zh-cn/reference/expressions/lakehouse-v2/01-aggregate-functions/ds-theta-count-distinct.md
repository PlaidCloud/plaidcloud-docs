---
title: DS_THETA_COUNT_DISTINCT (Lakehouse v2)
description: "在 PlaidCloud Lakehouse 中使用 DS_THETA_COUNT_DISTINCT 聚合函数。使用 DataSketches Theta 算法返回近似去重计数，支持交集和差集等集合运算。"
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/ds-theta-count-distinct.md
---

使用 DataSketches Theta 算法返回近似去重计数。支持交集和差集等集合运算。

## Analyze 语法

```python
func.ds_theta_count_distinct(get_column(table, 'user_id'))
```

## Analyze 示例

```python
func.ds_theta_count_distinct(get_column(table, 'user_id'))

┌───────┐
│ 10035 │
└───────┘
```

## SQL 语法

```sql
DS_THETA_COUNT_DISTINCT(<expr>)
```

## SQL 示例

```sql
SELECT DS_THETA_COUNT_DISTINCT(user_id) FROM page_views;

┌───────┐
│ 10035 │
└───────┘
```
