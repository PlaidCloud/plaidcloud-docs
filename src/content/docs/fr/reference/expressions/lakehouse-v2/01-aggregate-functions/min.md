---
title: MIN (Lakehouse v2)
description: MIN — renvoie la valeur minimale d'un ensemble de valeurs.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/min.md
---

Renvoie la valeur minimale d'un ensemble de valeurs.

## Syntaxe Analyze

```python
func.min(get_column(table, 'salary'))
```

## Exemples Analyze

```python
func.min(get_column(table, 'salary'))

┌───────┐
│ 35000 │
└───────┘
```

## Syntaxe SQL

```sql
MIN(<salary>)
```

## Exemples SQL

```sql
SELECT MIN(salary) FROM employees;

┌───────┐
│ 35000 │
└───────┘
```
