---
title: PERCENTILE_DISC_LC (Lakehouse v2)
description: PERCENTILE_DISC_LC — devuelve el valor del percentil mediante un algoritmo optimizado para baja cardinalidad.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/percentile-disc-lc.md
---

Devuelve el valor del percentil mediante un algoritmo optimizado para baja cardinalidad.

## Sintaxis de Analyze

```python
func.percentile_disc_lc(0.5)
```

## Ejemplos de Analyze

```python
func.percentile_disc_lc(0.5)

┌───────┐
│ 72000 │
└───────┘
```

## Sintaxis de SQL

```sql
PERCENTILE_DISC_LC(0.5)
```

## Ejemplos de SQL

```sql
SELECT PERCENTILE_DISC_LC(0.5) WITHIN GROUP (ORDER BY salary) FROM employees;

┌───────┐
│ 72000 │
└───────┘
```
