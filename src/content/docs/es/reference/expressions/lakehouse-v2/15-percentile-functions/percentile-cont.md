---
title: "PERCENTILE_CONT (Percentil, Lakehouse v2)"
description: PERCENTILE_CONT — devuelve un valor de percentil interpolado basado en una distribución continua.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/15-percentile-functions/percentile-cont.md
---

Devuelve un valor de percentil interpolado basado en una distribución continua.

## Sintaxis de Analyze

```python
func.percentile_cont(<percentile>)
```

## Ejemplos de Analyze

```python
func.percentile_cont(0.5)

┌───────┐
│ 72500  │
└───────┘
```

## Sintaxis de SQL

```sql
PERCENTILE_CONT(<percentile>)
```

## Ejemplos de SQL

```sql
SELECT PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY salary) FROM employees;

┌───────┐
│ 72500  │
└───────┘
```
