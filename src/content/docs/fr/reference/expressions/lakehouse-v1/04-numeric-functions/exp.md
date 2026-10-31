---
title: EXP (Lakehouse v1)
description: EXP — renvoie la valeur de e (la base des logarithmes naturels) élevée à la puissance x.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/exp.md
---

Renvoie la valeur de e (la base des logarithmes naturels) élevée à la puissance `x`.

## Syntaxe Analyze

```python
func.exp( <x> )
```

## Exemples Analyze

```python
func.exp(2)

┌──────────────────┐
│   func.exp(2)    │
├──────────────────┤
│ 7.38905609893065 │
└──────────────────┘
```

## Syntaxe SQL

```sql
EXP( <x> )
```

## Exemples SQL

```sql
SELECT EXP(2);

┌──────────────────┐
│      exp(2)      │
├──────────────────┤
│ 7.38905609893065 │
└──────────────────┘
```
