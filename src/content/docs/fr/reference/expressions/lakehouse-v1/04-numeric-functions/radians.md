---
title: RADIANS (Lakehouse v1)
description: RADIANS — renvoie l'argument x converti de degrés en radians.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/radians.md
---

Renvoie l'argument `x` converti de degrés en radians.

## Syntaxe Analyze

```python
func.radians( <x> )
```

## Exemples Analyze

```python
func.radians(90)

┌────────────────────┐
│  func.radians(90)  │
├────────────────────┤
│ 1.5707963267948966 │
└────────────────────┘
```

## Syntaxe SQL

```sql
RADIANS( <x> )
```

## Exemples SQL

```sql
SELECT RADIANS(90);

┌────────────────────┐
│     radians(90)    │
├────────────────────┤
│ 1.5707963267948966 │
└────────────────────┘
```
