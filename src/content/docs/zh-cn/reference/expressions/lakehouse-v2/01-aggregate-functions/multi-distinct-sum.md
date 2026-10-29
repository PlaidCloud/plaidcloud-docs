---
title: MULTI_DISTINCT_SUM (Lakehouse v2)
description: MULTI_DISTINCT_SUM：返回不同值之和。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/multi-distinct-sum.md
---

返回不同值之和。

## Analyze 语法

```python
func.multi_distinct_sum(get_column(table, 'bonus'))
```

## Analyze 示例

```python
func.multi_distinct_sum(get_column(table, 'bonus'))

┌───────┐
│ 25000 │
└───────┘
```

## SQL 语法

```sql
MULTI_DISTINCT_SUM(<bonus>)
```

## SQL 示例

```sql
SELECT MULTI_DISTINCT_SUM(bonus) FROM employees;

┌───────┐
│ 25000 │
└───────┘
```
