---
title: APPROX_COUNT_DISTINCT (Lakehouse v2)
description: APPROX_COUNT_DISTINCT — retorna uma contagem aproximada de valores distintos usando HyperLogLog.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/approx-count-distinct.md
---

Retorna uma contagem aproximada de valores distintos usando HyperLogLog.

## Sintaxe no Analyze

```python
func.approx_count_distinct(get_column(table, 'user_id'))
```

## Exemplos no Analyze

```python
func.approx_count_distinct(get_column(table, 'user_id'))

┌─────┐
│ 985 │
└─────┘
```

## Sintaxe SQL

```sql
APPROX_COUNT_DISTINCT(<user_id>)
```

## Exemplos de SQL

```sql
SELECT APPROX_COUNT_DISTINCT(user_id) FROM page_views;

┌─────┐
│ 985 │
└─────┘
```
