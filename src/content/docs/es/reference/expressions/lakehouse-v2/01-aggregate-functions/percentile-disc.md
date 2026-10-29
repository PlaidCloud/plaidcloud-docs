---
title: "PERCENTILE_DISC (Agregación, Lakehouse v2)"
description: "Use la función de agregación PERCENTILE_DISC en PlaidCloud Lakehouse. Devuelve el menor valor cuya distribución acumulada es >= el percentil especificado."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/percentile-disc.md
---

Devuelve el menor valor cuya distribución acumulada es >= el percentil especificado.

## Sintaxis de Analyze

```python
func.percentile_disc(0.5)
```

## Ejemplos de Analyze

```python
func.percentile_disc(0.5)

┌───────┐
│ 72000 │
└───────┘
```

## Sintaxis de SQL

```sql
PERCENTILE_DISC(0.5)
```

## Ejemplos de SQL

```sql
SELECT PERCENTILE_DISC(0.5) WITHIN GROUP (ORDER BY salary) FROM employees;

┌───────┐
│ 72000 │
└───────┘
```
