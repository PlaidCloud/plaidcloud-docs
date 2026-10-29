---
title: INTERSECT_COUNT (Lakehouse v2)
description: "Użyj funkcji bitmapowej INTERSECT_COUNT w PlaidCloud Lakehouse. Zwraca liczbę elementów w części wspólnej wielu bitmap przefiltrowanych według wymiaru."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/intersect-count.md
---

Zwraca liczbę elementów w części wspólnej wielu bitmap przefiltrowanych według wymiaru.

## Składnia Analyze

```python
func.intersect_count(get_column(table, 'bm'), get_column(table, 'dim'), val1, val2)
```

## Przykłady Analyze

```python
func.intersect_count(get_column(table, 'bm'), get_column(table, 'tag'), 1, 2)

┌─────┐
│ 150 │
└─────┘
```

## Składnia SQL

```sql
INTERSECT_COUNT(<bm>, <dim>, val1, val2)
```

## Przykłady SQL

```sql
SELECT INTERSECT_COUNT(user_bm, tag, 1, 2) FROM segments;

┌─────┐
│ 150 │
└─────┘
```
