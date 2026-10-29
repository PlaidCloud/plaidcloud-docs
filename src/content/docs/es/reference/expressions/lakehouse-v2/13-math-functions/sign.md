---
title: SIGN (Lakehouse v2)
description: "SIGN — devuelve el signo de un número: -1, 0 o 1."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/sign.md
---

Devuelve el signo de un número: -1, 0 o 1.

## Sintaxis de Analyze

```python
func.sign(<x>)
```

## Ejemplos de Analyze

```python
func.sign(-42)

┌────┐
│ -1  │
└────┘
```

## Sintaxis de SQL

```sql
SIGN(<x>)
```

## Ejemplos de SQL

```sql
SELECT SIGN(-42);

┌────┐
│ -1  │
└────┘
```
