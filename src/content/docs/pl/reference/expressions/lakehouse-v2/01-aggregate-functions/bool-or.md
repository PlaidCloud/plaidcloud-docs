---
title: BOOL_OR (Lakehouse v2)
description: BOOL_OR — zwraca TRUE, jeśli którakolwiek wartość w grupie ma wartość TRUE.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/bool-or.md
---

Zwraca TRUE, jeśli którakolwiek wartość w grupie ma wartość TRUE.

## Składnia Analyze

```python
func.bool_or(get_column(table, 'is_active'))
```

## Przykłady Analyze

```python
func.bool_or(get_column(table, 'is_active'))
```

## Składnia SQL

```sql
BOOL_OR(<is_active>)
```

## Przykłady SQL

```sql
SELECT department, BOOL_OR(is_active) FROM employees GROUP BY department;

┌────────────┬─────────────────────┐
│ department │ bool_or(is_active)  │
├────────────┼─────────────────────┤
│ Sales      │                   1 │
│ IT         │                   1 │
└────────────┴─────────────────────┘
```
