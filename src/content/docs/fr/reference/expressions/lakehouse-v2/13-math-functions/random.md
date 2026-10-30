---
title: RANDOM (Lakehouse v2)
description: RANDOM — renvoie une valeur aléatoire à virgule flottante comprise entre 0 et 1. Alias de `RAND`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/random.md
---

Renvoie une valeur aléatoire à virgule flottante comprise entre 0 et 1. Alias de `RAND`.

## Syntaxe Analyze

```python
func.random([<seed>])
```

## Exemples Analyze

```python
func.random()

┌───────────┐
│ 0.8123...  │
└───────────┘
```

## Syntaxe SQL

```sql
RANDOM([<seed>])
```

## Exemples SQL

```sql
SELECT RANDOM();

┌───────────┐
│ 0.8123...  │
└───────────┘
```
