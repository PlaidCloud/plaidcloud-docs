---
title: STRPOS (Lakehouse v2)
description: STRPOS — renvoie la position de la première occurrence d'une sous-chaîne. Alias de `LOCATE`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/strpos.md
---

Renvoie la position de la première occurrence d'une sous-chaîne. Alias de `LOCATE`.

## Syntaxe Analyze

```python
func.strpos(<str>, <substr>)
```

## Exemples Analyze

```python
func.strpos('hello world', 'world')

┌───┐
│ 7  │
└───┘
```

## Syntaxe SQL

```sql
STRPOS(<str>, <substr>)
```

## Exemples SQL

```sql
SELECT STRPOS('hello world', 'world');

┌───┐
│ 7  │
└───┘
```
