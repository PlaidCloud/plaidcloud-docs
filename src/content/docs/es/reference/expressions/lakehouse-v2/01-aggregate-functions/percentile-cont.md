---
title: "PERCENTILE_CONT (Agregación, Lakehouse v2)"
description: PERCENTILE_CONT — devuelve un valor de percentil interpolado a partir de una distribución continua.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/percentile-cont.md
---

Devuelve un valor de percentil interpolado a partir de una distribución continua.

## Sintaxis de Analyze

```python
func.percentile_cont(0.5)
```

## Ejemplos de Analyze

```python
func.percentile_cont(0.5)

┌──────────┐
│ 72500.00 │
└──────────┘
```

## Sintaxis de SQL

```sql
PERCENTILE_CONT(0.5)
```

## Ejemplos de SQL

```sql
SELECT PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY salary) FROM employees;

┌──────────┐
│ 72500.00 │
└──────────┘
```
