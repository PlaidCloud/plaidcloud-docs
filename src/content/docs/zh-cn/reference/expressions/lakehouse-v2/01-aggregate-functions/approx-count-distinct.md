---
title: APPROX_COUNT_DISTINCT (Lakehouse v2)
description: APPROX_COUNT_DISTINCT：使用 HyperLogLog 返回不同值的近似数量。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/approx-count-distinct.md
---

使用 HyperLogLog 返回不同值的近似数量。

## Analyze 语法

```python
func.approx_count_distinct(get_column(table, 'user_id'))
```

## Analyze 示例

```python
func.approx_count_distinct(get_column(table, 'user_id'))

┌─────┐
│ 985 │
└─────┘
```

## SQL 语法

```sql
APPROX_COUNT_DISTINCT(<user_id>)
```

## SQL 示例

```sql
SELECT APPROX_COUNT_DISTINCT(user_id) FROM page_views;

┌─────┐
│ 985 │
└─────┘
```
