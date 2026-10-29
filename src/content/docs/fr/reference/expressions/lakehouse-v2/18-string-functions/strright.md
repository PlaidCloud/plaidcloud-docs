---
title: STRRIGHT (Lakehouse v2)
description: STRRIGHT — renvoie les N derniers caractères d'une chaîne, en partant de la droite. Alias de `RIGHT`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/strright.md
---

Renvoie les N derniers caractères d'une chaîne, en partant de la droite. Alias de `RIGHT`.

## Syntaxe Analyze

```python
func.strright(<str>, <len>)
```

## Exemples Analyze

```python
func.strright('StarRocks', 5)

┌─────────┐
│ 'Rocks'  │
└─────────┘
```

## Syntaxe SQL

```sql
STRRIGHT(<str>, <len>)
```

## Exemples SQL

```sql
SELECT STRRIGHT('StarRocks', 5);

┌───────┐
│ Rocks  │
└───────┘
```
