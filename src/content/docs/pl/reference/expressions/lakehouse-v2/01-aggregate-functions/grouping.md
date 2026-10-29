---
title: GROUPING (Lakehouse v2)
description: "Użyj funkcji agregującej GROUPING w PlaidCloud Lakehouse. Wskazuje, czy wskazana kolumna w klauzuli GROUP BY jest agregowana. Zwraca 1, jeśli jest agregowana."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/grouping.md
---

Wskazuje, czy wskazana kolumna w klauzuli GROUP BY jest agregowana. Zwraca 1, jeśli jest agregowana, w przeciwnym razie 0.

## Składnia Analyze

```python
func.grouping(get_column(table, 'department'))
```

## Przykłady Analyze

```python
func.grouping(get_column(table, 'department'))
```

## Składnia SQL

```sql
GROUPING(<department>)
```

## Przykłady SQL

```sql
SELECT department, GROUPING(department), SUM(salary)
FROM employees GROUP BY ROLLUP(department);

┌────────────┬───────────────────────┬─────────────┐
│ department │ grouping(department)  │ sum(salary)  │
├────────────┼───────────────────────┼─────────────┤
│ Sales      │                     0 │      195000 │
│ IT         │                     0 │      246000 │
│ NULL       │                     1 │      441000 │
└────────────┴───────────────────────┴─────────────┘
```
