---
title: FLOOR (Lakehouse v1)
description: FLOOR — arrondit le nombre à l'entier inférieur.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/floor.md
---

Arrondit le nombre à l'entier inférieur.

## Syntaxe Analyze

```python
func.floor( <x> )
```

## Exemples Analyze

```python
func.floor(1.23)

┌──────────────────┐
│ func.floor(1.23) │
├──────────────────┤
│                1 │
└──────────────────┘
```

## Syntaxe SQL

```sql
FLOOR( <x> )
```

## Exemples SQL

```sql
SELECT FLOOR(1.23);

┌─────────────┐
│ floor(1.23) │
├─────────────┤
│           1 │
└─────────────┘
```
