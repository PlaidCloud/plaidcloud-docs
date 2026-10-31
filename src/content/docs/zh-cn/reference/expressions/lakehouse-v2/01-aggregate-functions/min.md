---
title: MIN (Lakehouse v2)
description: MIN：返回一组值中的最小值。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/min.md
---

返回一组值中的最小值。

## Analyze 语法

```python
func.min(get_column(table, 'salary'))
```

## Analyze 示例

```python
func.min(get_column(table, 'salary'))

┌───────┐
│ 35000 │
└───────┘
```

## SQL 语法

```sql
MIN(<salary>)
```

## SQL 示例

```sql
SELECT MIN(salary) FROM employees;

┌───────┐
│ 35000 │
└───────┘
```
