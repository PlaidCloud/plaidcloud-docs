---
title: GROUPING (Lakehouse v2)
description: "Utilisez la fonction d'agrégation GROUPING dans PlaidCloud Lakehouse. Indique si une colonne spécifiée d'une clause GROUP BY est agrégée. Renvoie 1 si elle est agrégée."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/grouping.md
---

Indique si une colonne spécifiée d'une clause GROUP BY est agrégée. Renvoie 1 si elle est agrégée, 0 sinon.

## Syntaxe Analyze

```python
func.grouping(get_column(table, 'department'))
```

## Exemples Analyze

```python
func.grouping(get_column(table, 'department'))
```

## Syntaxe SQL

```sql
GROUPING(<department>)
```

## Exemples SQL

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
