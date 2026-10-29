---
title: ACOS (Lakehouse v1)
description: ACOS — renvoie l'arc cosinus de x, c'est-à-dire la valeur dont le cosinus est x.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/acos.md
---

Renvoie l'arc cosinus de `x`, c'est-à-dire la valeur dont le cosinus est `x`. Renvoie NULL si `x` n'est pas compris entre -1 et 1.

## Syntaxe Analyze

```python
func.abs( <x> )
```

## Exemples Analyze

```python
func.abs(1)

┌──────────────┐
│ func.acos(1) │
├──────────────┤
│            0 │
└──────────────┘
```

## Syntaxe SQL

```sql
ACOS( <x> )
```

## Exemples SQL

```sql
SELECT ACOS(1);

┌─────────┐
│ acos(1) │
├─────────┤
│       0 │
└─────────┘
```
