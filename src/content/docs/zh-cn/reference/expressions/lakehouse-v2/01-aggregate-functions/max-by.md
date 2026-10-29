---
title: MAX_BY (Lakehouse v2)
description: MAX_BY：返回与另一列最大值对应的某一列的值。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/max-by.md
---

返回与另一列最大值对应的某一列的值。

## Analyze 语法

```python
func.max_by(get_column(table, 'name'), get_column(table, 'salary'))
```

## Analyze 示例

```python
func.max_by(get_column(table, 'name'), get_column(table, 'salary'))

┌───────┐
│ Alice │
└───────┘
```

## SQL 语法

```sql
MAX_BY(<name>, <salary>)
```

## SQL 示例

```sql
SELECT MAX_BY(name, salary) FROM employees;

┌───────┐
│ Alice │
└───────┘
```
