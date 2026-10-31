---
title: LEFT (Lakehouse v2)
description: LEFT — renvoie les N premiers caractères d'une chaîne, en partant de la gauche.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/left.md
---

Renvoie les N premiers caractères d'une chaîne, en partant de la gauche.

## Syntaxe Analyze

```python
func.left(<str>, <len>)
```

## Exemples Analyze

```python
func.left('StarRocks', 4)

┌────────┐
│ 'Star'  │
└────────┘
```

## Syntaxe SQL

```sql
LEFT(<str>, <len>)
```

## Exemples SQL

```sql
SELECT LEFT('StarRocks', 4);

┌──────┐
│ Star  │
└──────┘
```
