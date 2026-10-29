---
title: MIN_BY (Lakehouse v2)
description: MIN_BY — renvoie la valeur d'une colonne associée à la valeur minimale d'une autre colonne.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/min-by.md
---

Renvoie la valeur d'une colonne associée à la valeur minimale d'une autre colonne.

## Syntaxe Analyze

```python
func.min_by(get_column(table, 'name'), get_column(table, 'salary'))
```

## Exemples Analyze

```python
func.min_by(get_column(table, 'name'), get_column(table, 'salary'))

┌─────┐
│ Bob │
└─────┘
```

## Syntaxe SQL

```sql
MIN_BY(<name>, <salary>)
```

## Exemples SQL

```sql
SELECT MIN_BY(name, salary) FROM employees;

┌─────┐
│ Bob │
└─────┘
```
