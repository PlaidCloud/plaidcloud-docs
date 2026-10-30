---
title: ATAN2 (Lakehouse v1)
description: ATAN2 — renvoie l'arc tangente des deux variables x et y.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/atan2.md
---

Renvoie l'arc tangente des deux variables `x` et `y`. Elle équivaut au calcul de l'arc tangente de `y` / `x`, sauf que les signes des deux arguments servent à déterminer le quadrant du résultat. `ATAN(y, x)` est un synonyme de `ATAN2(y, x)`.

## Syntaxe Analyze

```python
func.atan2( <y, x> )
```

## Exemples Analyze

```python
func.atan2((- 2), 2)

┌─────────────────────┐
│ func.atan2((- 2), 2)│
├─────────────────────┤
│ -0.7853981633974483 │
└─────────────────────┘
```

## Syntaxe SQL

```sql
ATAN2( <y, x> )
```

## Exemples SQL

```sql
SELECT ATAN2(-2, 2);

┌─────────────────────┐
│   atan2((- 2), 2)   │
├─────────────────────┤
│ -0.7853981633974483 │
└─────────────────────┘
```
