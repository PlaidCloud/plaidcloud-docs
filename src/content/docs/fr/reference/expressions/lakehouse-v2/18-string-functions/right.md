---
title: RIGHT (Lakehouse v2)
description: RIGHT — renvoie les N derniers caractères d'une chaîne, en partant de la droite.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/right.md
---

Renvoie les N derniers caractères d'une chaîne, en partant de la droite.

## Syntaxe Analyze

```python
func.right(<str>, <len>)
```

## Exemples Analyze

```python
func.right('StarRocks', 5)

┌─────────┐
│ 'Rocks'  │
└─────────┘
```

## Syntaxe SQL

```sql
RIGHT(<str>, <len>)
```

## Exemples SQL

```sql
SELECT RIGHT('StarRocks', 5);

┌───────┐
│ Rocks  │
└───────┘
```
