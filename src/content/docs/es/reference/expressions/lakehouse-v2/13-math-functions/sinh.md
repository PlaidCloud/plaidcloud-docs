---
title: SINH (Lakehouse v2)
description: SINH — devuelve el seno hiperbólico de un número.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/sinh.md
---

Devuelve el seno hiperbólico de un número.

## Sintaxis de Analyze

```python
func.sinh(<x>)
```

## Ejemplos de Analyze

```python
func.sinh(0)

┌─────┐
│ 0.0  │
└─────┘
```

## Sintaxis de SQL

```sql
SINH(<x>)
```

## Ejemplos de SQL

```sql
SELECT SINH(0);

┌─────┐
│ 0.0  │
└─────┘
```
