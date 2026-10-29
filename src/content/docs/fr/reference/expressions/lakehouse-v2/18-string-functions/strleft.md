---
title: STRLEFT (Lakehouse v2)
description: STRLEFT — renvoie les N premiers caractères d'une chaîne, en partant de la gauche. Alias de `LEFT`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/strleft.md
---

Renvoie les N premiers caractères d'une chaîne, en partant de la gauche. Alias de `LEFT`.

## Syntaxe Analyze

```python
func.strleft(<str>, <len>)
```

## Exemples Analyze

```python
func.strleft('StarRocks', 4)

┌────────┐
│ 'Star'  │
└────────┘
```

## Syntaxe SQL

```sql
STRLEFT(<str>, <len>)
```

## Exemples SQL

```sql
SELECT STRLEFT('StarRocks', 4);

┌──────┐
│ Star  │
└──────┘
```
