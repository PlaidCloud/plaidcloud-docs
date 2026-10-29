---
title: SIGN (Lakehouse v1)
description: SIGN — devuelve el signo del argumento como -1, 0 o 1, según si x es negativo, cero o positivo.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/sign.md
---

Devuelve el signo del argumento como -1, 0 o 1, según si `x` es negativo, cero o positivo, o NULL si el argumento era NULL.

## Sintaxis de Analyze

```python
func.sign( <x> )
```

## Ejemplos de Analyze

```python
func.sign(0)

┌──────────────┐
│ func.sign(0) │
├──────────────┤
│            0 │
└──────────────┘
```

## Sintaxis de SQL

```sql
SIGN( <x> )
```

## Ejemplos de SQL

```sql
SELECT SIGN(0);

┌─────────┐
│ sign(0) │
├─────────┤
│       0 │
└─────────┘
```
