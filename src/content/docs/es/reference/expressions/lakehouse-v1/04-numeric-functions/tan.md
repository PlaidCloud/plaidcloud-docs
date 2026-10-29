---
title: TAN (Lakehouse v1)
description: TAN — devuelve la tangente de x, donde x se expresa en radianes.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/tan.md
---

Devuelve la tangente de `x`, donde `x` se expresa en radianes.

## Sintaxis de Analyze

```python
func.tan( <x> )
```

## Ejemplos de Analyze

```python
func.tan(90)

┌────────────────────┐
│    func.tan(90)    │
├────────────────────┤
│ -1.995200412208242 │
└────────────────────┘
```

## Sintaxis de SQL

```sql
TAN( <x> )
```

## Ejemplos de SQL

```sql
SELECT TAN(90);

┌────────────────────┐
│       tan(90)      │
├────────────────────┤
│ -1.995200412208242 │
└────────────────────┘
```
