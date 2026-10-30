---
title: COT (Lakehouse v1)
description: COT — renvoie la cotangente de x, où x est exprimé en radians.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/cot.md
---

Renvoie la cotangente de `x`, où `x` est exprimé en radians.

## Syntaxe Analyze

```python
func.cot( <x> )
```

## Exemples Analyze

```python
func.cot(12) 

┌─────────────────────┐
│    func.cot(12)     │
├─────────────────────┤
│ -1.5726734063976895 │
└─────────────────────┘
```

## Syntaxe SQL

```sql
COT( <x> )
```

## Exemples SQL

```sql
SELECT COT(12);

┌─────────────────────┐
│       cot(12)       │
├─────────────────────┤
│ -1.5726734063976895 │
└─────────────────────┘
```
