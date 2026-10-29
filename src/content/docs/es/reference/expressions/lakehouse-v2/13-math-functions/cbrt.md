---
title: CBRT (Lakehouse v2)
description: CBRT — devuelve la raíz cúbica de un número.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/cbrt.md
---

Devuelve la raíz cúbica de un número.

## Sintaxis de Analyze

```python
func.cbrt(<x>)
```

## Ejemplos de Analyze

```python
func.cbrt(27)

┌─────┐
│ 3.0  │
└─────┘
```

## Sintaxis de SQL

```sql
CBRT(<x>)
```

## Ejemplos de SQL

```sql
SELECT CBRT(27);

┌─────┐
│ 3.0  │
└─────┘
```
