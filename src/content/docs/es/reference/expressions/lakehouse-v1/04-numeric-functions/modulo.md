---
title: MODULO (Lakehouse v1)
description: MODULO — devuelve el resto de dividir x entre y.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/modulo.md
---

Devuelve el resto de dividir `x` entre `y`. Si `y` es 0, devuelve un error.

## Sintaxis de Analyze

```python
func.modulo( <x>, <y> )
```

## Ejemplos de Analyze

```python
func.modulo(9, 2)

┌───────────────────┐
│ func.modulo(9, 2) │
├───────────────────┤
│                 1 │
└───────────────────┘
```

## Sintaxis de SQL

```sql
MODULO( <x>, <y> )
```

## Alias

- [MOD](../mod)

## Ejemplos de SQL

```sql
SELECT MOD(9, 2), MODULO(9, 2);

┌──────────────────────────┐
│ mod(9, 2) │ modulo(9, 2) │
├───────────┼──────────────┤
│         1 │            1 │
└──────────────────────────┘
```
