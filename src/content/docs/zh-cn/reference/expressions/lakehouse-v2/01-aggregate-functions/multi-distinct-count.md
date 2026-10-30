---
title: MULTI_DISTINCT_COUNT (Lakehouse v2)
description: MULTI_DISTINCT_COUNT：返回不同值的个数，等同于 COUNT(DISTINCT)。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/multi-distinct-count.md
---

返回不同值的个数，等同于 COUNT(DISTINCT)。

## Analyze 语法

```python
func.multi_distinct_count(get_column(table, 'dept'))
```

## Analyze 示例

```python
func.multi_distinct_count(get_column(table, 'department'))

┌───┐
│ 5 │
└───┘
```

## SQL 语法

```sql
MULTI_DISTINCT_COUNT(<dept>)
```

## SQL 示例

```sql
SELECT MULTI_DISTINCT_COUNT(department) FROM employees;

┌───┐
│ 5 │
└───┘
```
