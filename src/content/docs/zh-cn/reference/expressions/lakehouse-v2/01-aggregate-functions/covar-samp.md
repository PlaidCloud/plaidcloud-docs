---
title: COVAR_SAMP (Lakehouse v2)
description: COVAR_SAMP：返回两个表达式的样本协方差。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/covar-samp.md
---

返回两个表达式的样本协方差。

## Analyze 语法

```python
func.covar_samp(get_column(table, 'y'), get_column(table, 'x'))
```

## Analyze 示例

```python
func.covar_samp(get_column(table, 'height'), get_column(table, 'weight'))

┌────────┐
│ 103.01 │
└────────┘
```

## SQL 语法

```sql
COVAR_SAMP(<y>, <x>)
```

## SQL 示例

```sql
SELECT COVAR_SAMP(height, weight) FROM measurements;

┌────────┐
│ 103.01 │
└────────┘
```
