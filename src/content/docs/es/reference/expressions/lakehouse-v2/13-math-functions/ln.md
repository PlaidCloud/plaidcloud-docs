---
title: LN (Lakehouse v2)
description: LN — devuelve el logaritmo natural de un número.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/ln.md
---

Devuelve el logaritmo natural de un número.

## Sintaxis de Analyze

```python
func.ln(<x>)
```

## Ejemplos de Analyze

```python
func.ln(2.718281828459045)

┌─────┐
│ 1.0  │
└─────┘
```

## Sintaxis de SQL

```sql
LN(<x>)
```

## Ejemplos de SQL

```sql
SELECT LN(EXP(1));

┌─────┐
│ 1.0  │
└─────┘
```
