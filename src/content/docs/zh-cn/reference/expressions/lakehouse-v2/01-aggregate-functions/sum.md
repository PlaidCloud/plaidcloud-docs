---
title: SUM (Lakehouse v2)
description: SUM：返回分组内所有值之和。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/sum.md
---

返回分组内所有值之和。

## Analyze 语法

```python
func.sum(get_column(table, 'amount'))
```

## Analyze 示例

```python
func.sum(get_column(table, 'amount'))
```

## SQL 语法

```sql
SUM(<amount>)
```

## SQL 示例

```sql
SELECT department, SUM(salary) FROM employees GROUP BY department;

┌────────────┬─────────────┐
│ department │ sum(salary) │
├────────────┼─────────────┤
│ Sales      │      195000 │
│ IT         │      246000 │
│ HR         │      210000 │
└────────────┴─────────────┘
```
