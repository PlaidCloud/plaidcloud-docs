---
title: MULTI_DISTINCT_COUNT (Lakehouse v2)
description: MULTI_DISTINCT_COUNT — devuelve el número de valores distintos. Equivale a COUNT(DISTINCT).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/multi-distinct-count.md
---

Devuelve el número de valores distintos. Equivale a COUNT(DISTINCT).

## Sintaxis de Analyze

```python
func.multi_distinct_count(get_column(table, 'dept'))
```

## Ejemplos de Analyze

```python
func.multi_distinct_count(get_column(table, 'department'))

┌───┐
│ 5 │
└───┘
```

## Sintaxis de SQL

```sql
MULTI_DISTINCT_COUNT(<dept>)
```

## Ejemplos de SQL

```sql
SELECT MULTI_DISTINCT_COUNT(department) FROM employees;

┌───┐
│ 5 │
└───┘
```
