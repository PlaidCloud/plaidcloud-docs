---
title: DEGREES (Lakehouse v1)
description: DEGREES — renvoie l'argument x converti de radians en degrés, où x est exprimé en radians.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/degrees.md
---

Renvoie l'argument `x` converti de radians en degrés, où `x` est exprimé en radians.

## Syntaxe Analyze

```python
func.degrees( <x> )
```

## Exemples Analyze

```python
func.degrees(func.pi())

┌─────────────────────────┐
│ func.degrees(func.pi()) │
├─────────────────────────┤
│                     180 │
└─────────────────────────┘
```

## Syntaxe SQL

```sql
DEGREES( <x> )
```

## Exemples SQL

```sql
SELECT DEGREES(PI());

┌───────────────┐
│ degrees(pi()) │
├───────────────┤
│           180 │
└───────────────┘
```
