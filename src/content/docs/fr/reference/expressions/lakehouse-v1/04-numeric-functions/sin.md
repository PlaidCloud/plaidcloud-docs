---
title: SIN (Lakehouse v1)
description: SIN — renvoie le sinus de x, où x est exprimé en radians.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/sin.md
---

Renvoie le sinus de `x`, où `x` est exprimé en radians.

## Syntaxe Analyze

```python
func.sin( <x> )
```

## Exemples Analyze

```python
func.sin(90)

┌────────────────────┐
│    func.sin(90)    │
├────────────────────┤
│ 0.8939966636005579 │
└────────────────────┘
```

## Syntaxe SQL

```sql
SIN( <x> )
```

## Exemples SQL

```sql
SELECT SIN(90);

┌────────────────────┐
│       sin(90)      │
├────────────────────┤
│ 0.8939966636005579 │
└────────────────────┘
```
