---
title: FACTORIAL (Lakehouse v1)
description: FACTORIAL — renvoie la factorielle de x.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/factorial.md
---

Renvoie la factorielle de `x`. Si `x` est inférieur ou égal à 0, la fonction renvoie 0.

## Syntaxe Analyze

```python
func.factorial( <x> )
```

## Exemples Analyze

```python
func.factorial(5)

┌───────────────────┐
│ func.factorial(5) │
├───────────────────┤
│               120 │
└───────────────────┘
```

## Syntaxe SQL

```sql
FACTORIAL( <x> )
```

## Exemples SQL

```sql
SELECT FACTORIAL(5);

┌──────────────┐
│ factorial(5) │
├──────────────┤
│          120 │
└──────────────┘
```
