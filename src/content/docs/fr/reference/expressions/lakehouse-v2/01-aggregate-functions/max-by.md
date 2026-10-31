---
title: MAX_BY (Lakehouse v2)
description: MAX_BY — renvoie la valeur d'une colonne associée à la valeur maximale d'une autre colonne.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/max-by.md
---

Renvoie la valeur d'une colonne associée à la valeur maximale d'une autre colonne.

## Syntaxe Analyze

```python
func.max_by(get_column(table, 'name'), get_column(table, 'salary'))
```

## Exemples Analyze

```python
func.max_by(get_column(table, 'name'), get_column(table, 'salary'))

┌───────┐
│ Alice │
└───────┘
```

## Syntaxe SQL

```sql
MAX_BY(<name>, <salary>)
```

## Exemples SQL

```sql
SELECT MAX_BY(name, salary) FROM employees;

┌───────┐
│ Alice │
└───────┘
```
