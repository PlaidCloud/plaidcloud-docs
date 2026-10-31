---
title: RAND (Lakehouse v2)
description: RAND — renvoie une valeur aléatoire à virgule flottante comprise entre 0 (inclus) et 1 (exclu).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/rand.md
---

Renvoie une valeur aléatoire à virgule flottante comprise entre 0 (inclus) et 1 (exclu).

## Syntaxe Analyze

```python
func.rand([<seed>])
```

## Exemples Analyze

```python
func.rand()

┌───────────┐
│ 0.6347...  │
└───────────┘
```

## Syntaxe SQL

```sql
RAND([<seed>])
```

## Exemples SQL

```sql
SELECT RAND();

┌───────────┐
│ 0.6347...  │
└───────────┘
```
