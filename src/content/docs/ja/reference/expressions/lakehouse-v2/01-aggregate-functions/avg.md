---
title: AVG (Lakehouse v2)
description: AVG — 数値列の平均値を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/avg.md
---

数値列の平均値を返します。

## Analyze の構文

```python
func.avg(get_column(table, 'salary'))
```

## Analyze の例

```python
func.avg(get_column(table, 'salary'))
```

## SQL の構文

```sql
AVG(<salary>)
```

## SQL の例

```sql
SELECT department, AVG(salary) FROM employees GROUP BY department;

┌────────────┬──────────────┐
│ department │ avg(salary)  │
├────────────┼──────────────┤
│ Sales      │     65000.00 │
│ IT         │     82000.00 │
└────────────┴──────────────┘
```
