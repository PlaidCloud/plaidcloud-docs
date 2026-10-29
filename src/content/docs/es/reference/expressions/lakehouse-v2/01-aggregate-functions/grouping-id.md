---
title: GROUPING_ID (Lakehouse v2)
description: GROUPING_ID devuelve una máscara de bits correspondiente a la agrupación de columnas.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/grouping-id.md
---

Devuelve una máscara de bits correspondiente a la agrupación de columnas.

## Sintaxis de Analyze

```python
func.grouping_id(get_column(table, 'a'), get_column(table, 'b'))
```

## Ejemplos de Analyze

```python
func.grouping_id(get_column(table, 'department'), get_column(table, 'year'))

┌───┐
│ 0 │
└───┘
```

## Sintaxis de SQL

```sql
GROUPING_ID(<a>, <b>)
```

## Ejemplos de SQL

```sql
SELECT department, year, GROUPING_ID(department, year), SUM(salary)
FROM employees GROUP BY ROLLUP(department, year);

┌───┐
│ 0 │
└───┘
```
