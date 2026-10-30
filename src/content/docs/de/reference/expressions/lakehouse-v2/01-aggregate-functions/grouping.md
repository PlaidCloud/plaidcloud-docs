---
title: GROUPING (Lakehouse v2)
description: "Verwenden Sie die Aggregatfunktion GROUPING in PlaidCloud Lakehouse. Sie zeigt an, ob eine angegebene Spalte in einer GROUP-BY-Klausel aggregiert wird. Gibt 1 zurück, wenn sie aggregiert wird."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/grouping.md
---

Zeigt an, ob eine angegebene Spalte in einer GROUP-BY-Klausel aggregiert wird. Gibt 1 zurück, wenn sie aggregiert wird, sonst 0.

## Analyze-Syntax

```python
func.grouping(get_column(table, 'department'))
```

## Analyze-Beispiele

```python
func.grouping(get_column(table, 'department'))
```

## SQL-Syntax

```sql
GROUPING(<department>)
```

## SQL-Beispiele

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
