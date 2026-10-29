---
title: CORR (Lakehouse v2)
description: CORR：返回两个表达式之间的皮尔逊相关系数。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/corr.md
---

返回两个表达式之间的皮尔逊相关系数。

## Analyze 语法

```python
func.corr(get_column(table, 'revenue'), get_column(table, 'ad_spend'))
```

## Analyze 示例

```python
func.corr(get_column(table, 'revenue'), get_column(table, 'ad_spend'))

┌───────┐
│ 0.872 │
└───────┘
```

## SQL 语法

```sql
CORR(<revenue>, <ad_spend>)
```

## SQL 示例

```sql
SELECT CORR(revenue, ad_spend) FROM marketing;

┌───────┐
│ 0.872 │
└───────┘
```
