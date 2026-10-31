---
title: COS (Lakehouse v1)
description: COS — devuelve el coseno de x, donde x se expresa en radianes.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/cos.md
---

Devuelve el coseno de `x`, donde `x` se expresa en radianes.

## Sintaxis de Analyze

```python
func.cos( <x> )
```

## Ejemplos de Analyze

```python
func.cos(func.pi())

┌─────────────────────┐
│ func.cos(func.pi()) │
├─────────────────────┤
│                  -1 │
└─────────────────────┘
```

## Sintaxis de SQL

```sql
COS( <x> )
```

## Ejemplos de SQL

```sql
SELECT COS(PI());

┌───────────┐
│ cos(pi()) │
├───────────┤
│        -1 │
└───────────┘
```
