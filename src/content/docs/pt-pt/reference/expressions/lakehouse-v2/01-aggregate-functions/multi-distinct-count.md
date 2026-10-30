---
title: MULTI_DISTINCT_COUNT (Lakehouse v2)
description: MULTI_DISTINCT_COUNT — devolve a contagem de valores distintos. Equivalente a COUNT(DISTINCT).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/multi-distinct-count.md
---

Devolve a contagem de valores distintos. Equivalente a COUNT(DISTINCT).

## Sintaxe do Analyze

```python
func.multi_distinct_count(get_column(table, 'dept'))
```

## Exemplos do Analyze

```python
func.multi_distinct_count(get_column(table, 'department'))

┌───┐
│ 5 │
└───┘
```

## Sintaxe SQL

```sql
MULTI_DISTINCT_COUNT(<dept>)
```

## Exemplos SQL

```sql
SELECT MULTI_DISTINCT_COUNT(department) FROM employees;

┌───┐
│ 5 │
└───┘
```
