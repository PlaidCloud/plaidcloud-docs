---
title: TAN (Lakehouse v1)
description: TAN — renvoie la tangente de x, où x est exprimé en radians.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/tan.md
---

Renvoie la tangente de `x`, où `x` est exprimé en radians.

## Syntaxe Analyze

```python
func.tan( <x> )
```

## Exemples Analyze

```python
func.tan(90)

┌────────────────────┐
│    func.tan(90)    │
├────────────────────┤
│ -1.995200412208242 │
└────────────────────┘
```

## Syntaxe SQL

```sql
TAN( <x> )
```

## Exemples SQL

```sql
SELECT TAN(90);

┌────────────────────┐
│       tan(90)      │
├────────────────────┤
│ -1.995200412208242 │
└────────────────────┘
```
