---
title: COUNT_IF (Lakehouse v2)
description: COUNT_IF：返回表达式为 TRUE 的行数。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/count-if.md
---

返回表达式为 TRUE 的行数。

## Analyze 语法

```python
func.count_if(get_column(table, 'salary') > 80000)
```

## Analyze 示例

```python
func.count_if(get_column(table, 'salary') > 80000)

┌────┐
│ 42 │
└────┘
```

## SQL 语法

```sql
COUNT_IF(<salary> > 80000)
```

## SQL 示例

```sql
SELECT COUNT_IF(salary > 80000) FROM employees;

┌────┐
│ 42 │
└────┘
```
