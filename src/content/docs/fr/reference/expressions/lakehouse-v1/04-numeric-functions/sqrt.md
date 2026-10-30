---
title: SQRT (Lakehouse v1)
description: SQRT — renvoie la racine carrée d'un nombre positif ou nul x.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/sqrt.md
---

Renvoie la racine carrée d'un nombre positif ou nul `x`. Renvoie NaN pour une entrée négative.

## Syntaxe Analyze

```python
func.sqrt( <x> )
```

## Exemples Analyze

```python
func.sqrt(4)

┌──────────────┐
│ func.sqrt(4) │
├──────────────┤
│            2 │
└──────────────┘
```

## Syntaxe SQL

```sql
SQRT( <x> )
```

## Exemples SQL

```sql
SELECT SQRT(4);

┌─────────┐
│ sqrt(4) │
├─────────┤
│       2 │
└─────────┘
```
