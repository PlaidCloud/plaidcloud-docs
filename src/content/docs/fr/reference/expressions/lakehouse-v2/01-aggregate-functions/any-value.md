---
title: ANY_VALUE (Lakehouse v2)
description: ANY_VALUE — renvoie une valeur arbitraire parmi un groupe de lignes.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/any-value.md
---

Renvoie une valeur arbitraire parmi un groupe de lignes.

## Syntaxe Analyze

```python
func.any_value(get_column(table, 'department'))
```

## Exemples Analyze

```python
func.any_value(get_column(table, 'department'))

┌───────┐
│ Sales │
└───────┘
```

## Syntaxe SQL

```sql
ANY_VALUE(<department>)
```

## Exemples SQL

```sql
SELECT ANY_VALUE(department) FROM employees;

┌───────┐
│ Sales │
└───────┘
```
