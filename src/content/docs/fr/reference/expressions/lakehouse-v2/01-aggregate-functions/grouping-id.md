---
title: GROUPING_ID (Lakehouse v2)
description: GROUPING_ID — renvoie un masque de bits correspondant au regroupement des colonnes.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/grouping-id.md
---

Renvoie un masque de bits correspondant au regroupement des colonnes.

## Syntaxe Analyze

```python
func.grouping_id(get_column(table, 'a'), get_column(table, 'b'))
```

## Exemples Analyze

```python
func.grouping_id(get_column(table, 'department'), get_column(table, 'year'))

┌───┐
│ 0 │
└───┘
```

## Syntaxe SQL

```sql
GROUPING_ID(<a>, <b>)
```

## Exemples SQL

```sql
SELECT department, year, GROUPING_ID(department, year), SUM(salary)
FROM employees GROUP BY ROLLUP(department, year);

┌───┐
│ 0 │
└───┘
```
