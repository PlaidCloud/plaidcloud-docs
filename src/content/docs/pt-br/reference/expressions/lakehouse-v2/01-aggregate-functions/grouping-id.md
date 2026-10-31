---
title: GROUPING_ID (Lakehouse v2)
description: GROUPING_ID — retorna uma máscara de bits correspondente ao agrupamento de colunas.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/grouping-id.md
---

Retorna uma máscara de bits correspondente ao agrupamento de colunas.

## Sintaxe no Analyze

```python
func.grouping_id(get_column(table, 'a'), get_column(table, 'b'))
```

## Exemplos no Analyze

```python
func.grouping_id(get_column(table, 'department'), get_column(table, 'year'))

┌───┐
│ 0 │
└───┘
```

## Sintaxe SQL

```sql
GROUPING_ID(<a>, <b>)
```

## Exemplos de SQL

```sql
SELECT department, year, GROUPING_ID(department, year), SUM(salary)
FROM employees GROUP BY ROLLUP(department, year);

┌───┐
│ 0 │
└───┘
```
