---
title: MIN_BY (Lakehouse v2)
description: MIN_BY：返回与另一列最小值对应的某一列的值。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/min-by.md
---

返回与另一列最小值对应的某一列的值。

## Analyze 语法

```python
func.min_by(get_column(table, 'name'), get_column(table, 'salary'))
```

## Analyze 示例

```python
func.min_by(get_column(table, 'name'), get_column(table, 'salary'))

┌─────┐
│ Bob │
└─────┘
```

## SQL 语法

```sql
MIN_BY(<name>, <salary>)
```

## SQL 示例

```sql
SELECT MIN_BY(name, salary) FROM employees;

┌─────┐
│ Bob │
└─────┘
```
