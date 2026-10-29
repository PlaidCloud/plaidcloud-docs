---
title: MAX (Lakehouse v2)
description: MAX：返回一组值中的最大值。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/max.md
---

返回一组值中的最大值。

## Analyze 语法

```python
func.max(get_column(table, 'salary'))
```

## Analyze 示例

```python
func.max(get_column(table, 'salary'))

┌────────┐
│ 150000 │
└────────┘
```

## SQL 语法

```sql
MAX(<salary>)
```

## SQL 示例

```sql
SELECT MAX(salary) FROM employees;

┌────────┐
│ 150000 │
└────────┘
```
