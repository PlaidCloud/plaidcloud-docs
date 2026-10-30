---
title: GROUPING (Lakehouse v2)
description: "Use a função de agregação GROUPING no PlaidCloud Lakehouse. Indica se uma coluna especificada em uma cláusula GROUP BY está agregada. Retorna 1 se estiver agregada."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/grouping.md
---

Indica se uma coluna especificada em uma cláusula GROUP BY está agregada. Retorna 1 se estiver agregada e 0 caso contrário.

## Sintaxe no Analyze

```python
func.grouping(get_column(table, 'department'))
```

## Exemplos no Analyze

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
