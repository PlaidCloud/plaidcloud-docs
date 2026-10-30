---
title: APPROX_COUNT_DISTINCT (Lakehouse v2)
description: APPROX_COUNT_DISTINCT — renvoie un nombre approximatif de valeurs distinctes à l'aide de HyperLogLog.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/approx-count-distinct.md
---

Renvoie un nombre approximatif de valeurs distinctes à l'aide de HyperLogLog.

## Syntaxe Analyze

```python
func.approx_count_distinct(get_column(table, 'user_id'))
```

## Exemples Analyze

```python
func.approx_count_distinct(get_column(table, 'user_id'))

┌─────┐
│ 985 │
└─────┘
```

## Syntaxe SQL

```sql
APPROX_COUNT_DISTINCT(<user_id>)
```

## Exemples SQL

```sql
SELECT APPROX_COUNT_DISTINCT(user_id) FROM page_views;

┌─────┐
│ 985 │
└─────┘
```
