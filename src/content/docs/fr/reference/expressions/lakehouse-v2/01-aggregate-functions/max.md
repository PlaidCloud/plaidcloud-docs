---
title: MAX (Lakehouse v2)
description: MAX — renvoie la valeur maximale d'un ensemble de valeurs.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/max.md
---

Renvoie la valeur maximale d'un ensemble de valeurs.

## Syntaxe Analyze

```python
func.max(get_column(table, 'salary'))
```

## Exemples Analyze

```python
func.max(get_column(table, 'salary'))

┌────────┐
│ 150000 │
└────────┘
```

## Syntaxe SQL

```sql
MAX(<salary>)
```

## Exemples SQL

```sql
SELECT MAX(salary) FROM employees;

┌────────┐
│ 150000 │
└────────┘
```
