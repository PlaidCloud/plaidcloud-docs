---
title: SUM (Lakehouse v2)
description: SUM — グループ内のすべての値の合計を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/sum.md
---

グループ内のすべての値の合計を返します。

## Analyzeの構文

```python
func.sum(get_column(table, 'amount'))
```

## Analyzeの例

```python
func.sum(get_column(table, 'amount'))
```

## SQLの構文

```sql
SUM(<amount>)
```

## SQLの例

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
