---
title: AVG (Lakehouse v2)
description: AVG — 返回数值列的平均值。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/avg.md
---

返回数值列的平均值。

## Analyze 语法

```python
func.avg(get_column(table, 'salary'))
```

## Analyze 示例

```python
func.avg(get_column(table, 'salary'))
```

## SQL 语法

```sql
AVG(<salary>)
```

## SQL 示例

```sql
SELECT department, AVG(salary) FROM employees GROUP BY department;

┌────────────┬──────────────┐
│ department │ avg(salary)  │
├────────────┼──────────────┤
│ Sales      │     65000.00 │
│ IT         │     82000.00 │
└────────────┴──────────────┘
```
