---
title: ANY_VALUE (Lakehouse v2)
description: ANY_VALUE：从一组行中返回任意一个值。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/any-value.md
---

从一组行中返回任意一个值。

## Analyze 语法

```python
func.any_value(get_column(table, 'department'))
```

## Analyze 示例

```python
func.any_value(get_column(table, 'department'))

┌───────┐
│ Sales │
└───────┘
```

## SQL 语法

```sql
ANY_VALUE(<department>)
```

## SQL 示例

```sql
SELECT ANY_VALUE(department) FROM employees;

┌───────┐
│ Sales │
└───────┘
```
