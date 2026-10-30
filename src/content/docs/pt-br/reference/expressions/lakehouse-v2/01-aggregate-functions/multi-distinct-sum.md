---
title: MULTI_DISTINCT_SUM (Lakehouse v2)
description: MULTI_DISTINCT_SUM — retorna a soma dos valores distintos.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/multi-distinct-sum.md
---

Retorna a soma dos valores distintos.

## Sintaxe do Analyze

```python
func.multi_distinct_sum(get_column(table, 'bonus'))
```

## Exemplos do Analyze

```python
func.multi_distinct_sum(get_column(table, 'bonus'))

┌───────┐
│ 25000 │
└───────┘
```

## Sintaxe SQL

```sql
MULTI_DISTINCT_SUM(<bonus>)
```

## Exemplos SQL

```sql
SELECT MULTI_DISTINCT_SUM(bonus) FROM employees;

┌───────┐
│ 25000 │
└───────┘
```
