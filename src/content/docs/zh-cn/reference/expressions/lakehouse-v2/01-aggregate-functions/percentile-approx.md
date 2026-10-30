---
title: PERCENTILE_APPROX (Lakehouse v2)
description: PERCENTILE_APPROX：使用 t-digest 算法返回近似百分位数。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/percentile-approx.md
---

使用 t-digest 算法返回近似百分位数。

## Analyze 语法

```python
func.percentile_approx(get_column(table, 'response_time'), 0.95)
```

## Analyze 示例

```python
func.percentile_approx(get_column(table, 'response_time'), 0.95)

┌───────┐
│ 245.3 │
└───────┘
```

## SQL 语法

```sql
PERCENTILE_APPROX(<response_time>, 0.95)
```

## SQL 示例

```sql
SELECT PERCENTILE_APPROX(response_time, 0.95) FROM requests;

┌───────┐
│ 245.3 │
└───────┘
```
