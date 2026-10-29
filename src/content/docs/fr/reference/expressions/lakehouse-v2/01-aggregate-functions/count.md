---
title: COUNT (Lakehouse v2)
description: COUNT — renvoie le nombre de lignes ou de valeurs non NULL.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/count.md
---

Renvoie le nombre de lignes ou de valeurs non NULL.

## Syntaxe Analyze

```python
func.count()
```

## Exemples Analyze

```python
func.count()
```

## Syntaxe SQL

```sql
COUNT()
```

## Exemples SQL

```sql
SELECT COUNT(*) FROM employees;

┌──────────┐
│ count(*) │
├──────────┤
│     1000 │
└──────────┘

SELECT COUNT(DISTINCT department) FROM employees;

┌──────────────────────────────┐
│ count(distinct department)   │
├──────────────────────────────┤
│                            5 │
└──────────────────────────────┘
```
