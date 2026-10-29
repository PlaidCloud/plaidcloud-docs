---
title: GROUPING_ID (Lakehouse v2)
description: GROUPING_ID gibt eine Bitmaske zurück, die der Gruppierung von Spalten entspricht.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/grouping-id.md
---

Gibt eine Bitmaske zurück, die der Gruppierung von Spalten entspricht.

## Analyze-Syntax

```python
func.grouping_id(get_column(table, 'a'), get_column(table, 'b'))
```

## Analyze-Beispiele

```python
func.grouping_id(get_column(table, 'department'), get_column(table, 'year'))

┌───┐
│ 0 │
└───┘
```

## SQL-Syntax

```sql
GROUPING_ID(<a>, <b>)
```

## SQL-Beispiele

```sql
SELECT department, year, GROUPING_ID(department, year), SUM(salary)
FROM employees GROUP BY ROLLUP(department, year);

┌───┐
│ 0 │
└───┘
```
