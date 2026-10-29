---
title: COSH (Lakehouse v2)
description: COSH — devuelve el coseno hiperbólico de un número.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/cosh.md
---

Devuelve el coseno hiperbólico de un número.

## Sintaxis de Analyze

```python
func.cosh(<x>)
```

## Ejemplos de Analyze

```python
func.cosh(0)

┌─────┐
│ 1.0  │
└─────┘
```

## Sintaxis de SQL

```sql
COSH(<x>)
```

## Ejemplos de SQL

```sql
SELECT COSH(0);

┌─────┐
│ 1.0  │
└─────┘
```
