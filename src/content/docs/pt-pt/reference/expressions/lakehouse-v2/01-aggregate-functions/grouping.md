---
title: GROUPING (Lakehouse v2)
description: "Utilize a função de agregação GROUPING no PlaidCloud Lakehouse. Indica se uma coluna especificada numa cláusula GROUP BY é agregada. Devolve 1 se for agregada."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/grouping.md
---

Indica se uma coluna especificada numa cláusula GROUP BY é agregada. Devolve 1 se for agregada e 0 caso contrário.

## Sintaxe do Analyze

```python
func.grouping(get_column(table, 'department'))
```

## Exemplos do Analyze

```python
func.grouping(get_column(table, 'department'))
```

## Sintaxe SQL

```sql
GROUPING(<department>)
```

## Exemplos de SQL

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
