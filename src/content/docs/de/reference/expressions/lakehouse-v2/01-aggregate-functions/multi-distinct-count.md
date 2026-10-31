---
title: MULTI_DISTINCT_COUNT (Lakehouse v2)
description: MULTI_DISTINCT_COUNT – gibt die Anzahl der eindeutigen Werte zurück. Entspricht COUNT(DISTINCT).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/multi-distinct-count.md
---

Gibt die Anzahl der eindeutigen Werte zurück. Entspricht COUNT(DISTINCT).

## Analyze-Syntax

```python
func.multi_distinct_count(get_column(table, 'dept'))
```

## Analyze-Beispiele

```python
func.multi_distinct_count(get_column(table, 'department'))

┌───┐
│ 5 │
└───┘
```

## SQL-Syntax

```sql
MULTI_DISTINCT_COUNT(<dept>)
```

## SQL-Beispiele

```sql
SELECT MULTI_DISTINCT_COUNT(department) FROM employees;

┌───┐
│ 5 │
└───┘
```
