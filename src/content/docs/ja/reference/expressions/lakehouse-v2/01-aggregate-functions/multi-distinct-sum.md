---
title: MULTI_DISTINCT_SUM (Lakehouse v2)
description: MULTI_DISTINCT_SUM — 重複を除いた値の合計を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/multi-distinct-sum.md
---

重複を除いた値の合計を返します。

## Analyzeの構文

```python
func.multi_distinct_sum(get_column(table, 'bonus'))
```

## Analyzeの例

```python
func.multi_distinct_sum(get_column(table, 'bonus'))

┌───────┐
│ 25000 │
└───────┘
```

## SQLの構文

```sql
MULTI_DISTINCT_SUM(<bonus>)
```

## SQLの例

```sql
SELECT MULTI_DISTINCT_SUM(bonus) FROM employees;

┌───────┐
│ 25000 │
└───────┘
```
