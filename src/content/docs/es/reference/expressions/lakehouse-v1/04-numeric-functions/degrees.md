---
title: DEGREES (Lakehouse v1)
description: DEGREES — devuelve el argumento x convertido de radianes a grados, donde x se expresa en radianes.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/degrees.md
---

Devuelve el argumento `x` convertido de radianes a grados, donde `x` se expresa en radianes.

## Sintaxis de Analyze

```python
func.degrees( <x> )
```

## Ejemplos de Analyze

```python
func.degrees(func.pi())

┌─────────────────────────┐
│ func.degrees(func.pi()) │
├─────────────────────────┤
│                     180 │
└─────────────────────────┘
```

## Sintaxis de SQL

```sql
DEGREES( <x> )
```

## Ejemplos de SQL

```sql
SELECT DEGREES(PI());

┌───────────────┐
│ degrees(pi()) │
├───────────────┤
│           180 │
└───────────────┘
```
