---
title: MULTI_DISTINCT_COUNT (Lakehouse v2)
description: MULTI_DISTINCT_COUNT — zwraca liczbę różnych wartości. Odpowiada COUNT(DISTINCT).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/multi-distinct-count.md
---

Zwraca liczbę różnych wartości. Odpowiada COUNT(DISTINCT).

## Składnia Analyze

```python
func.multi_distinct_count(get_column(table, 'dept'))
```

## Przykłady Analyze

```python
func.multi_distinct_count(get_column(table, 'department'))

┌───┐
│ 5 │
└───┘
```

## Składnia SQL

```sql
MULTI_DISTINCT_COUNT(<dept>)
```

## Przykłady SQL

```sql
SELECT MULTI_DISTINCT_COUNT(department) FROM employees;

┌───┐
│ 5 │
└───┘
```
