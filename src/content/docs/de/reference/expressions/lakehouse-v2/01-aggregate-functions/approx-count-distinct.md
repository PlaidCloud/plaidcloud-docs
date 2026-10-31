---
title: APPROX_COUNT_DISTINCT (Lakehouse v2)
description: APPROX_COUNT_DISTINCT gibt mithilfe von HyperLogLog eine ungefähre Anzahl eindeutiger Werte zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/approx-count-distinct.md
---

Gibt mithilfe von HyperLogLog eine ungefähre Anzahl eindeutiger Werte zurück.

## Analyze-Syntax

```python
func.approx_count_distinct(get_column(table, 'user_id'))
```

## Analyze-Beispiele

```python
func.approx_count_distinct(get_column(table, 'user_id'))

┌─────┐
│ 985 │
└─────┘
```

## SQL-Syntax

```sql
APPROX_COUNT_DISTINCT(<user_id>)
```

## SQL-Beispiele

```sql
SELECT APPROX_COUNT_DISTINCT(user_id) FROM page_views;

┌─────┐
│ 985 │
└─────┘
```
