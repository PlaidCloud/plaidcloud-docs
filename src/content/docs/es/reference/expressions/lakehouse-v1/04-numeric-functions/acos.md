---
title: ACOS (Lakehouse v1)
description: ACOS — devuelve el arcocoseno de x, es decir, el valor cuyo coseno es x.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/acos.md
---

Devuelve el arcocoseno de `x`, es decir, el valor cuyo coseno es `x`. Devuelve NULL si `x` no está en el rango de -1 a 1.

## Sintaxis de Analyze

```python
func.abs( <x> )
```

## Ejemplos de Analyze

```python
func.abs(1)

┌──────────────┐
│ func.acos(1) │
├──────────────┤
│            0 │
└──────────────┘
```

## Sintaxis de SQL

```sql
ACOS( <x> )
```

## Ejemplos de SQL

```sql
SELECT ACOS(1);

┌─────────┐
│ acos(1) │
├─────────┤
│       0 │
└─────────┘
```
