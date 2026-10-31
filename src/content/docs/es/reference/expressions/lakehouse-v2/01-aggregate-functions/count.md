---
title: COUNT (Lakehouse v2)
description: COUNT devuelve el número de filas o de valores distintos de NULL.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/count.md
---

Devuelve el número de filas o de valores distintos de NULL.

## Sintaxis de Analyze

```python
func.count()
```

## Ejemplos de Analyze

```python
func.count()
```

## Sintaxis de SQL

```sql
COUNT()
```

## Ejemplos de SQL

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
