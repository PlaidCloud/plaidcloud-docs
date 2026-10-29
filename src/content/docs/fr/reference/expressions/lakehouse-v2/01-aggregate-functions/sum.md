---
title: SUM (Lakehouse v2)
description: SUM — renvoie la somme de toutes les valeurs d'un groupe.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/sum.md
---

Renvoie la somme de toutes les valeurs d'un groupe.

## Syntaxe Analyze

```python
func.sum(get_column(table, 'amount'))
```

## Exemples Analyze

```python
func.sum(get_column(table, 'amount'))
```

## Syntaxe SQL

```sql
SUM(<amount>)
```

## Exemples SQL

```sql
SELECT department, SUM(salary) FROM employees GROUP BY department;

┌────────────┬─────────────┐
│ department │ sum(salary) │
├────────────┼─────────────┤
│ Sales      │      195000 │
│ IT         │      246000 │
│ HR         │      210000 │
└────────────┴─────────────┘
```
