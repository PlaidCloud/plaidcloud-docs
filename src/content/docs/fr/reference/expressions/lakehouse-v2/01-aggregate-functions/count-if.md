---
title: COUNT_IF (Lakehouse v2)
description: COUNT_IF — renvoie le nombre de lignes pour lesquelles l'expression est TRUE.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/count-if.md
---

Renvoie le nombre de lignes pour lesquelles l'expression est TRUE.

## Syntaxe Analyze

```python
func.count_if(get_column(table, 'salary') > 80000)
```

## Exemples Analyze

```python
func.count_if(get_column(table, 'salary') > 80000)

┌────┐
│ 42 │
└────┘
```

## Syntaxe SQL

```sql
COUNT_IF(<salary> > 80000)
```

## Exemples SQL

```sql
SELECT COUNT_IF(salary > 80000) FROM employees;

┌────┐
│ 42 │
└────┘
```
