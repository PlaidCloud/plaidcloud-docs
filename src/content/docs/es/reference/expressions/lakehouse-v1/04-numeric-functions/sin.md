---
title: SIN (Lakehouse v1)
description: SIN — devuelve el seno de x, donde x se expresa en radianes.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/sin.md
---

Devuelve el seno de `x`, donde `x` se expresa en radianes.

## Sintaxis de Analyze

```python
func.sin( <x> )
```

## Ejemplos de Analyze

```python
func.sin(90)

┌────────────────────┐
│    func.sin(90)    │
├────────────────────┤
│ 0.8939966636005579 │
└────────────────────┘
```

## Sintaxis de SQL

```sql
SIN( <x> )
```

## Ejemplos de SQL

```sql
SELECT SIN(90);

┌────────────────────┐
│       sin(90)      │
├────────────────────┤
│ 0.8939966636005579 │
└────────────────────┘
```
