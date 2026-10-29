---
title: COS (Lakehouse v1)
description: COS — renvoie le cosinus de x, où x est exprimé en radians.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/cos.md
---

Renvoie le cosinus de `x`, où `x` est exprimé en radians.

## Syntaxe Analyze

```python
func.cos( <x> )
```

## Exemples Analyze

```python
func.cos(func.pi())

┌─────────────────────┐
│ func.cos(func.pi()) │
├─────────────────────┤
│                  -1 │
└─────────────────────┘
```

## Syntaxe SQL

```sql
COS( <x> )
```

## Exemples SQL

```sql
SELECT COS(PI());

┌───────────┐
│ cos(pi()) │
├───────────┤
│        -1 │
└───────────┘
```
