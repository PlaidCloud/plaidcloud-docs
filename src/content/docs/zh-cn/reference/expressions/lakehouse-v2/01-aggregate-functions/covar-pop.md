---
title: COVAR_POP (Lakehouse v2)
description: COVAR_POP：返回两个表达式的总体协方差。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/covar-pop.md
---

返回两个表达式的总体协方差。

## Analyze 语法

```python
func.covar_pop(get_column(table, 'y'), get_column(table, 'x'))
```

## Analyze 示例

```python
func.covar_pop(get_column(table, 'height'), get_column(table, 'weight'))

┌────────┐
│ 102.46 │
└────────┘
```

## SQL 语法

```sql
COVAR_POP(<y>, <x>)
```

## SQL 示例

```sql
SELECT COVAR_POP(height, weight) FROM measurements;

┌────────┐
│ 102.46 │
└────────┘
```
