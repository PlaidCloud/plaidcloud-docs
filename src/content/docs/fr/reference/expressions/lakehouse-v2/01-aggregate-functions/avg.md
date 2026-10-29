---
title: AVG (Lakehouse v2)
description: AVG — renvoie la valeur moyenne d'une colonne numérique.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/avg.md
---

Renvoie la valeur moyenne d'une colonne numérique.

## Syntaxe Analyze

```python
func.avg(get_column(table, 'salary'))
```

## Exemples Analyze

```python
func.avg(get_column(table, 'salary'))
```

## Syntaxe SQL

```sql
AVG(<salary>)
```

## Exemples SQL

```sql
SELECT department, AVG(salary) FROM employees GROUP BY department;

┌────────────┬──────────────┐
│ department │ avg(salary)  │
├────────────┼──────────────┤
│ Sales      │     65000.00 │
│ IT         │     82000.00 │
└────────────┴──────────────┘
```
