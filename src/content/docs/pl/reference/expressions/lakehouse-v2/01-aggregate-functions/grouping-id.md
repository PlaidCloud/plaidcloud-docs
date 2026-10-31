---
title: GROUPING_ID (Lakehouse v2)
description: GROUPING_ID — zwraca maskę bitową odpowiadającą grupowaniu kolumn.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/grouping-id.md
---

Zwraca maskę bitową odpowiadającą grupowaniu kolumn.

## Składnia Analyze

```python
func.grouping_id(get_column(table, 'a'), get_column(table, 'b'))
```

## Przykłady Analyze

```python
func.grouping_id(get_column(table, 'department'), get_column(table, 'year'))

┌───┐
│ 0 │
└───┘
```

## Składnia SQL

```sql
GROUPING_ID(<a>, <b>)
```

## Przykłady SQL

```sql
SELECT department, year, GROUPING_ID(department, year), SUM(salary)
FROM employees GROUP BY ROLLUP(department, year);

┌───┐
│ 0 │
└───┘
```
